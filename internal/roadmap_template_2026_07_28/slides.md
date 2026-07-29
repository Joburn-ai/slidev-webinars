---
theme: default
title: "The Roadmap -- @@Prospect_Name@@"
colorSchema: dark
transition: fade
mdc: true
fonts:
  serif: Fraunces
  sans: Hanken Grotesk
  mono: Space Mono
drawings:
  persist: true
  enabled: true
css: unocss
---

<!--
ROADMAP TEMPLATE v1 -- 2026-07-28
ONE DECK, THREE JOBS: the personalised roadmap · a content source · a training-first video.

VARIABLES: at-at-NAME-at-at tokens. Bare NAME = per-prospect (Bucket B). CLIENT_NAME = per-client static (Bucket A).
Filled by fill.mjs, which REFUSES to write if any token is unset. Never use double-brace --
Vue compiles it as an interpolation and renders an empty string silently.
GATES: three prospect gates at 14 / 28 / 50. Five producer quality gates marked QG-n -- each is a
REWRITE condition, not a checkbox. Airlock: say "roadmap locked" before a human sees it.
ENERGY PIVOT at slide 28: Doctor energy (1-27) -> General energy (28-54). Real visual break.
ANIMATION: v-click for density · v-motion for quantities changing · magic-move for the two-path
crossroads · drauu for the mechanism and the plan. Nothing decorative.
CONTENT: every section carries a CONTENT CUT marker. See content_map.md.
CLEAN CLAIMS: verified numbers only. No ROI multiples. No AI-led mechanism framing. No em-dashes.
-->

# @@Prospect_Name@@

<div class="eyebrow">Prepared @@Date@@ · @@CLIENT_Name@@</div>

<div v-click class="mt-12 text-2xl opacity-80">
A map needs two points.
</div>

<div v-click class="text-2xl opacity-80">
Where you are, and where you're going.
</div>

<div v-click class="mt-8 text-3xl">
Miss either one and there's no route. Just guessing.
</div>

<!--
CUT TO CAMERA. Say their name out loud. Do not read this slide.
VIDEO VERSION: replace the name with "you" and open here. This is the strongest cold open we have.
-->

---
layout: center
---

# Cards on the table

<div class="grid grid-cols-2 gap-8 mt-8">
<div v-click>

**What this is**

A diagnosis and a route, built from what you told us. Not a template.

</div>
<div v-click>

**What this isn't**

A pitch. There's an offer at the end. You'll see it coming.

</div>
</div>

<div v-click class="mt-12 deal-box">

**Three checkpoints are built into this.** Thirty seconds each.

Complete all three within **72 hours** and you unlock @@Catalyst_Asset_Name@@ -- normally @@Catalyst_Asset_Value@@.

<span class="opacity-70">The checkpoints light up as you go.</span>

</div>

<!--
QG note: do not change the 72-hour rule. If the batch claim is not true, do not make it.
The reason this slide works is that it names the game before playing it. People will do almost
anything if they know the rules. They resent almost anything if they find them out halfway.
-->

---

# §0 · What you told us about your capacity

<div class="constraint-grid mt-8">

<div v-click class="constraint">
<div class="label">TIME</div>
<div class="value">@@Constraint_Time@@</div>
<div v-motion :initial="{ width: 0 }" :enter="{ width: 'var(--ct-time, 0%)' }" class="bar"></div>
</div>

<div v-click class="constraint">
<div class="label">ENERGY</div>
<div class="value">@@Constraint_Energy@@</div>
<div v-motion :initial="{ width: 0 }" :enter="{ width: 'var(--ct-energy, 0%)' }" class="bar"></div>
</div>

<div v-click class="constraint">
<div class="label">ATTENTION</div>
<div class="value">@@Constraint_Attention@@</div>
<div v-motion :initial="{ width: 0 }" :enter="{ width: 'var(--ct-attention, 0%)' }" class="bar"></div>
</div>

</div>

<div v-click class="mt-10 text-xl">
Everything after this is built for <strong>that</strong>, not for someone with twice the hours.
</div>

<!--
This slide is why the constraint questions are not extractive. They asked, we used it, and they
can see we used it. The bars animate because a filling bar communicates "measured" in a way a
number does not.
CONTENT CUT: "The question nobody asks before giving you a plan." 45 sec.
-->

---

# §1 · The Diagnosis

<div class="section-marker">Slides 1 to 6 · Doctor energy</div>

---

# Basically, what you told us

<div class="snapshot mt-6">

<div v-click>"@@Snapshot_Quote_1@@"</div>
<div v-click>"@@Snapshot_Quote_2@@"</div>
<div v-click>"@@Snapshot_Quote_3@@"</div>

</div>

