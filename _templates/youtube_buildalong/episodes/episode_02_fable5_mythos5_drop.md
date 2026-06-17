---
theme: default
title: Episode 02 · i spent 4 hours testing fable 5. (the deck fable built.)
info: |
  Joburn Build-Along · Episode 02 · 2026-06-10 · FABLE v2
  Personal-test workshop on Anthropic's Fable 5 / Mythos 5 drop.
  Frame: 2 real experiments run · head-to-head Fable 5 vs Opus 4.8 · 3-bucket routing verdict.
  Recursive meta-test: Opus 4.8 built deck v1 (preserved at joburn-buildalong-ep02-opus-v1.vercel.app).
  Fable 5 built this v2. Both shown side by side on camera in test 04.
  Format: 16-slide YouTube build-along, atomic-era retro-futurist.
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

<!-- SLIDE 01 / 16 · COVER · 8-12s · Scene A · FRAME -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow" style="color: var(--ff-orange);">Joburn · Build-Along · EP 02 · 2026-06-10</div>

<h1 style="font-size: 4.4rem; color: white; line-height: 1.04; margin-bottom: 1.5rem;">
i spent 4 hours testing<br/>
<span class="ff-orange">fable 5.</span>
</h1>

<v-click>

<p style="font-size: 1.5rem; color: rgba(255,255,255,0.88); max-width: 50rem; margin: 0 auto; line-height: 1.4;">
the new best model in the world. two head-to-head experiments against opus 4.8.
</p>

</v-click>

<v-click>

<p style="font-size: 1.7rem; color: rgba(255,255,255,0.95); max-width: 50rem; margin: 0.9rem auto 0; line-height: 1.3;">
<strong style="color: var(--ff-orange);">it lost one of them.</strong>
</p>

</v-click>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.45); font-size: 0.72rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOHN COBURN · JOBURN.COM
</div>

</div>

<!--
COVER VERBATIM (Scene A · 8-12s):

anthropic shipped the best model in the world on monday. i spent four hours testing it against the old one.

[CLICK · reveal sub]

and the new one lost. sort of. let me show you.

PRESENTER NOTES:
- cold open. no logo bumper, no "what's up." straight in.
- "mythos-class" is the curiosity hook. nobody else will lead with the class distinction.
- hold final beat 1 second before clicking forward.
TIMING: 8-12s
TRANSITION: "but first. full disclosure."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 02 / 16 · THE TWIST · ~20s · Scene B · FRAME · open loop -->

<div class="absolute inset-0 px-14 py-10 flex flex-col justify-center" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="ff-eyebrow" style="color: var(--ff-orange);">full disclosure</div>

<h2 style="font-size: 2.7rem; line-height: 1.12; max-width: 52rem;">
the model under review <span class="ff-cyan">built this deck.</span>
</h2>

<div class="rule-thin"></div>

<v-click>

<div class="comparison-pair mt-4">

<div class="model-card opus" style="min-height: 8rem; padding: 1.1rem 1.25rem;">
<div class="model-name">Opus 4.8</div>
<p style="margin: 0; font-size: 1rem; line-height: 1.45;">built version one of this deck. it's live. link below the video.</p>
</div>

<div class="model-card fable" style="min-height: 8rem; padding: 1.1rem 1.25rem;">
<div class="model-name">Fable 5</div>
<p style="margin: 0; font-size: 1rem; line-height: 1.45;">built the one you're watching. same brand kit. same job.</p>
</div>

</div>

</v-click>

<v-click>

<div class="mt-5 px-5 py-3.5" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 1.08rem; line-height: 1.4;">before the end, i'll put them side by side and you judge. that's not a gimmick. <strong>that's the most honest test i can run.</strong> the model doing real work. on camera.</p>
</div>

</v-click>

</div>

<!--
TWIST VERBATIM (Scene B · ~20s):

but first. full disclosure. the model under review built this deck.

[CLICK 1 · the two cards]
i asked opus four eight to build version one. then i gave fable five the exact same job. same brand kit. same script. the deck you're watching right now is fable's.

[CLICK 2 · navy callout]
before the end of this video i'll put both versions side by side and you can judge for yourself. that's not a gimmick. that's the most honest test i can run. the model doing real work. on camera. right?

