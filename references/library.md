# Library

Four pages of numbered specimens in `library/`: buttons, motion, heroes and type. Each specimen is one working mechanism to re-cut into a design, not a component to drop in.

## How to use it

- **Roll, don't choose.** `python3 scripts/roll.py --library buttons` (or `motion`, `heroes`, `type`; `--count N` for a batch, never repeating). Picking by taste lands on the same few favourites every time.
- **One per page per design.** A design takes at most one button, one motion, one hero and one type specimen, and never the same specimen twice in a batch.
- **Re-cut it.** Change the copy, colours and type to the product's own until it reads as part of that page. The sample products, words and figures in the specimens are placeholders.
- **Copy three parts.** The specimen's `<article>`, its CSS block (every rule starts with its `#id`, under a `/* id Name */` comment) and its JS block (`// id Name`, one `{ }` block). Take its font family from the page's Google Fonts link. The gallery shell around the specimens is not part of any of them.

Every specimen works by keyboard with a visible focus ring, respects `prefers-reduced-motion`, fits a 390px phone, and labels its sample figures as samples. Keep all of that when you re-cut it.

## Buttons (`library/buttons.html`)

| id | Name | Use it when | Change before use | Font |
|---|---|---|---|---|
| btn-01 | Rubber stamp | An approve or sign-off should feel final | Stamp word, ink and paper colours | Bowlby One SC |
| btn-02 | Ticket stub | Claiming a seat or an RSVP, one time | Ticket words, colours, fine print | Rye |
| btn-03 | Pull chain | A two-state toggle (dark mode, a feature on or off) | Room colours, tag word, lamp | Train One |
| btn-04 | Keycap | An action with a shortcut worth teaching; fires on its key too | Legend, shortcut letter, cap and plate colours | Mochiy Pop One |
| btn-05 | Wax seal | Opening an invitation, a result or a reveal | Wax colour, monogram, letter copy | Fascinate Inline |
| btn-06 | Fuse | A destructive action: hold to confirm, or click twice | Action word, hold time, colours | Londrina Solid |
| btn-07 | Price tag | Add to bag on a shop for physical goods | Tag copy, twine, cloth | Gochi Hand |
| btn-08 | Split-flap | A booking or check-in status that changes | Two words of the same length, colours | Martian Mono |
| btn-09 | Elevator call | Joining a queue, a waitlist or a callback | Floors, LED colour, panel; label the countdown as sample | Zen Dots |
| btn-10 | Sticker peel | Revealing a code or a reward | Sticker colour and copy, the hidden code | Bagel Fat One |
| btn-11 | Ballot mark | A vote or a one-of-several choice; works without JS | Options, paper, pencil colour | Courier Prime |
| btn-12 | Safety cover | Publish or go live in two deliberate steps | Action word, stripes, panel | Saira Stencil One |
| btn-13 | Signature | Sign up or agree, where signing is the honest metaphor | Signed words, ink, terms line | Reenie Beanie |
| btn-14 | Tally | An upvote or like counter | Board and chalk colours, label, cap | Sedgwick Ave Display |
| btn-15 | Zipper | A details disclosure on a fashion or outdoor product | Fabric and lining colours, label, copy | Potta One |
| btn-16 | Piano keys | A segmented choice with an interlock; works without JS | Options, body colour, key count | Krona One |
| btn-17 | Embroidered patch | A join or follow toggle | Word, thread and canvas colours | Shrikhand |

## Motion (`library/motion.html`)

One-shots start when they scroll into view and have a Replay button. Scroll-driven ones use CSS scroll timelines with a JS fallback for browsers without them. Loops run only on screen and can be paused.

