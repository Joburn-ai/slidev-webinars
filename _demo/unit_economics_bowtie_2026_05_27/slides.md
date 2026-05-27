---
theme: default
title: Unit Economics & The Bowtie
info: |
  Demo workshop deck — showcases Slidev interactive capabilities.
  v-motion builds, Magic Move, v-mark annotation, a live reactive LTV/CAC calculator.
  Content: John Coburn's dual-bowtie frame + unit economics + leverage zoom.
class: text-center
highlighter: shiki
lineNumbers: false
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

<div class="ff-eyebrow">
The Operator's Workshop · Module 1
</div>

<h1 style="font-size: 4.5rem; color: white;">
Unit Economics<br/>& The <span class="ff-cyan">Bowtie</span>
</h1>

<p style="font-size: 1.5rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 48rem; margin-left:auto; margin-right:auto;">
How to model any business as two bowties, and know your real numbers in 30 minutes.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST
</div>

</div>

<!--
This deck is a CAPABILITY DEMO. It uses: v-motion (kinetic builds), Magic Move
(animated formula), v-mark (rough-notation highlight), and a LIVE reactive
LTV/CAC calculator (Vue script setup + sliders). Press the pencil icon to draw.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center px-20" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">By the end of this module you will be able to</div>

<div class="space-y-4 mt-2 max-w-4xl">

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.25rem;">
<span style="font-size:2rem;" class="ff-cyan">1</span>
<p style="margin:0; font-size:1.4rem; font-weight:600;">Draw any business as a <strong>bowtie</strong>, and spot exactly where it leaks.</p>
</div>

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.25rem;">
<span style="font-size:2rem;" class="ff-green">2</span>
<p style="margin:0; font-size:1.4rem; font-weight:600;">Calculate <strong>LTV, CAC, and payback</strong> live, and read what they're telling you.</p>
</div>

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.25rem;">
<span style="font-size:2rem;" class="ff-orange">3</span>
<p style="margin:0; font-size:1.4rem; font-weight:600;">Use the <strong>same math</strong> for customers AND talent. One operating system.</p>
</div>

</div>

</div>

<!--
WORKSHOP SURVIVAL (Fitzpatrick): open by telling them exactly what they'll be
able to DO. Concrete capability promises, not topics. Each clicks in.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">The shape of every business</div>

<h2 style="font-size: 2.6rem; margin-bottom: 2.5rem;">The Bowtie.</h2>

<div class="flex items-center justify-center gap-2" style="height: 220px;">

<div v-motion :initial="{ x: -120, opacity: 0 }" :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }" class="flex flex-col items-center">
<div class="bowtie-half bowtie-left"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#0891b2; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Acquisition</div>
<div style="font-size:0.8rem; color:#64748b;">cold → opt-in → first sale</div>
</div>

<div v-motion :initial="{ scale: 0, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { delay: 500 } }" class="flex flex-col items-center" style="margin: 0 -10px; z-index: 5;">
<div class="bowtie-pinch"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#ea580c; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Trust</div>
</div>

<div v-motion :initial="{ x: 120, opacity: 0 }" :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }" class="flex flex-col items-center">
<div class="bowtie-half bowtie-right"></div>
<div style="margin-top:0.75rem; font-weight:800; color:#059669; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em;">Expansion</div>
<div style="font-size:0.8rem; color:#64748b;">repeat → advocate → upsell</div>
</div>

</div>

<p v-click style="font-size: 1.3rem; margin-top: 2.5rem; max-width: 44rem; text-align:center; font-weight:500;">
Left side fills the room. Right side is where the money actually compounds. The <span class="ff-orange" style="font-weight:800;">pinch</span> is where trust is won or lost.
</p>

</div>

<!--
v-motion DEMO: the two halves slide in from the sides, the pinch scales up in
the middle on a delay. This is the "pieces fly into the diagram" build that
holds attention on video.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">John Coburn's frame</div>

<h2 style="font-size: 2.4rem; margin-bottom: 2rem;">Two bowties. One square.</h2>

<div class="grid grid-cols-2 gap-6 max-w-6xl w-full">

<div v-click class="ff-card">
<div style="font-weight:800; color:#0891b2; text-transform:uppercase; letter-spacing:0.12em; font-size:0.8rem; margin-bottom:0.75rem;">Customer Bowtie</div>
<p style="margin:0; font-size:1.05rem;">Audience → opt-in → application → call → <strong class="ff-orange">close</strong> → onboarding → retention → advocacy</p>
</div>

<div v-click class="ff-card">
<div style="font-weight:800; color:#059669; text-transform:uppercase; letter-spacing:0.12em; font-size:0.8rem; margin-bottom:0.75rem;">Talent Bowtie</div>
<p style="margin:0; font-size:1.05rem;">Audience → application → assessment → interview → <strong class="ff-orange">hire</strong> → ramp → review → operator-graduate</p>
</div>

</div>