PRESENTER NOTES:
- this is the differentiator hook. nobody else can run this play on launch week.
- it opens a loop that test 04 closes (Fitzpatrick cliffhanger principle).
- "right?" tag at the end. keep it.
TIMING: ~20s
TRANSITION: "now. why should you care."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 03 / 16 · STAKES · ~25s · Scene B · FRAME · identity-level -->

<div class="absolute inset-0 px-14 py-10 flex flex-col justify-center" style="background: var(--ff-cream);">

<div class="ff-bar"></div>

<div class="ff-eyebrow">before i show you anything</div>

<h2 style="font-size: 2.5rem; line-height: 1.15; max-width: 50rem;">
this is not a model review. it's a <span class="ff-cyan">labor-cost reality check.</span>
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
<p style="margin: 0; font-size: 0.98rem; line-height: 1.45;">your defaults drift. and competitors with sharper defaults <strong style="color: #94463b;">out-position you on cost per outcome.</strong> quietly. for months.</p>
</div>

</v-click>

</div>

<v-click>

<div class="mt-6 px-5 py-3.5" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 1.05rem; line-height: 1.4;">the version of you who knows which model fits where <span class="ff-orange">beats the version that defaults to the newest.</span> by a lot. by next monday.</p>
</div>

</v-click>

</div>

<!--
STAKES VERBATIM (Scene B · slow · ~25s):

one frame before we start.

this is not a model review. it's a labor-cost reality check.

[CLICK 1 · "if you test it"]
if you test this thing for a few hours, you walk away knowing which model to default to per bucket. you stop paying opus dollars on tasks fable handles cheaper. your cost per outcome drops.

[CLICK 2 · "if you don't"]
if you don't. your defaults drift. and competitors with sharper defaults out-position you on cost per outcome. quietly. for months.

[CLICK 3 · navy callout]
the version of you who knows which model fits where beats the version that defaults to the newest. by a lot. by next monday.

PRESENTER NOTES:
- Scene B (large cam, intimate)
- "by next monday" is the punch. let it sit.
TIMING: ~25s
TRANSITION: "quick. who's testing."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 04 / 16 · WHO'S TESTING · ~30s · Scene B -->

<div class="absolute inset-0 px-14 py-10 flex flex-col justify-center" style="background: var(--ff-warm);">

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
i build with claude every day across three buckets. <strong class="ff-cyan">acquisition. customer success. operations.</strong> so this test isn't "does it win benchmarks." it's <strong>"does it replace work i'm already paying opus to do."</strong>
</p>
</div>

</v-click>

</div>

<!--
WHO VERBATIM (Scene B · ~30s):

quick. who's testing.

i'm john coburn. i build operator-OS for founders. claude runs in my stack every single day.

not an anthropic employee. not a benchmark site. not a hype creator.

[CLICK · hero card]
i build with claude every day across three buckets. acquisition. customer success. operations. so this test isn't "does it win benchmarks." it's "does it actually replace work i'm already paying opus to do."

PRESENTER NOTES:
- 3 not-cards lower defenses (BSMD pattern)
- hero card lands the operator frame
TIMING: ~30s
TRANSITION: "so here's what actually dropped."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 05 / 16 · WHAT DROPPED · ~60s · Scene A · MOVE FAST -->

<div class="absolute inset-0 ff-navy-bg flex">

<div class="ff-bar"></div>

<div class="w-1/2 flex items-center justify-center p-10">

<img src="../assets/ep02/hero_butterfly5.png" alt="Anthropic Fable 5 and Mythos 5" style="max-width: 100%; max-height: 64vh; object-fit: contain; border-radius: 8px; filter: drop-shadow(0 12px 40px rgba(0,0,0,0.45));" />

</div>

<div class="w-1/2 flex flex-col justify-center p-10 pr-14">

<div class="ff-eyebrow" style="color: var(--ff-orange);">what dropped · june 9</div>

<h2 style="font-size: 2.4rem; color: white; line-height: 1.08; margin-bottom: 0.5rem;">two models. <span class="ff-orange">one of them is yours.</span></h2>

<div style="height: 1px; background: rgba(255,255,255,0.2); margin: 1rem 0 1.25rem; width: 80px;"></div>

<v-clicks>

<p style="color: rgba(255,255,255,0.92); font-size: 1.05rem; margin-bottom: 0.8rem;"><strong style="color: var(--ff-orange);">fable 5</strong> · mythos-class, made safe for general use. ships to everyone. api, pro, max, team.</p>

