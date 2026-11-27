# Brasa Nove: three AntiDesign landing pages

Skill: `/Users/fayo/AntiDesign/SKILL.md`, version 1.5.0. Every fact on the pages comes from the brief: open Tuesday to Saturday, 17:00 to 23:00; book online up to 8, larger groups by phone; flatbread with lardo 9, charred leeks with romesco 11, clams in cider 16, half chicken 24, rib-eye for two 68, burnt cheesecake 8 (euros); "Everything on the menu touches the fire." appears word for word in all three. "Closed Sunday and Monday" is derived from the opening days. The brief gives no phone number, address or booking system. So the pages say "by phone" without a number, and every booking form says on the page that nothing is sent.

## The default first (section 1)

This is the page I would have made without the skill.

| Trait | My default for Brasa Nove |
|---|---|
| Reading direction | Vertical scroll |
| Layout | Centred container: hero, menu, hours, booking, stacked |
| Navigation | Logo left; Menu, Hours, Book links; a "Book a table" button far right; footer columns |
| Hero | Full-bleed photo of flames, "Cooked over fire", two buttons (Book, See the menu) |
| Components | Menu in two columns with dotted leaders, icons beside the hours |
| Type | Serif display over a sans |
| Colour | Charcoal with an ember-orange accent, or cream with clay |
| Texture | Grain, soft shadows, an ember glow |
| Pricing | Menu list, prices right-aligned |
| Voice | Warm hospitality copy |
| Motion | Fade-ins on scroll |

Tones: a restaurant holds no money, health or law, so the default is loud. In a batch of three, at least one design takes the other tone. Design 1 and design 3 are loud; design 2 is quiet.

---

## Design 1: "Check in for the fire" (`design-1.html`)

- **Tone:** loud
- **Move:** Roll (5), built exactly as rolled; one trait rerolled for a batch clash (see below)
- **The idea that ties it:** a round wood fire seen from above through a thermal camera. You check in like a flight before the camera warms up. The rim of the hearth holds the sections. The menu is a team sheet whose squad numbers are the prices.

Roll output, verbatim (`python3 scripts/roll.py --count 1 --tone loud`):

```
Design 71314933890  (loud; drawn: 14009857467 22911609462 11798216756 78915831614 93000562614 71314933890)
  Reading direction: Read around a circle (library/layouts.html#lay-08)
  Layout: One real-world object fills the page
  Navigation: A map legend: each section is a place
  Hero: A form you fill before you see anything
  Components: Index tabs down one edge
  Type: A colour 3D font (Nabla)
  Colour: Thermal camera
  Texture: Glitch and RGB split (library/textures.html#tex-04)
  Pricing: Team sheets
  Voice: A boarding pass
  Motion: A WebGL shader
```

Reroll of one trait only (`python3 scripts/roll.py --trait navigation --tone loud`). The rolled "map legend" nav nearly duplicates design 2, whose movement roll is a topographic map with a legend.

```
Navigation (loud): Footnotes: every link is a numbered note
```

Library specimens: `lay-08` Ring and `tex-04` RGB split, both named by the roll and re-cut to the product.

| Trait | What was built | Status |
|---|---|---|
| Reading direction | Six places sit around the hearth's rim. The ring turns the short way until the chosen place is at the top; you read it in the centre. Arrow keys, marks and footnotes all turn it. | broken |
| Layout | One object fills the screen: the round hearth. Day tabs, the name and the notes sit on its edges; nothing is stacked. | broken |
| Navigation | Numbered footnotes 1–6. Each note is a link that turns the ring to its place. No top bar, no footer columns. | broken (rerolled) |
| Hero | A check-in form comes before the fire: party, day, boarding time. It starts pre-filled. "Skip, show the fire" gets past it, and so does any footnote link. | broken |
| Components | Index tabs down the left edge are the departure days, Tue–Sat. Sun and Mon are shown shut and disabled. | broken |
| Type | Nabla (colour 3D) for the name, the squad numbers and the marks; system monospace for text. If Nabla fails to load, a shadow extrusion stands in. | broken |
| Colour | Thermal camera: cold violet-black ground, white-hot ink, ember orange accent, flare magenta signal. The shader paints the ramp between them. | broken |
| Texture | RGB split on the one headline (the house rule), with flare and ember fringes. The jitter only runs without reduced motion. | broken |
| Pricing | Team sheet in three pairs (front two, middle two, back two). Squad number = price in euros, and the page says so. | broken |
| Voice | Boarding pass: check in, departures, boarding from 17:00, the gate closes at 23:00, group travel. | broken |
| Motion | WebGL thermal shader of the fire. It warms from cold to hot on check-in. Under reduced motion it draws one static frame; without WebGL, a CSS radial gradient stands in. | broken |

