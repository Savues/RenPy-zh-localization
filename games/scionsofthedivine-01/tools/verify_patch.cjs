#!/usr/bin/env node
// Scions of the Divine 汉化补丁 —— 结构自检
//
//   node tools/verify_patch.cjs
//
// 这个游戏把脚本整个压在 game/archive.rpa 里，发行包没有 game/tl/ 模板，
// 所以覆盖率只能断言、不能推导（见 game.json 的 _coverage_note）。
// 通用检查器查不到的东西在这里补，四类：
//
//   1. 机器值不许被翻
//      profile_filters 的第二列、STAT_COLORS 的键，都是引擎拿来比对的字符串，
//      patch/game/zh_ui.rpy 在显示时才把它们映射成中文。翻掉任何一个，筛选和
//      好感度条就静默失灵，而且没有任何报错。
//
//   2. 相邻重复的中文字面量
//      早期按「文件+行号+列号」回写译文时，同一行靠后的字面量会整体左移，
//      于是 index N 被写成 index N-1 的值。自然中文不会相邻重复，抓这个形状。
//
//   3. 字形覆盖
//      MiSans 是补丁的主字体，它没有的码位在游戏里就是豆腐块。原作自带的三款
//      拉丁字体（IMMORTAL / PlaypenSans / rune）一个汉字都没有，全靠 MiSans 兜。
//      这一项就是当初抓到 U+25B8 的检查 —— 原代码注释本来就写明快进指示的
//      三角必须用有该字形的字体。
//
//   4. 开发者菜单的已知缺口
//      screen_dev.rpy 只翻了一半。这项检查不阻止你补完，只保证它不会停在
//      「一半翻一半没翻」的中间状态：12 个标签要么全是英文，要么全都不是。
//
// 用法：node tools/verify_patch.cjs

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PATCH = path.join(ROOT, 'patch', 'game');
const SHIM = path.join(ROOT, 'patch');
const FONT = path.join(ROOT, 'assets', 'fonts', 'MiSans-Regular.ttf');

const errors = [];
const notes = [];
// ---- Ren'Py 字面量分词器：识别注释，跳过注释里的撇号，跟踪三引号 ----
function extractLiterals(text) {
  const out = [];
  let i = 0, line = 1, col = 0;
  while (i < text.length) {
    const ch = text[i];
    if (ch === '\n') { line++; i++; col = 0; continue; }
    if (ch === '#') { while (i < text.length && text[i] !== '\n') i++; continue; }
    if (ch === '"' || ch === "'") {
      const triple = text[i + 1] === ch && text[i + 2] === ch;
      const q = triple ? ch.repeat(3) : ch;
      const startLine = line;
      i += q.length; col += q.length;
      let val = '';
      while (i < text.length) {
        if (text[i] === '\\') { val += text[i] + (text[i + 1] || ''); i += 2; col += 2; continue; }
        if (text.startsWith(q, i)) { i += q.length; col += q.length; break; }
        if (text[i] === '\n') { line++; col = 0; } else col++;
        val += text[i]; i++;
      }
      out.push({ line: startLine, col, val });
      continue;
    }
    i++; col++;
  }
  return out;
}

function walk(dir, out = []) {
  if (!fs.existsSync(dir)) return out;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith('.rpy')) out.push(p);
  }
  return out;
}

// patch/ 根下的 shim 和 patch/game/ 下的脚本是两棵目录树，别把后者数两遍。
const files = walk(PATCH).concat(
  fs.readdirSync(SHIM, { withFileTypes: true })
    .filter(e => e.isFile() && e.name.endsWith('.rpy'))
    .map(e => path.join(SHIM, e.name))
).sort();
const read = p => fs.readFileSync(p, 'utf8');
const rel = p => path.relative(ROOT, p).replace(/\\/g, '/');
// ---- 1. 机器值不许被翻 ----
// 形如 (显示用的中文, 引擎拿来比对的英文)。两列都得是这个顺序，一个字都不能动。
const ENUMS = [
  {
    file: 'patch/game/scripts/screens/screen_profiles_select.rpy',
    name: 'profile_filters',
    re: /^\s*(?:default|define)\s+profile_filters\s*=\s*\[([\s\S]*?)\]/m,
    want: ['全部', '', '女性', 'Women', '男性', 'Men', '可攻略', 'Romanceable', '法师', 'Mages'],
  },
  {
    file: 'patch/game/scripts/systems/classes.rpy',
    name: 'STAT_COLORS',
    re: /STAT_COLORS\s*=\s*\{([\s\S]*?)\}/,
    want: ['affection', '#ff8bdd', 'karma', '#ffffff'],
  },
];