| id | Name | Use it when | Change before use | Font |
|---|---|---|---|---|
| mo-01 | Odometer | A running total should feel counted by a machine | From and to values, unit line, drum colours | Chakra Petch |
| mo-02 | Split-flap headline | A headline changes with the time or season | The lines (two rows of up to 12 characters), colours | Antonio |
| mo-03 | Letterpress proof | A short statement should look pressed into paper | Words, two inks, paper | Ultra |
| mo-04 | Gravity pile | One sentence carries the page with weight | Words (5 to 10), block colours, gravity | Erica One |
| mo-05 | Pen plotter | An image should arrive the way it was made | Paths, inks, pen speed | Major Mono Display |
| mo-06 | Line boil | Hand-drawn warmth that never sits still | Drawing, wobble scale | Shantell Sans |
| mo-07 | Axis wave | A headline changes character as you scroll past | Line, axis values | Recursive |
| mo-08 | Aperture iris | A photo revealed the way a camera takes it | The image, blade count, ring markings | Syncopate |
| mo-09 | Tri-vision billboard | Three short messages share one spot | Three panels, slat count, interval | Black Han Sans |
| mo-10 | Thermal receipt | An order or a price total is the proof | Line items and amounts (they must add up), shop line | Anonymous Pro |
| mo-11 | Flipbook | Scrolling should step through a process | Frame drawing, frame count, pencil colour | Fredericka the Great |
| mo-12 | Word swap | Two plans can be said with the same words | Both sentences (same words; the self-check compares them) | Gloock |
| mo-13 | Ink bloom | A section should open slowly and quietly | Drops, ink and paper colours, copy | Young Serif |
| mo-14 | Dither dissolve | A product shot has two states (day and night, before and after) | Drawings or images, palettes, captions | Familjen Grotesk |
| mo-15 | Tear-off calendar | A countdown where each day is a step | Pages (dates and lines), colours | Chonburi |
| mo-16 | CRT power-on | A schedule or anything live should switch on | Screen copy, phosphor colours, axis values | Sixtyfour |
| mo-17 | Clock wipe | A service changes state at set times | Both faces, tick count, hand colour | Old Standard TT |
| mo-18 | Darkroom print | An image should develop rather than appear | The image (in grey tones), safelight tint | Poiret One |
| mo-19 | Fold-out leaflet | A guide or a route should unfold panel by panel | Four panels, fold angle | Tenor Sans |

## Heroes (`library/heroes.html`)

Each hero is built for a different sample product, named small inside it. Its headline is an `h3` in the gallery; make it the page's `h1`.

| id | Name | Use it when | Change before use | Fonts |
|---|---|---|---|---|
| hero-01 | Fill-in sentence | The value is a sum of the visitor's own numbers | Sentence, blanks, formula, the sample assumption | Young Serif, Sometype Mono |
| hero-02 | Front page | The product makes something fresh every day, or has real news | Masthead, ears, folio line, story; never borrow a real paper's name | Libre Caslon Display and Text |
| hero-03 | Proof divider | The product turns a clumsy version into a good one | Both sentences, the editor's marks | Newsreader |
| hero-04 | Exploded view | An object or service with parts worth naming | Drawing, callout positions, parts list, prices | Zilla Slab Highlight, Overpass Mono |
| hero-05 | Crossword | The idea fits in a handful of short words | Answers, clues, grid | Alegreya SC, Abhaya Libre |
| hero-06 | Tape measure | The product works to a measurement the visitor knows | Unit, range, scale, what the reading prices | Sedan SC, Bevan |
| hero-07 | Local sky | The product is used at different times of day | The four lines, bucket hours, band colours | Corben |
| hero-08 | Venn overlap | The product lives where two things meet | Circle labels, inks, headline | Coustard |
| hero-09 | Dictionary entry | The product's name is a word you can define | Headword, pronunciation, senses, origin, thumb tab | Gelasio |
| hero-10 | Sampler | Domestic, slow or handmade products | Motto (add letters to the 5×7 table), motifs, threads | Calistoga |
| hero-11 | Sheet music | Voice, sound or rhythm | Lyric, melody, tempo; keep four beats a bar | Vollkorn SC |
| hero-12 | Tide chart | A changing level becomes a yes or no | Terrain, contour levels, slider unit, the question | Shippori Mincho |
| hero-13 | Transit line | A run of steps with times | Stops, times, line name and colour | Lexend Zetta |

