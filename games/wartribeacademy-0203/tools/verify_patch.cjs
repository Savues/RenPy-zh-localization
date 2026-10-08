#!/usr/bin/env node
// Wartribe Academy 简体中文补丁 —— 结构自检
//
// `script-override` 补丁真正的风险是：按「文件 + 行号 + 列号」定位字面量回写，
// 中文比英文短，同一行里靠后的字面量整体左移，再跑一次就写错位置。这种改动
// 语法完全合法，没有任何通用 linter 看得出来（Cosy Cafe 的 WeekDays 就是
// 这么把星期四写成了星期三）。
//
// 所以本补丁不靠「抽查若干已知枚举」来防，而是拿英文原版的**遮蔽骨架**逐行
// 比对：
//
//   * 每个字面量替换成只记录引号样式的标记（@S / @Q / @T3 / @T3'），剩下的
//     纯代码骨架必须与英文版一致；
//   * 字面量个数、引号类型、三引号一一对应；
//   * data/en_masked/<file>.flags 逐个字面量记下英文提取阶段的分类
//     （p 玩家可见 / a 资源路径 / s 纯替换 / n 其它），据此算覆盖率。
//
// 骨架里没有任何英文原文，所以这个脚本只凭本仓库的克隆就能跑，不必再附带一份
// 原作文本。
//
// 另外三件事：
//   * 覆盖率里「有意保留英文」的，必须在 docs/glossary.json 的 _kept_verbatim
//     里登记，或者整个字面量只由 Ren'Py 变量/标签构成，否则算失败；
//   * gui.rpy 是唯一允许结构分歧的文件（三行 define 被字体接线取代），对它改用
//     「切掉已知块后仍须与英文版一致」这种更精确的检查；
//   * 字体覆盖，以及「中文被误用在资源键位置」。
//
// 用法：node tools/verify_patch.cjs

'use strict';

const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const ROOT = path.join(HERE, '..');
const PATCH = path.join(ROOT, 'patch', 'game');
const BASE = path.join(ROOT, 'data', 'en_masked');
const FONTS = path.join(ROOT, 'assets', 'fonts');
const GLOSSARY = path.join(ROOT, 'docs', 'glossary.json');

const MARKERS = { '"': '"', "'": "'" };
const QUOTE_MARK = { '"': '@S', "'": '@Q', '"""': '@T3', "'''": "@T3'" };

const CJK = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]/u;
const ZERO_WIDTH = new Set([0x200b, 0x200c, 0x200d, 0x2060, 0xfeff]);

// gui.rpy replaces these three defines with a FontGroup; it is the one file
// whose skeleton is allowed to differ, and only by exactly this much.
const GUI_FONT_DEFINES = [
  'define gui.text_font = @S',
  'define gui.name_text_font = @S',
  'define gui.interface_text_font = @S',
];
const GUI_WIRING = [
  'def _localised_font(',
  'group.add(',
  'gui.text_font = _localised_font(',
  'gui.name_text_font = _localised_font(',
  'gui.interface_text_font = _localised_font(',
];

// "anything that is not a letter, a digit or an underscore" -- Unicode aware,
// so '…', '？' and CJK count as filler just as they do in Python's \W.
const FILL = '[^\\p{L}\\p{N}_]';
const SUBST_ONLY = new RegExp(
  '^' + FILL + '*(?:(?:\\[[^\\]]*\\]|\\{[^{}]*\\})' + FILL + '*)*$', 'u');

const problems = [];
const notes = [];
const fail = (m) => problems.push(m);

function readText(p) {
  let s = fs.readFileSync(p, 'utf8');
  if (s.charCodeAt(0) === 0xfeff) s = s.slice(1);
  return s.replace(/\r\n/g, '\n');
}

// --------------------------------------------------------------------------
// literal tokeniser -- must stay in step with the baseline builder
function scan(text) {
  const values = [];
  let out = '';
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
      values.push(buf);
      continue;
    }
    out += ch;
    i++;
  }
  return { masked: out, values };
}

// a literal made only of Ren'Py substitutions, tags and punctuation has no
// prose in it to translate, so it needs no glossary entry
const isSubstOnly = (v) => SUBST_ONLY.test(v);

