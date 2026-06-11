# Episode 02 · Recording Pack · v3 (FABLE v2 deck)

**Date locked:** 2026-06-10
**Episode:** i spent 2 hours testing fable 5. (the deck fable built.)
**Deck (16 slides):** [episode_02_fable5_mythos5_drop.md](episode_02_fable5_mythos5_drop.md)

| URL | What |
|---|---|
| https://joburn-buildalong-ep02.vercel.app | Main · currently Fable v2 · record off this |
| https://joburn-buildalong-ep02-fable-v2.vercel.app | Permanent Fable v2 snapshot |
| https://joburn-buildalong-ep02-opus-v1.vercel.app | Permanent Opus v1 snapshot · the A/B artifact |

> **The play:** one recording session produces the YouTube workshop (16-22 min) + 2 vertical green-screen hot takes + 3 clipped shorts from the long-form. The deck's test 04 shows BOTH deck versions on camera. Put both URLs in the video description.

---

## 1 · BEFORE recording: run the 5 tests (this is the 2 hours)

The deck has `[JOHN FILLS]` placeholder blocks on slides 9, 10, 11, 12, 14, 16. Run each test on BOTH models first, paste the outputs in, rebuild, redeploy. Test prompts:

| # | Bucket | Exact play |
|---|---|---|
| 01 | Acquisition | Same prompt to both models: "pull F6 + voice DNA for [Enable or SupportED] from copy brain. write 5 ad hooks. apply our taxonomy." Zero retries. Paste each model's strongest hook. |
| 02 | Customer success | Hand both a real client CSV (spend / clicks / conversions). "Produce the full weekly growth report. dollar-anchor every recommendation." Paste each model's sharpest insight. |
| 03 | Operations | "Read skill X + memory lesson Y. refactor X to include Y. preserve existing behavior. ship a diff." Compare turns + whether behavior survived. |
| 04 | Meta · the deck | DONE. Opus built v1, Fable built v2. Both live at the URLs above. Add your honest read to the Fable card on slide 12. |
| 05 | Judgment | Ask both: "which of the three buckets benefits most from fable 5 specifically, and why?" Compare the REASONING. Feeds the verdict + recap. |

**Fact locks while talking:**
- You tested **Fable 5**, not Mythos. Mythos 5 is the same model with cyber safeguards lifted, locked to Project Glasswing. The deck teaches this distinction on slide 5. Don't undo it on camera.
- Stripe: 50 million lines of Ruby, codebase-wide migration, one day, team had it scoped at two-plus months. Say "roughly" on any compression multiple. Never "literally."
- Pricing: $10 in / $50 out per million tokens. Less than half of Mythos Preview. Free on Pro/Max through June 22, credits start June 23.
- Benchmarks: SWE-Bench Pro 80.3 vs 69.2 (Opus) vs 58.6 (GPT-5.5). FrontierCode 29.3 vs 13.4 vs 5.7.
- Safety fallback: roughly 5% of sessions route to Opus 4.8 on cyber/bio/chem topics. Users are told when it happens.

---

## 2 · The 16-slide map (scene + tempo + time)

| # | Slide | Scene | Tempo | Time |
|---|---|---|---|---|
| 1 | Cover · "i spent 2 hours testing fable 5" | A | FRAME | 8-12s |
| 2 | The twist · "the model under review built this deck" | B | FRAME | ~20s |
| 3 | Stakes · "labor-cost reality check" | B | FRAME | ~25s |
| 4 | Who's testing · 3 not-tags + hero card | B | FRAME | ~30s |
| 5 | What dropped · butterfly hero + 4 facts | A | MOVE FAST | ~60s |
| 6 | Receipts · agentic-coding chart + annotations | A | ZOOM | ~75s |
| 7 | The frame · 3 buckets | A | MOVE FAST | ~45s |
| 8 | Test plan · 5 rows | A | MOVE FAST | ~40s |
| 9 | Test 01 · acquisition | A | MOVE FAST | ~2min |
| 10 | Test 02 · customer success | A | MOVE FAST | ~2min |
| 11 | Test 03 · operations | A | MOVE FAST | ~2min |
| 12 | Test 04 · the deck test (closes slide-2 loop) | B | MOVE FAST | ~2min |
| 13 | Whiteboard · draw the routing layer (drauu) | A | STOP | 2-3min |
| 14 | Verdict by bucket | A | LAND | ~60s |
| 15 | Identity beat · "you still pick" | A | LAND · SLOW | ~75s |
| 16 | Recap + CTA | D | LAND | ~35s |

**Estimated runtime: 16-21 min.** Hero's Journey: call (1) → stakes (2-3) → guide (4) → truth (5-8) → trials (9-12) → map (13) → verdict (14) → transformation (15) → return (16).

**The slide-2 / slide-12 loop:** slide 2 opens the "both decks" loop, slide 12 closes it. Don't reveal the verdict early. If you slip, cut it in the edit.

---

## 3 · OBS scenes (same 4-scene rig + vertical)

| Scene | Hotkey | Use on |
|---|---|---|
| A · Slides + cam corner | Cmd+1 | 1, 5-11, 13-15 |
| B · Slides + large cam | Cmd+2 | 2, 3, 4, 12 |
| D · Cam only | Cmd+4 | 16 |
| E · Vertical green-screen | Cmd+5 | IG clips after the main recording |

Whiteboard (slide 13) stays in Scene A: drauu pen on the slide itself. Drawings persist between rehearsals (`drawings.persist: true`).

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
| Identity beat | Slide 15 | ~60s vertical |
| Mic drop | Slide 16 close | ~20s vertical |

---

## 6 · Verification checklist (before publishing)

- [ ] All `[JOHN FILLS]` placeholders replaced with real test outputs (slides 9-12, 14, 16)
- [ ] Zero em-dashes anywhere visible (deck verified at build; check overlays + captions + description)
- [ ] "fable 5" naming used throughout. Mythos referenced only as the locked variant.
- [ ] Stripe number phrased "roughly," never "literally"
- [ ] Slide-2 loop closed at slide 12, not before
- [ ] Whiteboard drawn live, final line hand-printed: "route by bucket. not by hype."
- [ ] "pick well" delivered on slide 15 before cutting
- [ ] Both deck URLs in the video description: opus-v1 + fable-v2
- [ ] Final line: "go judge the machines yourself."
- [ ] Hold 2 full seconds before stopping recording

---

## 7 · Why v3 of this pack exists (changelog)

- v1 (ab7d547): "months became days / shelf is the strategy" angle. Killed by John 2026-06-09: jargon hook, design quality below bar.
- v2 (db6e8a9): Stakes slide added. Same angle. Superseded.
- v3 (this): personal-test angle, 16-slide Fable v2 deck, mythos→fable factual fix, restored whiteboard + receipts, real A/B meta-test with both decks deployed. Built BY Fable 5 as part of the test.

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