## Type (`library/type.html`)

Each specimen's caption names the font's axes, licence (all OFL) and the local fallback, and says what is lost offline.

| id | Name | Use it when | Change before use | Font and axes |
|---|---|---|---|---|
| type-01 | Melting year | A year or a trend is the story | The word, the year span, what drives it | Climate Crisis, YEAR |
| type-02 | Chart in a sentence | A chart belongs inside prose | Sentence, values (real or marked sample) | Linefont, wdth wght |
| type-03 | Waveform from typing | Voice, audio or messaging | The mapping (real peaks beat letters), colours | Wavefont, ROND wght |
| type-04 | Tilt with the pointer | A shopfront, venue or opening-hours page | Words, colour, axis limits | Tilt Prism, XROT YROT |
| type-05 | Inkjet element shapes | Logistics, packing, anything stamped on a crate | Lot-code format, shape, crate colour | Handjet, ELSH ELGR |
| type-06 | Scannable label | Tickets, labels, inventory | Where the code comes from; test with a scanner | Libre Barcode 39 Text |
| type-07 | Pixel-snapped weave | Textiles, crafts, heritage goods | Words, ground and thread colours | Jacquard 24 |
| type-08 | Microscope loupe | Biology, labs, food science | Line, stain colours, lens size and zoom | Rubik Microbe |
| type-09 | Bus vinyl cut by scroll | Transport, street culture, long pages | Words, stripe colours, scroll range | Danfo, ELSH |
| type-10 | Palette cycle | Events, kids, festivals | Palettes kept, override colours | Honk, MORF SHLN (colour font) |
| type-11 | Keystroke burst | A playful input that answers every key | Burst colour, decay speed, start word | Kablammo, MORF |
| type-12 | Copy of a copy | Archives, zines, reprints | Words, paper colour, generation mapping | Workbench, BLED SCAN |
| type-13 | Dot-matrix clock | Transit, live status, where "now" is the content | Data source, what drives the dots | Doto, ROND wght |
| type-14 | Copybook ruling | Education, practice apps | Line, Playwrite country, ink and rule colours | Playwrite DE Grund, wght |
| type-15 | Click to unredact | Investigations, privacy, reveals | Memo text, which words hide | Flow Block |
| type-16 | Set in 1640 | History, publishing, letterpress | Text, rubric colour; keep the long-s rule | IM Fell English |
| type-17 | Layered sign | Signage, food, nightlife | Word, four layer colours | Bungee, Shade, Inline, Outline |
| type-18 | Light and dark glaze | Luxury, theatre, light and dark sections | Line, palette per section, width | Kalnia Glaze, wdth wght (colour font) |
| type-19 | Vertical shop sign | Japanese or vertical headlines | Copy, real hours, the seal | Dela Gothic One |
| type-20 | Text on a spiral | Manifestos, menus, slow reads | Text, turns, offset range | Ojuju, wght |

## Watch out

- **Fonts.** Every page loads its faces from Google Fonts, and offline previews fall back to system fonts and lose the idea. Self-host the font for anything that ships. Colour fonts (Honk, Kalnia Glaze) need a browser with COLRv1 support and draw flat without it.
- **Claims.** A barcode, a countdown or a counter is a claim: make it real or label it as sample. Test type-06 with a scanner before shipping.
- **Hold and drag.** The fuse, pull chain, zipper and price tag have click and keyboard equivalents; keep them when you re-cut. hero-03 and hero-06 lay an invisible range input over the artwork: test them on a real phone.
- **Sound.** hero-09 speaks the headword and hero-11 plays its melody, only when the visitor presses their button. Never autoplay.
