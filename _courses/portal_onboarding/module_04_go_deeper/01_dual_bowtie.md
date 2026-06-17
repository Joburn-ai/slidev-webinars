---
theme: default
title: The Dual Bowtie — Lesson 4.1
info: |
  Portal Onboarding · Go Deeper · Lesson 4.1
  The Dual Bowtie. Customer acquisition + talent acquisition are the same
  shape. Foundation for Unit Economics (4.2) and the Leverage Zoom (4.3).
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: true
transition: slide-left
mdc: true
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow">Go Deeper · Lesson 4.1</div>

<h1 style="font-size: 4rem; color: white;">
The Dual <span class="ff-cyan">Bowtie</span>
</h1>

<p style="font-size: 1.3rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 46rem; margin-left:auto; margin-right:auto;">
Customer acquisition and talent acquisition are the same shape. Once you see it, you can&apos;t unsee it.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST
</div>

</div>

<!--
COLD OPEN. Name the lesson, name the thesis. 10s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Asked at a dinner</div>

<h1 style="font-size: 3.6rem; line-height: 1.15; max-width: 56rem; text-align:center;">
&ldquo;What does your business <em>actually look like</em>?&rdquo;
</h1>

<p v-click style="font-size: 1.4rem; margin-top: 3rem; max-width: 52rem; text-align:center; color:#475569; font-style:italic;">
Most operators answer with tactics. We run ads, we have a funnel, we have a coach who closes. They&apos;ve described the moving parts. They haven&apos;t described the <strong>shape</strong>.
</p>

</div>

<!--
TENSION. The dinner-party question is universal; the answer they reach for
proves the point. They name tactics. The shape stays invisible. 15s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">The diagnosis</div>

<h1 style="font-size: 3.2rem; line-height: 1.2; max-width: 54rem; text-align:center;">
Every business has the <span v-mark.underline.cyan="1">same shape</span>.
</h1>

<h2 v-click="2" style="font-size: 2rem; margin-top: 2rem; color:#475569;">
You just haven&apos;t drawn it yet.
</h2>

<p v-click="3" style="font-size: 1.25rem; margin-top: 2.5rem; max-width: 42rem; text-align:center; font-weight:500;">
And once you do, the leak in your business stops being mysterious.
</p>

</div>

<!--
AHA #1 (declarative). The cognitive flip: there's a SHAPE. Universal.
Click 1: underline "same shape". Click 2: kicker. Click 3: payoff tease.
15s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Know this</div>

<h2 style="font-size: 2.4rem; margin-bottom: 2.5rem;">The Bowtie.</h2>

<div class="flex items-center justify-center gap-2" style="height: 220px;">

<div v-motion :initial="{ x: -160, opacity: 0 }" :enter="{ x: 0, opacity: 1, transition: { delay: 200, duration: 500 } }" class="flex flex-col items-center">
<div class="bowtie-half bowtie-left"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#0891b2; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Acquisition</div>
<div style="font-size:0.8rem; color:#64748b;">cold → opt-in → first sale</div>
</div>

<div v-motion :initial="{ scale: 0, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { delay: 700, duration: 400 } }" class="flex flex-col items-center" style="margin: 0 -10px; z-index: 5;">
<div class="bowtie-pinch"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#ea580c; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Trust</div>
<div style="font-size:0.8rem; color:#64748b;">the pinch</div>
</div>

<div v-motion :initial="{ x: 160, opacity: 0 }" :enter="{ x: 0, opacity: 1, transition: { delay: 1000, duration: 500 } }" class="flex flex-col items-center">
<div class="bowtie-half bowtie-right"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#059669; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Expansion</div>
<div style="font-size:0.8rem; color:#64748b;">repeat → advocate → upsell</div>
</div>

</div>

<p v-click style="font-size: 1.3rem; margin-top: 2.5rem; max-width: 50rem; text-align:center; font-weight:500;">
Left side fills the room. Right side is where the money compounds. The <span class="ff-orange" style="font-weight:800;">pinch</span> is where trust is won or lost.
</p>

<p v-click style="font-size: 0.85rem; margin-top: 1rem; color:#94a3b8; font-style:italic;">
Originated by Jacco van der Kooij / Winning by Design. Our contribution is the dual adaptation, next.
</p>

</div>

<!--
DECLARATIVE — the bowtie reveal. v-motion: left half slides in from left,
pinch pops up in middle, right half slides in from right (sequence delays
in transitions). Then the caption clicks in. Attribution second click.
AHA #2: a named shape, not abstract. 30s.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">The part most operators miss</div>

<h2 style="font-size: 2.8rem; color: white; line-height:1.2;">
Everyone obsesses over the <span v-mark.underline.cyan="1">left side</span>.
</h2>