<div v-click class="mt-10 status-row">
<span class="pill red">@@Status_1@@</span>
<span class="pill yellow">@@Status_2@@</span>
<span class="pill green">@@Status_3@@</span>
</div>

<!--
QG-1 GATE. Does this use their ACTUAL WORDS, not paraphrases? At least one red or yellow,
never all green. If it fails: rewrite using direct quotes from the intake. Do not proceed.

This is the highest-trust slide in the deck. If they read their own sentence back, everything
after it is believed. If they read a paraphrase, everything after it is discounted.
-->

---

# What staying here costs

<div class="cost-stack mt-8">
<div v-click><span class="num">@@Cost_Monthly@@</span> a month, on your own numbers</div>
<div v-click><span class="num">@@Cost_Annual@@</span> over a year</div>
<div v-click class="opacity-70">And @@Cost_Non_Financial@@</div>
</div>

<!--
Their numbers, not ours. QG-4 later benchmarks the investment against THIS slide, so if this
is vague the close is vague.
-->

---

# §2 · The Argument

<div class="section-marker">Slides 7 to 13</div>

---
layout: center
---

<div class="text-5xl">Most people at your stage think the problem is <span class="strike">@@Common_Belief@@</span></div>

<div v-click class="mt-10 text-5xl accent">It's @@The_Actual_Problem@@</div>

<!--
CONTENT CUT: this slide alone is a reel. "Most people think X. It's actually Y." 30 sec, no context needed.
-->

---

# Your three pains, and the one door behind all of them

<div class="grid grid-cols-3 gap-6 mt-8">
<div v-click class="pain">
<div class="quote">"@@Pain_Quote_1@@"</div>
<div class="because">@@Door_Explanation_1@@</div>
</div>
<div v-click class="pain">
<div class="quote">"@@Pain_Quote_2@@"</div>
<div class="because">@@Door_Explanation_2@@</div>
</div>
<div v-click class="pain">
<div class="quote">"@@Pain_Quote_3@@"</div>
<div class="because">@@Door_Explanation_3@@</div>
</div>
</div>

<div v-click class="mt-10 text-center text-3xl accent">@@Invisible_Door_Name@@</div>

<!--
QG-2 GATE. All three pains must be DIRECT QUOTES. All three explanations must be DISTINCT and
each must name the Invisible Door differently. If two explanations say the same thing, rewrite.
-->

---

# The damaging admission

<div v-click class="text-3xl mt-8">@@Damaging_Admission@@</div>

<div v-click class="mt-8 text-xl opacity-80">
We're telling you because you'll find out anyway, and we'd rather you heard it from us.
</div>

<!--
Never soften this. It is the single highest-trust move in the deck and softening it is how it
becomes a throwaway line.
-->

---
layout: center
class: gate-slide
---

# Checkpoint 1 of 3

## The Reality Audit

<div class="mt-8 opacity-80">Thirty seconds. Then section three unlocks.</div>

<div class="mt-8 gate-fields">
<div>How big a priority is fixing this right now? <span class="field">1 to 10</span></div>
<div>Which of these have you already tried? <span class="field">multi-select</span></div>
<div>What's actually in the way? <span class="field">short text</span></div>
</div>

<!--
GATE 1 -- slide 14. Fields: fc1_priority, fc1_solutions_tried, fc1_obstacle_text.
Enforced: GHL tag Roadmap:Active, stop abandon sequence, start nudge.
This gate's job is a micro-yes plus segmentation. There is no right answer, so it is easy to pass.
-->

---

# §3 · Every option on the table

<div class="section-marker">Slides 15 to 21 · Including the ones that aren't us</div>

---

# Four ways to fix this

<div class="options mt-6">
<div v-click class="opt"><h3>Do it yourself</h3><div class="good">Good for: @@DIY_Good@@</div><div class="flaw">Fatal flaw: @@DIY_Flaw@@</div></div>
<div v-click class="opt"><h3>The cheap fix</h3><div class="good">Good for: @@Cheap_Good@@</div><div class="flaw">Fatal flaw: @@Cheap_Flaw@@</div></div>
<div v-click class="opt"><h3>The expensive fix</h3><div class="good">Good for: @@Expensive_Good@@</div><div class="flaw">Fatal flaw: @@Expensive_Flaw@@</div></div>
<div v-click class="opt us"><h3>@@CLIENT_Mechanism_Name@@</h3><div class="good">Good for: @@Us_Good@@</div><div class="flaw">Not ideal if: @@Us_Not_Ideal@@</div></div>
</div>

<!--
The "not ideal if" on our own option is load-bearing. An option list where ours has no downside
is an advert, and everyone can read an advert.
CONTENT CUT: "Four ways to fix this and the fatal flaw in each." Carousel or 60-sec reel.
-->

