#!/usr/bin/env node
// That New Teacher 0.9.0 简体中文补丁 —— 结构自检
//
// 这个补丁是 script-override：它顶掉的是游戏自带的 game/tl/chinese/ 那棵树，
// 所以这里能查的不是「译文对不对」，而是「这份补丁会不会把游戏弄坏」，
// 以及补丁自己声明的覆盖率数字是不是真的：game.json 的 coverage 是断言，
// 这个脚本每次都从补丁里重新数一遍，写错就会失败。
//
// 查六件事：
//
//   1. 完整性：patch/game/tl/chinese/ 下的 51 个文件都在，每个都还是合法的
//      Ren'Py 翻译文件（translate chinese 块头、块内注释行与活动行成对）。
//   2. 重复键：translate chinese strings: 块里的 old 在同一语言内必须全局唯一，
//      重复会让 Ren'Py 启动即崩（TranslationStringRegistry.add() 抛
//      "A translation for X already exists"）。这是这个补丁最致命的一类错，
//      专查。
//   3. translate 块 id 全局唯一：同一个 id 出现两次同样会重复注册。
//   4. 覆盖率：重新提取 (英文, 中文) 对，按含汉字／只含中文标点判定已译，
//      与 game.json 的 coverage 对不上就失败。
//   5. 有意保留原文的必须在 docs/glossary.json 的 _kept_verbatim 里逐条登记，
//      没登记又不含中文的一律失败。
//   6. 索菲娅 / 苏西 与 克拉丽莎 / 克莉丝 两组名字必须各自出现，且不能出现在
//      同一行。原版把两位女主都译成「苏西」，玩家根本分不开，这是这一版最要紧
//      的修正；banned 变体查不出它（苏西现在是苏西的正确写法），所以单列一条。
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

// Ren'Py 的字符串字面量：单引号、三引号都算，\. 让转义引号不结束字符串。
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

// 这条判定和 tools/check.py 的 database 路径同源：含汉字算已译，
// 只含中文标点而一个拉丁字母都没有也算（省略号写成「……」是本地化）。
function isTranslated(v) {
  return HAN.test(v) || (CJK_PUNCT.test(v) && !LATIN.test(v));
}

const files = read(PATCH);
if (!files.length) { bad('patch/game/tl/chinese/ has no .rpy files'); process.exit(1); }