<h2 v-click="2" style="font-size: 2.8rem; color: white; line-height:1.2; margin-top:1rem;">
The leak is almost always at the <span v-mark.circle.orange="3">pinch</span>.
</h2>

<p v-click="4" style="font-size: 1.25rem; color: rgba(255,255,255,0.88); margin-top: 2.5rem; line-height:1.5;">
The first delivery. The first thirty days. The first time a new customer feels seen, or doesn&apos;t. The highest-leverage point in the entire system, and the one that gets the least attention.
</p>

</div>

</div>

<!--
AHA #3 (declarative painful flip). Click 1: underline "left side".
Click 2: second line clicks in. Click 3: circle "pinch". Click 4: payoff.
This is the slide that earns the lesson. 20s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Know this · the transformation inside the bowtie</div>

<h2 style="font-size: 2rem; margin-bottom: 2rem;">It&apos;s not just a funnel. It&apos;s a transformation.</h2>

<div class="grid grid-cols-3 gap-4 max-w-6xl mx-auto w-full">

<div v-click class="ff-card" style="border-top: 4px solid #0891b2;">
<div style="font-weight:900; color:#0891b2; text-transform:uppercase; letter-spacing:0.12em; font-size:0.78rem; margin-bottom:0.6rem;">Acquisition</div>
<p style="margin:0; font-size:0.95rem; line-height:1.5;"><strong>They go from:</strong> a stranger with a problem, to a person who trusts you enough to hand you money.</p>
</div>

<div v-click class="ff-card" style="border-top: 4px solid #ea580c;">
<div style="font-weight:900; color:#ea580c; text-transform:uppercase; letter-spacing:0.12em; font-size:0.78rem; margin-bottom:0.6rem;">Trust (the pinch)</div>
<p style="margin:0; font-size:0.95rem; line-height:1.5;"><strong>They go from:</strong> a hopeful buyer who paid you, to a believer who has felt the work land. Or doesn&apos;t. Lose them here, lose them forever.</p>
</div>

<div v-click class="ff-card" style="border-top: 4px solid #059669;">
<div style="font-weight:900; color:#059669; text-transform:uppercase; letter-spacing:0.12em; font-size:0.78rem; margin-bottom:0.6rem;">Expansion</div>
<p style="margin:0; font-size:0.95rem; line-height:1.5;"><strong>They go from:</strong> a satisfied customer, to an advocate who brings you more customers and pays you more themselves.</p>
</div>

</div>

<p v-click style="font-size: 1.2rem; margin-top: 2rem; max-width: 50rem; margin-left:auto; margin-right:auto; text-align:center; font-weight:600;">
Three stages, three transformations. Move them through each, and the business compounds.
</p>

</div>

<!--
DECLARATIVE — the customer transformation arc. The bowtie isn't a funnel
diagram, it's a transformation arc. AHA #4: human change is the product.
20s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">The twist</div>

<h1 style="font-size: 3.2rem; line-height: 1.15; max-width: 56rem; text-align:center;">
Now look at how you <span v-mark.underline.green="1">hire</span>.
</h1>

<p v-click="2" style="font-size: 1.3rem; margin-top: 2.5rem; max-width: 46rem; text-align:center; color:#475569;">
Audience of candidates → application → assessment → interview → <strong>hire</strong> → ramp → review → operator who delivers.
</p>

<p v-click="3" style="font-size: 1.5rem; margin-top: 1.5rem; max-width: 46rem; text-align:center; font-weight:700;">
Cold strangers in. The right person out. <span class="ff-cyan">Same shape.</span>
</p>

</div>

<!--
TRANSITION to the dual bowtie. Plant the idea before showing the visual.
Click 1: underline "hire". Click 2: the talent flow named in sentence form.
Click 3: the kicker — same shape. 18s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">The dual bowtie</div>

<h2 style="font-size: 1.9rem; margin-bottom: 1.8rem;">Two bowties. Same operator. Same physics.</h2>

<div class="grid grid-cols-2 gap-8 max-w-6xl mx-auto w-full">

<div v-click class="ff-card" style="border-left: 6px solid #0891b2;">
<div style="font-weight:900; color:#0891b2; text-transform:uppercase; letter-spacing:0.12em; font-size:0.82rem; margin-bottom:1rem;">Customer Bowtie</div>
<div class="flex items-center justify-center gap-1 mb-3" style="height: 130px;">
<div class="bowtie-half-sm bowtie-left-sm"></div>
<div style="margin: 0 -6px; z-index: 5;"><div class="bowtie-pinch-sm"></div></div>
<div class="bowtie-half-sm bowtie-right-sm"></div>
</div>
<p style="margin:0; font-size:0.95rem; line-height:1.5;"><strong>Pinch:</strong> first delivery. First 30 days. The moment they decide whether to believe.</p>
</div>

