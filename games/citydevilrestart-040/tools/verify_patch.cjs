#!/usr/bin/env node
// City Devil: Restart 0.4.0 简体中文补丁 —— 结构自检
//
// 这是 script-override 补丁：翻译本身就是被替换掉的脚本，patch/game/ 一比一
// 镜像原作的 game/。所以「译文对不对」只能拿英文原版的**遮蔽骨架**来证明，
// 而且证明得比抽查强：
//
//   * 每个字面量替换成只记录引号样式的标记（@S / @Q / @T3 / @T3'），剩下的
//     纯代码骨架必须逐行等于英文版；
//   * game.json 的 structure_exceptions 逐行列出允许分歧的那几行，并把英文与
//     中文两边的原文都写死 —— 改一行就失败，防止例外慢慢长胖；
//   * data/en_masked/<file>.flags 逐个字面量记下分类，据此算覆盖率。
//
// 骨架里没有任何英文原文，所以这个脚本只凭本仓库的克隆就能跑，不必再附带一份
// 原作文本。
//
// 另外四件事：
//   * 覆盖率里「有意保留原文」的必须在 docs/glossary.json 的 _kept_verbatim
//     登记；含汉字、或只含中文标点而一个拉丁字母都没有的字面量算已译；
//   * 资源键位置（image/scene/play/define/label…）出现非 ASCII 即失败 —— 中文
//     写进标识符不会报错，只会让图裂掉，静默得很；
//   * 安装器的关键前提：archive.rpa 里同名 .rpyc 会和松散的 .rpy 一起被加载，
//     所以每个覆盖文件都必须补一个同名 .rpyc 影子文件。这条从仓库这一侧就能查；
//   * shim 用到的字体全部来自 archive.rpa，补丁不重新分发它们。
//
// 用法：node tools/verify_patch.cjs

'use strict';

const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const ROOT = path.join(HERE, '..');
const PATCH = path.join(ROOT, 'patch', 'game');
const BASE = path.join(ROOT, 'data', 'en_masked');
const GLOSSARY = path.join(ROOT, 'docs', 'glossary.json');
const MANIFEST = path.join(ROOT, 'game.json');

const QUOTE_MARK = { '"': '@S', "'": '@Q', '"""': '@T3', "'''": "@T3'" };
const MARKER = /@S|@Q|@T3'|@T3/g;

const HAN = /[\u3400-\u9fff\uf900-\ufaff]/u;
const CJK_PUNCT = /[\u2e80-\u2eff\u3000-\u303f\uff00-\uffef]/u;
const ASCII_LETTER = /[A-Za-z]/u;

// "anything that is not a letter, a digit or an underscore" -- Unicode aware,
// so '…', '？' and CJK count as filler just as they do in Python's \W.
const FILL = '[^\\p{L}\\p{N}_]';
const SUBST_ONLY = new RegExp(
  '^' + FILL + '*(?:(?:\\[[^\\]]*\\]|\\{[^{}]*\\})' + FILL + '*)*$', 'u');

