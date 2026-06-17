# Slide Pattern — World-Class Lesson Decks

The teaching architecture every portal-onboarding lesson follows. Lifted from the Priority Lever deck (`module_01_start_here/1_5_priority_lever.md`); copy that one as the template for any new lesson.

## The three pedagogical labels (eyebrow tags)

Every slide carries one of these. The learner always knows what to do with the slide:

| Tag | Meaning | What the learner does |
|---|---|---|
| **Know this** | Declarative knowledge — fact, definition, framework. | Encode it. They'll be tested by reality, not us. |
| **Do this** | Procedural knowledge — a step, a test, a rep. | Execute it. The rep is the point. |
| **We've got this** | What Joburn does for them. | Relax about it. Don't duplicate the work. |

Plus a fourth ambient class (no tag needed): **the cognitive flip** — slides whose only job is to reframe. Tension setups, kickers, closers.

## The aha-stacking spine

Every lesson needs **5–6 aha moments**, each on its own slide, stacked so each one earns the next. Don't dilute by spreading aha across two slides. One aha per slide; one slide per aha. The Priority Lever deck stacks:

1. **AHA #1** — recognition: "I've heard this from myself."
2. **AHA #2** — declarative reframe: priority is singular by definition.
3. **AHA #3** — declarative kicker: "multiple most importants" is a logical contradiction.
4. **AHA #4** — procedural: there's a *test*, not just intuition.
5. **AHA #5** — painful flip: busy ≠ progress. Often opposite.
6. **AHA #6** — operational: the we-do / you-do split kills the "I thought you had that" trap.

## The arc (every deck, every time)

1. **Cold open** (~10s) — name the mechanism. No definition yet. Curiosity is the trade.
2. **Tension slide** (~15s) — a quote, a stat, a recognizable moment they live in.
3. **The diagnosis** (~15s) — label their condition. The first aha.
4. **Declarative core** (1–3 slides) — the truth they need to encode.
5. **The kicker** (~10s) — undeniable, short, lands the truth.
6. **Procedural definition** (~20s) — define the working concept they'll use.
7. **The test or method** (~25s) — break the procedure into 2–3 visible steps.
8. **Worked example** (~25s) — the click-by-click diagram, with *why this answer*, not just *that it's the answer*.
9. **The painful aha** (~15s) — the slide that reframes a default behavior.
10. **We-do / you-do split** (~25s) — clean division of labor, two columns.
11. **The two rules** (~20s) — procedural commitments. Never more than two.
12. **Closing synthesis** (~12s) — two big lines. Memorable.
13. **The rep** (~20s) — concrete homework. 2–3 steps. With permission to come honest if they fail.
14. **Cliffhanger to next lesson** (~12s) — forward momentum + name what they unlock.

Total: ~14 slides, ~4–6 minutes of recording. **Fladlien-style: many fast slides beats few dense ones.**

## Build patterns to reuse

- **v-mark.strike-through.red** + **v-mark.circle.cyan** — the etymology/definition reveal pair. Used in slide 4.
- **v-mark.crossed-off.red** + **v-mark.circle.cyan** on tiles — the worked example. Used in slide 8.
- **Build-the-statement pattern** — start with a partial sentence, click reveals the back half (slide 6).
- **Two-column we/you split** with colored left borders — slide 10. Cyan + orange separates the actors visually.
- **Card stack with numbered counters** — procedural steps (slide 7, 11, 13). Use `<div class="ff-card">` from the shared style.
- **Big-text emotional kicker on navy** — slides 5, 9, 12. The "feel it" slides. White text on navy with one cyan or orange highlight word.

## What makes a slide world-class vs. just OK

- **One job per slide.** If you can't say what the slide does in one sentence, split it.
- **The aha is visible.** A reader scanning the deck without audio should still see the moment.
- **Procedural slides have numbered steps.** Don't bury actions in paragraphs.
- **Declarative slides cite the source or the proof.** "Latin *prior*, 1450" beats "this is a fundamental principle."
- **Every navy slide is short.** Navy is for emphasis. Three lines max.
- **Every cream slide has whitespace.** Aim for 40% empty pixels minimum.
- **v-mark is for the load-bearing word, not the decoration.** One v-mark per slide. Two max.

## When to break the pattern

- The cold open and the cliffhanger can repeat across many lessons; that's a feature (rhythm).
- The worked example slide is the most flexible. For some lessons it's a diagram, others a code snippet, others a screen recording embed.
- Procedural lessons (e.g., "how to grant Leadsie access") collapse to: cold open → 3 procedural steps → cliffhanger. Five slides. That's fine. Don't force a 14-slide arc onto a screen-share lesson.

## Reference deck

`module_01_start_here/1_5_priority_lever.md` is the canonical implementation. Copy it. Replace the content. Keep the pattern.
