# ROADMAP SLIDEV TEMPLATE

**One deck, three jobs.** This is the SAGE roadmap spine as a Slidev template, built so the same file serves as the prospect-facing personalised roadmap, a content source, and a training-first long-form video.

---

## The three uses

| Use | How | What changes |
|---|---|---|
| **1. The roadmap** | Fill the `{{variables}}` per prospect, export or host | Personalised. Gates live. Password gated |
| **2. Content** | Each section carries a `CONTENT CUT` marker naming the reel that comes out of it | Anonymised. Gates stripped. One section = one post |
| **3. The video** | Present it and talk. Speaker notes ARE the script | Generic example instead of a real prospect. **Teaching-first, no pitch** |

**Why one file and not three.** The 54-section canon is already a teaching argument -- diagnosis, why the obvious fixes fail, the mechanism, the plan. That is the same shape as a good training video and the same shape as a content series. Building three assets from one spine means the argument gets sharper every time it is used, instead of drifting three ways.

---

## Structure

Six sections, three prospect gates, five producer quality gates.

```
§0  CONSTRAINTS CAPTURE      <- new. Before the roadmap is built at all
§1  The Diagnosis            slides 1-6     QG-1 at slide 5
§2  The Argument             slides 7-13    QG-2 at slide 12
    ▸ GATE 1  Reality Audit  slide 14
§3  Honest Alternatives      slides 15-21   QG-3 at slide 21
§4  The Path Forward         slides 22-27
    ▸ GATE 2  Mechanism Check + ENERGY PIVOT   slide 28
§5  Your Personal Roadmap    slides 29-42
§6  The Close                slides 43-49   QG-4 at 43, QG-5 at 47
    ▸ GATE 3  The Unlock     slide 50
§7  Proof + Resources        slides 51-54
```

**The energy pivot at 28 is not decoration.** Sections 1 to 27 are Doctor energy -- diagnostic, calm, unflinching. From 28 it becomes General energy -- directive, forward, we-go-now. In the deck this is a genuine visual break: colour temperature shifts, type scale steps up, transitions get faster.

---

## Animation doctrine

**Animation carries meaning or it gets cut.** Four uses only.

| Mechanic | Where | What it does |
|---|---|---|
| **`v-click`** | throughout | Value density. One idea revealed per beat, so the voice leads and the slide follows |
| **`v-motion`** | the score assembling, the constraint bars filling | Shows a quantity changing, which a static number cannot |
| **magic-move** | the two-path Crossroads at 47 | Same elements re-arranging into two futures. The re-arrangement IS the argument |
| **drauu** | the mechanism at 24 and the plan at 32 | Live drawing. **Nothing beats a hand building a diagram in real time for trust** |

**Never:** entrance animations on body text, decorative transitions between every slide, anything that moves while someone is reading.

---

## Files

- `slides.md` -- the deck
- `style.css` -- theme, unscoped. Both light and dark
- `constraints.md` -- §0, the constraint capture spec and the industry variants
- `content_map.md` -- which section produces which content unit

## Run

```bash
cd /root/slidev-webinars/internal/roadmap_template_2026_07_28
npx slidev slides.md          # present
npx slidev export slides.md   # PDF for the prospect
npx slidev build slides.md    # host it
```

Press `d` for the drawing layer on the two whiteboard slides.

## Before shipping any filled version

Run the five producer quality gates. They are marked in the deck as `QG-n` comments and every one of them is a rewrite condition, not a checkbox:

1. **QG-1, slide 5** -- does the Snapshot use their actual words, not paraphrases?
2. **QG-2, slide 12** -- are all three pains direct quotes, each explanation distinct?
3. **QG-3, slide 21** -- is what they tried named in their exact language?
4. **QG-4, slide 43** -- is the investment benchmarked against their own cost of inaction?
5. **QG-5, slide 47** -- exactly two paths, both grounded in their real numbers?

Then the airlock: **say "roadmap locked" before it goes to a human.**
