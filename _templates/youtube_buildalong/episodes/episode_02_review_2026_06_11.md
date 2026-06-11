# EP02 Deck Review — Decision-Ready Synthesis (2026-06-11)

Four-lens review (structure / storytelling / retention+length / QC) of the Fable 5 vs Opus 4.8 build-along deck.
Files: `episode_02_fable5_mythos5_drop.md` + `episode_02_recording_pack.md`.

---

## 1. VERDICT (2 lines)

**Not good to record as-is.** The content and the writing are strong (the loss-first head-to-head is a genuine moat), but the deck has live placeholder text that will be read on camera, a broken/triple-conflicting slide count (13 actual / 15 pack / 16 title+labels) that desyncs presenter notes, and two redundant idea-pairs plus a 5x refrain that pad the back half.
**Fix the four blockers below (roughly 30-45 min of surgical edits), then record.** No re-scripting, no re-design — the slides are 90% there.

---

## 2. TARGET RUNTIME

**11-13 minutes (target ~12), NOT the planned 15-18.**

Reasoning:
- At 3,680 subs there is no retention floor to absorb a sag — every minute pays full freight. The density-winners (Saraev 22%, AI Explained 21%, AI Jason 19%) win on promise-to-payload ratio, not minutes; AI Jason only sustains 15-30 min at 223K subs.
- The entire payload (the new model lost + the deck under review built itself) is fully deliverable in ~11 min. Past that, the open loops are closed and retention falls regardless of how good the tail slides are.
- The two retention anchors — the receipts chart and the deck-test loop-close — land at better curve positions in a 12-min cut. The loop-close hits ~minute 8 (66% through, textbook bump position); in an 18-min cut it slips to ~minute 11 with 6+ min of tail most viewers never reach.
- The length problem is entirely front-load (3 consecutive frame slides + double stakes) and back-load (3 close slides + 2-3 min whiteboard + 5x "route by bucket" refrain). Cutting those lands ~12 min with every minute earning itself.

---

## 3. TOP 5 CHANGES (ranked by leverage)

### 1. Fill the live placeholders + fix the numbering (BLOCKER — all-lens)
Two issues that will visibly break the recording:
- **Placeholders the presenter will read on camera**, while the pack claims "zero placeholders, verified":
  - Deck-test notes (lines 698, 701): `[ADD YOUR HONEST READ]`, `[SAY IT. ONE REASON.]` — fill with John's locked read already on-slide ("more context, real fact-checks, added the chart. better. but not night-and-day better").
  - Verdict notes (lines 890-895): `[CLICK 1] acquisition. [WINNER]. because [REASON]...` — stale; rewrite verbatim to match the locked on-slide cards (acq = opus for now, CS = opus 4.8, ops = split, rule = fable architects / opus executes).
  - Whiteboard (lines 808-809) + recap (lines 1039-1041): fill winners, or explicitly relabel `[LIVE DRAW]` / `[AD-LIB]` so they read as stage directions.
- **Numbering chaos**: comments run 01-09, jump to "SLIDE 12 / 16 · TEST 04", an un-numbered settings slide, then 13-16/16. There are 13 actual content slides. Renumber every comment to N/13 in render order, kill the "TEST 04" leftover label, change frontmatter `info` (line 10) from "16-slide" to "13-slide", and rebuild recording-pack §2 as a true 13-row table (update every "slide 10 / 12 / 14" reference in §1/§2/§5/§6 to match).

