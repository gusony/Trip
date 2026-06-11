# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static travel-planning site — no build tools, no bundler, no tests. All files are hand-written HTML/CSS and Markdown. Open any `.html` directly in a browser.

## Folder conventions

Each trip lives in its own folder named `YYYY-MM-location` (e.g. `2026-05-osaka`).

Standard contents per trip folder:

| File | Purpose |
|------|---------|
| `00-overview.md` | Dates, flights, accommodation, budget |
| `01-day1-*.md` … `0N-dayN-*.md` | Per-day itineraries |
| `transport.md` | Transport options and tickets |
| `restaurants.md` | Restaurant shortlist and reservation status |
| `packing.md` | Packing list and pre-departure checklist |
| `html/` or trip root | Rendered HTML views |

HTML entry points per trip:
- Osaka → `2026-05-osaka/html/index.html`
- Tokyo → `2026-07-03-Tokyo/trip.html`
- NZ → `2026-09-028-NZ/NZ-2026-travel-plan.html`

The landing page `index.html` at repo root links to each trip.

## Design system (HTML pages)

All pages use **Inter** (Google Fonts) with no external CSS framework.

**Color palette per trip:**

| Trip | Accent | CSS class |
|------|--------|-----------|
| Osaka | Blue → Indigo (`#3B82F6` → `#6366F1`) | `.card-osaka` |
| Tokyo | Purple → Orange (`#7C6AFF` → `#E8956D`) | `.card-tokyo` |
| NZ | Teal → Green (`#10B981` → `#06B6D4`) | `.card-nz` |

**Background tones:**
- Landing page: `#0B0F1A` (near-black, dark navy)
- Trip detail pages: `#0f0f14` (darker)

Trip cards on the landing page follow this structure: coloured top band → emoji + badge → title + date → tags → footer with status dot (green = done, amber pulse = in progress).

## Adding a new trip

1. Create folder `YYYY-MM-location/` with the standard Markdown files.
2. Build the HTML view following the existing dark-card pattern with a new accent color.
3. Add a card to `index.html` using the `.trip-card` markup pattern; pick a new CSS class name and define the matching `.card-band` gradient, `.card-badge` tint, and hover `box-shadow`.
4. Add the trip to the table in `README.md`.

## Language

All content and UI text is **Traditional Chinese (繁體中文)**. HTML `lang` attribute should be `zh-TW` or `zh-Hant`.
