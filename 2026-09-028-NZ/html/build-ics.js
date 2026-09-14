// 由 reminders.html 的事件資料產生靜態 .ics
// 為什麼要靜態檔：iOS Safari 拒絕下載 blob: 來源的 text/calendar，
// 只信任伺服器回應的 Content-Type，所以必須是真的檔案。
// 用法：node build-ics.js
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, 'reminders.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1].split('/* ---------- 綁定 ---------- */')[0];

const { EVENTS, SORTED, SCOPES, buildICS } =
  new Function(script + ';return {EVENTS, SORTED, SCOPES, buildICS};')();

// 固定 DTSTAMP：內容沒變時產物就不變，git diff 才乾淨
const STAMP = '20260101T000000Z';

const outDir = path.join(__dirname, 'ics');
fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir);

const write = (name, list) => {
  fs.writeFileSync(path.join(outDir, name + '.ics'), buildICS(list, STAMP), 'utf8');
  return list.length;
};

let n = 1;
console.log('all.ics', write('all', SORTED));
for (const key of Object.keys(SCOPES)) {
  console.log(key + '.ics', write(key, SORTED.filter(SCOPES[key].fn)));
  n++;
}
EVENTS.forEach(e => { write(e.id, [e]); n++; });
console.log('共 ' + n + ' 個檔 → ics/');

// 自檢：unfold 後每一行都必須是合法的 property，且 BEGIN/END 成對
const assert = require('assert');
for (const f of fs.readdirSync(outDir)) {
  const raw = fs.readFileSync(path.join(outDir, f), 'utf8');
  assert(raw.endsWith('\r\n'), f + ' 結尾缺 CRLF');
  const lines = raw.replace(/\r\n[ \t]/g, '').split('\r\n').filter(Boolean);
  let depth = 0, events = 0;
  for (const line of lines) {
    assert(/^[A-Z][A-Z0-9-]*(;[^:]+)?:/.test(line), f + ' 非法行：' + line.slice(0, 40));
    if (line.startsWith('BEGIN:')) depth++;
    if (line.startsWith('END:')) depth--;
    if (line === 'BEGIN:VEVENT') events++;
  }
  assert(depth === 0, f + ' BEGIN/END 不配對');
  assert(events > 0, f + ' 沒有事件');
}
console.log('自檢通過：' + fs.readdirSync(outDir).length + ' 個檔');