<p style="color: rgba(255,255,255,0.92); font-size: 1.05rem; margin-bottom: 0.8rem;"><strong style="color: var(--ff-cyan);">mythos 5</strong> · same model. cyber safeguards lifted. locked to project glasswing. you and i don't get it.</p>

<p style="color: rgba(255,255,255,0.92); font-size: 1.05rem; margin-bottom: 0.8rem;"><strong>$10 in / $50 out</strong> per million tokens. less than half what mythos preview cost.</p>

<p style="color: rgba(255,255,255,0.65); font-size: 0.95rem; font-style: italic;">free on pro and max through june 22. credits start june 23. the clock is real.</p>

</v-clicks>

</div>

</div>

<!--
WHAT DROPPED VERBATIM (Scene A · ~60s):

here's what shipped yesterday. two models. one underlying system.

[CLICK 1 · fable]
fable 5. it's a mythos-class model that anthropic made safe enough for general release. ships to everyone. api, pro, max, team plans.

[CLICK 2 · mythos]
mythos 5 is the same model with the cybersecurity safeguards lifted. it's locked inside project glasswing. government cyberdefenders only. you and i don't get it. so when people say "i tested mythos" this week, they tested fable. small detail. matters.

[CLICK 3 · pricing]
price went down. ten bucks in, fifty out per million tokens. less than half what mythos preview cost a few weeks ago.

[CLICK 4 · window]
and it's free on pro and max plans through june twenty-two. credits start the twenty-third. so the testing window is right now.

PRESENTER NOTES:
- the mythos correction doubles as authority. you read the announcement properly. most didn't.
- "the clock is real" sets urgency without hype.
TIMING: ~60s
TRANSITION: "and before you say benchmarks don't matter. one chart."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 06 / 16 · RECEIPTS · ~75s · Scene A · ZOOM tempo -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the receipts</div>

<h2 style="font-size: 2rem; margin-top: 0.25rem;">one chart. <span class="ff-cyan">read it like an operator.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-12 gap-5 mt-3">

<div class="col-span-7">
<img src="../assets/ep02/knowledge_work_graph.png" alt="Agentic coding: SWE-Bench Pro and FrontierCode, Fable vs Opus 4.8 vs GPT-5.5" style="width: 100%; border: 1px solid var(--ff-rule); border-radius: 8px; background: white;" />
<div class="fig-caption mt-2">FIG. 1 · AGENTIC CODING · FABLE VS OPUS 4.8 VS GPT-5.5 · SOURCE: ANTHROPIC</div>
</div>

<div class="col-span-5" style="display: flex; flex-direction: column; gap: 0.7rem;">

<v-clicks>

<div class="ff-card" style="padding: 0.9rem 1.1rem;">
<div class="model-name" style="color: var(--ff-cyan); font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; letter-spacing: 0.2em; font-weight: 700;">SWE-BENCH PRO</div>
<p style="margin: 0.35rem 0 0; font-size: 0.95rem;"><strong style="font-size: 1.3rem; color: var(--ff-navy);">80.3%</strong> vs opus 69.2 vs gpt 58.6. <span class="ff-cyan">eleven points clear of anthropic's own best.</span></p>
</div>

<div class="ff-card" style="padding: 0.9rem 1.1rem;">
<div class="model-name" style="color: var(--ff-orange); font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; letter-spacing: 0.2em; font-weight: 700;">FRONTIERCODE · THE HARD ONE</div>
<p style="margin: 0.35rem 0 0; font-size: 0.95rem;"><strong style="font-size: 1.3rem; color: var(--ff-navy);">29.3%</strong> vs opus 13.4 vs gpt 5.7. <span class="ff-orange">2x opus. 5x gpt.</span></p>
</div>

<div class="px-4 py-3" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 0.95rem; line-height: 1.45;">the harder the task, <strong>the wider the gap gets.</strong> stripe ran a 50-million-line migration in one day. their team had it scoped at two months.</p>
</div>

</v-clicks>

</div>

</div>

</div>

<!--
RECEIPTS VERBATIM (Scene A · ZOOM tempo · ~75s):

before you say benchmarks don't matter. one chart. and i want you to read it like an operator, not a researcher.

[CLICK 1 · swe-bench card]
swe-bench pro. real software engineering tasks. fable: eighty point three percent. opus was sixty-nine. gpt five five was fifty-eight. that's eleven points clear of anthropic's own previous best. in one release.

