---
name: antidesign
description: Design web pages that break the conventions an AI model reaches for by default. Use when someone asks for an unconventional, unexpected, experimental or "not AI-looking" website, landing page or UI; when a serious product (a bank, a law firm, B2B software) needs a page that is distinctive but still credible; when they say designs look templated, safe or alike; when they ask for designs you would not make on your own; or when they want buttons, animations, heroes, layouts, textures or type that are not the usual.
license: MIT
metadata:
  version: "1.5.0"
---

# AntiDesign

Your first design is your most probable one. This skill makes you write that design down, then move away from it on purpose, while the page stays true, usable and accessible.

## 1. Write down the default first

Before any new design, fill in this table for the product: the page you would make unprompted. Build it as `baseline` when the user wants to compare.

| Trait | The default to expect from yourself |
|---|---|
| Reading direction | Vertical scroll, left to right |
| Layout | Centred container, grid, stacked sections |
| Navigation | Logo left, links, a button far right; a footer of link columns |
| Hero | Eyebrow pill, headline, subhead, two buttons, a product shot beside them |
| Components | Cards, icons in rounded squares, numbered steps, accordions |
| Type | One sans for everything, or a serif display over a sans |
| Colour | Dark with a blue-violet gradient, or cream with a clay accent |
| Texture | Soft shadows, glows, glass blur |
| Pricing | Three cards or columns side by side, the middle one highlighted, a monthly/yearly toggle |
| Voice | Calm product marketing |
| Motion | None, or fade-ins on scroll |

Where a line names two defaults ("or"), the design must avoid both. This skill's own demos (the README's `demo/` shots and the pages in `elements/` and `library/`) count as default too: never rebuild them as they stand.

## 2. Pick a tone, lock the brand

- **Loud** is strange on purpose: games, odd reading directions, display faces, clashing colour.
- **Quiet** is unusual but credible: a strict grid broken once, a datasheet, an annual report, one spot colour. Quiet is not the default in disguise; it breaks as many traits as loud does.

Take the tone the user asks for. Otherwise go quiet for products that hold money, health, law or a buyer's job, and loud for the rest; in a batch of three or more, give at least one design the other tone.

If the product already has a brand (a logo, colours, typefaces), those traits are locked: build them from the brand, pass them to the roll with `--keep` (for example `--keep colour,type`), and never let a move override them.

## 3. Five moves

Give each design its own move; combine them when it helps.

1. **Invert.** Write your own opposite for every line. The first opposite that comes to mind is the next default, so take the second or third. Then find one idea from the product's world that ties the opposites into a single page; without it they read as eleven separate tricks. Stuck on a line: `python3 scripts/roll.py --trait <trait> --tone <tone>` gives one unusual option for it.
2. **Let the data draw.** Make the layout the product's own numbers: blocks sized by value, copy riding a chart line, a hero that is the calculation. Inputs that reshape the page beat static figures.
3. **Become a domain artifact.** Ask which physical object the product's world already trusts (banknote, bond coupon, ledger, ticket, receipt, field guide, scoreboard) and make the page that object, down to its craft details: guilloché, microtext, perforations, serial numbers.
4. **Borrow a movement.** Run `python3 scripts/roll.py --movement --tone <tone>`. It names a design movement and its rules (Swiss International Style, Constructivism, a 1970s identity manual and others). Follow every rule strictly across all eleven traits: a movement's rules are what keep a strange page looking professional. Borrow the movement's system, never one designer's named work.
5. **Roll.** Run `python3 scripts/roll.py --count N --tone <tone>` from this skill's folder, with `--keep` for brand traits. It rolls all eleven traits, a hundred billion combinations per tone. Build exactly what it rolls. If you cannot run commands, ask the user to run it and paste the output; never invent a roll. When two rolled options clash (a terminal in a handwriting font), keep both and settle it toward the stranger reading, never toward the default. If an option built plainly would come out as the default (bordered cards in a grid, numbered steps), build it so it doesn't. Never reroll for taste.

In one batch, no choice appears in two designs, rolled or your own, and near-duplicates count (two typewriter faces, two yellows, two grid-based movements). If a roll repeats one, reroll that trait only.

## 4. Ready-made elements and the library