Kept: 0. The skeleton shows a tab strip on the left edge, one large circle with six marks around it, and a narrow column with the name and notes. There is no headline beside a picture, no link bar and no stacked sections.

Self-checks on load (console.assert): the menu on the page matches the facts; party routing (8 online, 9+ by phone); time slots sit inside 17:00–23:00; the open days are Tue–Sat; the ring turns the short way.

---

## Design 2: "Sheet 1: the menu and the fire" (`design-2.html`)

- **Tone:** quiet
- **Move:** Borrow a movement (4)
- **The idea that ties it:** a survey sheet where each dish is a hill. Spot heights are prices in euros, with a contour every €4. The fire is one line across the sheet, and the foot of every hill touches it. The fire line is lettered with the house rule.

Roll output, verbatim (`python3 scripts/roll.py --movement --tone quiet`):

```
Movement (quiet): Topographic survey map
  Follow its rules: thin precise lines, labels set along the features, a legend, a scale bar, contour tints
```

How the movement's rules were followed:

- **Thin precise lines:** hairline grid, 0.8 contours, an index contour every €20.
- **Labels set along the features:** dish names run along each hill's foot; the house rule runs along the fire line.
- **A legend:** in the margin.
- **A scale bar:** it counts guests, 0–8 online, then a dashed run marked "9+ ☎".
- **Contour tints:** one ochre stepped by height, so the same price gets the same tint on every hill.

No library specimen was used.

| Trait | What was built | Status |
|---|---|---|
| Reading direction | One sheet, read by grid reference (A–F, 1–8). On desktop the whole sheet fits with no page scroll. A phone pans east across it: map, then booking, then legend and index. | broken |
| Layout | Survey sheet: a map field inside a neatline with a lettered and numbered grid, plus two margin columns. | broken |
| Navigation | Index of features (a gazetteer) in the margin, with grid references worked out from where each hill actually stands. Each entry pans the sheet to its hill and marks it. | broken |
| Hero | A title cartouche inside the neatline, in the empty south-west of the map: name, "a wood-fire restaurant", hours, "Book a table, up to 8 →". | broken. The first build put the title in a left column beside the map. The skeleton read that as headline-beside-picture, so the title moved into the map. |
| Components | Annotations with thin leader lines (spot height, contour interval, a foot touching the fire), a legend, and a ruled index table. No cards. | broken |
| Type | Barlow Semi Condensed (light letterspaced caps for the title, regular for notes) and Spectral italic for feature names, as maps set natural features. | broken |
| Colour | Cool paper, slate ink, ochre contours and tints, one vermilion for the fire. | broken |
| Texture | Hairlines and stepped contour tints only. No shadows, glow or blur. | broken |
| Pricing | Spot heights: ▲68 is the rib-eye for two. The index lists each grid square and price in tabular figures. | broken |
| Voice | Map marginalia: sheet title, legend entries, notes ("Heights are menu prices in euros"). | broken |
| Motion | Contours and the fire line draw themselves once on load. Under reduced motion they don't animate at all. | broken |

Kept: 0. The final skeleton is a large framed field of irregular shapes with a small box inside it and two narrow margin columns.

Self-checks on load:

- The index matches the menu.
- Each hill has one ring per €4 band.
- Each hill's foot touches the fire line (within 2 units).
- Each hill sits inside the sheet.
- Hills on the same side don't overlap.
- Party routing and time slots are correct.

---

## Design 3: "68 = 9 + 11 + 16 + 24 + 8" (`design-3.html`)

- **Tone:** loud
- **Move:** Let the data draw (2), with Invert (1) for the remaining traits
- **The idea that ties it:** the menu's own numbers say that one rib-eye for two (68) costs exactly as much as the other five dishes together (9 + 11 + 16 + 24 + 8 = 68). The page states this as a theorem and proves it by drawing. It reads from the bottom up, like heat rising. Two columns of blocks, each as tall as its price, end level at 68. The colour is ash: what the fire leaves.

