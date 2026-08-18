# PER-SLIDE VISUAL MAP — Easy Care Finder "The Four Kinds of Place" walkthrough

> Built to the Brad Pounds `_VISUAL_MAP.md` pattern. One row per slide. Drives BOTH the concept-image
> batch AND the section build. Source copy = `show_up_system_2026_08_13.md` §5.2, verbatim, 1,346
> words. Speaker notes are that script segmented at sentence boundaries. **Do not rewrite the copy.**
>
> **Columns:** `id` · on-slide headline (≤7 visible words) · tempo · VISUAL (`gen:` concept image |
> `html:` CSS-built | `type:` big-type-as-visual) · treatment · animation
>
> **Register: BEHIND-THE-SCENES.** He is a man explaining something honestly, not a brand presenting.
> Warm, plain, unhurried. Market Archetype 1, Sensitive Premium Care.
>
> **Rules in force:** ≤7 visible words on headlines · v-clicks on every 2+ list · NO em-dash ·
> NO emoji (Iconify or text badge) · content fits 16:9 at every click · never a naked text slide ·
> speaker notes on EVERY slide · **no clinical vocabulary, ever** · **no invented proof**

## Treatments legend
- **HERO-BLEED** — full-bleed concept image, headline in a solid cream card. `layout: cover`
- **IMG-SIDE** — image one half, copy the other. Alternate L/R, never 3 the same in a row
- **STAT-HERO** — one giant number or word, image as accent
- **GREEN-STATEMENT** — full `#1D5C4D` field, big cream type. The "land it" slide
- **REVEAL-CARDS** — 2-4 cards revealed via `<v-clicks>`, each with its own icon
- **TWO-COL** — the comparison device (what you find online vs what is licensed)
- **DIVIDER** — green field, section title + Iconify, one slide between the four kinds

---

## SECTION: open.md — the frame (script slides 1-3)

| id | headline (<=7 words) | tempo | VISUAL | treatment | anim |
|---|---|---|---|---|---|
| op-01 | The four kinds of place | FRAME | `gen:c01_four_doors` | HERO-BLEED | fade-rise |
| op-02 | And which one fits | FRAME | `gen:c01_four_doors` dimmed | text-over-image | v-click |
| op-03 | I am not going to pitch you | STOP | `type:` big cream type on green | GREEN-STATEMENT | v-click |
| op-04 | Useful whether we work together or not | LAND | `gen:c02_kitchen_table` | IMG-SIDE L | fade |
| op-05 | Let me guess where you are | MOVE-FAST | `gen:c03_phone_dusk` | HERO-BLEED | fade |
| op-06 | You have days, not months | STOP | `type:` giant "DAYS" | STAT-HERO | v-click |
| op-07 | Calling places one at a time | MOVE-FAST | `html:` call-log device | REVEAL-CARDS | v-clicks x3 |
| op-08 | Every site wants your number first | MOVE-FAST | `gen:c04_form_wall` | IMG-SIDE R | fade |
| op-09 | You have not done anything wrong | LAND | `type:` cream on green | GREEN-STATEMENT | v-click |
| op-10 | The tools you were handed are bad | LAND | `type:` | GREEN-STATEMENT | v-click |
| op-11 | The map is what is broken | ZOOM | `gen:c05_broken_map` | HERO-BLEED | fade |
| op-12 | What you find online | FRAME | `html:` two-column device | TWO-COL left build | v-click |
| op-13 | What is actually licensed near you | STOP | `html:` two-column device | TWO-COL right build | v-click |
| op-14 | It is the advertising near you | LAND | `type:` | GREEN-STATEMENT | v-mark |

## SECTION: four.md — the four kinds (script slides 4-7)