<p v-click style="font-size: 1.35rem; margin-top: 2.5rem; max-width: 46rem; text-align:center; font-weight:600;">
Stack them side by side and you get a square. <span class="ff-cyan" style="font-weight:800;">That square is the whole operator economy</span> — customers and talent flow through the same physics.
</p>

</div>

<!--
John's dual-bowtie thesis. Customer acquisition + talent acquisition are the
same shape. Attribution note: bowtie funnel concept is Winning by Design /
Jacco van der Kooij; John's contribution is the dual-adaptation. Cite on first use.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">The part most operators miss</div>

<h2 style="font-size: 2.8rem; color: white; line-height:1.25;">
Everyone obsesses over the <span v-mark.underline.cyan="1">left side</span>.<br/>
The leak is almost always at the <span v-mark.circle.orange="2">pinch</span>.
</h2>

<p v-click="3" style="font-size: 1.3rem; color: rgba(255,255,255,0.85); margin-top: 2.5rem; line-height:1.5;">
The first delivery. The first onboarding. The first 30 days of a new hire. That trust moment is the highest-leverage point in the entire system, and it gets the least attention.
</p>

</div>

</div>

<!--
v-mark DEMO (built-in rough-notation): underline animates under "left side" on
click 1, circle animates around "pinch" on click 2. The persuasion-grade
emphasis tool. Then the payoff line on click 3.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-20" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">The only formula that matters</div>

<h2 style="font-size: 2rem; margin-bottom: 2rem;">Build it up, one piece at a time.</h2>

````md magic-move {at:1}
```
LTV
```
```
LTV : CAC
```
```
LTV : CAC   →   must beat 3 : 1
```
```
LTV : CAC   →   3 : 1
Payback < 12 months
```
````

<p v-click="5" style="font-size:1.25rem; margin-top:2.5rem; max-width:42rem; text-align:center; font-weight:600;">
A healthy business: <span class="ff-green" style="font-weight:800;">earn 3x what it costs to acquire</span>, and get the cash back inside a year.
</p>

</div>

<!--
MAGIC MOVE DEMO: the formula morphs across 4 states on each click — LTV →
ratio → threshold → +payback. Keynote-style animated build, not cuts.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-12" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">Live model · drag the sliders</div>

<h2 style="font-size: 1.8rem; margin-bottom: 1.5rem;">Watch the numbers move.</h2>

<script setup>
import { ref, computed } from 'vue'
const price = ref(2000)
const margin = ref(70)
const repeat = ref(2.5)
const cac = ref(900)
const ltv = computed(() => Math.round(price.value * (margin.value/100) * repeat.value))
const ratio = computed(() => (ltv.value / cac.value))
const payback = computed(() => (cac.value / (price.value * (margin.value/100))) )
const ratioColor = computed(() => ratio.value >= 3 ? '#059669' : ratio.value >= 1.5 ? '#FB923C' : '#ef4444')
const paybackColor = computed(() => payback.value <= 1 ? '#059669' : payback.value <= 3 ? '#FB923C' : '#ef4444')
</script>

<div class="calc-shell max-w-3xl w-full">

<div class="calc-row">
<div class="calc-label">Price</div>
<input class="calc-slider" type="range" min="200" max="10000" step="100" v-model.number="price" />
<div class="calc-val">${{ price.toLocaleString() }}</div>
</div>

<div class="calc-row">
<div class="calc-label">Margin %</div>
<input class="calc-slider" type="range" min="20" max="95" step="1" v-model.number="margin" />
<div class="calc-val">{{ margin }}%</div>
</div>

<div class="calc-row">
<div class="calc-label">Repeat buys</div>
<input class="calc-slider" type="range" min="1" max="8" step="0.1" v-model.number="repeat" />
<div class="calc-val">{{ repeat.toFixed(1) }}x</div>
</div>

<div class="calc-row">
<div class="calc-label">CAC</div>
<input class="calc-slider" type="range" min="100" max="5000" step="50" v-model.number="cac" />
<div class="calc-val">${{ cac.toLocaleString() }}</div>
</div>

<div class="calc-out">
<div class="calc-metric">
<div class="calc-metric-num" style="color:#0F172A;">${{ ltv.toLocaleString() }}</div>
<div class="calc-metric-label">LTV</div>
</div>
<div class="calc-metric">
<div class="calc-metric-num" :style="{ color: ratioColor }">{{ ratio.toFixed(1) }}:1</div>
<div class="calc-metric-label">LTV : CAC</div>
</div>
<div class="calc-metric">
<div class="calc-metric-num" :style="{ color: paybackColor }">{{ payback.toFixed(1) }}mo</div>
<div class="calc-metric-label">Payback</div>
</div>
</div>

</div>

<p style="font-size:0.95rem; margin-top:1.25rem; color:#64748b;">Green = healthy · Orange = watch it · Red = underwater. This is a live Vue widget — every drag recomputes.</p>

</div>

<!--
THE SHOWPIECE: a fully reactive calculator. Drag any slider and LTV, the ratio,
and payback recompute live, with color-coded health. This is what "every slide
is a Vue component" unlocks — a playable model, not a static chart.
-->

---
layout: cover
---