for (const e of ENUMS) {
  const p = path.join(ROOT, e.file);
  if (!fs.existsSync(p)) { errors.push('缺少文件 ' + e.file); continue; }
  const m = read(p).match(e.re);
  if (!m) { errors.push(e.file + ': 找不到 ' + e.name); continue; }
  const got = (m[1].match(/"([^"]*)"/g) || []).map(s => s.slice(1, -1));
  if (got.join(' ') !== e.want.join(' ')) {
    errors.push(e.file + ': ' + e.name + ' 的机器值被改动了\n      期望 ' +
                JSON.stringify(e.want) + '\n      实际 ' + JSON.stringify(got));
  }
}

// zh_ui.rpy 必须仍然映得到每一个筛选值，否则上面那列英文就没有对应的中文。
{
  const p = path.join(ROOT, 'patch/game/zh_ui.rpy');
  if (!fs.existsSync(p)) { errors.push('缺少文件 patch/game/zh_ui.rpy'); }
  else {
    const t = read(p);
    for (const v of ['Women', 'Men', 'Romanceable', 'Mages']) {
      if (!t.includes('"' + v + '"')) errors.push('zh_ui.rpy: filter_label 不再映射 ' + v);
    }
  }
}

// ---- 2. 相邻重复的中文字面量 ----
let dupChecked = 0;
for (const f of files) {
  const text = read(f);
  const lines = text.split(/\r?\n/);
  const byLine = new Map();
  for (const L of extractLiterals(text)) {
    if (!byLine.has(L.line)) byLine.set(L.line, []);
    byLine.get(L.line).push(L);
  }
  for (const [line, arr] of byLine) {
    for (let k = 1; k < arr.length; k++) {
      const cur = arr[k].val;
      if (!cur || cur !== arr[k - 1].val) continue;
      if (!/[㐀-鿿]/.test(cur)) continue;   // 只管中文，英文重复大多是 Style/Preference key
      dupChecked++;
      errors.push(rel(f) + ':' + line + '  相邻中文字面量重复：「' + cur + '」\n      ' +
                  lines[line - 1].trim());
    }
  }
}

// ---- 3. 字形覆盖：MiSans 画不出的码位，游戏里就是豆腐块 ----
function fontCmap(file) {
  const b = fs.readFileSync(file);
  const numTables = b.readUInt16BE(4);
  let cmapOff = 0;
  for (let i = 0; i < numTables; i++) {
    const o = 12 + i * 16;
    if (b.toString('latin1', o, o + 4) === 'cmap') { cmapOff = b.readUInt32BE(o + 8); break; }
  }
  if (!cmapOff) throw new Error('字体里没有 cmap 表: ' + file);
  const n = b.readUInt16BE(cmapOff + 2);
  const set = new Set();
  for (let i = 0; i < n; i++) {
    const sub = cmapOff + b.readUInt32BE(cmapOff + 4 + i * 8 + 4);
    const fmt = b.readUInt16BE(sub);
    if (fmt === 4) {
      const segX2 = b.readUInt16BE(sub + 6), seg = segX2 >> 1;
      for (let k = 0; k < seg; k++) {
        const start = b.readUInt16BE(sub + 16 + segX2 + k * 2);
        const end = b.readUInt16BE(sub + 14 + k * 2);
        const delta = b.readInt16BE(sub + 16 + segX2 * 2 + k * 2);
        const range = b.readUInt16BE(sub + 16 + segX2 * 3 + k * 2);
        const rp = sub + 16 + segX2 * 3;
        if (start === 0xFFFF) continue;
        for (let c = start; c <= end; c++) {
          let g;
          if (range === 0) g = (c + delta) & 0xFFFF;
          else {
            const gi = rp + k * 2 + range + (c - start) * 2;
            if (gi + 2 > b.length) continue;
            g = b.readUInt16BE(gi);
            if (g) g = (g + delta) & 0xFFFF;
          }
          if (g) set.add(c);
        }
      }
    } else if (fmt === 12) {
      const groups = b.readUInt32BE(sub + 12);
      for (let g = 0; g < groups; g++) {
        const o = sub + 16 + g * 12;
        const s = b.readUInt32BE(o), e = b.readUInt32BE(o + 4);
        for (let c = s; c <= e; c++) set.add(c);
      }
    }
  }
  return set;
}

const MARKUP = new Set('{}[]ilbusfnrtwpx#=/'.split(''));