function diffReport(name, want, got) {
  const wl = want.split('\n');
  const gl = got.split('\n');
  const bad = [];
  for (let k = 0; k < Math.max(wl.length, gl.length); k++) {
    const w = k < wl.length ? wl[k] : '<missing>';
    const g = k < gl.length ? gl[k] : '<missing>';
    if (w !== g) bad.push([k + 1, w, g]);
  }
  if (!bad.length) return;
  fail(`${name}: masked skeleton differs from the English baseline (${bad.length} line(s))`);
  for (const [ln, w, g] of bad.slice(0, 6)) {
    fail(`    line ${ln}\n      en: ${w.slice(0, 120)}\n      zh: ${g.slice(0, 120)}`);
  }
  if (bad.length > 6) fail(`    ... and ${bad.length - 6} more`);
}

function keptVerbatim() {
  try {
    const g = JSON.parse(readText(GLOSSARY));
    return new Set(g._kept_verbatim || []);
  } catch (e) {
    fail(`docs/glossary.json unreadable: ${e}`);
    return new Set();
  }
}

// --------------------------------------------------------------------------
// 1. structural parity
function checkGuiFontBlock(want, got) {
  // That block is excised from both sides and the remainder compared as a
  // sequence of non-blank lines. Blank lines are ignored on purpose: the masker
  // drops comments, so the two blocks do not leave the same number of blank
  // lines behind, and padding is not what this check is about. Every other file
  // in this patch is compared line for line, blanks included.
  let wl = want.split('\n');
  let gl = got.split('\n');

  const we = [];
  for (let k = 0; k < wl.length; k++) {
    if (GUI_FONT_DEFINES.includes(wl[k].trim())) we.push(k);
  }
  if (we.length !== 3) {
    fail(`gui.rpy: baseline should hold exactly the three font defines, found ${we.length}`);
    return [want, got];
  }
  wl = wl.slice(0, we[0]).concat(wl.slice(we[we.length - 1] + 1));

  let gs = -1;
  let ge = -1;
  for (let k = 0; k < gl.length; k++) {
    if (gl[k].trim() === 'init python:' && k + 1 < gl.length
        && gl[k + 1].trim().startsWith('def _localised_font(')) gs = k;
    if (gl[k].includes('gui.interface_text_font = _localised_font(')) ge = k;
  }
  if (gs < 0 || ge < gs) {
    fail('gui.rpy: the _localised_font() block is missing or malformed');
    return [want, got];
  }
  const outside = gl.slice(0, gs).concat(gl.slice(ge + 1));

  const wantLines = wl.filter((l) => l.trim());
  const gotLines = outside.filter((l) => l.trim());
  if (wantLines.join('\n') !== gotLines.join('\n')) {
    fail('gui.rpy: outside the font block it differs from the English baseline');
    let shown = 0;
    for (let k = 0; k < Math.max(wantLines.length, gotLines.length); k++) {
      const w = k < wantLines.length ? wantLines[k] : '<missing>';
      const g = k < gotLines.length ? gotLines[k] : '<missing>';
      if (w !== g) {
        fail(`    statement ${k + 1}\n      en: ${w.slice(0, 120)}\n      zh: ${g.slice(0, 120)}`);
        if (++shown >= 6) { fail('    ... more'); break; }
      }
    }
  }
  for (const w of GUI_WIRING) {
    if (!got.includes(w)) fail(`gui.rpy: font wiring is missing '${w}'`);
  }
  return [wantLines.join('\n'), gotLines.join('\n')];
}

function checkStructure() {
  const verbatim = keptVerbatim();
  let files = 0;
  let total = 0;
  let translated = 0;
  const unregistered = [];

  for (const name of fs.readdirSync(BASE).sort()) {
    if (!name.endsWith('.rpy.masked')) continue;
    const stem = name.slice(0, -'.masked'.length);
    const flagsPath = path.join(BASE, stem + '.flags');
    const patchPath = path.join(PATCH, stem);
    if (!fs.existsSync(flagsPath) || !fs.existsSync(patchPath)) {
      fail(`${stem}: baseline or patch file missing`);
      continue;
    }

    let want = readText(path.join(BASE, name));
    const { masked: gotRaw, values } = scan(readText(patchPath));
    let got = gotRaw;

    if (stem === 'gui.rpy') {
      [want, got] = checkGuiFontBlock(want, gotRaw);
    } else {
      diffReport(stem, want, got);
    }

    const flags = readText(flagsPath).trim();
    if (stem !== 'gui.rpy' && flags.length !== values.length) {
      fail(`${stem}: ${flags.length} baseline literals but ${values.length} in the patch`);
      continue;
    }

    for (let k = 0; k < flags.length; k++) {
      if (flags[k] !== 'p') continue;
      total++;
      const v = values[k];
      if (CJK.test(v)) {
        translated++;
      } else if (!isSubstOnly(v) && !verbatim.has(v)) {
        unregistered.push(`${stem}: ${JSON.stringify(v.slice(0, 60))}`);
      }
    }
    files++;
  }

  for (const f of fs.readdirSync(PATCH)) {
    if (f.endsWith('.rpy') && !fs.existsSync(path.join(BASE, f + '.masked'))) {
      notes.push(`no English baseline for ${f}, so literal parity cannot be proven for it; `
        + 'the font and resource-key checks still apply. Its display titles were '
        + 'translated in place before this patch existed.');
    }
  }

  if (unregistered.length) {
    fail(`${unregistered.length} player-visible literal(s) left in English but not registered `
      + 'in docs/glossary.json _kept_verbatim and not substitution-only:');
    for (const u of unregistered.slice(0, 20)) fail('    ' + u);
  }
  return { files, total, translated };
}

