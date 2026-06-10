---
theme: default
title: Episode 02 · i spent 2 hours testing claude mythos so you don't have to.
info: |
  Joburn Build-Along · Episode 02 · 2026-06-09
  Personal-test workshop on Anthropic's Fable 5 / Mythos 5 drop.
  Frame: 5 real operator tasks · head-to-head Mythos vs Opus 4.8 · 3-bucket recommendation.
  Format: 12-slot YouTube build-along, atomic-era retro-futurist.
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  enabled: true
  persist: true
  syncAll: false
transition: slide-left
mdc: true
clickAnimation: fade
fonts:
  sans: Inter
  serif: 'Crimson Pro'
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
css: unocss
---


<!-- ============================================================
     SLIDE 01 / 12 · COVER · 8-12s · Scene A
     ============================================================ -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow" style="color: var(--ff-orange);">Joburn · Build-Along · EP 02 · 2026-06-09</div>

<h1 style="font-size: 4.4rem; color: white; line-height: 1.04; margin-bottom: 1.5rem;">
i spent 2 hours testing<br/>
<span class="ff-orange">claude mythos.</span>
</h1>

<v-click>

<p style="font-size: 1.5rem; color: rgba(255,255,255,0.88); max-width: 50rem; margin: 0 auto; line-height: 1.4;">
so you don't have to. five real tasks. head-to-head against opus 4.8. here's what i found.
</p>

</v-click>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.45); font-size: 0.72rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOHN COBURN · JOBURN.COM
</div>

</div>

<!--
COVER VERBATIM (Scene A · 8-12s):

i spent two hours testing claude mythos. so you don't have to.

[CLICK · reveal sub]

five real tasks. head-to-head against opus four point eight. here's what i found.

PRESENTER NOTES:
- cold open. no logo bumper, no "what's up." straight in.
- "mythos" gets emphasis. that's the name nobody else will know yet.
- hold final beat 1 second before clicking forward.
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 02 / 12 · STAKES · ~25s · Scene B (large cam) -->

<div class="absolute inset-0 px-14 py-10 flex flex-col justify-center" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="ff-eyebrow">before i show you anything</div>

<h2 style="font-size: 2.5rem; line-height: 1.15; max-width: 50rem;">
this is not a model review video. it's a <span class="ff-cyan">labor-cost reality check.</span>
</h2>

<div class="rule-thin"></div>

<div class="comparison-pair mt-5">

<v-click>

<div class="ff-card" style="border-left: 4px solid var(--ff-cyan); padding: 1.1rem 1.25rem;">
<div class="ff-eyebrow" style="margin-bottom: 0.45rem; font-size: 0.65rem; color: var(--ff-cyan);">if you test it</div>
<p style="margin: 0; font-size: 0.98rem; line-height: 1.45;">you know which model to default to per bucket. you stop paying opus dollars for tasks fable handles cheaper. <strong class="ff-cyan">your cost per outcome drops.</strong></p>
</div>

</v-click>

<v-click>

<div class="ff-card" style="border-left: 4px solid #94463b; padding: 1.1rem 1.25rem;">
<div class="ff-eyebrow" style="margin-bottom: 0.45rem; font-size: 0.65rem; color: #94463b;">if you don't</div>
<p style="margin: 0; font-size: 0.98rem; line-height: 1.45;">you let your defaults drift. and competitors with sharper defaults <strong style="color: #94463b;">out-leverage you on cost per outcome.</strong> quietly. for months.</p>
</div>

</v-click>

</div>

<v-click>

<div class="mt-6 px-5 py-3.5" style="background: var(--ff-navy); color: white; border-radius: 10px;">
<p style="margin: 0; font-size: 1.05rem; line-height: 1.4;">the version of you who knows which model fits where <span class="ff-orange">beats the version that defaults to the latest.</span> by a lot. by next monday.</p>
</div>

</v-click>

</div>

<!--
STAKES VERBATIM (Scene B · slow · ~25s):

before i show you anything else. one frame.

this is not a model review video. it's a labor-cost reality check.