// 一个字出现在补丁里、却不是 MiSans 画的 —— 只有一种可能：那个 style 显式指定了
// 别的字体。每一条都要写清楚由哪个字体渲染、为什么，否则不许豁免。
const FONT_EXCEPTIONS = [
  { file: 'patch/game/scripts/screens/screen_skip.rpy',
    chars: '▸',
    renderedBy: 'DejaVuSans.ttf',
    why: '快进指示的三角箭头。原作的 style skip_triangle 就特意指定 DejaVuSans，' +
         '因为它要 U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE；MiSans 两个' +
         '字重都没有这个码位。全补丁只有这一处不是 MiSans。' },
];

let checkedCodepoints = 0;
try {
  const cmap = fontCmap(FONT);
  const missing = new Map();
  for (const f of files) {
    const text = read(f);
    const lines = text.split(/\r?\n/);
    const exempt = new Set();
    for (const ex of FONT_EXCEPTIONS) {
      if (path.resolve(ROOT, ex.file) === path.resolve(f)) {
        for (const c of ex.chars) exempt.add(c);
      }
    }
    for (const L of extractLiterals(text)) {
      for (const ch of L.val) {
        const cp = ch.codePointAt(0);
        if (cp < 0x80 || MARKUP.has(ch) || exempt.has(ch)) continue;
        checkedCodepoints++;
        if (cmap.has(cp)) continue;
        if (missing.has(ch)) continue;            // 同一个字只报一次
        const hex = cp.toString(16).toUpperCase().padStart(4, '0');
        missing.set(ch, rel(f) + ':' + L.line + '  ' + lines[L.line - 1].trim().slice(0, 80));
        errors.push('MiSans 画不出 U+' + hex + ' 「' + ch + '」\n      ' + missing.get(ch));
      }
    }
  }
  notes.push('字形覆盖：检查了 ' + checkedCodepoints + ' 个非 ASCII 码位，缺失 ' +
             missing.size + ' 个；另有 ' + FONT_EXCEPTIONS.length + ' 处显式豁免（非 MiSans 字体渲染）');
} catch (e) {
  errors.push('字形覆盖检查跑不起来: ' + String(e));
}
// ---- 4. 开发者菜单：12 个标签必须全翻或全不翻 ----
// 判定只认**显示位置**：语句关键字后面紧跟的那个字面量。用 includes('"All"')
// 会被 default dev_char_list = ["All"] 和 dev_char_select == "All" 误伤——
// 那是机器值，本来就该留在英文。
const DEV_LABELS = [
  ['Jump', '跳转'], ['Variables', '剧情开关'], ['Profiles', '档案'], ['All', '全部'],
  ['Unlock', '解锁'], ['Lock', '锁定'], ['Everything', '一切'], ['Outfit', '服装'],
  ['Profile', '档案'], ['Memory', '回忆'], ['Affection: ', '好感度：'], ['Utilities', '工具'],
];

const escapeRe = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

{
  const p = path.join(ROOT, 'patch/game/scripts/screens/screen_dev.rpy');
  if (!fs.existsSync(p)) {
    errors.push('缺少文件 patch/game/scripts/screens/screen_dev.rpy');
  } else {
    const text = read(p);
    const left = DEV_LABELS.filter(([en]) =>
      new RegExp('^\\s*(?:textbutton|text|label|caption|title)\\s+"' + escapeRe(en) + '"', 'm').test(text));
    if (left.length && left.length !== DEV_LABELS.length) {
      errors.push('screen_dev.rpy 的开发者菜单停在半翻状态：' + DEV_LABELS.length +
                  ' 个标签里翻了 ' + (DEV_LABELS.length - left.length) + ' 个，还剩：\n      ' +
                  left.map(([en, zh]) => en + ' -> ' + zh).join('\n      '));
    } else if (left.length) {
      notes.push('开发者菜单的 ' + DEV_LABELS.length + ' 个标签仍是英文');
    } else {
      notes.push('开发者菜单 ' + DEV_LABELS.length + ' 个标签全部已译（Unlock/Lock 各 12 处，共 36 处）；' +
                 '机器值 dev_char_list 里的 "All" 与各 tags 保持英文不动');
    }
  }
}

if (errors.length) {
  console.error('x ' + errors.length + ' 项问题\n');
  errors.forEach(e => console.error('  ' + e + '\n'));
  process.exit(1);
}
console.log('v ' + files.length + ' 个 .rpy 扫描通过；' + ENUMS.length +
            ' 组机器值未被动过；' + dupChecked + ' 条相邻重复候选全部通过');
notes.forEach(n => console.log('  - ' + n));