[CLICK 2 · frontiercode card]
now the hard one. frontiercode. production-grade tasks at the frontier. fable: twenty-nine point three. opus: thirteen point four. gpt: five point seven. that's two x opus and five x gpt on the hardest tier.

[CLICK 3 · navy card]
and here's the operator read. the harder the task, the wider the gap gets. that's backwards from every model release before this one. stripe ran a fifty-million-line migration in one day. their own team had it scoped at two months. that's the number under the hood.

PRESENTER NOTES:
- "read it like an operator" is the framing. you're not reciting benchmarks, you're pricing labor.
- "under the hood" = voice DNA.
- say "roughly" if you quote compression multiples. never "literally."
TIMING: ~75s
TRANSITION: "okay. so how do we test it for real. quick map first."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 07 / 16 · THE FRAME · 3 BUCKETS · ~45s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-8">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the frame</div>

<h2 style="font-size: 2.2rem; margin-top: 0.25rem;">three buckets. <span class="ff-cyan">every operator task lives in one.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-3 gap-5 mt-5">

<v-clicks>

<div class="bucket-card acq">
<div class="ff-numeral" style="color: #94463b;">01</div>
<div class="bucket-name">acquisition</div>
<div class="bucket-headline">getting attention</div>
<div class="bucket-examples">ads · hooks · funnels · landing pages · copy · creative</div>
</div>

<div class="bucket-card cs">
<div class="ff-numeral" style="color: var(--ff-cyan);">02</div>
<div class="bucket-name">customer success</div>
<div class="bucket-headline">keeping it working</div>
<div class="bucket-examples">reports · audits · strategy calls · retention · weekly cadence</div>
</div>

<div class="bucket-card ops">
<div class="ff-numeral" style="color: var(--ff-orange);">03</div>
<div class="bucket-name">operations</div>
<div class="bucket-headline">making it scale</div>
<div class="bucket-examples">skills · SOPs · refactors · data pipes · internals</div>
</div>

</v-clicks>

</div>

<v-click>

<div class="mt-6 px-5 py-3" style="background: var(--ff-warm); border-left: 4px solid var(--ff-orange); border-radius: 6px;">
<p style="margin: 0; font-size: 1.05rem; color: var(--ff-navy);"><strong>just because you can</strong> use the new model on every task <strong class="ff-cyan">doesn't mean you should.</strong> route by bucket. not by hype.</p>
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
and here's my whole philosophy in one line. just because you can use the new model on every task doesn't mean you should. route by bucket. not by hype.

PRESENTER NOTES:
- this is the channel's spine frame. it returns in the whiteboard and the verdict.
TIMING: ~45s
TRANSITION: "so here's the test plan."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 08 · WHAT I ACTUALLY RAN · ~40s · Scene A · MOVE FAST -->

<div class="grid-paper absolute inset-0 px-12 py-8">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the experiments</div>

<h2 style="font-size: 2.1rem; margin-top: 0.25rem;">two head-to-heads. <span class="ff-cyan">same prompt. same context. zero retries.</span></h2>

<div class="rule-thin"></div>

<div class="mt-5" style="display: flex; flex-direction: column; gap: 0.8rem;">

<v-clicks>

<div class="ff-card" style="padding: 1rem 1.2rem; display: flex; align-items: center; gap: 1rem;">
<span class="ff-numeral" style="color: var(--ff-cyan); font-size: 1.4rem;">01</span>
<span class="bucket-name" style="color: var(--ff-cyan); font-size: 0.7rem; min-width: 9rem;">THE REPORT TEST</span>
<span style="font-size: 1.02rem; flex: 1;">a full end-of-week client report from the live database. identical prompt, pasted into both models at the same moment.</span>
</div>

<div class="ff-card" style="padding: 1rem 1.2rem; display: flex; align-items: center; gap: 1rem; background: var(--ff-warm);">
<span class="ff-numeral" style="font-size: 1.4rem;">02</span>
<span class="bucket-name" style="font-size: 0.7rem; min-width: 9rem;">THE DECK TEST</span>
<span style="font-size: 1.02rem; flex: 1;"><strong>both models build this youtube deck.</strong> same brand kit. same script. you're watching the result.</span>
</div>

</v-clicks>

</div>

<v-click>

<div class="mt-6 px-5 py-3" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 1.02rem;">settings: both on edit-automatically. fable at ultra-high effort plus workflows. opus at default. i tallied <strong class="ff-orange">time, permission asks, and quality.</strong></p>
</div>

