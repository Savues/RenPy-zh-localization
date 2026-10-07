#!/usr/bin/env node
// Cosy Cafe 汉化补丁 —— 结构自检
//
// 背景：早期回写脚本按「文件 + 行号 + 列号」定位字面量。中文比英文短，
// 同一行里靠后的字面量会整体左移，再跑一次就写错位置。实际翻车的是
// scripts/flags.rpy 的 WeekDays：index 3 被写成了 index 2 的值，
// 导致第 6 / 13 / 20 / 27 天在 HUD 上显示「星期三」。
//
// 这个脚本不需要英文原文，只查两类会把 bug 挡下来的特征：
//   1. 已知枚举被改坏（WeekDays / Time 必须是完整的 7 项 / 5 项）
//   2. 同一行里相邻的两个中文字面量重复（自然中文枚举不会相邻重复）
//
// 用法：node tools/verify_patch.cjs

const fs = require('fs');
const path = require('path');

const PATCH = path.join(__dirname, '..', 'patch', 'game');

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
      const startLine = line, startCol = col;
      i += q.length; col += q.length;
      let val = '';
      while (i < text.length) {
        if (text[i] === '\\') { val += text[i] + (text[i + 1] || ''); i += 2; col += 2; continue; }
        if (text.startsWith(q, i)) { i += q.length; col += q.length; break; }
        if (text[i] === '\n') { line++; col = 0; } else col++;
        val += text[i]; i++;
      }
      out.push({ line: startLine, col: startCol, val });
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

// ---- 1. 已知枚举 ----
const ENUMS = [
  { file: 'scripts/flags.rpy', name: 'WeekDays',
    want: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'] },
  { file: 'scripts/flags.rpy', name: 'Time',
    want: ['黎明', '上午', '下午', '傍晚', '夜晚'] },
];

const errors = [];

for (const e of ENUMS) {
  const p = path.join(PATCH, e.file);
  if (!fs.existsSync(p)) { errors.push(`缺少文件 ${e.file}`); continue; }
  const text = fs.readFileSync(p, 'utf8');
  const re = new RegExp('^\\s*(?:default|define)\\s+' + e.name + '\\s*=\\s*\\[(.*)\\]\\s*$', 'm');
  const m = text.match(re);
  if (!m) { errors.push(`${e.file}: 找不到 ${e.name} 枚举`); continue; }
  const got = m[1].split(',').map(s => s.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
  if (got.join('|') !== e.want.join('|')) {
    errors.push(`${e.file}: ${e.name} 被改坏\n    期望 ${JSON.stringify(e.want)}\n    实际 ${JSON.stringify(got)}`);
  }
}

// ---- 2. 相邻重复的中文字面量 ----
const files = walk(PATCH);
let dupChecked = 0;
for (const f of files) {
  const text = fs.readFileSync(f, 'utf8');
  const lines = text.split(/\r?\n/);
  const lits = extractLiterals(text);
  const byLine = new Map();
  for (const L of lits) {
    if (!byLine.has(L.line)) byLine.set(L.line, []);
    byLine.get(L.line).push(L);
  }
  for (const [line, arr] of byLine) {
    for (let k = 1; k < arr.length; k++) {
      const prev = arr[k - 1].val, cur = arr[k].val;
      if (!cur || cur !== prev) continue;
      if (!/[㐀-鿿]/.test(cur)) continue;   // 只管中文，英文重复大多是 ColorizeMatrix / Preference key
      dupChecked++;
      errors.push(`${path.relative(PATCH, f)}:${line}  相邻中文字面量重复：「${cur}」\n    ${lines[line - 1].trim()}`);
    }
  }
}

if (errors.length) {
  console.error(`✗ ${errors.length} 项问题\n`);
  errors.forEach(e => console.error('  ' + e + '\n'));
  process.exit(1);
}
console.log(`✓ ${files.length} 个 .rpy 扫描通过；${ENUMS.length} 个枚举正确；${dupChecked + 0} 条相邻重复候选全部通过`);