[CLICK 1 · "if you test it"]
if you test this thing for two hours, you walk away knowing which model to default to per bucket. you stop paying opus dollars on tasks fable handles cheaper. your cost per outcome drops.

[CLICK 2 · "if you don't"]
if you don't. your defaults drift. and competitors with sharper defaults out-leverage you on cost per outcome. quietly. for months.

[CLICK 3 · navy callout]
the version of you who knows which model fits where beats the version that defaults to the latest. by a lot. by next monday.

PRESENTER NOTES:
- Scene B (large cam, intimate)
- "by next monday" is the punch. let it sit.
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 03 / 12 · WHO I AM · ~30s · Scene B -->

<div class="absolute inset-0 px-14 py-10 flex flex-col justify-center" style="background: var(--ff-cream);">

<div class="ff-bar"></div>

<div class="ff-eyebrow">who's testing</div>

<h2 style="font-size: 2.3rem; line-height: 1.15; max-width: 48rem;">
i'm john coburn. i build operator-OS <span class="ff-cyan">for founders.</span>
</h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-3 gap-4 mt-5 max-w-4xl">

<div class="not-tag">not an anthropic employee</div>
<div class="not-tag">not a benchmark site</div>
<div class="not-tag">not a hype creator</div>

</div>

<v-click>

<div class="ff-card-hero mt-6" style="max-width: 50rem;">
<p style="font-size: 1.1rem; line-height: 1.5; margin: 0; color: var(--ff-navy);">
i build with claude every day across three buckets. <strong class="ff-cyan">acquisition. customer success. operations.</strong> so this test isn't "does it win swe-bench." it's <strong>"does it actually replace work i'm already paying opus to do."</strong>
</p>
</div>

</v-click>

</div>

<!--
WHO I AM VERBATIM (Scene B · ~30s):

quick. who's testing.

i'm john coburn. i build operator-OS for founders. hyper-leverage agency. claude in my stack every day.

not an anthropic employee. not a benchmark site. not a hype creator.

[CLICK · hero card]
i build with claude every day across three buckets. acquisition. customer success. operations. so this test isn't "does it win swe-bench." it's "does it actually replace work i'm already paying opus to do."

PRESENTER NOTES:
- still Scene B
- 3 not-cards lower defenses (per BSMD pattern)
- hero card lands the operator frame
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 04 / 12 · THE FRAME · ~45s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-8">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the frame</div>

<h2 style="font-size: 2.2rem; margin-top: 0.25rem;">three buckets. <span class="ff-cyan">every operator task lives in one.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-3 gap-5 mt-5">

<v-click>

<div class="bucket-card acq">
<div class="ff-numeral" style="color: #94463b;">01</div>
<div class="bucket-name">acquisition</div>
<div class="bucket-headline">getting attention</div>
<div class="bucket-examples">ads · hooks · funnels · landing pages · copy · creative</div>
</div>

</v-click>

<v-click>

<div class="bucket-card cs">
<div class="ff-numeral" style="color: var(--ff-cyan);">02</div>
<div class="bucket-name">customer success</div>
<div class="bucket-headline">keeping it working</div>
<div class="bucket-examples">reports · audits · strategy calls · retention · weekly cadence</div>
</div>

</v-click>

<v-click>

<div class="bucket-card ops">
<div class="ff-numeral" style="color: var(--ff-orange);">03</div>
<div class="bucket-name">operations</div>
<div class="bucket-headline">making it scale</div>
<div class="bucket-examples">skills · SOPs · refactors · data pipes · internals</div>
</div>

</v-click>

</div>

<v-click>

<div class="mt-6 px-5 py-3" style="background: var(--ff-warm); border-left: 4px solid var(--ff-orange); border-radius: 6px;">
<p style="margin: 0; font-size: 1.05rem; color: var(--ff-navy);"><strong>just because you can</strong> use mythos on every task <strong class="ff-cyan">doesn't mean you should.</strong> pick the bucket that compounds.</p>
</div>

</v-click>

</div>

<!--
FRAME VERBATIM (Scene A · ~45s):

quick map. then we test.