</v-click>

</div>

<!--
WHAT I RAN VERBATIM (Scene A · ~40s):

so here's what i actually ran. two head-to-head experiments. same prompt. same context. pasted into both models at the same moment. zero retries.

[CLICK 01]
one. the report test. a full end-of-week client report from our live database. real client data. real numbers. the exact work my agency ships every week.

[CLICK 02]
two. the deck test. both models build this youtube deck. same brand kit. same script. you are literally watching the result right now.

[CLICK 3 · settings callout]
settings. both on edit-automatically. fable at ultra-high effort plus workflows. opus at default. and i tallied three things. time. how many times each one asked me for permission. and the quality of the final thing.

PRESENTER NOTES:
- "you are literally watching the result" re-opens the slide-2 loop.
TIMING: ~40s
TRANSITION: "experiment one. the report."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 09 · EXPERIMENT 01 RESULTS · THE REPORT TEST · ~2min · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="color: var(--ff-cyan); font-size: 1.6rem;">01</span>
<span class="section-tag">EXPERIMENT · THE REPORT TEST</span>
</div>

<h2 style="font-size: 2rem; margin-top: 0.4rem;">what actually happened.</h2>

<div class="comparison-pair mt-4">

<v-click>

<div class="model-card fable">
<div class="model-name">Fable 5</div>
<p style="margin: 0.4rem 0 0; font-size: 0.95rem; line-height: 1.55;"><strong>50 minutes.</strong> asked me for something every two minutes. pulled organic, crm, even news. spun up subagents and side quests. turned over stones i had forgotten about. <strong>7 pages. accurate.</strong></p>
</div>

</v-click>

<v-click>

<div class="model-card opus">
<div class="model-name">Opus 4.8</div>
<p style="margin: 0.4rem 0 0; font-size: 0.95rem; line-height: 1.55;"><strong>30 minutes.</strong> way fewer questions. leaner path to the same destination. <strong>7 pages. accurate.</strong> finished while fable was still researching.</p>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-5">
<span class="winner-tag">winner: opus 4.8</span>
<p style="margin: 0; font-size: 0.95rem;">fable's extra 25 minutes bought context nobody reads. for spec'd, repeatable work, the cheaper executor wins. a blind ai judge agreed.</p>
</div>

</v-click>

</div>

<!--
EXPERIMENT 01 VERBATIM (Scene A · ~2 min):

experiment one. the report test.

[CLICK 1 · fable card]
fable took fifty minutes. it asked me for something every two minutes. it pulled organic data, crm data, it even went and researched news. it spun up subagents. it turned over stones i had forgotten about. seven pages. accurate.

[CLICK 2 · opus card]
opus took thirty minutes. way fewer questions. leaner path to the same destination. seven pages. accurate. it finished while fable was still researching.

[CLICK 3 · verdict]
winner: opus four point eight. and here's the lesson. fable's extra twenty-five minutes bought context that nobody reads. for spec'd, repeatable work, the cheaper executor wins. i even ran both reports through a blind ai judge. it agreed.

PRESENTER NOTES:
- "context nobody reads" is the quotable line. let it sit.
- honest beat: the newest model LOSING is the most credible moment in this video.
TIMING: ~2 min
TRANSITION: "experiment two. the one i promised you at the start."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 12 / 16 · TEST 04 · THE DECK TEST · ~2min · Scene B · closes the loop -->

<div class="absolute inset-0 px-14 py-8 flex flex-col justify-center" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="flex items-center gap-3 mb-2">
<span class="ff-numeral" style="font-size: 1.6rem;">02</span>
<span class="section-tag gold">EXPERIMENT · THE DECK TEST</span>
</div>

<h2 style="font-size: 2.2rem; margin-top: 0.4rem; line-height: 1.1;">same job. same brand kit. <span class="ff-cyan">two decks.</span></h2>

<div class="rule-thin"></div>

<div class="comparison-pair mt-3">

<v-click>

<div class="model-card opus" style="min-height: 12rem;">
<div class="model-name">Opus 4.8 · deck v1</div>
<p style="margin: 0.4rem 0 0; font-size: 0.92rem; line-height: 1.5;">locked the angle and the identity beat. but it shipped <strong>three visual bugs</strong> that QC had to catch, dropped the whiteboard segment from the format, and called the model under test "mythos." <strong style="color: var(--ff-cyan);">the one you can't even access.</strong></p>
</div>