<div v-click class="ff-card" style="border-left: 6px solid #059669;">
<div style="font-weight:900; color:#059669; text-transform:uppercase; letter-spacing:0.12em; font-size:0.82rem; margin-bottom:1rem;">Talent Bowtie</div>
<div class="flex items-center justify-center gap-1 mb-3" style="height: 130px;">
<div class="bowtie-half-sm bowtie-left-sm"></div>
<div style="margin: 0 -6px; z-index: 5;"><div class="bowtie-pinch-sm"></div></div>
<div class="bowtie-half-sm bowtie-right-sm"></div>
</div>
<p style="margin:0; font-size:0.95rem; line-height:1.5;"><strong>Pinch:</strong> first 30 days as a hire. Onboarding. Whether they fall in love with the work or quietly check out.</p>
</div>

</div>

<p v-click style="font-size: 1.25rem; margin-top: 2rem; max-width: 52rem; margin-left:auto; margin-right:auto; text-align:center; font-weight:600;">
Stack them side-by-side and you get a <span class="ff-cyan" style="font-weight:900;">square</span>. <span class="ff-orange">That square is your whole operator economy.</span>
</p>

</div>

<!--
AHA #5 (declarative kicker). Two bowties side by side, both with the same
structure, both with a pinch. The "square" framing makes it memorable.
25s.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">The unlock</div>

<h2 style="font-size: 2.8rem; color: white; line-height:1.25;">
The same physics moves <span class="ff-cyan">both</span> flows.
</h2>

<div v-click class="grid grid-cols-2 gap-4 mt-8 max-w-3xl mx-auto text-left">
<div style="color:white;">
<div style="color:var(--ff-cyan); font-weight:800; text-transform:uppercase; letter-spacing:0.1em; font-size:0.8rem; margin-bottom:0.5rem;">Customer</div>
<div style="font-size:0.95rem;">Attention → Trust → Transaction → Belief → Advocacy</div>
</div>
<div style="color:white;">
<div style="color:var(--ff-green); font-weight:800; text-transform:uppercase; letter-spacing:0.1em; font-size:0.8rem; margin-bottom:0.5rem;">Talent</div>
<div style="font-size:0.95rem;">Attention → Trust → Acceptance → Belief → Mastery</div>
</div>
</div>

<p v-click style="font-size: 1.2rem; color: rgba(255,255,255,0.92); margin-top: 2.5rem; font-weight:600;">
If you can move people through one, you can move people through the other. One operating system. Two applications.
</p>

</div>

</div>

<!--
AHA #6: the deepest insight. Same physics, two applications.
Click 1: the side-by-side stages. Click 2: the synthesis line.
This is the takeaway operators leave with. 20s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Where attention typically goes</div>

<h2 style="font-size: 2rem; margin-bottom: 2rem; max-width: 50rem; text-align:center;">
And where it should go instead.</h2>

<div class="grid grid-cols-2 gap-6 max-w-5xl mx-auto w-full">

<div v-click class="ff-card" style="background:#fef2f2; border-left: 6px solid #ef4444;">
<div style="font-weight:900; color:#b91c1c; text-transform:uppercase; letter-spacing:0.12em; font-size:0.78rem; margin-bottom:0.8rem;">Where it goes</div>
<ul style="margin:0; padding-left:1.1rem; font-size:1rem; line-height:1.6; text-align:left;">
<li>More ads, more reach, more leads (left side, customer bowtie)</li>
<li>More resumes, more interviews (left side, talent bowtie)</li>
<li>Wider, wider, wider</li>
</ul>
</div>

<div v-click class="ff-card" style="background:#f0fdf4; border-left: 6px solid #16a34a;">
<div style="font-weight:900; color:#15803d; text-transform:uppercase; letter-spacing:0.12em; font-size:0.78rem; margin-bottom:0.8rem;">Where it should go</div>
<ul style="margin:0; padding-left:1.1rem; font-size:1rem; line-height:1.6; text-align:left;">
<li>The first delivery (customer pinch)</li>
<li>The first 30 days (talent pinch)</li>
<li>Both pinches before either left side</li>
</ul>
</div>

</div>

<p v-click style="font-size: 1.25rem; margin-top: 2rem; max-width: 50rem; margin-left:auto; margin-right:auto; text-align:center; font-style:italic; color:#475569;">
A leaky pinch is worth ten broken left sides. Fix the pinch and the left side <em>gets cheaper</em>.
</p>

</div>

<!--
AHA #7 (procedural prescription). Where attention SHOULD go.
Most operators allocate backwards. The narrative payoff: fix pinches first
because they make the left side cheaper (better retention = lower CAC needed).
25s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Who does what</div>

<h2 style="font-size: 2.2rem; margin-bottom: 2.5rem;">
Inside Growth Starter, here&apos;s the split on this worldview.
</h2>

<div class="grid grid-cols-2 gap-6 max-w-6xl mx-auto w-full">