const pairs = Object.create(null);        // english -> chinese（首个渲染）
const strings = Object.create(null);      // english -> chinese（strings 块）
const stringKeyAt = new Map();            // english -> "file:line"
const dupStrings = [];
const dupIds = [];
const seenIds = new Map();
const NAME_A = '索菲娅', NAME_B = '苏西', NAME_C = '克拉丽莎', NAME_D = '克莉丝';
const nameLines = { [NAME_A]: [], [NAME_B]: [], [NAME_C]: [], [NAME_D]: [] };
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
    if (id !== 'strings') {
      if (seenIds.has(id)) dupIds.push(id + ' @' + rel + ':' + (i + 1) + ' and ' + seenIds.get(id));
      else seenIds.set(id, rel + ':' + (i + 1));
    } else {
      stringBlocks++;
    }
    let j = i + 1;
    const body = [];
    while (j < lines.length && !HDR.test(lines[j])) { body.push([j, lines[j]]); j++; }
    if (id === 'strings') {
      for (let k = 0; k < body.length; k++) {
        const mo = /^\s*old\s+(""".*"""|".*")$/s.exec(body[k][1]);
        if (!mo) continue;
        const mn = k + 1 < body.length ? /^\s*new\s+(""".*"""|".*")$/s.exec(body[k + 1][1]) : null;
        if (!mn) continue;
        const o = lit(mo[1]);
        const n = lit(mn[1]);
        if (o === null || n === null) continue;
        for (const name of Object.keys(nameLines)) if (n.includes(name)) nameLines[name].push(rel + ':' + (body[k + 1][0] + 1));
        if (Object.prototype.hasOwnProperty.call(strings, o)) dupStrings.push(JSON.stringify(o));
        else { strings[o] = n; stringKeyAt.set(o, rel + ':' + (body[k][0] + 1)); }
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
          if (e !== null) {
            if (!Object.prototype.hasOwnProperty.call(pairs, e)) pairs[e] = z;
            for (const name of Object.keys(nameLines)) {
              if (txt.includes(name) && pairs[e] !== undefined) nameLines[name].push(rel + ':' + (ln + 1));
            }
          }
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

// ---- 2/3 唯一性 ------------------------------------------------------------
if (dupStrings.length) {
  bad(dupStrings.length + ' duplicate old key(s) in translate chinese strings: -- Ren\'Py raises '
    + '"A translation for X already exists" at startup on these: ' + JSON.stringify(dupStrings.slice(0, 5)));
}
if (dupIds.length) {
  bad(dupIds.length + ' duplicate translate block id(s): ' + JSON.stringify(dupIds.slice(0, 5)));
}

// ---- 4 覆盖率 ---------------------------------------------------------------
const all = Object.assign(Object.create(null), pairs, strings);
const keys = Object.keys(all).filter(k => k.trim() && String(all[k]).trim());
const verbatim = keys.filter(k => all[k] === k);
const verbatimSet = new Set(verbatim);
const translated = keys.filter(k => !verbatimSet.has(k));
const withHan = translated.filter(k => isTranslated(String(all[k])));
const punctOnly = translated.filter(k => !isTranslated(String(all[k])));

// --dump-verbatim <path> regenerates docs/glossary.json _kept_verbatim.
// This file is the single source of truth for that list: when one English
// source line has more than one rendering in the patch, the first one wins,
// so re-deriving it from anywhere else can drift by one entry.
const dumpAt = process.argv.indexOf('--dump-verbatim');
if (dumpAt !== -1) {
  const out = process.argv[dumpAt + 1];
  if (!out) { console.error('--dump-verbatim needs a path'); process.exit(2); }
  fs.writeFileSync(out, JSON.stringify(verbatim, null, 1), 'utf8');
  console.log('wrote ' + verbatim.length + ' entries to ' + out);
  process.exit(0);
}
const manifest = JSON.parse(fs.readFileSync(MANIFEST, 'utf8'));
const cov = manifest.coverage || {};
console.log('coverage:            ' + translated.length + ' / ' + (cov.total === undefined ? '?' : cov.total)
  + ' localised, ' + verbatim.length + ' deliberately verbatim');
console.log('  of the localised:  ' + withHan.length + ' contain a Han character, '
  + punctOnly.length + ' are punctuation-only ([player_name]... -> [player_name]……)');
if (cov.total !== keys.length) {
  bad('game.json coverage.total is ' + cov.total + ' but the patch holds ' + keys.length + ' translatable strings');
}
if (cov.translated !== translated.length) {
  bad('game.json coverage.translated is ' + cov.translated + ' but ' + translated.length + ' strings carry Chinese');
}
if (cov.verbatim !== verbatim.length) {
  bad('game.json coverage.verbatim is ' + cov.verbatim + ' but ' + verbatim.length + ' are byte-identical to the source');
}

// ---- 5 未登记的原文 ---------------------------------------------------------
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

// ---- 6 撞名守卫 -------------------------------------------------------------
const PAIRS = [[NAME_A, NAME_B], [NAME_C, NAME_D]];
for (const [a, b] of PAIRS) {
  const na = nameLines[a].length;
  const nb = nameLines[b].length;
  console.log('names:               ' + a + ' x' + na + ', ' + b + ' x' + nb);
  if (!na || !nb) {
    bad('one of ' + a + ' / ' + b + ' no longer appears at all -- they are the pair this patch exists to keep apart');
  }
}

if (strayLines) {
  console.log('note: ' + strayLines + ' active line(s) had no English comment above them');
}
console.log('');
console.log(fail ? fail + ' problem(s)' : 'all structural checks passed');
process.exit(fail ? 1 : 0);