</v-click>

<v-click>

<div class="model-card fable" style="min-height: 12rem;">
<div class="model-name">Fable 5 · deck v2 · this one</div>
<p style="margin: 0.4rem 0 0; font-size: 0.92rem; line-height: 1.5;">caught the naming error and fixed the claim. restored the whiteboard and the benchmark receipts. <strong style="color: var(--ff-orange);">and filled in this exact slide you're reading.</strong> my honest read: more context, real fact-checks, added the chart. better. but not night-and-day better.</p>
</div>

</v-click>

</div>

<v-click>

<div class="verdict-strip mt-4">
<span class="winner-tag">john judges</span>
<p style="margin: 0; font-size: 0.95rem;">both decks are live, linked below the video. i recorded with fable's. it caught a factual error opus shipped. that one catch is the difference.</p>
</div>

</v-click>

</div>

<!--
TEST 04 VERBATIM (Scene B · the loop-closer · ~2 min):

experiment two. the one i promised you at the start.

same job. same brand kit. same script. two decks.

[CLICK 1 · opus card]
opus built version one. structurally solid. it locked the angle and the identity beat. but it shipped three visual bugs that quality control had to catch. it dropped the whiteboard segment from my own format. and it titled the whole video around testing mythos. the model you literally cannot access.

[CLICK 2 · fable card]
fable built version two. the one you're watching. it caught the naming error. it restored the whiteboard and the benchmark receipts. and it wrote this exact slide. the one you're reading right now. [ADD YOUR HONEST READ]

[CLICK 3 · verdict]
both decks are live. links below the video. you judge. my call: i recorded with fable's, because it caught a factual error opus shipped. that one catch is the difference.

PRESENTER NOTES:
- this closes the loop opened on slide 2. biggest payoff moment in the video.
- be honest if you find flaws in v2. honesty IS the persuasion.
TIMING: ~2 min
TRANSITION: "okay. whiteboard. let's route this."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE · THE SETTINGS THAT MATTER · ~60s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-8">

<div class="ff-bar"></div>

<div class="ff-eyebrow">so you don't have to</div>

<h2 style="font-size: 2.1rem; margin-top: 0.25rem;">the settings that matter. <span class="ff-cyan">learned the long way.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-2 gap-5 mt-5">

<v-clicks>

<div class="ff-card" style="padding: 1.1rem 1.25rem;">
<div class="bucket-name" style="color: var(--ff-cyan); font-size: 0.68rem;">EDIT AUTOMATICALLY</div>
<p style="margin: 0.45rem 0 0; font-size: 0.95rem; line-height: 1.5;">it still asks before running commands. that's a feature, not friction. <strong>you see every move it wants to make.</strong></p>
</div>

<div class="ff-card" style="padding: 1.1rem 1.25rem;">
<div class="bucket-name" style="color: var(--ff-orange); font-size: 0.68rem;">EFFORT LEVELS</div>
<p style="margin: 0.45rem 0 0; font-size: 0.95rem; line-height: 1.5;">ultra-high plus workflows = thorough but slow. <strong>use it to plan.</strong> drop the effort, or switch models, to execute.</p>
</div>

<div class="ff-card" style="padding: 1.1rem 1.25rem;">
<div class="bucket-name" style="color: var(--ff-cyan); font-size: 0.68rem;">THE FALLBACK</div>
<p style="margin: 0.45rem 0 0; font-size: 0.95rem; line-height: 1.5;">roughly 5% of sessions quietly route to opus 4.8 on sensitive topics. <strong>you get told when it happens.</strong> log it.</p>
</div>

<div class="ff-card" style="padding: 1.1rem 1.25rem; background: var(--ff-warm);">
<div class="bucket-name" style="color: var(--ff-orange); font-size: 0.68rem;">THE WINDOW</div>
<p style="margin: 0.45rem 0 0; font-size: 0.95rem; line-height: 1.5;"><strong>free on pro and max until june 22.</strong> credits after. run your own tests this week, not next month.</p>
</div>

</v-clicks>

</div>

</div>

<!--
SETTINGS VERBATIM (Scene A · ~60s):

quick. the settings that matter. learned the long way so you don't have to.

[CLICK 1] edit automatically. it still asks before running commands. that's a feature, not friction. you see every move it wants to make before it makes it.