const KEY_CHECKS = [
  ['image statement', /^\s*image\s+(['"])([^'"]*)\1/],
  ['scene/show/hide', /^\s*(?:scene|show|hide)\s+(['"])([^'"]*)\1/],
  ['renpy.image name', /renpy\.image\(\s*(['"])([^'"]*)\1/],
  ['audio file', /^\s*(?:play|queue|stop|voice)\b[^'"]*?(['"])([^'"]+)\1/],
  ['call/jump label', /^\s*(?:call|jump)\s+(['"])([^'"]*)\1/],
  ['define', /^\s*define\s+([A-Za-z_][\w.]*)/],
  ['label', /^\s*label\s+([A-Za-z_][\w.]*)/],
  ['screen', /^\s*screen\s+([A-Za-z_][\w.]*)/],
  ['transform', /^\s*transform\s+([A-Za-z_][\w.]*)/],
  ['style', /^\s*style\s+([A-Za-z_][\w.]*)/],
];

const problems = [];
const notes = [];
const fail = (m) => problems.push(m);

function readText(p) {
  let s = fs.readFileSync(p, 'utf8');
  if (s.charCodeAt(0) === 0xfeff) s = s.slice(1);
  return s.replace(/\r\n/g, '\n');
}

const readJson = (p) => JSON.parse(readText(p));

// ---------------------------------------------------------------------------
// literal tokeniser -- must stay in step with the baseline builder's scan()
function scan(text) {
  const values = [];
  let out = '';
  let lineno = 0;
  let i = 0;
  const n = text.length;
  while (i < n) {
    const ch = text[i];
    if (ch === '#') {
      while (i < n && text[i] !== '\n') i++;
      continue;
    }
    if (ch === '"' || ch === "'") {
      const triple = text.substr(i, 3) === ch.repeat(3);
      const q = triple ? ch.repeat(3) : ch;
      out += QUOTE_MARK[q];
      i += q.length;
      let buf = '';
      while (i < n) {
        if (text[i] === '\\') { buf += text.substr(i, 2); i += 2; continue; }
        if (text.substr(i, q.length) === q) { i += q.length; break; }
        buf += text[i];
        i++;
      }
      values.push({ text: buf, line: lineno });
      continue;
    }
    if (ch === '\n') lineno++;
    out += ch;
    i++;
  }
  return { masked: out, values };
}

const unescape = (s) => s.replace(/\\(.)/gu, '$1');

// A literal counts as translated when it carries Han, or when it carries CJK
// punctuation and no Latin letters at all.  CJK punctuation on its own is not
// enough: "Start、Guide" is a Chinese comma between two English words, and
// counting that as translated is how a label stays untranslated for ever.
const isTranslated = (v) =>
  HAN.test(v) || (CJK_PUNCT.test(v) && !ASCII_LETTER.test(v));

const isSubstOnly = (v) => SUBST_ONLY.test(unescape(v));

// ---------------------------------------------------------------------------
// 1. structural parity against the English baseline
//
// game.json pins every line allowed to differ, with both sides written out, so
// an exception cannot quietly widen: touch either line and this fails.
function diffExcept(stem, want, got, except) {
  const wl = want.split('\n');
  const gl = got.split('\n');
  const skip = new Set();
  for (const e of except) {
    const idx = e.line - 1;
    const w = wl[idx];
    const g = gl[idx];
    if (w === undefined || g === undefined) {
      fail(stem + ': declared exception at line ' + e.line + ' is past the end of a file');
      continue;
    }
    if (w !== e.en || g !== e.zh) {
      fail(stem + ': line ' + e.line + ' is no longer the exception game.json declares\n'
        + '      baseline now: ' + JSON.stringify(w) + '\n'
        + '      declared en:  ' + JSON.stringify(e.en) + '\n'
        + '      patch now:    ' + JSON.stringify(g) + '\n'
        + '      declared zh:  ' + JSON.stringify(e.zh));
    }
    skip.add(idx);
  }
  const bad = [];
  for (let k = 0; k < Math.max(wl.length, gl.length); k++) {
    if (skip.has(k)) continue;
    const w = k < wl.length ? wl[k] : '<missing>';
    const g = k < gl.length ? gl[k] : '<missing>';
    if (w !== g) bad.push([k + 1, w, g]);
  }
  if (!bad.length) return 0;
  fail(stem + ': masked skeleton differs from the English baseline outside the declared '
    + 'exceptions (' + bad.length + ' line(s))');
  for (const [ln, w, g] of bad.slice(0, 6)) {
    fail('    line ' + ln + '\n      en: ' + w.slice(0, 120)
      + '\n      zh: ' + g.slice(0, 120));
  }
  if (bad.length > 6) fail('    ... and ' + (bad.length - 6) + ' more');
  return bad.length;
}

// ---------------------------------------------------------------------------
// 2. coverage
//
// <file>.flags is one character per baseline literal, in source order, and the
// patch's literals come out of scan() in that same order, so the two line up by
// index.  The one place they do not is where a declared exception deleted a
// literal: the live arm of the name prompt in script.rpy loses its allow=
// clause, which is what makes renpy.input accept Chinese characters.  How many
// were deleted, and where, is read back off the exception by counting quote
// markers in its en/zh strings -- so the number cannot drift away from the
// thing it is describing -- and the gap is attributed to the trailing
// positions of that line, which is what dropping a keyword argument looks like.
function alignFlags(stem, flags, values, except) {
  // Which baseline literals the patch deleted, as indices into flags.
  const dropped = [];
  let deficit = flags.length - values.length;
  if (deficit < 0) {
    fail(stem + ': the patch holds ' + values.length + ' literals but the baseline holds '
      + flags.length + '; a patch may not add one where no exception says so');
    deficit = 0;
  }
  for (const e of except) {
    const lost = (e.en.match(MARKER) || []).length - (e.zh.match(MARKER) || []).length;
    if (lost <= 0) continue;
    const here = [];
    values.forEach((v, k) => { if (v.line === e.line - 1) here.push(k); });
    if (!here.length) {
      fail(stem + ': the exception declared on line ' + e.line + ' holds no literal in the patch');
      continue;
    }
    // Nothing was dropped before this line, so the patch index of its first
    // literal is also the baseline index of its first literal.  The deleted
    // ones are the trailing arguments of the line -- what dropping a keyword
    // argument looks like -- so they start one line-length past that.
    for (let d = 0; d < lost; d++) dropped.push(here[0] + here.length + d);
    deficit -= lost;
  }
  if (deficit !== 0) {
    fail(stem + ': ' + deficit + ' literal(s) short of the baseline with no exception to '
      + 'account for them');
  }
  dropped.sort((a, b) => a - b);
  const gone = new Set(dropped);
  // flag index -> patch index.  Every deleted literal before this one shifts
  // the patch back by one; a deleted literal itself has no counterpart.
  const map = [];
  let shift = 0;
  for (let k = 0; k < flags.length; k++) {
    if (gone.has(k)) { map.push(-1); shift++; continue; }
    map.push(k - shift);
  }
  return map;
}

function checkStructure(manifest) {
  let glossary = {};
  try { glossary = readJson(GLOSSARY); } catch (e) { fail('docs/glossary.json unreadable: ' + e); }
  const verbatim = new Set(glossary._kept_verbatim || []);
  const exceptions = manifest.structure_exceptions || [];

  const auditOnly = new Set(manifest.audit_only || []);
  let files = 0;
  let audited = 0;
  let total = 0;
  let translated = 0;
  let kept = 0;
  let bare = 0;
  const bag = new Set();
  const unregistered = [];

  for (const name of fs.readdirSync(BASE).sort()) {
    if (!name.endsWith('.rpy.masked')) continue;
    const stem = name.slice(0, -'.masked'.length);
    const flagsPath = path.join(BASE, stem + '.flags');
    const patchPath = path.join(PATCH, stem);
    if (!fs.existsSync(flagsPath)) {
      fail(stem + ': baseline has no flags sidecar');
      continue;
    }

    // game.json splits the baselines in two.  audit_only names the scripts the
    // patch deliberately leaves alone, and they are held to a stricter rule
    // than the eight it replaces: not one literal may be player-visible.  That
    // is what makes "every player-visible string in this game sits in one of
    // the eight files we replaced" a thing the build checks rather than a
    // claim somebody checked once.
    if (auditOnly.has(stem)) {
      if (fs.existsSync(patchPath)) {
        fail(stem + ' is listed in game.json audit_only but patch/game/' + stem + ' exists');
      }
      const af = readText(flagsPath).trim();
      const prose = [...af].filter((c) => c === 'p').length;
      if (prose) {
        fail(stem + ': game.json says this script carries no player-visible text, but '
          + prose + ' of its ' + af.length + ' literals are classified player-visible. '
          + 'Either it wants translating, or the classifier is wrong; both are worth a look.');
      }
      audited++;
      continue;
    }

    if (!fs.existsSync(patchPath)) {
      fail(stem + ': a baseline exists but the patch does not ship it, and game.json does '
        + 'not list it under audit_only either');
      continue;
    }

    const except = exceptions.filter((e) => e.file === stem);
    const want = readText(path.join(BASE, name));
    const { masked: got, values } = scan(readText(patchPath));
    diffExcept(stem, want, got, except);

    const flags = readText(flagsPath).trim();
    if (!flags.length) { fail(stem + ': empty flags file'); continue; }

    const map = alignFlags(stem, flags, values, except);
    let missing = 0;
    for (let k = 0; k < flags.length; k++) {
      if (flags[k] !== 'p') continue;
      total++;
      const v = values[map[k]];
      if (!v) { missing++; continue; }
      if (isTranslated(v.text)) { translated++; continue; }
      if (verbatim.has(v.text)) { kept++; continue; }
      if (isSubstOnly(v.text)) { bare++; bag.add(v.text); continue; }
      unregistered.push(stem + ':' + (v.line + 1) + ': ' + JSON.stringify(v.text.slice(0, 60)));
    }
    if (missing) fail(stem + ': ' + missing + ' player-visible literal(s) have no counterpart '
      + 'in the patch');
    files++;
  }

  for (const f of fs.readdirSync(PATCH)) {
    if (f.endsWith('.rpy') && !fs.existsSync(path.join(BASE, f + '.masked'))) {
      notes.push(f + ' has no English baseline: nothing archived carries that name, so it is a '
        + 'file this patch introduces and there is no original to compare it against');
    }
  }

  // Every baseline is either audited or overridden.  A script in neither column
  // would sit outside the coverage figure without anybody deciding that.
  for (const stem of auditOnly) {
    if (!fs.existsSync(path.join(BASE, stem + '.masked'))) {
      fail('game.json audit_only lists ' + stem + ' but data/en_masked/' + stem
        + '.masked does not exist');
    }
  }

  if (unregistered.length) {
    fail(unregistered.length + ' player-visible literal(s) are left in a non-Chinese script but '
      + 'are not registered in docs/glossary.json _kept_verbatim');
    for (const u of unregistered.slice(0, 20)) fail('    ' + u);
    if (unregistered.length > 20) fail('    ... and ' + (unregistered.length - 20) + ' more');
  }
  if (bare) notes.push(bare + ' player-visible literal(s) are nothing but Ren\'Py substitutions '
    + 'and punctuation, so there is no prose in them to translate: '
    + [...bag].slice(0, 6).map((s) => JSON.stringify(s)).join(' ')
    + (bag.size > 6 ? ' (+' + (bag.size - 6) + ' more distinct)' : ''));
  return { files, audited, total, translated, kept, bare };
}

// ---------------------------------------------------------------------------
// 3. no Chinese where Ren'Py wants an identifier
function checkKeys() {
  let hits = 0;
  for (const f of fs.readdirSync(PATCH)) {
    if (!f.endsWith('.rpy')) continue;
    const lines = readText(path.join(PATCH, f)).split('\n');
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trimStart().startsWith('#')) continue;
      for (const [label, rx] of KEY_CHECKS) {
        const m = rx.exec(lines[i]);
        if (!m) continue;
        const ident = m[m.length - 1];
        if (/[^\x00-\x7f]/u.test(ident)) {
          fail(f + ':' + (i + 1) + ': non-ASCII in ' + label + ' position: '
            + JSON.stringify(ident));
          hits++;
        }
      }
    }
  }
  return hits;
}

// ---------------------------------------------------------------------------
// 4. the installer's load-bearing assumption, checked from this side
// archive.rpa holds every script as BOTH foo.rpy and foo.rpyc.  Ren'Py keys
// loadable files by name and scans the game directory before the archive, so
// dropping a loose foo.rpy in does not by itself shadow the archived foo.rpyc:
// the two load together and every label is defined twice.  Each overridden file
// therefore needs a loose foo.rpyc of the same name, which the installer
// creates.  The shim does not, because nothing archived carries that name.
function checkShadowing(manifest) {
  const shadowed = new Set(manifest.archive_shadowed || []);
  const shipped = fs.readdirSync(PATCH).filter((f) => f.endsWith('.rpy')).sort();
  for (const f of shipped) {
    if (!shadowed.has(f)) {
      fail(f + ' is shipped but is not listed in game.json archive_shadowed, so the installer '
        + 'would not create the .rpyc that shadows archive.rpa');
    }
  }
  for (const f of shadowed) {
    if (!fs.existsSync(path.join(PATCH, f))) {
      fail('game.json archive_shadowed lists ' + f + ' but patch/game/' + f + ' does not exist');
    }
  }
  if (shadowed.has(manifest.shim)) {
    fail('game.json archive_shadowed lists the shim ' + manifest.shim + '; nothing archived '
      + 'carries that name, so it needs no .rpyc shadow');
  }
  return shipped.length;
}

// ---------------------------------------------------------------------------
// 5. the shim's fonts come out of the game's own archive
function checkFonts(manifest) {
  const shimPath = path.join(ROOT, 'patch', manifest.shim);
  if (!fs.existsSync(shimPath)) {
    fail('shim patch/' + manifest.shim + ' is missing');
    return 0;
  }
  const shim = readText(shimPath);
  const used = [...new Set([...shim.matchAll(/"([^"]+\.ttf)"/g)].map((m) => m[1]))].sort();
  const declared = [...(manifest.archive_fonts || [])].sort();
  if (used.join('\n') !== declared.join('\n')) {
    fail('the shim references ' + JSON.stringify(used) + ' but game.json archive_fonts says '
      + JSON.stringify(declared));
  }
  if ((manifest.font_assets || []).length) {
    fail('this patch ships no fonts: both faces live in archive.rpa and are the publisher\'s '
      + 'own, so redistributing them here is not this patch\'s to do');
  }
  return used.length;
}

// ---------------------------------------------------------------------------
// 6. every shipped script actually carries Chinese
function checkTranslatedFiles() {
  for (const f of fs.readdirSync(PATCH).sort()) {
    if (!f.endsWith('.rpy')) continue;
    const han = (readText(path.join(PATCH, f)).match(/[\u3400-\u9fff]/gu) || []).length;
    if (!han) fail('patch/game/' + f + ' holds no Han at all -- it looks untranslated');
    else notes.push(f + ': ' + han.toLocaleString('en-US') + ' Han characters');
  }
}

function main() {
  const manifest = readJson(MANIFEST);
  const s = checkStructure(manifest);
  const keys = checkKeys();
  const shipped = checkShadowing(manifest);
  const faces = checkFonts(manifest);
  checkTranslatedFiles();

  console.log('structural parity: ' + s.files + ' file(s) replaced, '
    + s.audited + ' audited as carrying no player-visible text');
  console.log('coverage:         ' + s.translated.toLocaleString('en-US') + ' / ' + s.total.toLocaleString('en-US')
    + ' player-visible literals carry Chinese'
    + (s.kept ? ' (+' + s.kept + ' registered as deliberately verbatim)' : ''));
  console.log('kept verbatim:     ' + s.kept + ' registered + ' + s.bare + ' substitution-only');
  console.log('patch scripts:    ' + shipped + ', each with a declared .rpyc shadow');
  console.log('shim fonts:       ' + faces + ' face(s), all resolved out of archive.rpa');
  console.log('resource keys:    ' + keys + ' non-ASCII identifier(s)');
  for (const n of notes) console.log('note: ' + n);
  if (problems.length) {
    console.log('');
    for (const p of problems.slice(0, 40)) console.log('FAIL ' + p);
    console.log('\n' + problems.length + ' problem(s)');
    process.exit(1);
  }
  console.log('\nall structural checks passed');
}

main();
