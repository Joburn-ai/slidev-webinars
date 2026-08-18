# GOLDEN-EXAMPLE QC — Easy Care Finder walkthrough deck

**Run 17 Aug 2026.** Protocol: `00_Foundations/ref_golden_example_qc_2026_08_11.md`.
**QC is a comparison, not a checklist.** Both decks rendered, both opened, both measured.

## The goldens, named by path

| Role | Golden |
|---|---|
| Webinar image pacing | `slidev-webinars/bradley_pounds/evergreen_60programs_2026_07/` (also Housing Special Ad Category, so the compliance posture transfers) |
| Workshop / training register | `06_Clients/cassie_lincoln/05_assets_and_deliverables/roadmap_2026_06_29/slides_workshop/` |
| Slide-by-slide plan format | Brad's `_VISUAL_MAP.md` |
| Section build rules | Brad's `_SECTION_BUILD_CONTRACT.md` |

## The measurement

| | Brad (golden) | Cassie (golden) | **This deck** |
|---|---|---|---|
| Rendered pages | 111 | 22 | **47** |
| Embedded images | 129 | 19 | **57** |
| **Images per page** | **1.16** | **0.86** | **1.21** |
| Speaker notes coverage | every slide | every slide | **47 of 47** |
| v-clicks | 142 source | 168 source | **65** |
| Longest image-free run | 16 (one deliberate block) | not measured | **3** |
| Longest same-ground run | not measured | not measured | **3** |
| Em-dashes | 0 | 0 | **0** |
| Emoji in slide body | 0 | 0 | **0** |
| Markdown H1 | 0 | 0 | **0** |

## Verdict: **AT STANDARD**, and above it on image density

**Above the golden:** 1.21 images per page beats Brad's 1.16 and Cassie's 0.86. Every slide carries
speaker notes, which is the thing that makes this recordable rather than merely pretty.

**Where it is deliberately below:** 11 of 47 slides carry no photograph or card. **Nine of those are
GREEN-STATEMENT slides**, the register's "land it" beat, which is big serif type on a full brand-green
field. Brad's golden does exactly this and his build contract names it: the navy yes-momentum cards
are *"deliberately image-free."* His run of them is 16 consecutive. **Ours never runs past 3**, which
is better distribution than the golden, not worse.

🔴 **The one honest finding.** The image-free run of 3 at `cl-01` to `cl-02` exists partly because
`cl-02` is a **placeholder awaiting a real photograph of Singh in the doorway of a home he owns.**
When that photo lands the run drops to 2. **The run is a symptom of a missing asset, not a design
choice**, and it is the strongest single slide in the deck once it is filled.

## Register check

Behind-the-scenes, per the deck_production selector. Warm editorial-documentary, Market Archetype 1.
No urgency, no scarcity, no pressure, no proof claims, no clinical vocabulary anywhere in 47 slides or
47 note blocks. Verified by grep, not by memory.

## Content fidelity

Every speaker note is the §5.2 script **verbatim**, segmented at sentence boundaries. Nothing was
rewritten. The two `[OPEN]` items the script carries are surfaced ON the relevant slides as footers
rather than buried, so Singh cannot record them by accident:

1. The ownership and fee disclosure needs attorney-cleared wording before `cl-04` is recorded.
2. No count of homes is said out loud anywhere, pending a fresh CCLD pull.

## Defects found by looking, and fixed

The Invisible-Render Law: an assertion that passes is not a picture that works. All four were found by
rendering and opening it, and every one would have passed a checklist.

| Defect | Fix |
|---|---|
| **Slide 1 rendered blank white.** The headmatter block was creating an empty slide before the cover. | Cover content moved into `slides.md`, duplicate `op-01` removed |
| **Kickers invisible on every hero.** Brand gold on a photographic ground failed the contrast test on 4 slides. | `.ecf-onimg .ecf-kicker` overridden to a lighter gold `#EBCE86` |
| **Dead cream band across the middle of all six card slides.** Short copy shrank the cards to chips. | `min-height` floor on `.ecf-card`, type up from 1.35rem to 1.5rem |
| **Disclosure footer cramped to two tiny lines.** | Shortened, and the footer type raised |

## Build notes worth keeping

- **`vite.config.ts` is required.** The production build resolves leading-slash public paths as fs
  imports and fails with *"resolves outside of Vite server.fs.allow"*. Dev runs clean, only the build
  trips. **The fix was already solved and documented in Brad's deck as Rule 18** and was copied
  rather than re-derived.
- **Build from inside the deck directory**, not the repo root, or `public/` resolves against the wrong
  root.
- **Grounds are CLASSES, never `background:` frontmatter.** Slidev 52 puts no inline style on
  `.slidev-layout`, so a `[style*=]` selector cannot fire and you get cream text on a cream ground,
  silently.