[CLICK 2] effort levels. ultra-high plus workflows is thorough but slow. that's the fifty-minute report. use max effort to plan. drop the effort, or switch models, to execute.

[CLICK 3] the fallback. roughly five percent of sessions quietly route to opus on sensitive topics. you get told when it happens. log it, or you'll blame your own prompting.

[CLICK 4] and the window. it's free on pro and max plans until june twenty-two. credits after that. so run your own tests this week. not next month.

PRESENTER NOTES:
- this is the "what settings to use" payoff from the hook.
TIMING: ~60s
TRANSITION: "okay. whiteboard. let's route this."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 13 / 16 · WHITEBOARD · DRAW THE ROUTING LAYER · 2-3min · drauu · STOP tempo -->

<div class="absolute inset-0 px-16 py-10" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="section-tag gold">FIG. 2 · THE ROUTING LAYER</div>

<h2 style="font-size: 2.4rem; margin-top: 0.85rem;">draw it. <span class="ff-cyan">task → bucket → model.</span></h2>

<div class="rule-thin"></div>

<div class="whiteboard-scene mt-5" style="min-height: 380px; border-style: solid; border-color: rgba(46,139,139,0.18); background: var(--ff-cream);">
<span style="opacity: 0.25; font-size: 0.7rem;">FIG. 2</span>
</div>

</div>

<!--
WHITEBOARD VERBATIM (drauu pen on this slide · 2-3 min · STOP tempo):

alright. whiteboard. let's route this.

three boxes. acquisition. customer success. operations.

[DRAW the three boxes as you name them]

now under each box i'm writing the winner from the tests. acquisition: [MODEL]. customer success: [MODEL]. operations: [MODEL].

[WRITE each winner]

and here's how work actually flows now. a task comes in. first question is not "which model." first question is "which bucket." the bucket picks the model. not the launch-day hype.

[DRAW arrows: task → bucket → model]

and i'm writing the rule under all of it.

route by bucket. not by hype.

[HAND-PRINT the rule. hold the board 2 seconds.]

that's the whole operating system in one drawing.

PRESENTER NOTES:
- drawing IS the pacing. don't speed-run.
- this is the STOP beat that resets attention before the verdict.
- the drawing persists (drawings.persist = true) so you can rehearse once and keep it.
TIMING: 2-3 min
TRANSITION: "so. the verdict."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 14 / 16 · VERDICT BY BUCKET · ~60s · Scene A -->

<div class="grid-paper absolute inset-0 px-12 py-7">

<div class="ff-bar"></div>

<div class="ff-eyebrow">the verdict</div>

<h2 style="font-size: 2.1rem; margin-top: 0.25rem;">by bucket. <span class="ff-cyan">which model goes default.</span></h2>

<div class="rule-thin"></div>

<div class="grid grid-cols-3 gap-5 mt-4">

<v-clicks>

<div class="bucket-card acq">
<div class="bucket-name">acquisition</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">opus, for now</div>
<div class="bucket-examples">untested head-to-head. cheaper default until fable earns it.</div>
</div>

<div class="bucket-card cs">
<div class="bucket-name">customer success</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">opus 4.8</div>
<div class="bucket-examples">tested. 30 vs 50 min, equal accuracy, fewer decisions.</div>
</div>

<div class="bucket-card ops">
<div class="bucket-name">operations</div>
<div class="bucket-headline" style="margin-top: 0.4rem;">split the layer</div>
<div class="bucket-examples">fable plans + architects. opus executes the spec.</div>
</div>

</v-clicks>

</div>

<v-click>

<div class="mt-6 px-5 py-3.5" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 1.05rem;"><strong>the rule going forward:</strong> fable architects. opus executes. route by bucket, not by hype. right?</p>
</div>

</v-click>

</div>

<!--
VERDICT VERBATIM (Scene A · ~60s):

so. the verdict. by bucket.

[CLICK 1] acquisition. opus, for now. i have not run that head-to-head yet, so the cheaper model stays the default until fable earns it.
[CLICK 2] customer success. opus four eight. that one i did test. thirty minutes versus fifty, same accuracy, fewer decisions. opus wins it.
[CLICK 3] operations. split the layer. fable plans and architects, opus executes the spec.

[CLICK 4 · navy callout]
and the rule going forward: [READ THE ROUTING RULE]. right?