<div v-click class="ff-card" style="border-left: 6px solid #0891b2;">
<div style="font-weight:900; color:#0891b2; text-transform:uppercase; letter-spacing:0.12em; font-size:0.82rem; margin-bottom:1rem;">We&apos;ve got this</div>
<ul style="margin:0; padding-left:1.1rem; font-size:1rem; line-height:1.6; text-align:left;">
<li>Map your customer bowtie on the Day 7 call</li>
<li>Surface where your real pinch is from the data</li>
<li>Ship the work that strengthens the pinch (copy, scripts, sequences)</li>
<li>Tell you when the leak shifts</li>
</ul>
</div>

<div v-click class="ff-card" style="border-left: 6px solid #ea580c;">
<div style="font-weight:900; color:#ea580c; text-transform:uppercase; letter-spacing:0.12em; font-size:0.82rem; margin-bottom:1rem;">You do this</div>
<ul style="margin:0; padding-left:1.1rem; font-size:1rem; line-height:1.6; text-align:left;">
<li>Execute the pinch work — onboarding, first delivery, first 30 days</li>
<li>Notice the talent pinch too — it&apos;s yours to design</li>
<li>Stop greenlighting more left-side spend until the pinch holds</li>
<li>Tell us when something at the pinch isn&apos;t landing</li>
</ul>
</div>

</div>

</div>

<!--
PROCEDURAL — the responsibility split. Mirrors the pattern from the
Priority Lever deck. Sets clear expectations: pinch work is COLLABORATIVE,
but execution is theirs. 25s.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">If you remember one thing</div>

<h1 style="font-size: 3.4rem; color: white; line-height:1.15;">
Every business is <span class="ff-cyan">two bowties</span>.
</h1>

<h1 v-click style="font-size: 3.4rem; color: white; line-height:1.15; margin-top:1.2rem;">
Know your numbers at the <span class="ff-orange">pinch</span>.
</h1>

<p v-click style="font-size: 1.25rem; color: rgba(255,255,255,0.88); margin-top: 2.5rem; max-width: 44rem; margin-left:auto; margin-right:auto;">
That&apos;s the worldview. The next two lessons make it operational.
</p>

</div>

</div>

<!--
THE SYNTHESIS. Two big lines. Lands. Pause on recording. 12s.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream);">

<div class="ff-eyebrow">Do this · your rep this week</div>

<h2 style="font-size: 2rem; margin-bottom: 2.5rem; max-width: 50rem; text-align:center;">
Three things. Twenty minutes total.
</h2>

<div class="max-w-3xl mx-auto space-y-3 text-left">

<div v-click class="ff-card">
<p style="margin:0; font-size:1.1rem;"><strong class="ff-cyan">1. Draw your customer bowtie.</strong> Stages on each side. Mark where you think the pinch is.</p>
</div>

<div v-click class="ff-card">
<p style="margin:0; font-size:1.1rem;"><strong class="ff-green">2. Draw your talent bowtie.</strong> Even if you&apos;re solo. Audience → application → hire → ramp → operator. Mark its pinch too.</p>
</div>

<div v-click class="ff-card">
<p style="margin:0; font-size:1.1rem;"><strong class="ff-orange">3. Ask one question.</strong> <em>Where am I spending more attention right now, the left side or the pinch?</em> Be honest. Bring the answer to the next call.</p>
</div>

</div>

</div>

<!--
PROCEDURAL — the rep. Three concrete actions. The third one is the mirror.
20s.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">What&apos;s next</div>

<h2 style="font-size: 2.4rem; color: white; line-height:1.25;">
Now we put <span class="ff-cyan">math</span> under it.
</h2>

<p v-click style="font-size: 1.3rem; color: rgba(255,255,255,0.9); margin-top: 2rem; max-width: 50rem; margin-left:auto; margin-right:auto;">
Lesson 4.2: <strong>Unit Economics + The Vehicle</strong>. LTV, CAC, payback — the formulas that make the bowtie real, plus how those numbers translate to stability, profitability, and freedom.
</p>

<p v-click style="font-size: 1.2rem; color: rgba(255,255,255,0.75); margin-top: 1rem; max-width: 50rem; margin-left:auto; margin-right:auto;">
Then 4.3: <strong>The Leverage Zoom</strong>. Where to intervene — Global, Macro, Micro, Nano — without spreading thin.
</p>

<p v-click style="font-size: 1.15rem; color: var(--ff-cyan); margin-top: 1.8rem; font-weight:600;">
Three lessons, one worldview. See you in 4.2.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST · GO DEEPER
</div>

</div>

<!--
CLIFFHANGER. Set up the 3-lesson arc and tease both 4.2 (Unit Econ + Vehicle)
and 4.3 (Leverage Zoom Global/Macro/Micro/Nano). Forward momentum. 15s.
-->