---
layout: center
---

# @@Micro_Agreement_Question@@

<div v-click class="mt-8 text-xl opacity-80">
If that's not right, that's useful too. Tell us at the next checkpoint.
</div>

<!--
QG-3 GATE. Is the thing they tried named with THEIR EXACT WORDS? If not, go back to the intake.
This is a soft airlock: a micro-agreement obtained BEFORE the mechanism is revealed. Skip it and
the mechanism lands on someone who hasn't agreed there's a problem.
-->

---

# §4 · The Path Forward

<div class="section-marker">Slides 22 to 27</div>

---
layout: center
class: whiteboard
---

# How it actually works

<div class="opacity-60 text-sm">Press <kbd>d</kbd> and draw this live</div>

<!--
DRAUU SLIDE. Draw the three-gear mechanism by hand while talking. Never more than three gears --
if the mechanism has more phases, group them. A hand building a diagram in real time does more
for trust than any rendered graphic, and it is the single best reason this deck is Slidev and
not a PDF.
VIDEO VERSION: this is the moment the video earns its length. Draw slowly.
CONTENT CUT: screen-record just this. "The whole mechanism in 90 seconds."
-->

---

# Your timeline

<div class="timeline mt-8">
<div v-click>Phase 1 · @@Phase_1_Name@@ <span class="dur">@@Phase_1_Duration@@</span></div>
<div v-click>Phase 2 · @@Phase_2_Name@@ <span class="dur">@@Phase_2_Duration@@</span></div>
<div v-click>Phase 3 · @@Phase_3_Name@@ <span class="dur">@@Phase_3_Duration@@</span></div>
</div>

<div v-click class="mt-10 opacity-80">
These durations are built from the @@Constraint_Time@@ you told us. Not a standard timeline.
</div>

<!--
Durations MUST be computed from the time band in §0. If every prospect gets the same timeline,
the constraint questions were theatre.
-->

---
layout: center
class: gate-slide pivot
---

# Checkpoint 2 of 3

## The Mechanism Check

<div class="mt-8 gate-fields">
<div>How clear does this feel right now? <span class="field">1 to 10</span></div>
<div>Compared to what you've tried, does this fill the gap? <span class="field">select</span></div>
<div>What still needs explaining? <span class="field">short text</span></div>
</div>

<div v-click class="mt-10 pivot-note">Everything after this is about you specifically.</div>

<!--
GATE 2 -- slide 28. Fields: fc2_clarity, fc2_comparison_check, fc2_explanation_text.
*** ENERGY PIVOT. *** Doctor energy ends here. General energy begins.
In the deck: colour temperature warms, type scale steps up, transitions get faster.
On camera: posture changes. Diagnostic becomes directive.
-->

---

# §5 · Your roadmap

<div class="section-marker">Slides 29 to 42 · General energy</div>

---
layout: center
class: whiteboard
---

# Where you start

<div class="opacity-60 text-sm">Press <kbd>d</kbd></div>

<!--
Second DRAUU slide. Draw THEIR plan, starting from THEIR constraint. If they said "tired" in §0,
the first thing you draw is the fastest visible win, not the highest-leverage task.
-->

---

# §6 · The Close

<div class="section-marker">Slides 43 to 49</div>

---

# What it costs

<div class="invest mt-8">
<div v-click class="line">Staying where you are <span class="num red">@@Cost_Annual@@</span></div>
<div v-click class="line">The expensive fix <span class="num">@@Expensive_Cost@@</span></div>
<div v-click class="line us">This <span class="num accent">@@Investment@@</span></div>
</div>

<!--
QG-4 GATE. Is the investment benchmarked against THEIR cost of inaction from slide 6 and THEIR
alternatives? If the comparison is generic, pull their numbers and recalculate.
Order matters: cost of inaction FIRST, our price LAST. Reverse it and the price is the anchor.
-->

---
layout: center
---

# Two ways this goes

<div class="crossroads mt-8" v-click>
<div class="path">
<h3>@@Path_A_Name@@</h3>
<div>@@Path_A_Outcome@@</div>
<div class="num">@@Path_A_Number@@</div>
</div>
<div class="path">
<h3>@@Path_B_Name@@</h3>
<div>@@Path_B_Outcome@@</div>
<div class="num">@@Path_B_Number@@</div>
</div>
</div>

<!--
QG-5 GATE. EXACTLY TWO PATHS. Both grounded in this prospect's real numbers and stated goal.
Three paths means no decision. Generic outcomes mean no stakes.
MAGIC-MOVE: the elements from the timeline slide re-arrange into these two futures. The
re-arrangement is the argument -- same inputs, two destinations, their choice.
CONTENT CUT: "Two ways this goes." The most re-postable slide in the deck.
-->