// --------------------------------------------------------------------------
// 2. font coverage -- a cmap miss is exactly what renders as a tofu box
function facesOf(buf, off = 0) {
  if (buf.toString('latin1', off, off + 4) === 'ttcf') {
    const n = buf.readUInt32BE(off + 8);
    const out = [];
    for (let i = 0; i < n; i++) out.push(...facesOf(buf, buf.readUInt32BE(off + 12 + 4 * i)));
    return out;
  }
  const num = buf.readUInt16BE(off + 4);
  const d = {};
  let p = off + 12;
  for (let i = 0; i < num; i++) {
    d[buf.toString('latin1', p, p + 4)] = buf.readUInt32BE(p + 8);
    p += 16;
  }
  return [d];
}

function fmt4(buf, so) {
  const segX2 = buf.readUInt16BE(so + 6);
  const seg = segX2 / 2;
  const ends = [], starts = [], deltas = [], ranges = [];
  for (let i = 0; i < seg; i++) ends.push(buf.readUInt16BE(so + 14 + i * 2));
  const sp = so + 14 + segX2 + 2;
  for (let i = 0; i < seg; i++) starts.push(buf.readUInt16BE(sp + i * 2));
  const dp = sp + segX2;
  for (let i = 0; i < seg; i++) deltas.push(buf.readInt16BE(dp + i * 2));
  const rp = dp + segX2;
  for (let i = 0; i < seg; i++) ranges.push(buf.readUInt16BE(rp + i * 2));
  const cps = new Set();
  for (let i = 0; i < seg; i++) {
    if (starts[i] > ends[i]) continue;
    const hi = Math.min(ends[i], 0xffff);
    for (let c = starts[i]; c <= hi; c++) {
      let g;
      if (ranges[i] === 0) {
        g = (c + deltas[i]) & 0xffff;
      } else {
        const gi = rp + i * 2 + ranges[i] + (c - starts[i]) * 2;
        if (gi + 2 > buf.length) continue;
        g = buf.readUInt16BE(gi);
        if (g) g = (g + deltas[i]) & 0xffff;
      }
      if (g) cps.add(c);
    }
  }
  return cps;
}

function fmt12(buf, so) {
  const n = buf.readUInt32BE(so + 12);
  const cps = new Set();
  let p = so + 16;
  for (let i = 0; i < n; i++) {
    const s = buf.readUInt32BE(p);
    const e = buf.readUInt32BE(p + 4);
    p += 12;
    if (e - s < 20000) for (let c = s; c <= e; c++) cps.add(c);
  }
  return cps;
}

function coverage(file) {
  const buf = fs.readFileSync(file);
  const best = new Set();
  for (const face of facesOf(buf)) {
    const cmap = face['cmap'];
    if (!cmap) continue;
    const n = buf.readUInt16BE(cmap + 2);
    for (let i = 0; i < n; i++) {
      const off = buf.readUInt32BE(cmap + 8 + i * 8);
      const so = cmap + off;
      const fmt = buf.readUInt16BE(so);
      try {
        if (fmt === 4) for (const c of fmt4(buf, so)) best.add(c);
        else if (fmt === 12) for (const c of fmt12(buf, so)) best.add(c);
      } catch (e) { /* a malformed subtable must not hide the rest */ }
    }
  }
  return best;
}