| id | headline (<=7 words) | tempo | VISUAL | treatment | anim |
|---|---|---|---|---|---|
| fk-00 | Four kinds | DIVIDER | `type:` numeral | DIVIDER | fade |
| fk-01 | One. Help that comes to the house | FRAME | `gen:c06_home_help` | HERO-BLEED | fade |
| fk-02 | Nobody moves | MOVE-FAST | `gen:c06_home_help` dimmed | text-over-image | v-click |
| fk-03 | Who it suits | STOP | `html:` fit-card | REVEAL-CARDS | v-clicks x2 |
| fk-04 | Where it stops working | LAND | `html:` fit-card amber | REVEAL-CARDS | v-clicks x2 |
| fk-05 | Two. An apartment where older people live | FRAME | `gen:c07_independent_apt` | HERO-BLEED | fade |
| fk-06 | Independence, with people around | MOVE-FAST | `gen:c07_independent_apt` | IMG-SIDE L | v-click |
| fk-07 | Who it suits | STOP | `html:` fit-card | REVEAL-CARDS | v-clicks x2 |
| fk-08 | Where it stops working | LAND | `html:` fit-card amber | REVEAL-CARDS | v-clicks x2 |
| fk-09 | Three. The large community | FRAME | `gen:c08_large_community` | HERO-BLEED | fade |
| fk-10 | Sixty people. Or a hundred | STOP | `type:` giant numerals | STAT-HERO | v-click |
| fk-11 | What that buys you | MOVE-FAST | `html:` fit-card | REVEAL-CARDS | v-clicks x3 |
| fk-12 | What it costs you | LAND | `html:` fit-card amber | REVEAL-CARDS | v-clicks x2 |
| fk-13 | Four. The small home | FRAME | `gen:c09_small_home_street` | HERO-BLEED | fade |
| fk-14 | An ordinary house on an ordinary street | STOP | `gen:c09_small_home_street` | text-over-image | v-click |
| fk-15 | Six people. Sometimes fewer | STOP | `type:` giant "6" | STAT-HERO | v-click |
| fk-16 | Who it suits | MOVE-FAST | `html:` fit-card | REVEAL-CARDS | v-clicks x3 |
| fk-17 | Where it stops working | LAND | `html:` fit-card amber | REVEAL-CARDS | v-clicks x2 |

## SECTION: why.md — why they are invisible (script slides 8-9)

| id | headline (<=7 words) | tempo | VISUAL | treatment | anim |
|---|---|---|---|---|---|
| wh-01 | Why you have never heard of them | FRAME | `gen:c10_invisible_street` | HERO-BLEED | fade |
| wh-02 | They cannot afford to be found | STOP | `html:` cost-gap device | IMG-SIDE R | v-clicks x2 |
| wh-03 | A six bed home has no marketing budget | LAND | `type:` | GREEN-STATEMENT | v-click |
| wh-04 | The thing no website can tell you | FRAME | `gen:c11_two_doors_same_street` | HERO-BLEED | fade |
| wh-05 | Two homes. Same street. Same price | STOP | `html:` compare device | TWO-COL | v-clicks x2 |
| wh-06 | One is right for her. One is not | LAND | `type:` | GREEN-STATEMENT | v-mark |
| wh-07 | You cannot tell from a listing | LAND | `gen:c11_two_doors_same_street` dimmed | text-over-image | v-click |

## SECTION: close.md — who I am, the call, the ask (script slides 10-13)

| id | headline (<=7 words) | tempo | VISUAL | treatment | anim |
|---|---|---|---|---|---|
| cl-01 | Who I am, and how I get paid | FRAME | `gen:c12_singh_doorway` | HERO-BLEED | fade |
| cl-02 | I owned and ran care homes | STOP | `gen:c12_singh_doorway` | IMG-SIDE L | v-click |
| cl-03 | The home pays me. You never do | STOP | `html:` fee-flow diagram | ZOOM, 3 v-click callouts | v-clicks x3 |
| cl-04 | I will tell you which ones I own | LAND | `type:` | GREEN-STATEMENT | v-click |
| cl-05 | What our call does | FRAME | `gen:c13_shortlist_table` | HERO-BLEED | fade |
| cl-06 | About thirty minutes | MOVE-FAST | `type:` giant "30" | STAT-HERO | v-click |
| cl-07 | Usually three homes | STOP | `html:` three-card device | REVEAL-CARDS | v-clicks x3 |
| cl-08 | What it costs you | STOP | `type:` giant "Nothing." | GREEN-STATEMENT | v-click |
| cl-09 | Three things before we talk | FRAME | `html:` numbered list device | REVEAL-CARDS | v-clicks x3 |
| cl-10 | Talk soon | LAND | `gen:c02_kitchen_table` dimmed | HERO-BLEED, wordmark | fade |

---

## Totals
**49 slides · 13 generated concept images · 0 naked text slides.**
Every `type:` slide is big-type-as-visual, which counts under Visual Law §3.1. Every `html:` slide is a
CSS-built device (diagram, cards, comparison), which also counts.

## 🔴 Locks specific to this deck
- **No clinical vocabulary anywhere.** Not one condition is named, in any slide or any note.
- **No invented proof.** No counts of homes, no families helped, no results. He has none.
- **Nothing that dates it.** No date, no day, no price, no tally. It never gets re-recorded.
- **No real, identifiable property in any image.** No house number, street sign or plate.
- **Singh's own photograph is required for `c12_singh_doorway`.** Until it exists the slide ships with
  a placeholder and is flagged. **A generated stand-in for the founder is never acceptable.**