<div class="absolute inset-0 flex flex-col justify-center items-center px-16" style="background: var(--ff-cream, #f8fafc);">

<div class="ff-eyebrow">The unlock</div>

<h2 style="font-size: 2.4rem; margin-bottom: 2.5rem; max-width: 48rem; text-align:center;">
The same math runs <span class="ff-cyan">both</span> bowties.
</h2>

<div class="grid grid-cols-2 gap-6 max-w-5xl w-full">

<div v-click class="ff-card">
<div style="font-weight:800; color:#0891b2; font-size:0.95rem; margin-bottom:0.75rem;">CUSTOMER</div>
<p style="margin:0; font-size:1rem; line-height:1.6;"><strong>CAC</strong> = cost to close a client<br/><strong>LTV</strong> = margin × repeat purchases<br/><strong>Payback</strong> = months to recover CAC</p>
</div>

<div v-click class="ff-card">
<div style="font-weight:800; color:#059669; font-size:0.95rem; margin-bottom:0.75rem;">TALENT</div>
<p style="margin:0; font-size:1rem; line-height:1.6;"><strong>CAC</strong> = cost to hire + ramp<br/><strong>LTV</strong> = output value × tenure<br/><strong>Payback</strong> = months to recover hiring cost</p>
</div>

</div>

<p v-click style="font-size: 1.3rem; margin-top: 2.5rem; max-width: 44rem; text-align:center; font-weight:600;">
If you can model customer unit economics, you can model talent. <span class="ff-orange" style="font-weight:800;">One operating system, two applications.</span>
</p>

</div>

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center px-16">

<div class="ff-bar"></div>

<div class="max-w-5xl mx-auto w-full">

<div class="ff-eyebrow">Where you intervene · the leverage zoom</div>

<h2 style="font-size: 2.2rem; color: white; margin-bottom: 2rem;">Global → Macro → Micro.</h2>

<div class="space-y-3">

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.5rem; background: rgba(255,255,255,0.96);">
<div style="font-size:1.6rem; font-weight:900; color:#0891b2; width:7rem;">GLOBAL</div>
<p style="margin:0; font-size:1.05rem;">Company, offer, market. The whole square. <span style="color:#64748b;">Highest leverage, slowest to move.</span></p>
</div>

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.5rem; background: rgba(255,255,255,0.96);">
<div style="font-size:1.6rem; font-weight:900; color:#059669; width:7rem;">MACRO</div>
<p style="margin:0; font-size:1.05rem;">The process. One bowtie, one funnel, one hiring pipeline. <span style="color:#64748b;">Where audits live.</span></p>
</div>

<div v-click class="ff-card" style="display:flex; align-items:center; gap:1.5rem; background: rgba(255,255,255,0.96);">
<div style="font-size:1.6rem; font-weight:900; color:#ea580c; width:7rem;">MICRO</div>
<p style="margin:0; font-size:1.05rem;">The execution. One ad, one call, one onboarding email. <span style="color:#64748b;">Fastest to change, easiest to test.</span></p>
</div>

</div>

<p v-click style="font-size: 1.2rem; color: rgba(255,255,255,0.85); margin-top: 2rem; text-align:center;">
Most operators fix Micro when the leak is Global. <span class="ff-cyan" style="font-weight:700;">Zoom to the right altitude first.</span>
</p>

</div>

</div>

<!--
John's leverage-zoom axis. Global=company/offer/market, Macro=process,
Micro=execution. Maps to the audit ladder. Applies to both bowties.
-->

---
layout: cover
---

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-16">

<div class="ff-bar"></div>

<div class="max-w-4xl text-center">

<div class="ff-eyebrow">If you remember one thing</div>

<h1 style="font-size: 3.4rem; color: white; line-height:1.2;">
Every business is two bowties.<br/>
<span class="ff-cyan">Know your numbers at the pinch.</span>
</h1>

<div class="grid grid-cols-3 gap-4 mt-12 max-w-3xl mx-auto">
<div v-click style="background: rgba(34,211,238,0.12); border:1px solid rgba(34,211,238,0.3); border-radius:12px; padding:1.1rem;">
<div style="color:white; font-weight:700; font-size:1rem;">Draw the bowtie</div>
</div>
<div v-click style="background: rgba(52,211,153,0.12); border:1px solid rgba(52,211,153,0.3); border-radius:12px; padding:1.1rem;">
<div style="color:white; font-weight:700; font-size:1rem;">Run the numbers</div>
</div>
<div v-click style="background: rgba(251,146,60,0.12); border:1px solid rgba(251,146,60,0.3); border-radius:12px; padding:1.1rem;">
<div style="color:white; font-weight:700; font-size:1rem;">Zoom to the leak</div>
</div>
</div>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.2em;">
JOHN COBURN · FUNNEL FUTURIST · THE OPERATOR'S WORKSHOP
</div>

</div>

<!--
WORKSHOP SURVIVAL close: one memorable takeaway + the 3-step recall scaffold.
Send them out able to DO the thing, not just having heard about it.
-->