three buckets. every operator task lives in one of them.

[CLICK 1 · acquisition]
one. acquisition. getting attention. ads, hooks, funnels, landing pages, copy.

[CLICK 2 · CS]
two. customer success. keeping it working. reports, audits, strategy calls, retention.

[CLICK 3 · ops]
three. operations. making it scale. skills, SOPs, refactors, internals.

[CLICK 4 · callout]
just because you can use mythos on every task doesn't mean you should. pick the bucket that compounds. that's the whole philosophy.

PRESENTER NOTES:
- Scene A. could also live-draw this on drauu if you want STOP tempo here
- "just because you can" line is the philosophy. don't rush it.
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 05 / 12 · THE 5 TESTS · ~40s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the test plan</div>

<h2 style="font-size: 2.1rem; margin-top: 0.25rem;">five tasks. real client data. <span class="ff-cyan">side-by-side.</span></h2>

<div class="rule-thin"></div>

<div class="space-y-2 mt-4" style="display: flex; flex-direction: column; gap: 0.65rem;">

<v-clicks>

<div class="ff-card" style="padding: 0.85rem 1.1rem; display: flex; align-items: center; gap: 1rem;">
<span class="ff-numeral" style="color: #94463b; font-size: 1.3rem;">01</span>
<span class="bucket-name" style="color: #94463b; font-size: 0.7rem; min-width: 8rem;">ACQUISITION</span>
<span style="font-size: 1rem; flex: 1;">5-hook ad pack for a real client via <code style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: var(--ff-cyan);">copy_brain_retrieve</code></span>
</div>

<div class="ff-card" style="padding: 0.85rem 1.1rem; display: flex; align-items: center; gap: 1rem;">
<span class="ff-numeral" style="color: var(--ff-cyan); font-size: 1.3rem;">02</span>
<span class="bucket-name" style="color: var(--ff-cyan); font-size: 0.7rem; min-width: 8rem;">CUSTOMER SUCCESS</span>
<span style="font-size: 1rem; flex: 1;">complete weekly growth report from a real client CSV</span>
</div>

<div class="ff-card" style="padding: 0.85rem 1.1rem; display: flex; align-items: center; gap: 1rem;">
<span class="ff-numeral" style="color: var(--ff-orange); font-size: 1.3rem;">03</span>
<span class="bucket-name" style="color: var(--ff-orange); font-size: 0.7rem; min-width: 8rem;">OPERATIONS</span>
<span style="font-size: 1rem; flex: 1;">refactor an existing skill incorporating a new memory lesson</span>
</div>

<div class="ff-card" style="padding: 0.85rem 1.1rem; display: flex; align-items: center; gap: 1rem; background: var(--ff-warm);">
<span class="ff-numeral" style="font-size: 1.3rem;">04</span>
<span class="bucket-name" style="font-size: 0.7rem; min-width: 8rem;">META · RECURSIVE</span>
<span style="font-size: 1rem; flex: 1;"><strong>use mythos to design this very deck.</strong> compare to opus version.</span>
</div>

<div class="ff-card" style="padding: 0.85rem 1.1rem; display: flex; align-items: center; gap: 1rem;">
<span class="ff-numeral" style="font-size: 1.3rem;">05</span>
<span class="bucket-name" style="font-size: 0.7rem; min-width: 8rem;">IDENTITY</span>
<span style="font-size: 1rem; flex: 1;">which bucket benefits MOST from mythos specifically. ask both. compare judgment.</span>
</div>

</v-clicks>

</div>

</div>

<!--
TEST PLAN VERBATIM (Scene A · ~40s · click each row as you read):

five tests. each one runs on both models. clean prompt. zero retries. winner takes the bucket.

[CLICK 01]
one. acquisition. five-hook ad pack for a real client. grounded in copy_brain_retrieve.

[CLICK 02]
two. customer success. full weekly growth report from a real client CSV.

[CLICK 03]
three. operations. refactor a skill incorporating a memory lesson. long-horizon agentic work.

