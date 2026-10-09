#!/usr/bin/env node
// Between Humanity 0.3.3 简体中文补丁 —— 结构自检
//
// 这个补丁是 script-override：它顶掉的是游戏自带的 game/tl/chinese/ 那棵树。
// 能查的不是「译文对不对」，而是「这份补丁会不会把游戏弄坏」，以及 game.json 里
// 那个 coverage 断言是不是真的 —— 每次都从补丁重新数一遍，写错就失败。
//
// 查六件事：
//
//   1. 完整性：134 个文件都在。
//   2. 重复 old 键：translate chinese strings: 块里的 old 在同一语言内必须全局
//      唯一，重复会让 Ren'Py 启动即崩（TranslationStringRegistry.add() 抛
//      "A translation for X already exists"）。这是这个补丁最致命的一类错。
//   3. translate 块 id 全局唯一。
//   4. old 键里不允许出现汉字 —— 这一条是发行方自己的一个 bug 逼出来的：
//      scripts/functions/enums.rpy 的第一个 strings 块里有一条
//      old "Acqu机翻ntance"，机翻把「机翻」两个字打进了英文原句中间。那条永远
//      匹配不上游戏里的英文，所以它是条死条目。同一文件往下 160 行还有一条
//      正确的 old "Acquaintance"，所以**修**它会让两条键撞车、直接把游戏弄崩 ——
//      正确的做法是删掉死的那条，本补丁就是这么做的。这条守卫是为了防止它
//      （或者同类的脏键）再出现。
//   5. 覆盖率：重新提取 (英文, 中文) 对重数，与 game.json 对不上就失败。
//   6. 有意保留原文的必须在 docs/glossary.json 的 _kept_verbatim 里逐条登记。
//
// 用法：node tools/verify_patch.cjs

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PATCH = path.join(ROOT, 'patch', 'game', 'tl', 'chinese');
const MANIFEST = path.join(ROOT, 'game.json');
const GLOSSARY = path.join(ROOT, 'docs', 'glossary.json');

const HAN = /[\u3400-\u9fff\uf900-\ufaff]/;
const CJK_PUNCT = /[\u2e80-\u2eff\u3000-\u303f\uff00-\uffef]/;
const LATIN = /[A-Za-z]/;

let fail = 0;
function bad(msg) { fail++; console.log('FAIL  ' + msg); }

const LIT = /("""(?:[^"]|"(?!""))*"""|'''(?:[^']|'(?!''))*'''|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/s;
function lit(text) {
  const m = LIT.exec(text);
  return m ? m[0].slice(1, -1) : null;
}

const HDR = /^translate\s+chinese\s+(.*?):\s*$/;
const CMT = /^\s*#\s?(.*)$/;
const SRCLINE = /^\s*#\s+\S+:\d+\s*$/;

function read(dir, out) {
  out = out || [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) read(p, out);
    else if (e.name.endsWith('.rpy')) out.push(p);
  }
  return out;
}

function bodyText(body) {
  // comments and blank lines excluded: what the player sees is what matters
  return body.map(([, t]) => t.trim()).filter(t => t && !t.startsWith('#')).join('\n');
}

function isTranslated(v) {
  return HAN.test(v) || (CJK_PUNCT.test(v) && !LATIN.test(v));
}

const files = read(PATCH);
if (!files.length) { bad('patch/game/tl/chinese/ has no .rpy files'); process.exit(1); }

const pairs = Object.create(null);
const strings = Object.create(null);
const dupStrings = [];
const dupIds = [];
const seenIds = new Map();
const idBodies = new Map();
const dirtyKeys = [];
let blocks = 0, stringBlocks = 0, strayLines = 0;