PRESENTER NOTES:
- if one model sweeps all three buckets, SAY SO explicitly and explain why that's still a routing decision, not a default-to-newest decision.
- "right?" tag stays.
TIMING: ~60s
TRANSITION: "one more thing. and it's the part nobody's saying out loud."
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 15 / 16 · IDENTITY BEAT · ~75s · Scene A · SLOW · LAND -->

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
just because you can use the strongest model on every task doesn't mean you should. just because you can build the shiny new thing doesn't mean you should. the model lowers the cost. <strong>the bucket you pick decides whether you compound or you burn.</strong>
</p>

<div class="px-5 py-4 text-center" style="background: var(--ff-navy); border-radius: 10px;">
<p style="margin: 0; font-size: 1.45rem; font-weight: 700;">the model lowers the cost. <span class="ff-orange">you still pick.</span></p>
</div>

</v-clicks>

</div>

<!--
IDENTITY BEAT VERBATIM (Scene A · slow · intimate · ~75s):

[FULL BEAT · one second of silence]

one more thing. and it's the part nobody's saying out loud.

[CLICK 1 · strike-through line]
this is not a question of which model to use.

[CLICK 2 · second line]
it's a question of which bucket compounds.

[CLICK 3 · expansion]
just because you can use the strongest model on every task doesn't mean you should. just because you can build the shiny new thing doesn't mean you should. the model lowers the cost. the bucket you pick decides whether you compound or you burn.

[CLICK 4 · navy callout]
the model lowers the cost. you still pick.

pick well.

PRESENTER NOTES:
- DROP TEMPO. sit forward. lower voice. kill the teaching energy.
- "pick well" is the two-word close. let it sit before cutting to recap.
- this beat is the spine of the whole channel philosophy.
TIMING: ~75s
TRANSITION: cut to Scene D. recap.
-->

---
layout: default
class: !p-0
---

<!-- SLIDE 16 / 16 · RECAP + CTA · ~35s · Scene D (cam only) · LAND -->

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
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> four hours of testing beats two weeks of opinions. and the window is free until june 22. opus won the report. fable won the deck.</span>
</div>

<div style="margin-bottom: 0.9rem;">
<span class="ff-orange" style="font-family: monospace; font-weight: 700; font-size: 0.92rem;">02 ·</span>
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> route by bucket. not by hype. fable architects. opus executes.</span>
</div>

<div>
<span class="ff-orange" style="font-family: monospace; font-weight: 700; font-size: 0.92rem;">03 ·</span>
<span style="color: rgba(255,255,255,0.92); font-size: 1.02rem; line-height: 1.4;"> just because you can doesn't mean you should. <strong style="color: white;">the model lowers the cost. you still pick.</strong></span>
</div>

</v-clicks>

</div>

<div>

<v-click>

<div class="cta-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.3);">
<div class="section-tag gold" style="margin-bottom: 0.75rem;">NEXT EPISODE</div>
<p style="font-size: 1.1rem; color: white; margin: 0; line-height: 1.4;">i build the operator-OS routing layer live. one prompt in. it picks the bucket. it picks the model. it ships the output.</p>
<p style="font-size: 0.88rem; color: rgba(255,255,255,0.55); margin-top: 0.7rem; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.1em;">subscribe so you don't miss it.</p>
</div>

</v-click>

</div>

</div>

<div class="absolute bottom-7 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
YOUTUBE · @JOHNCOBURN · BOTH DECKS LINKED BELOW · 2026-06-10
</div>

</div>

<!--
RECAP VERBATIM (Scene D · cam only · eye contact · ~35s):

three things to remember.

[CLICK 1] one. four hours of testing beats two weeks of opinions. and the window is free until june twenty-two. [YOUR INSIGHT]

[CLICK 2] two. route by bucket. not by hype. [YOUR ROUTING RULE]

[CLICK 3] three. just because you can doesn't mean you should. the model lowers the cost. you still pick.

[CLICK 4 · CTA card]
next episode i build the operator-OS routing layer live. one prompt in. it picks the bucket. it picks the model. it ships the output. subscribe so you don't miss it.

and both versions of this deck are linked below. go judge the machines yourself.

PRESENTER NOTES:
- Scene D · cam only · sign-off intimacy.
- "go judge the machines yourself" is the final CTA driver to the description links. it converts curiosity into a click.
- hold 2 full seconds before stopping recording.
TIMING: ~35s
-->