---

# Who this isn't for

<div class="anti mt-8">
<div v-click>@@Anti_Avatar_1@@</div>
<div v-click>@@Anti_Avatar_2@@</div>
<div v-click>@@Anti_Avatar_3@@</div>
</div>

<div v-click class="mt-10 opacity-80">If that's you, genuinely, don't. We'd rather say it now.</div>

---
layout: center
class: gate-slide final
---

# Checkpoint 3 of 3

<div class="mt-4 opacity-80">Only about 1 in 10 people make it here.</div>

<div class="mt-8 gate-fields">
<div>Write one honest sentence about this roadmap. <span class="field">text</span></div>
<div>Would you recommend this to a peer? <span class="field">1 to 10</span></div>
<div>What's the number one question we didn't answer? <span class="field">text</span></div>
</div>

<div v-click class="mt-8 unlock">Submit and @@Catalyst_Asset_Name@@ unlocks.</div>

<!--
GATE 3 -- slide 50. Fields: fc3_testimonial_text, fc3_star_rating, fc3_objection_text.
HARDEST-ENFORCED GATE. On submit: is now < start + 72h?
  YES -> Status:Winner -> Catalyst + Fast-Action Credit + pre-call resource
  NO  -> Status:Slow   -> Catalyst only
Q1 routes to testimonial capture. Q3 becomes the pre-call intel packet.

Note what this gate really is: a testimonial harvest at peak perceived value, before any ask,
from someone who just watched their own diagnosis assemble. A person who writes down that
something worked has made an argument to themselves, and self-generated arguments hold.
-->

---
layout: center
---

# @@CTA_Line@@

<div v-click class="mt-8">
<div class="calendar-embed">@@Calendar_Embed@@</div>
</div>

<div v-click class="mt-6 opacity-70 text-sm">
Or reply to the email. A person reads it.
</div>

<!--
Calendar hosted ON this page. No redirect. The booking is the normal next step in a page they
are already scrolling, not a new destination they have to decide to visit.
VIDEO VERSION: cut this slide entirely. The video is the diagnosis; the call is the sale, and
pitching on a teaching asset costs more than it makes.
-->

---
hide: true
class: icon-safelist
---

<!--
TOOLBAR ICON SAFELIST -- hidden slide. Never rendered. Do not delete.

WHY IT EXISTS. Slidev's toolbar components live inside node_modules/@slidev/client
and reference icons as class="i-carbon:pen". UnoCSS only generates icon CSS for
classes it finds while scanning SOURCE, and node_modules is not scanned, so on
every deck in this repo the buttons rendered with no glyph. The masks in style.css
are the actual fix; this div keeps the class strings present in scanned source so
nothing regresses if the masks are ever replaced by a proper Uno config.

`hide: true` means the audience never sees this. Presenter mode skips it too.

Note the COLON: i-carbon:pen, not i-carbon-pen. The hyphen form generates nothing,
silently.
-->

<div hidden aria-hidden="true" class="i-carbon:pen i-carbon:erase i-carbon:undo i-carbon:redo i-carbon:trash-can i-carbon:arrow-up-right i-carbon:radio-button i-carbon:checkbox i-carbon:pin i-carbon:pin-filled i-carbon:close-outline i-carbon:error i-carbon:arrow-left i-carbon:arrow-right i-carbon:apps i-carbon:moon i-carbon:sun i-carbon:maximize i-carbon:camera i-carbon:information"></div>

---
layout: center
class: miro-slide
---

# How it all connects

<div class="miro-frame">
<iframe
  src="https://miro.com/app/live-embed/uXjVLcJeJiM=/?focusWidget=3458764600705984458&embedMode=view_only_without_ui&embedId=498631205240"
  frameborder="0" scrolling="no"
  allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen>
</iframe>
</div>

<!--
MIRO EMBED TEST -- 2026-07-28.
Works: Slidev renders raw iframes, so a live Miro board embeds directly. embedMode=
view_only_without_ui strips Miro's chrome so it reads as a diagram rather than a
tool someone else is using.

WHY THIS MATTERS BEYOND THIS SLIDE. If a Miro board embeds cleanly, then the
mechanism diagram in a client's roadmap can be a LIVE board rather than a
screenshot. Generate the board via the Miro REST API from their config, drop the
embed id into their deck, and their flowchart is theirs, zoomable, and updatable
without re-exporting a single image. That is the automation John is pointing at.

CAVEAT -- it needs a network connection at present time. An offline present or a
PDF export shows an empty frame. So: live board for screen-share and web, static
image fallback for the PDF cut. Both from the same board.
-->
