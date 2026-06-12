# NZ Daily HTML Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create 14 daily itinerary pages + 1 overview page for the 2026 NZ South Island road trip, following the Osaka trip HTML design pattern.

**Architecture:** Each page is a standalone HTML file with inlined CSS. Light theme (#F0F4F8 bg, white cards, Inter font). Per-day accent colour in CSS `--a` variable. Pages are linked via sticky top nav (day pills) and fixed bottom prev/next buttons.

**Tech Stack:** Vanilla HTML/CSS/JS, Leaflet.js (overview map only), localStorage (checkbox persistence)

---

## Files

| File | Day | Route |
|------|-----|-------|
| `2026-09-028-NZ/html/index.html` | Overview | — |
| `2026-09-028-NZ/html/day01-0927.html` | D1 9/27 | 抵達基督城 |
| `2026-09-028-NZ/html/day02-0928.html` | D2 9/28 | CHC → Lake Tekapo |
| `2026-09-028-NZ/html/day03-0929.html` | D3 9/29 | Tekapo → Mt Cook |
| `2026-09-028-NZ/html/day04-0930.html` | D4 9/30 | Mt Cook 整天 |
| `2026-09-028-NZ/html/day05-1001.html` | D5 10/1 | Mt Cook → Wanaka |
| `2026-09-028-NZ/html/day06-1002.html` | D6 10/2 | Wanaka 整天 |
| `2026-09-028-NZ/html/day07-1003.html` | D7 10/3 | Wanaka → Queenstown |
| `2026-09-028-NZ/html/day08-1004.html` | D8 10/4 | QT 跳傘日 |
| `2026-09-028-NZ/html/day09-1005.html` | D9 10/5 | QT Luge 日 |
| `2026-09-028-NZ/html/day10-1006.html` | D10 10/6 | QT → Te Anau |
| `2026-09-028-NZ/html/day11-1007.html` | D11 10/7 | Te Anau → Franz Josef |
| `2026-09-028-NZ/html/day12-1008.html` | D12 10/8 | 冰川健行 → Punakaiki |
| `2026-09-028-NZ/html/day13-1009.html` | D13 10/9 | Punakaiki → CHC |
| `2026-09-028-NZ/html/day14-1010.html` | D14 10/10 | 出境 |

## Design Rules

- Per-day accent: `--a` (primary), `--al` (light bg), `--am` (mid, used for timeline line)
- Day colour map: D1=#1e6091, D2=#7c3aed, D3-4=#2d6a4f, D5-6=#b45309, D7-9=#ea580c, D10=#78350f, D11=#374151, D12=#065f46, D13=#0369a1, D14=#1e6091
- Drive time between stops: small grey badge `🚗 約 Xh Xm · Xkm`
- Key events (departure/arrival): filled dot (class `key`)
- Bottom nav: ← prev | next → fixed
- localStorage key prefix: `nz26_dN_` where N = 2-digit day number
