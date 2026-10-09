#!/usr/bin/env node
// 60 Days Of Us 3.1.3 简体中文补丁 —— 结构自检
//
// 这个补丁是 script-override：顶掉的是游戏自带的 game/tl/Chinese/ 那 12 个文件。
// 能查的不是「译文对不对」，而是「这份补丁会不会把游戏弄坏」，以及 game.json 里
// coverage 这个断言是不是真的 —— 每次都从补丁重新数一遍，写错就失败。
//
// 查六件事：
//
//   1. 完整性：12 个文件都在，且文件数与 game.json 的 archive_prefix_entries 对得上
//      （归档里被摘掉的就是这 12 个 .rpy 及其 12 个 .rpyc；少一个就说明补丁和
//      索引手术对不上号，会留下一个还在归档里的旧文件）。
//   2. 重复 old 键：`translate Chinese strings:` 块里的 old 在同一语言内必须全局
//      唯一，重复会让 Ren'Py 启动即崩。
//   3. 同名 `translate Chinese python:` 块只允许有一个 —— 同名的会后加载的顶掉先加载的，
//      而注册思源宋体的那个不能被顶掉。
//   4. old 键里不允许出现汉字 —— 非 ASCII 键不可能匹配英文原文。
//   5. 覆盖率：重新提取 (英文, 中文) 对重数，与 game.json 对不上就失败。
//   6. 有意保留原文的必须在 docs/glossary.json 的 _kept_verbatim 里逐条登记。
//
// 用法：node tools/verify_patch.cjs

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PATCH = path.join(ROOT, 'patch', 'game', 'tl', 'Chinese');
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

// The language code is Chinese with a capital C -- that is what the game ships.
const HDR = /^translate\s+Chinese\s+(.*?):\s*$/;
const HDRS = /^translate\s+Chinese\s*$/;
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

function isTranslated(v) {
  return HAN.test(v) || (CJK_PUNCT.test(v) && !LATIN.test(v));
}

const files = read(PATCH);
if (!files.length) { bad('patch/game/tl/Chinese/ has no .rpy files'); process.exit(1); }
const manifest = JSON.parse(fs.readFileSync(MANIFEST, 'utf8'));

const pairs = Object.create(null);
const strings = Object.create(null);
const dupStrings = [];
const dirtyKeys = [];
const pythonBlocks = [];
let blocks = 0, stringBlocks = 0, strayLines = 0;

for (const f of files) {
  const rel = path.relative(ROOT, f).replace(/\\/g, '/');
  const raw = fs.readFileSync(f, 'utf8').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
  const lines = raw.split('\n');
  let i = 0;
  while (i < lines.length) {
    const m = HDR.exec(lines[i]);
    // "translate Chinese strings:" matches HDR too, with the id captured as
    // "strings" -- so the id has to be read off whichever regex matched, or the
    // block gets parsed as dialogue and every old/new pair is lost.
    const isStrings = m ? m[1].trim() === 'strings' : HDRS.test(lines[i].trim());
    if (!m && !isStrings) { i++; continue; }
    blocks++;
    const id = m ? m[1].trim() : 'strings';
    if (id === 'strings') stringBlocks++;
    if (!isStrings && id === 'python') pythonBlocks.push(rel + ':' + (i + 1));
    let j = i + 1;
    const body = [];
    while (j < lines.length && !HDR.test(lines[j]) && !HDRS.test(lines[j].trim())) { body.push([j, lines[j]]); j++; }
    if (isStrings) {
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

if (files.length * 2 !== manifest.archive_prefix_entries) {
  bad('the patch ships ' + files.length + ' .rpy but game.json says the archive holds '
    + manifest.archive_prefix_entries + ' entries to remove -- that is one .rpy plus its .rpyc each, '
    + 'so a mismatch means a stale archived file would survive the surgery');
}
if (pythonBlocks.length > 1) {
  bad(pythonBlocks.length + ' named translate Chinese python blocks (' + pythonBlocks.join(', ')
    + ') -- same name means the later one replaces the earlier, and the font registration must not be shadowed');
}
if (dupStrings.length) {
  bad(dupStrings.length + ' duplicate old key(s) -- Ren\'Py raises "A translation for X already exists" at startup on these: '
    + JSON.stringify(dupStrings.slice(0, 5)));
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
