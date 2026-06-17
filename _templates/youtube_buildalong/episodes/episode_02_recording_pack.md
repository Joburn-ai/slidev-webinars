# Episode 02 · Recording Pack · v4 (FABLE v2 deck, two-experiment cut)

**Date locked:** 2026-06-11
**Episode:** i spent 4 hours testing fable 5. (it lost one of two tests.)
**Deck (15 slides):** [episode_02_fable5_mythos5_drop.md](episode_02_fable5_mythos5_drop.md)

| URL | What |
|---|---|
| https://joburn-buildalong-ep02.vercel.app | Main · currently Fable v2 · record off this (use the DEV server for drawing, see §3) |
| https://joburn-buildalong-ep02-fable-v2.vercel.app | Permanent Fable v2 snapshot |
| https://joburn-buildalong-ep02-opus-v1.vercel.app | Permanent Opus v1 snapshot · the A/B artifact |

> **The play:** one recording session produces the YouTube workshop (~15-18 min) + 2 vertical green-screen hot takes + clipped shorts from the long-form. Slide 12 (the deck test) shows BOTH deck versions on camera. Put both snapshot URLs in the video description.

---

## 1 · BEFORE recording: nothing to run. The experiments are done.

The deck reflects **two experiments already run** (no placeholders left, nothing to fill):
- **Experiment 1 · The Report Test:** identical EOW client-report prompt to both models. **Opus won** (30 min vs 50, equal accuracy, far fewer decisions; Gemini blind judge agreed). Full data: `ai-os/11_Operations/model_experiments/eow_report_ab_2026_06_10/`.
- **Experiment 2 · The Deck Test:** both models built this very deck. **Fable won** on one catch (it fixed the Mythos-vs-Fable naming error Opus shipped). Both decks live at the snapshot URLs.

Pre-record: open the dev server (§3), do one dry run of the whiteboard draw (slide 12), and confirm your two monitors (play view + presenter notes).

**Fact locks while talking:**
- You tested **Fable 5**, not Mythos. Mythos 5 is the same model with cyber safeguards lifted, locked to Project Glasswing. The deck teaches this distinction on slide 5. Don't undo it on camera.
- Stripe: 50 million lines of Ruby, codebase-wide migration, one day, team had it scoped at two-plus months. Say "roughly" on any compression multiple. Never "literally."
- Pricing: $10 in / $50 out per million tokens. Less than half of Mythos Preview. Free on Pro/Max through June 22, credits start June 23.
- Benchmarks: SWE-Bench Pro 80.3 vs 69.2 (Opus) vs 58.6 (GPT-5.5). FrontierCode 29.3 vs 13.4 vs 5.7.
- Safety fallback: roughly 5% of sessions route to Opus 4.8 on cyber/bio/chem topics. Users are told when it happens.
- **Routing verdict to land:** fable architects, opus executes. Route by bucket, not by hype.

---

## 2 · The 15-slide map (scene + tempo + time)

| # | Slide | Scene | Tempo | Time |
|---|---|---|---|---|
| 1 | Cover · "i spent 4 hours testing fable 5" (outcome-first: it lost one) | A | FRAME | 8-12s |
| 2 | The twist · "the model under review built this deck" (opens loop) | B | FRAME | ~20s |
| 3 | Stakes · "labor-cost reality check" | B | FRAME | ~25s |
| 4 | Who's testing · 3 not-tags + hero card | B | FRAME | ~30s |
| 5 | What dropped · butterfly hero + 4 facts | A | MOVE FAST | ~60s |
| 6 | Receipts · agentic-coding chart + annotations | A | ZOOM | ~75s |
| 7 | The frame · 3 buckets | A | MOVE FAST | ~45s |
| 8 | What I actually ran · the two experiments + settings tally | A | MOVE FAST | ~40s |
| 9 | Experiment 01 results · the report test (OPUS WON) | A | MOVE FAST | ~2min |
| 10 | Experiment 02 · the deck test (FABLE WON, closes slide-2 loop) | B | MOVE FAST | ~2min |
| 11 | The settings that matter (the "what settings to use" payoff) | A | MOVE FAST | ~60s |
| 12 | Whiteboard · draw the routing layer (drauu) | A | STOP | 2-3min |
| 13 | Verdict by bucket | A | LAND | ~60s |
| 14 | Identity beat · "you still pick" | A | LAND · SLOW | ~75s |
| 15 | Recap + CTA · "go judge the machines yourself" | D | LAND | ~35s |

**Estimated runtime: 15-18 min.** Hero's Journey: call (1) → stakes (2-3) → guide (4) → truth (5-7) → trials (8-10) → settings payoff (11) → map (12) → verdict (13) → transformation (14) → return (15).

**The slide-2 / slide-10 loop:** slide 2 opens the "both decks" loop, slide 10 closes it. Don't reveal the deck-test verdict early. If you slip, cut it in the edit.

---

## 3 · OBS scenes (same 4-scene rig + vertical)

| Scene | Hotkey | Use on |
|---|---|---|
| A · Slides + cam corner | Cmd+1 | 1, 5-9, 11-14 |
| B · Slides + large cam | Cmd+2 | 2, 3, 4, 10 |
| D · Cam only | Cmd+4 | 15 |
| E · Vertical green-screen | Cmd+5 | IG clips after the main recording |

Whiteboard (slide 12) stays in Scene A: drauu pen on the slide itself. **Record off the DEV server** (`pnpm dev:buildalong-ep02`, localhost:3030) so the pen toolbar exists. Press `d` to toggle drawing. The production build strips the drawing UI. Drawings persist between rehearsals (`drawings.persist: true`).

