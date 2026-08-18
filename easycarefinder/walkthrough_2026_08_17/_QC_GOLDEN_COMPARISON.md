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
| Rendered pages | 111 | 22 | **51** |
| Embedded images | 129 | 19 | **62** |
| **Images per page** | **1.16** | **0.86** | **1.22** |
| Speaker notes coverage | every slide | every slide | **51 of 51** |
| v-clicks | 142 source | 168 source | **73** |
| Longest image-free run | 16 (one deliberate block) | not measured | **3** |
| Longest same-ground run | not measured | not measured | **3** |
| Em-dashes | 0 | 0 | **0** |
| Emoji in slide body | 0 | 0 | **0** |
| Markdown H1 | 0 | 0 | **0** |

## Verdict: **AT STANDARD**, and above it on image density

**Above the golden:** 1.22 images per page beats Brad's 1.16 and Cassie's 0.86. Every slide carries
speaker notes, which is the thing that makes this recordable rather than merely pretty.

**Where it is deliberately below:** 11 of 51 slides carry no photograph or card. **Nine of those are
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


---

# ADDENDUM — Singh's staffing-ratio feedback, 17 Aug

Singh asked for two specific numbers on camera: **1 staff per 20 residents** in a large community, and
**1 staff to 3 residents** in a small home.

🔴 **The numbers are not in the deck, and the reason is not squeamishness.**

1. **California sets no fixed staffing ratio for an RCFE.** Title 22 requires staffing sufficient for
   residents' needs, with specific overnight minimums. There is no statutory 1:20 and no statutory 1:3,
   so neither number is a fact about the category. It varies by building, by licence type and by shift.
2. **This exact class of claim has already been removed from this script twice.** The v2 log struck
   *"fifty to a couple of hundred residents"* as invented, and struck a cost claim about in-home care
   for the same reason. Putting a ratio back in reintroduces the defect the document already fixed.
3. **It is said on camera**, where it cannot be adjusted per family and will not be re-recorded.
4. **A number stated about facilities he does not own is a claim about somebody else's business.**

**What shipped instead, which is stronger and carries no exposure:**

| Singh's ask | What is on the slide |
|---|---|
| "1 staff per 20 residents" | `fk-12b`: **the question he teaches her to ask.** *"How many residents does one caregiver have? Ask it about the night shift, not about the tour."* Plus, in the notes: *"I'm not going to give you a number, because anyone who quotes you one number for the whole industry is guessing."* |
| "small nuances missed due to staff turnover" | `fk-12c`: *"People move on. The person who learned her routine may not be the person on shift next month."* Framed as what large rosters structurally do, never as an accusation. Payoff: *"That she takes her tea weak. That she will not say when she is cold."* |
| "1 staff to 3 residents" | `fk-16b`: **six residents is the licence, not a promise.** Then, in his own voice and first person: *"In the homes I work with, the number of people one caregiver is looking after is a great deal smaller."* His own experience is defensible. A category-wide ratio is not. |
| "they know what mom had for lunch / doesn't like her food spicy" | `fk-16c`: **shipped almost verbatim.** *"They know what she had for lunch. They know she does not like her food spicy. They notice she is off, before it becomes a problem."* |

**Singh's last line is the best writing in the whole deck** and it is the one thing in his note that
needed no editing at all. The specific, ordinary detail does the work the statistic was reaching for,
and unlike the statistic it cannot be wrong.

**If he wants the numbers on camera**, the route is open and it is one sentence: *"In the homes I work
with it runs about one to three."* First person, his own homes, his own observation. Say the word and
it goes in.

## Title
Changed to an indirect training title at Singh's request:
**"How To Tell Which Kind Of Care Home Actually Fits Her."**
It promises teaching rather than a service, which is the frame the script already insists on: a family
who watches all of it and never calls should still be better off.
