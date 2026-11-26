---
name: anti-default-design
description: Design web pages that break the conventions an AI model reaches for by default. Use when someone asks for an unconventional, unexpected, experimental or "not AI-looking" website, landing page or UI; when they say designs look templated, safe or alike; or when they ask for designs you would not make on your own.
---

# Anti-default design

Your first design is your most probable one. This skill makes you name that design, then move away from it on purpose, while the page stays true, usable and accessible.

## 1. Write down the default first

Before any new design, list the page you would make unprompted, line by line, using the traits below. Build it only if the user wants a baseline. Every later design must differ from that list on most lines.

| Trait | The default to expect from yourself | Ways to break it |
|---|---|---|
| Reading direction | Vertical scroll, left to right | Horizontal scroll; vertical columns read right to left; one screen that changes in place |
| Layout | Centred container, grid, stacked sections | Layout computed from the data; a 2D surface; the page as one real-world object |
| Hero | Headline, subhead, two buttons, product shot | A working machine (calculator, slot machine, quiz); one giant number; no headline |
| Components | Cards, icons in rounded squares, accordions | Tables, ledgers, coupons, tickets, specimen cards, a stack you flip |
| Type | One sans for everything, or serif display over sans | One display face for everything; a variable axis driven by layout; text on a path |
| Colour | Dark with a blue-violet gradient, or cream with a clay accent | Mid-tones; clashing flats; greys only; print inks (intaglio, riso, safety colours) |
| Pricing | Three cards, the middle one highlighted | Sizes proportional to price; one sentence; coupons; seat classes; a fee schedule |
| Voice | Calm product marketing | A genre: field guide, sports commentary, boarding pass, legal instrument, ledger |
| Motion | None, or fade-ins | A shader, a counter, spinning reels, glitch; interaction the visitor drives |

## 2. Four moves

Give each design its own move; combine them when it helps.

1. **Invert.** Flip every line of the default list. This is the "exact opposite" design.
2. **Let the data draw.** Make the layout the product's own numbers: blocks sized by value, copy riding a chart line, a hero that is the calculation. Inputs that reshape the page beat static figures.
3. **Become a domain artifact.** Ask which physical object the product's world already trusts (banknote, bond coupon, ledger, ticket, receipt, field guide, scoreboard) and make the page that object, down to its craft details: guilloché, microtext, perforations, serial numbers.
4. **Roll.** Run `python3 scripts/roll.py --count N` from this skill's folder. Its table holds 6 traits × 10 unusual choices, a million combinations. Build exactly what it rolls, overlaps included. Never reroll for taste: that rebuilds the default.

## 3. The safe-table trap

A list of options you write from your own taste holds only options you already like, so every pick comes out safe. Any table you write yourself must be filled with choices you would normally reject.

## 4. Never break these

- **Truth.** Use the product's real facts and prices. Label sample figures as illustrative and make them add up across every design. No invented stats, testimonials or client logos.
- **Access.** Text contrast 4.5:1 (3:1 at 24px and up), real buttons, links and labelled inputs, keyboard reachable, `prefers-reduced-motion` respected.
- **Function.** Works at phone width, even if that means a horizontal scroll box. WebGL, custom fonts and animation each get a fallback.
- **Identity.** Never copy a real brand's look or a named existing site.

## 5. Build and report

- One self-contained page per design, in the project's own stack or plain HTML.
- Money, scoring or other logic gets a small assert-based test before you hand it over.
- In `writing-mode: vertical-rl`, a flex `row` runs top to bottom; use `flex-direction: column` to lay blocks right to left.
- Before handing over, ask of each design: would I have made this unprompted? If yes, push it further.
- Report what you could not check (rendering, shader output, font loading) and the riskiest part of each design.