[CLICK 04]
four. meta. recursive. use mythos to design this very deck. then compare to what opus gave me. you're literally watching the result right now.

[CLICK 05]
five. identity. ask both models which bucket benefits most from mythos specifically. compare the judgment, not just the output.

PRESENTER NOTES:
- click each row AS you say the number
- "you're literally watching the result right now" lands the recursive test
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 06 / 12 · TEST 01 · Acquisition · ~2 min · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="color: #94463b; font-size: 1.6rem;">01</span>
<span class="section-tag" style="color: #94463b; border-color: #94463b;">TEST · ACQUISITION</span>
</div>

<h2 style="font-size: 2rem; margin-top: 0.4rem;">a 5-hook ad pack <span class="ff-cyan">grounded in client canon.</span></h2>

<p style="font-size: 0.92rem; color: var(--ff-charcoal); margin-top: 0.4rem; margin-bottom: 0.5rem; font-style: italic;">prompt: pull F6 + voice DNA via <code>copy_brain_retrieve</code>. write 5 ad hooks for [client]. apply our taxonomy. zero retries.</p>

<div class="comparison-pair mt-3">

<v-click>

<div class="model-card mythos">
<div class="model-name">Mythos 5 · output</div>
<div class="placeholder-block">
[JOHN FILLS · paste verbatim Mythos hook output here. ~5 lines max so it fits the card.]
</div>
</div>

</v-click>

<v-click>

<div class="model-card opus">
<div class="model-name">Opus 4.8 · output</div>
<div class="placeholder-block">
[JOHN FILLS · paste verbatim Opus hook output here. ~5 lines max.]
</div>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-4">
<span class="winner-tag">winner: [TBD]</span>
<p style="margin: 0; font-size: 0.95rem;">[JOHN FILLS · 1-line verdict. what made the difference. which one is your default for acquisition copy going forward.]</p>
</div>

</v-click>

</div>

<!--
TEST 01 VERBATIM (Scene A · ~2 min):

test one. acquisition. five hooks for a real client. grounded in F6 plus voice DNA via copy_brain_retrieve. same prompt to both models. zero retries.

[CLICK 1 · Mythos card]
here's what mythos gave me. [READ MYTHOS OUTPUT verbatim or paraphrase the strongest line]

[CLICK 2 · Opus card]
here's what opus gave me. [READ OPUS OUTPUT verbatim]

[CLICK 3 · verdict strip]
the winner. [READ VERDICT]. and that's because [one specific reason · voice fit, brand fit, sultanic pattern adherence, etc].

PRESENTER NOTES:
- prep: copy actual model outputs to the placeholders BEFORE recording
- read verdict slow. that's the moment.
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 07 / 12 · TEST 02 · CS · ~2 min · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="color: var(--ff-cyan); font-size: 1.6rem;">02</span>
<span class="section-tag">TEST · CUSTOMER SUCCESS</span>
</div>

<h2 style="font-size: 2rem; margin-top: 0.4rem;">weekly growth report from <span class="ff-cyan">real CSV ad data.</span></h2>

<p style="font-size: 0.92rem; color: var(--ff-charcoal); margin-top: 0.4rem; margin-bottom: 0.5rem; font-style: italic;">prompt: this client spent $X. got Y leads. produce a complete weekly growth report. dollar-anchor every recommendation.</p>

<div class="comparison-pair mt-3">

<v-click>