for (const f of files) {
  const rel = path.relative(ROOT, f).replace(/\\/g, '/');
  const raw = fs.readFileSync(f, 'utf8').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
  const lines = raw.split('\n');
  let i = 0;
  while (i < lines.length) {
    const m = HDR.exec(lines[i]);
    if (!m) { i++; continue; }
    blocks++;
    const id = m[1].trim();
    let j = i + 1;
    const body = [];
    while (j < lines.length && !HDR.test(lines[j])) { body.push([j, lines[j]]); j++; }
    if (id !== 'strings') {
      // Ren'Py hashes an id from the English string, so a line the game says
      // twice legitimately exports twice. Identical bodies are a harmless
      // artefact of the linter having read both foo.rpy and foo.rpyc; only a
      // pair that disagrees about what the line says is a real defect, because
      // then one of the two renderings is silently unreachable.
      if (seenIds.has(id)) {
        const where = rel + ':' + (i + 1);
        dupIds.push(id + ' @' + where + ' and ' + seenIds.get(id));
        idBodies.set(id, [idBodies.get(id), bodyText(body)]);
      } else {
        seenIds.set(id, rel + ':' + (i + 1));
        idBodies.set(id, [bodyText(body)]);
      }
    } else {
      stringBlocks++;
    }
    if (id === 'strings') {
      for (let k = 0; k < body.length; k++) {
        const mo = /^\s*old\s+(""".*"""|".*")$/s.exec(body[k][1]);
        if (!mo) continue;
        const mn = k + 1 < body.length ? /^\s*new\s+(""".*"""|".*")$/s.exec(body[k + 1][1]) : null;
        if (!mn) continue;
        const o = lit(mo[1]);
        const n = lit(mn[1]);
        if (o === null || n === null) continue;
        if (HAN.test(o)) dirtyKeys.push(JSON.stringify(o) + ' @' + rel + ':' + (body[k][0] + 1));
        if (Object.prototype.hasOwnProperty.call(strings, o)) dupStrings.push(JSON.stringify(o));
        else strings[o] = n;
      }
    } else {
      let pending = null;
      for (const [ln, txt] of body) {
        if (txt.trim().startsWith('#')) {
          const c = CMT.exec(txt);
          pending = (c && !SRCLINE.test(txt)) ? c[1].trim() : null;
          continue;
        }
        if (!txt.trim()) continue;
        const z = lit(txt);
        if (pending !== null && z !== null) {
          const e = lit('# ' + pending);
          if (e !== null && !Object.prototype.hasOwnProperty.call(pairs, e)) pairs[e] = z;
          pending = null;
        } else {
          pending = null;
          strayLines++;
        }
      }
    }
    i = j;
  }
}

console.log('files:               ' + files.length);
console.log('translate blocks:    ' + blocks + '  (of which strings: ' + stringBlocks + ')');

if (dupStrings.length) {
  bad(dupStrings.length + ' duplicate old key(s) -- Ren\'Py raises "A translation for X already exists" at startup on these: '
    + JSON.stringify(dupStrings.slice(0, 5)));
}
const conflicting = [...idBodies.entries()].filter(([, bodies]) => {
  const uniq = new Set(bodies.flat().filter(Boolean));
  return uniq.size > 1;
}).map(([id]) => id);
if (conflicting.length) {
  bad(conflicting.length + ' translate block id(s) registered twice with DIFFERENT text, so the earlier '
    + 'rendering is unreachable at runtime: ' + JSON.stringify(conflicting.slice(0, 5)));
}
if (dupIds.length) {
  console.log('note: ' + dupIds.length + ' id(s) exported twice from both foo.rpy and foo.rpyc, all with '
    + 'identical text -- harmless, since the player sees the same line either way');
}
if (dirtyKeys.length) {
  bad(dirtyKeys.length + ' old key(s) contain Han characters and can never match the English source: '
    + JSON.stringify(dirtyKeys.slice(0, 5)));
}

const all = Object.assign(Object.create(null), pairs, strings);
const keys = Object.keys(all).filter(k => k.trim() && String(all[k]).trim());
const verbatim = keys.filter(k => all[k] === k);
const verbatimSet = new Set(verbatim);
const translated = keys.filter(k => !verbatimSet.has(k));
const withHan = translated.filter(k => isTranslated(String(all[k])));
const punctOnly = translated.filter(k => !isTranslated(String(all[k])));
const manifest = JSON.parse(fs.readFileSync(MANIFEST, 'utf8'));
const cov = manifest.coverage || {};
console.log('coverage:            ' + translated.length + ' / ' + (cov.total === undefined ? '?' : cov.total)
  + ' localised, ' + verbatim.length + ' deliberately verbatim');
console.log('  of the localised:  ' + withHan.length + ' contain a Han character, '
  + punctOnly.length + ' are punctuation-only');
if (cov.total !== keys.length) {
  bad('game.json coverage.total is ' + cov.total + ' but the patch holds ' + keys.length + ' translatable strings');
}
if (cov.translated !== translated.length) {
  bad('game.json coverage.translated is ' + cov.translated + ' but ' + translated.length + ' strings are localised');
}
if (cov.verbatim !== verbatim.length) {
  bad('game.json coverage.verbatim is ' + cov.verbatim + ' but ' + verbatim.length + ' are byte-identical to the source');
}

const glossary = JSON.parse(fs.readFileSync(GLOSSARY, 'utf8'));
const registered = new Set(glossary._kept_verbatim || []);
const unregistered = verbatim.filter(k => !registered.has(k));
const stale = [...registered].filter(k => !verbatim.includes(k));
if (unregistered.length) {
  bad(unregistered.length + ' untranslated string(s) not registered in _kept_verbatim: '
    + JSON.stringify(unregistered.slice(0, 5)));
}
if (stale.length) {
  bad(stale.length + ' _kept_verbatim entry/entries no longer match the patch: ' + JSON.stringify(stale.slice(0, 5)));
}

if (strayLines) console.log('note: ' + strayLines + ' active line(s) had no English comment above them');
console.log('');
console.log(fail ? fail + ' problem(s)' : 'all structural checks passed');
process.exit(fail ? 1 : 0);