### 2. Re-spine from hero's-journey to TRIAL/VERDICT + hold the loss reveal (highest narrative leverage)
The deck is labeled hero's-journey but the content is a courtroom: two contenders, two trials, one verdict, viewer is the jury. That is the moat ("the channel where things are allowed to lose"). Almost no slide surgery — relabel the beats and change ~3 transition lines:
- **Slide 1 cover**: stop resolving the outcome. Change the sub-reveal from the statement "it lost one of them" to the verdict QUESTION — open the loop, hold WHICH trial it lost. Move the "it lost" gut-punch to land on the report-test slide where it has earned weight (it is the most credible moment in the video; do not spend it in second 10).
- **Split that cover reveal into two v-clicks** (QC #8): click 1 = "the new best model in the world. two head-to-head experiments against opus 4.8." click 2 = the bolded loss line — so the audience does not read the payoff before John says it.
- Reframe the whiteboard opener from "let's route this" to "let's enter the verdict into the record," and land slide 15 on the verdict identity ("every other channel told you it wins everything; I'm the one who let it lose") feeding the existing "go judge the machines yourself" CTA.

### 3. Kill the redundant idea-pairs: stakes/identity and whiteboard/verdict
Two ideas are each told twice, padding the back half (structure + storytelling agree):
- **Stakes (slide 3) duplicates the identity beat (slide 14).** Slide 3's "the version of you who knows which model fits where" IS the slide-14 thesis. Demote slide 3 to a tight cost-stakes frame — keep the labor-cost reality-check + the if-test/if-don't pair, CUT the third "version of you" callout. Let the identity payoff land once, on slide 14.
- **Whiteboard (slide 12) duplicates the verdict grid (slide 13).** Both deliver the same per-bucket routing answer. Collapse to one beat: make the whiteboard BE the verdict — draw the winner under each bucket live (most native to build-along) and cut the static verdict slide, OR keep slide 13 as the screenshot-able summary and strip the whiteboard's redundant rule-printing. Two slides, one idea = drag.

### 4. Cut the front-load tax: fold slide 4, halve slide 3, compress the benchmark
Get to first proof in ~30-40s instead of ~83s (winners open ON the receipt):
- **Cut slide 4 (who's testing)** — weakest retention slide. Fold the one load-bearing line ("I build with Claude every day across three buckets: acquisition, customer success, operations") into slide 3 over cam in ~8s; this also plants the 3-bucket spine earlier (currently it floats until slide 7).
- **Compress slide 3** to a single ~12s cost-stakes line (per change 3); move the "by next Monday" urgency to the recap.
- **Compress the benchmark (slide 6)** to one stat pair + the Stripe line (~40s, not 75s) and reframe the speaker beat as "here's their pitch — now watch what happened when I ran it," so Anthropic's marketing chart becomes the claim your experiments TEST, not standalone proof borrowed from the hype machine you're positioned against. KEEP the chart — it is a real retention anchor — just tighten it and verify the asset (`knowledge_work_graph.png`) actually plots the SWE-Bench/FrontierCode bars the cards cite, on the ZOOM slide where the audience stares.

### 5. Drop the "route by bucket" refrain from 5x to 3x + tighten the close
"Route by bucket, not by hype" fires on slides 7, 12, 13, 14, AND 15 — past the third hit it reads as padding / stretching.
- Keep it on **slide 7 (plant)** + **slide 12 whiteboard (live-drawn payoff, most powerful)** + **slide 15 recap (takeaway)**. Cut it from slide 13 (eliminated anyway if change 3 collapses the whiteboard/verdict) and from slide 14's callout.
- **Cap the whiteboard at 90s** (it is 2-3 min budgeted — webinar pacing; three boxes, one winner each, hand-print the rule, done).
- **Trim settings (slide 11) to 2 cards** (THE FALLBACK + THE WINDOW; drop edit-automatically + effort-levels inside-baseball) and move it OUT from between the loop-close and the whiteboard — it kills the emotional peak. Put it after the verdict as a "before you go test it yourself" coda, or fold into slide 8's tally.
- **Split overloaded recap point 01** (currently 4 ideas in one click): keep the two verdicts + effort claim, drop the urgency window (it lives elsewhere).

---

## 4. DO NOT CHANGE — these are working (do not over-edit)

- **Slide 14 identity beat** — "the model lowers the cost. you still pick. pick well." Already verdict-spine writing; the strongest line in the deck. The strike-through on "which model to use" is intentional and lands.
- **Slide 15 CTA** — "go judge the machines yourself." The best line in the deck; it literally hands the jury role to the viewer and confirms the trial spine.
- **The slide-6 receipts chart** — strongest retention slide, correctly placed mid-video as the earned spike. Tighten the runtime (change 4), but keep the slide and the ZOOM treatment.
- **The slide-2 deck-built-itself loop** — keep it; do NOT cut. Subordinate it to the does-it-win loop (secondary garnish, not co-equal), but it is a genuinely strong open-at-2 / close-at-10 loop.
- **The slide-10 deck-test loop-close** — the marquee retention anchor; protect its ~2 min dwell. This is the one experiment that earns the full budget.
- **The two experiments existing as the core** — the report test (Opus won) + deck test (Fable won) are the unique value; tighten the report test to ~85s but keep both intact.
- **Em-dash compliance** — deck and recording pack are both clean. No sweep needed on the ship artifacts.
- **The hero's-journey arc skeleton** — the call/stakes/guide/trials/map/return spine is fundamentally sound; the re-spine (change 2) is a relabel + reveal-hold, not a rebuild. Do not throw out the structure.

---

## Cross-lens note: where all four reviewers converged
The four lenses independently flagged the same high-leverage items, which raises confidence:
- Broken numbering (structure + QC) — blocker.
- Live placeholders (QC) — blocker.
- Stakes/identity duplication (structure + storytelling).
- Whiteboard/verdict duplication (structure + storytelling + retention).
- 5x "route by bucket" refrain (structure + retention).
- Front-load tax / cut slide 4 + halve slide 3 (retention + structure).
- Loss should lead, not be buried (structure + storytelling).
The disagreement is narrow: storytelling wants a full re-spine label change; structure/retention treat it as reordering + cuts. They are compatible — the re-spine is achieved by the same edits (hold the reveal, sequence trials by stakes, land identity once).
