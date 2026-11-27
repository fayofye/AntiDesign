# Evals

Five product briefs and a rubric, to check each version of the skill before publishing and to catch regressions. Every product, figure and name below is invented for the test.

## How to run

1. For each brief, open a fresh agent session with the skill installed and send: "Use antidesign to design three landing pages for this product." followed by the brief.
2. Once per version, run one brief in a fresh session **without** the skill, as the control.
3. Run `python3 scripts/skeleton.py` on every page and screenshot each page and its skeleton at 1280px and 390px.
4. Score each design against the rubric yourself; don't use the agent's own trait table. Log the result at the bottom.

## Briefs

### 1. Halden Mutual (a member-owned savings bank) · expect quiet
- Easy-access saver: 3.10% AER variable. 95-day notice saver: 3.60% AER variable. No fees. Open with £1.
- Member-owned since 1874, 41 branches.
- Must stay word for word: "Halden Mutual is owned by its members, not by shareholders."
- Brand: colour Halden green `#1F4D3A` on white is locked (`--keep colour`).
- Gated, never advertise: joint accounts (early access).

### 2. Tally Ledger (B2B software that matches bank lines to invoices) · expect quiet
- Starter $29 a month: 1 bank connection, 500 lines. Team $99 a month: 5 connections, 5,000 lines. Enterprise: contact sales.
- In a sample of 40 customers, 87% of lines matched with no human touch.
- Exports to the three largest accounting packages (don't name them).
- Gated, never advertise: AI dispute drafting (behind a flag).

### 3. Brasa Nove (a wood-fire restaurant) · expect loud
- Open Tuesday to Saturday, 17:00 to 23:00. Book online for up to 8; larger groups by phone.
- Menu: flatbread with lardo 9, charred leeks with romesco 11, clams in cider 16, half chicken 24, rib-eye for two 68, burnt cheesecake 8 (euros).
- Must stay word for word: "Everything on the menu touches the fire."

### 4. Riverkeep (a charity that cleans rivers) · either tone, defend it
- Last year 2,140 volunteers removed 38 tonnes of litter from 61 km of river.
- £12 a month kits out one volunteer for a year of cleanups.
- Registered charity 1189204 (fictional).
- Brand: the wordmark is set in Literata and is locked (`--keep type`).

### 5. Driftwood (an open-source command-line tool for database migrations) · expect loud
- Commands: `drift plan`, `drift apply`, `drift undo`. Supports Postgres, MySQL and SQLite.
- Free and open source (MIT). Driftwood Cloud: free for 3 projects; Team $20 per seat a month.
- Gated, never advertise: SQL Server support (beta).

## Rubric

Score each design 0 (fails), 1 (partly) or 2 (passes) on each line; 18 is the top score.

| # | Check | Passes when |
|---|---|---|
| 1 | Skeleton | Its skeleton shows at most two default shapes from the default table, besides locked traits (no headline beside a picture, no bar of links, no three pricing columns) |
| 2 | Traits | At most two of the eleven traits kept, besides locked ones, judged by you |
| 3 | Five seconds | At 390px the first screen says what it is, who it's for and what to do next |
| 4 | Truth | Every fact and price matches the brief, the word-for-word line is exact, the gated feature is absent, samples are labelled |
| 5 | Access | Contrast holds, everything works by keyboard, reduced motion is respected, inputs are labelled |
| 6 | Function | No horizontal overflow at 390px, no console errors, fallbacks work |
| 7 | Craft | At most five type sizes and four colours, tabular figures for money, a grid you can find |
| 8 | Tone | The tone fits the brief (or is defended), and a batch of three mixes tones |
| 9 | Fresh | No choice repeats across the batch, and nothing is a demo or specimen of this skill shipped as it stands |

## Results

| Version | Date | Brief | Designs | Scores | Control | Notes |
|---|---|---|---|---|---|---|
| 1.5.0 | 2026-11-27 | 1 Halden Mutual | quiet, quiet, loud | 17, 18, 18 | 11 / 16 | Ruler nav read as a top bar; three quiet roll options equal to the default were fixed. `runs/1.5.0/NOTES.md` |
| 1.5.0 | 2026-11-27 | 3 Brasa Nove | loud, quiet, loud | 18, 18, 18 | — | All checks clean in Chrome and WebKit. `runs/1.5.0/NOTES.md` |