There is no roll output: every trait is my own inversion, each the second or third opposite, checked against designs 1 and 2 for repeats.

Library specimens: `lay-04` Bottom to top and `tex-06` Dither. Both match the reading direction and texture I chose, and both were re-cut. The specimen's scroll box became the whole page; the dither uses charcoal and white pixels.

| Trait | What was built | Status |
|---|---|---|
| Reading direction | Bottom to top. The page is one full-height `column-reverse` scroll box that opens at its foot, so DOM, reading and tab order all run upward. | broken |
| Layout | Blocks sized by price, 1 € = one unit of height. The left column is the rib-eye for two alone (68). The right column stacks the other five (9, 11, 16, 24, 8). Both stop at the same height. | broken |
| Navigation | One sentence at the foot, where each phrase is a link: "Climb the proof, check the hours, or book a table for up to eight." | broken |
| Hero | The equation 68 = 9 + 11 + 16 + 24 + 8, stretched across the screen, over a theorem and a lemma (the house rule). | broken |
| Components | Each block is filled by its own stretched numeral. Tags carry the dish, the price and a running total. | broken |
| Type | Six Caps, stretched in SVG to fill each block, with Kalam handwriting for the proof. Fallbacks: Impact (the SVG stretch keeps the tall idea) and Chalkboard SE or Comic Sans. | broken |
| Colour | Mid-grey only: ash ground, charcoal ink, chalk white for the big figures. | broken |
| Texture | 4×4 Bayer dither of charcoal and white pixels inside the blocks; from a step back it reads as the same grey. Text sits on solid tags, never on the dither. | broken |
| Pricing | Blocks sized by price; the price is the block. | broken |
| Voice | A maths proof: Theorem, Lemma, Given (hours), Corollary (booking), ∎. | broken |
| Motion | A level line that counts how high you have climbed in euros. It also shows the right column's running sum, e.g. "€36 up. Right so far: 9 + 11 + 16 = 36". | broken |

Kept: 0. The skeleton shows a foot screen with one wide stretched line of type and a sentence row, two full-bleed columns of uneven blocks, then a two-column booking area at the top. Nothing is centred and there is no top bar.

Self-checks on load: both columns total 68; the right column holds exactly the other five prices; running totals are 9, 20, 36, 60, 68; booking rules are correct; the dither lights half the pixels at 50 %.

---

## No choice appears twice in the batch

| Trait | Design 1 | Design 2 | Design 3 |
|---|---|---|---|
| Reading direction | Around a circle | Sheet panned sideways | Bottom to top |
| Layout | One object (the hearth) | Survey sheet | Blocks sized by price |
| Navigation | Numbered footnotes | Index of features with grid references | One sentence of links |
| Hero | Form first (check-in) | Title cartouche on the map | The equation |
| Components | Index tabs (days) | Leader-line annotations, legend | Self-filling blocks with running totals |
| Type | Nabla + system mono | Barlow Semi Condensed + Spectral italic | Six Caps + Kalam |
| Colour | Thermal camera | Paper, slate, ochre, vermilion | Mid-grey only |
| Texture | RGB split | Hairlines and contour tints | Bayer dither |
| Pricing | Team sheet | Spot heights | Blocks sized by price |
| Voice | Boarding pass | Map marginalia | Maths proof |
| Motion | WebGL shader | Lines draw once | Counting level line |

## Checks run

- Each page screenshotted at 1280×800 and 390×844 in the built-in browser, with no console errors and every `console.assert` passing.
- Skeletons made with `scripts/skeleton.py`, screenshotted and then deleted.
- Flows clicked through:
  - Design 1: check-in with 9+ shows the phone message and stays gated; check-in with 4 / Sat / 21:30 fills the pass and moves focus to its heading; skip and footnote hashes work.
  - Design 2: index links pan to the hill and mark it.
  - Design 3: the level line counts while you climb.

Not checked:

- Reduced-motion emulation, a real phone, Safari or Firefox, a screen reader, and the offline font fallbacks. Fonts loaded from the network here.
- The no-WebGL fallback, which I didn't render.