`elements/` holds working, self-contained demos: a 3D liquid shader with 180 models, banknote security print, neon with a counting number, copy that flows along a data line, a commentary quiz, a slot machine and a money map. Read `references/elements.md` when a design needs one. Elements are optional, and most designs need none. When you use one: at most one per design, never the same one twice in a batch, and always re-cut to the product (its copy, numbers and colours).

`library/` holds smaller parts as numbered specimens on six pages: buttons, motion, heroes, type, layouts and textures; `references/library.md` lists them. Layouts and textures follow the trait: when a rolled reading direction or texture names a specimen, open that one, since it already handles phones, keyboards and reduced motion. For the other pages, never pick a specimen by taste: run `python3 scripts/roll.py --library <page>` (`--count N` for a batch, which never repeats) and build what it rolls. Take at most one specimen from each page per design, and never ship one as it stands: change its copy, colours and type to the product's, so it reads as part of that page and not as a sticker on it.

## 5. The safe-table trap

A list of options written from your own taste holds only options you already like, so every pick comes out safe. Any table you write yourself, and this skill's own examples, are starting points to move past, not a menu.

## 6. Never break these

- **Truth.** Use the product's real facts and prices. Before writing, search the codebase for copy that must stay word for word (slogans, legal lines) and for features behind flags or early access; never advertise a gated feature. Label sample figures as illustrative and make them add up across every design. Label a game's or simulation's numbers as invented. No made-up stats, testimonials, people or client logos.
- **Access.** Text contrast 4.5:1 (3:1 at 24px and up), real buttons, links and labelled inputs, keyboard reachable, `prefers-reduced-motion` respected. Never lock the page behind input: a form-first or game-first hero starts pre-filled or has a way past it. However strange the navigation, every section stays reachable by plain links.
- **Function.** Works at phone width. Put `writing-mode: vertical-rl` on a full-width scroll box (`width: 100%`), never on `html` or `body`: phones zoom the whole page out to fit it. Inside vertical-rl, flex `row` runs top to bottom; use `flex-direction: column` to lay blocks right to left. WebGL and animation each get a fallback.
- **Fonts.** Previews often have no network. When a move lives in the font (variable axes, a neon or stencil face), self-host it if you can; otherwise link it and pick a local fallback that keeps the idea.
- **Identity.** Never copy a real brand's look or a named existing site.

## 7. Make it good

Strange reads as intentional when everything around the break is strict.

- **System.** At most five type sizes on one scale. One spacing unit, every gap a multiple of it. At most four colours, each with one job (ground, ink, accent, signal). A grid even where the page breaks it: a break only reads against something.
- **Detail.** Tabular figures for money and tables. Real quotes, dashes and ×. Body lines of 45 to 75 characters; `text-wrap: balance` on headings, `pretty` on paragraphs. The small print, captions, serials and edges get the care the hero gets.
- **Images.** Use the product's own photos and screenshots, treated so they share the page's colours and texture (duotone, halftone, dither, hard crops: `library/textures.html`), or draw in SVG. No stock people at laptops, no generated faces, no empty gradient where an image should be.
- **Five-second test.** At 390px, the first screen says what the product is, who it is for and what to do next, in words a visitor reads without touching anything.

## 8. Prove it broke

- **Skeleton.** Run `python3 scripts/skeleton.py <page>` for each design. It writes a copy beside the page with fonts, colours, shadows and images stripped and every box outlined. Screenshot it and hold it against the default table (and the baseline's skeleton, if you built one). Wherever the shape is the default (a headline beside a picture, a bar of links across the top, three pricing columns in a row), that trait is kept, whatever the skin says. Delete the skeleton copies afterwards.
- **Traits.** For every design, write a table of the eleven traits marking each one kept, broken or locked, judging the shape from the skeleton. A trait that is only partly broken counts as kept. A design keeps at most two traits besides locked ones; push any design past that further before handing it over.
- **Screens.** Screenshot every design at desktop (1280px) and phone (390px) widths and fix what breaks. If you cannot take screenshots, say so.
- **Logic.** Money, scoring or game logic gets a small assert-based test; a self-check that runs when the page loads is enough.
- **Report** what you could not check and the riskiest part of each design.