**Two-surface rig:** OBS records the play view (localhost:3030) fullscreen. You read notes from `localhost:3030/presenter/1` on a second monitor or your phone. Both views sync on click. Never screen-record the presenter view (notes would be on camera).

---

## 4 · IG / TikTok hot takes (record in same session, Scene E)

### Winner · reframe (~42s)

Hook: *"stripe just shipped two months of engineering work in one day with fable 5. fifty million lines of ruby. one model. one day."*

```
stripe just shipped two months of engineering work in one day with fable 5. fifty million lines of ruby. one model. one day.

everyone's gonna read that and panic about their job.

wrong panic.

if you're an employee, yeah, the floor is rising under you and the ceiling isn't moving. that's the trade you signed up for. your output is now benchmarked against a thing that costs ten bucks a million tokens and doesn't sleep. anthropic literally cut the price in half on the most capable model ever shipped. that's not a product release. that's a repricing of human labor.

but operators? this is the cheapest leverage that has ever existed in the history of business. a two-month engineering project just became a tuesday. that's not a tool. that's an unfair advantage you can rent for the price of a dinner.

the gap is not ai vs human. the gap is operator vs employee. one group is watching their wages get compressed. the other is watching their output multiply.

pick a side. the model doesn't care. the market doesn't care. only you care, and only for about another quarter.
```

Payoff card (static on black): *"cheap intelligence punishes rented time and pays compounded ownership. that's the whole game now."*

Overlays: `STRIPE: 2 MONTHS → 1 DAY` · `$10 / $50 per million tokens` · `this is not a tool drop. it's a repricing of labor.` · `operator vs employee` · `pick a side`

### Runner-up · rant (~85s)

Hook: *"anthropic just dropped a model that compressed two months of stripe engineering into one day. and the average operator is gonna spend today arguing in a slack thread about whether to try it."*

Full script in git history (commit ab7d547 recording pack). Payoff: *"the model got cheaper. your excuses got more expensive."*

### Bonus vertical · the deck test (~30s, new)

Green-screen both deck URLs side by side. Script beat: *"i asked the old model and the new model to build the same youtube deck. same brand kit. same script. one of them shipped three visual bugs and got the model's name wrong. the other one caught it. links in bio. judge the machines yourself."* This clip IS the trailer for the long-form.

---

## 5 · Clip plan from the long-form (no extra recording)

| Clip | Source | Runtime |
|---|---|---|
| Hook + twist | Slides 1-2 | ~35s vertical |
| The receipts read | Slide 6 | ~60s vertical |
| Identity beat | Slide 14 | ~60s vertical |
| Mic drop | Slide 15 close | ~20s vertical |

---

## 6 · Verification checklist (before publishing)

- [ ] No `[JOHN FILLS]` placeholders remain (verified zero in v4 deck)
- [ ] Zero em-dashes anywhere visible (deck verified at build; check overlays + captions + description)
- [ ] "fable 5" naming used throughout. Mythos referenced only as the locked variant.
- [ ] Stripe number phrased "roughly," never "literally"
- [ ] Slide-2 loop closed at slide 10, not before
- [ ] Whiteboard drawn live on slide 12, final line hand-printed: "route by bucket. not by hype."
- [ ] "pick well" delivered on slide 14 before cutting
- [ ] Both deck URLs in the video description: opus-v1 + fable-v2
- [ ] Final line: "go judge the machines yourself."
- [ ] Hold 2 full seconds before stopping recording

---

## 7 · Changelog

- v1 (ab7d547): "months became days / shelf is the strategy" angle. Killed by John 2026-06-09: jargon hook, design quality below bar.
- v2 (db6e8a9): Stakes slide added. Same angle. Superseded.
- v3 (3604267): personal-test angle, 16-slide Fable v2 deck, mythos→fable factual fix, restored whiteboard + receipts, real A/B meta-test, both decks deployed.
- v4 (this): rebuilt to the TWO experiments actually run (report test + deck test), zero placeholders, 15 slides, outcome-first hook ("it lost one of two tests"), settings-that-matter slide added. Recording-ready.

## 8 · Packaging (added 2026-06-11 · hook review)

First principle (copy-brain HOOK ANATOMY): the hook's one job is to CONFIRM THE CLICK and open a curiosity loop. Title + thumbnail do the attracting. The cold open confirms.

**Title (pick one):**
1. I Tested Anthropic's New AI. It Lost. (recommended: contrarian vs the "WILD!"/"Full Breakdown" hype wave, outcome-first)
2. Claude's New AI Just Lost To The Old One (I Tested Both)
3. The New Best AI In The World Has A Problem

**Thumbnail:** FABLE vs OPUS as two cards/fighters, red X or "LOST?" sticker over the NEW one. 3D style per profile-photo direction. Max 4 words on image.

**Cold open (locked in deck slide 1 verbatim):** "anthropic shipped the best model in the world on monday. i spent four hours testing it against the old one. and the new one lost. sort of. let me show you." The "sort of" is load-bearing: it is honest (fable won the deck test) AND it keeps the loop open.

**Retention spikes:** second hook at ~30s = the recursive twist (slide 2). Third at ~8min = the verdict strip. Description links: both deck URLs.

**Competitive gap (verified 6/11):** launch-wave titles are hype formats. Nobody has head-to-head data, nobody has new-model-loses, nobody can claim "this video was built by the model it reviews."