<div class="model-card mythos">
<div class="model-name">Mythos 5 · output</div>
<div class="placeholder-block">
[JOHN FILLS · top 2-3 lines of Mythos's report. surface its strongest insight or its tightest dollar-anchor.]
</div>
</div>

</v-click>

<v-click>

<div class="model-card opus">
<div class="model-name">Opus 4.8 · output</div>
<div class="placeholder-block">
[JOHN FILLS · top 2-3 lines of Opus's report. same selection rule.]
</div>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-4">
<span class="winner-tag">winner: [TBD]</span>
<p style="margin: 0; font-size: 0.95rem;">[JOHN FILLS · 1-line verdict. did one model catch a leak the other missed? what changes your CS default.]</p>
</div>

</v-click>

</div>

<!--
TEST 02 VERBATIM (Scene A · ~2 min):

test two. customer success. real client CSV. spend, leads, conversions. produce a full weekly growth report. dollar-anchor every rec.

[CLICK 1 · Mythos]
mythos read the data and gave me this. [READ TOP INSIGHT]

[CLICK 2 · Opus]
opus gave me this. [READ TOP INSIGHT]

[CLICK 3 · verdict]
the winner. [READ VERDICT]. [ONE CONCRETE DIFFERENCE]. and if you're running weekly reports for clients, this is the model you actually want under the hood. or not.

PRESENTER NOTES:
- weekly reports are recurring spend. this is the highest-cost-of-being-wrong bucket
- use the verb "under the hood" (voice DNA)
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 08 / 12 · TEST 03 · Ops · ~2 min · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="color: var(--ff-orange); font-size: 1.6rem;">03</span>
<span class="section-tag gold">TEST · OPERATIONS</span>
</div>

<h2 style="font-size: 2rem; margin-top: 0.4rem;">refactor a skill <span class="ff-cyan">with a new memory lesson woven in.</span></h2>

<p style="font-size: 0.92rem; color: var(--ff-charcoal); margin-top: 0.4rem; margin-bottom: 0.5rem; font-style: italic;">prompt: read skill X + memory file Y. refactor X to include Y's lesson. preserve existing tests. ship a diff.</p>

<div class="comparison-pair mt-3">

<v-click>

<div class="model-card mythos">
<div class="model-name">Mythos 5 · output</div>
<div class="placeholder-block">
[JOHN FILLS · summary of Mythos's diff. did it preserve tests? did it weave the memory cleanly? how many turns?]
</div>
</div>

</v-click>

<v-click>

<div class="model-card opus">
<div class="model-name">Opus 4.8 · output</div>
<div class="placeholder-block">
[JOHN FILLS · Opus's diff summary. same questions.]
</div>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-4">
<span class="winner-tag">winner: [TBD]</span>
<p style="margin: 0; font-size: 0.95rem;">[JOHN FILLS · which one ran longer-horizon without breaking? which one preserved the existing test suite? winner takes ops.]</p>
</div>

</v-click>

</div>

<!--
TEST 03 VERBATIM (Scene A · ~2 min):

test three. operations. refactor an existing skill. weave in a new memory lesson. preserve tests. ship a diff.

this is where mythos's swe-bench-pro number gets pressure-tested. eighty point three percent vs opus's sixty-nine. on paper. but does that translate to my actual skills folder?

[CLICK 1 · Mythos] [READ]
[CLICK 2 · Opus] [READ]
[CLICK 3 · verdict] [READ]

PRESENTER NOTES:
- operations is the bucket where token efficiency compounds most (cron jobs, scheduled runs)
- if mythos is materially better here, weekly burn drops
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 09 / 12 · TEST 04 · META RECURSIVE · ~90s · Scene B -->

<div class="absolute inset-0 px-14 py-9 flex flex-col justify-center" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="font-size: 1.6rem;">04</span>
<span class="section-tag gold">TEST · META · RECURSIVE</span>
</div>

<h2 style="font-size: 2.2rem; margin-top: 0.4rem; line-height: 1.1;">i asked both models to design <span class="ff-cyan">this very deck.</span></h2>

<p style="font-size: 1.05rem; color: var(--ff-navy); margin-top: 0.65rem;">same prompt. same brand kit. same target runtime. zero retries. you're watching one of them right now.</p>

<div class="rule-thin"></div>

<div class="comparison-pair mt-3">

<v-click>

<div class="model-card mythos" style="min-height: 11rem;">
<div class="model-name">Mythos 5 · deck</div>
<div class="placeholder-block">
[JOHN FILLS · 2-3 lines on what Mythos's deck looked like. tone, structure, what it nailed, what it missed.]
</div>
</div>

</v-click>

<v-click>

<div class="model-card opus" style="min-height: 11rem;">
<div class="model-name">Opus 4.8 · deck</div>
<div class="placeholder-block">
[JOHN FILLS · same 2-3 lines for Opus's deck. (this one. the one you're watching.) honest read.]
</div>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-4">
<span class="winner-tag">winner: [TBD]</span>
<p style="margin: 0; font-size: 0.95rem;">[JOHN FILLS · which deck you would have actually recorded with. and one specific reason.]</p>
</div>

</v-click>

</div>

<!--
TEST 04 VERBATIM (Scene B · the killer demo · ~90s):

test four. meta test. recursive. i asked both models to design this exact deck. same prompt. same brand kit. same target runtime. zero retries.

and you're watching one of them right now.

[CLICK 1 · Mythos]
here's the deck mythos gave me. [DESCRIBE]

[CLICK 2 · Opus]
here's what opus gave me. [DESCRIBE]

[CLICK 3 · verdict]
the one i actually recorded with is [WINNER]. and the reason is [ONE SPECIFIC REASON].

PRESENTER NOTES:
- Scene B for emphasis (this is the killer-demo moment)
- the line "you're watching one of them right now" is the hook of the entire video
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 10 / 12 · VERDICT BY BUCKET · ~60s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the verdict</div>

<h2 style="font-size: 2.1rem; margin-top: 0.25rem;">by bucket. <span class="ff-cyan">which model goes default.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-3 gap-5 mt-4">

<v-click>

<div class="bucket-card acq">
<div class="bucket-name">acquisition</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">[winner TBD]</div>
<div class="bucket-examples">[JOHN FILLS · 1-line reason]</div>
</div>

</v-click>

<v-click>

<div class="bucket-card cs">
<div class="bucket-name">customer success</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">[winner TBD]</div>
<div class="bucket-examples">[JOHN FILLS · 1-line reason]</div>
</div>

</v-click>

<v-click>

<div class="bucket-card ops">
<div class="bucket-name">operations</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">[winner TBD]</div>
<div class="bucket-examples">[JOHN FILLS · 1-line reason]</div>
</div>

</v-click>

</div>

<v-click>

<div class="mt-6 px-5 py-3.5" style="background: var(--ff-navy); color: white; border-radius: 10px;">
<p style="margin: 0; font-size: 1.05rem;"><strong>the rule i'm using going forward:</strong> [JOHN FILLS · the routing rule. one sentence.] right?</p>
</div>

</v-click>

</div>

<!--
VERDICT VERBATIM (Scene A · ~60s):

so what's the call. by bucket.

[CLICK 1 · acquisition]
acquisition. winner is [X]. because [REASON].

[CLICK 2 · CS]
customer success. winner is [X]. because [REASON].

[CLICK 3 · ops]
operations. winner is [X]. because [REASON].

[CLICK 4 · navy callout]
the rule i'm using going forward. [READ ROUTING RULE]. right?

PRESENTER NOTES:
- "right?" is the John signature tag at the end. don't drop it.
- if same model wins all three, say so explicitly and explain why
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 11 / 12 · IDENTITY BEAT · ~75s · Scene A · SLOW -->

<div class="absolute inset-0 flex flex-col justify-center px-14 py-10" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="ff-eyebrow" style="color: var(--ff-orange);">the part nobody's saying out loud</div>

<v-clicks>

<h2 style="font-size: 2.5rem; line-height: 1.15; color: var(--ff-navy);">
this is not a question of <span style="text-decoration: line-through; color: rgba(30,58,95,0.45);">which model to use.</span>
</h2>

<h2 style="font-size: 2.5rem; line-height: 1.15; color: var(--ff-navy); margin-top: 0.5rem;">
it's a question of <span class="ff-cyan">which bucket compounds.</span>
</h2>

<div class="rule-thin"></div>

<p style="font-size: 1.15rem; color: var(--ff-navy); line-height: 1.5;">
just because you can use the most expensive model on every task doesn't mean you should. just because you can build the shiny new thing doesn't mean you should. the model lowers the cost. <strong>the bucket you pick decides whether you compound or you burn.</strong>
</p>

<div class="px-5 py-4 text-center" style="background: var(--ff-navy); color: white; border-radius: 10px;">
<p style="margin: 0; font-size: 1.45rem; font-weight: 700;">the model lowers the cost. <span class="ff-orange">you still pick.</span></p>
</div>

</v-clicks>

</div>

<!--
IDENTITY BEAT VERBATIM (Scene A · slow · intimate · ~75s):

[FULL BEAT · one second of silence]

now the part nobody's saying out loud.

[CLICK 1 · h2 with strike-through]
this is not a question of which model to use.

[CLICK 2 · second h2]
it's a question of which bucket compounds.

[CLICK 3 · expansion]
just because you can use the most expensive model on every task doesn't mean you should. just because you can build the shiny new thing doesn't mean you should. the model lowers the cost. the bucket you pick decides whether you compound or you burn.

[CLICK 4 · navy callout]
the model lowers the cost. you still pick.

pick well.

PRESENTER NOTES:
- DROP TEMPO. sit forward. lower voice. kill teaching energy.
- "pick well" is the 2-word close. let it sit.
- this beat is the spine of the whole channel philosophy
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 12 / 12 · RECAP + CTA · ~35s · Scene D (cam only) -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center px-14 py-10">

<div class="ff-bar"></div>

<div class="ff-eyebrow" style="color: rgba(255,255,255,0.65);">RECAP · EPISODE 02</div>

<h1 style="font-size: 3rem; color: white; line-height: 1.1;">three things <span class="ff-orange">to remember.</span></h1>

<div style="height: 1px; background: rgba(255,255,255,0.2); margin: 1.25rem 0 1.5rem;"></div>

<div class="grid grid-cols-2 gap-10">

<div>

<v-clicks>

<div style="margin-bottom: 0.9rem;">
<span class="ff-orange" style="font-family: monospace; font-weight: 700; font-size: 0.92rem;">01 ·</span>
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> two hours of testing beats two weeks of opinions. [JOHN FILLS · one specific insight from your test.]</span>
</div>

<div style="margin-bottom: 0.9rem;">
<span class="ff-orange" style="font-family: monospace; font-weight: 700; font-size: 0.92rem;">02 ·</span>
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> the routing rule by bucket: [JOHN FILLS · 1-line rule].</span>
</div>

<div>
<span class="ff-orange" style="font-family: monospace; font-weight: 700; font-size: 0.92rem;">03 ·</span>
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> just because you can doesn't mean you should. <strong style="color: white;">the model lowers the cost. you still pick.</strong></span>
</div>

</v-clicks>

</div>

<div>

<v-click>

<div class="cta-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.3); color: white;">
<div class="section-tag gold" style="margin-bottom: 0.75rem;">NEXT EPISODE</div>
<p style="font-size: 1.1rem; color: white; margin: 0; line-height: 1.4;">i'm building the operator-OS routing layer live. one prompt to claude. it picks the bucket. it picks the model. it ships the output.</p>
<p style="font-size: 0.88rem; color: rgba(255,255,255,0.55); margin-top: 0.7rem; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.1em;">subscribe so you don't miss it.</p>
</div>

</v-click>

</div>

</div>

<div class="absolute bottom-7 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
YOUTUBE · @JOHNCOBURN · 2026-06-09
</div>

</div>

<!--
RECAP VERBATIM (Scene D · cam only · 30-45s):

three things to remember.

[CLICK 1 · takeaway 01]
one. two hours of testing beats two weeks of opinions. [INSIGHT FROM YOUR TEST]

[CLICK 2 · takeaway 02]
two. the routing rule by bucket. [READ ROUTING RULE]

[CLICK 3 · takeaway 03]
three. just because you can doesn't mean you should. the model lowers the cost. you still pick.

[CLICK 4 · CTA card]
next episode i'm building the operator-OS routing layer live. one prompt to claude. it picks the bucket. it picks the model. it ships the output. subscribe so you don't miss it.

PRESENTER NOTES:
- Scene D · cam only · eye contact
- "you still pick" lands the philosophy one more time
- hold 2 full seconds before stopping recording
-->