function checkFonts() {
  const gui = readText(path.join(PATCH, 'gui.rpy'));
  const fb = new Set();
  for (const m of gui.matchAll(/DejaVuSans\.ttf",\s*0x([0-9a-fA-F]+)/g)) {
    fb.add(parseInt(m[1], 16));
  }
  const defaults = [...new Set([...gui.matchAll(/_localised_font\("([^"]+)"\)/g)].map((m) => m[1]))];
  if (!defaults.length) {
    fail('gui.rpy: no _localised_font() call -- font wiring missing');
    return { chars: 0, missing: 0 };
  }
  const cov = new Set();
  for (const ref of defaults) {
    const p = path.join(FONTS, path.basename(ref));
    if (!fs.existsSync(p)) {
      fail(`font asset ${ref} is missing from assets/fonts/`);
      continue;
    }
    for (const c of coverage(p)) cov.add(c);
  }
  const dj = coverage(path.join(FONTS, 'DejaVuSans.ttf'));
  for (const cp of fb) {
    if (!dj.has(cp)) fail(`U+${cp.toString(16).toUpperCase().padStart(4, '0')} is routed to `
      + 'DejaVuSans, which has no glyph for it');
  }

  const chars = new Set();
  for (const f of fs.readdirSync(PATCH)) {
    if (!f.endsWith('.rpy')) continue;
    for (const ch of readText(path.join(PATCH, f))) {
      if (ch.codePointAt(0) > 0x7f && !ZERO_WIDTH.has(ch.codePointAt(0))) chars.add(ch);
    }
  }
  const missing = [...chars].filter((c) => {
    const cp = c.codePointAt(0);
    return !cov.has(cp) && !fb.has(cp);
  }).sort();
  if (missing.length) {
    fail(`${missing.length} character(s) have no glyph in any shipped font: `
      + missing.slice(0, 20).map((c) => 'U+' + c.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' '));
  }
  return { chars: chars.size, missing: missing.length };
}

// --------------------------------------------------------------------------
// 3. no Chinese where Ren'Py wants an identifier
const KEY_CHECKS = [
  ['renpy.image name', /renpy\.image\(\s*(['"])([^'"]*)\1/g],
  ['image statement', /^\s*image\s+(['"])([^'"]*)\1\s*=/g],
  ['scene/show/hide', /^\s*(?:scene|show|hide)\s+(['"])([^'"]*)\1/g],
  ['call/jump label', /^\s*(?:call|jump)\s+(?:expression\s+)?(['"])([^'"]*)\1/g],
  ['audio file', /^\s*(?:play|queue|stop|voice)\s+(?:music|voice|sound)?\s*['"]([^'"]+)['"]/g],
  ['renpy.music/voice', /renpy\.(?:music|voice|play)\(\s*(['"])([^'"]*)\1/g],
  ['replay title key', /replay_make_titles\([^)]*?\(\s*'[^']*'\s*,\s*'([^']*)'\s*\)/g],
];

function checkKeys() {
  let hits = 0;
  for (const f of fs.readdirSync(PATCH)) {
    if (!f.endsWith('.rpy')) continue;
    const lines = readText(path.join(PATCH, f)).split('\n');
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trimStart().startsWith('#')) continue;
      for (const [label, rx] of KEY_CHECKS) {
        rx.lastIndex = 0;
        let m;
        while ((m = rx.exec(lines[i])) !== null) {
          const ident = m[m.length - 1];
          if ([...ident].some((c) => c.codePointAt(0) > 0x7f)) {
            fail(`${f}:${i + 1}: non-ASCII in ${label} position: ${JSON.stringify(ident)}`);
            hits++;
          }
        }
      }
    }
  }
  return hits;
}

function main() {
  const { files, total, translated } = checkStructure();
  const { chars, missing } = checkFonts();
  const keys = checkKeys();

  console.log(`structural parity: ${files} file(s) against the English baseline`);
  console.log(`coverage:         ${translated} / ${total} player-visible literals carry Chinese`);
  console.log(`font coverage:    ${chars} distinct non-ASCII characters, ${missing} without a glyph`);
  console.log(`resource keys:    ${keys} non-ASCII identifier(s)`);
  for (const n of notes) console.log('note: ' + n);
  if (problems.length) {
    console.log('');
    for (const p of problems.slice(0, 40)) console.log('FAIL ' + p);
    console.log(`\n${problems.length} problem(s)`);
    process.exit(1);
  }
  console.log('\nall structural checks passed');
}

main();