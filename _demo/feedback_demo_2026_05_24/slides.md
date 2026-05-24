---
theme: default
title: Feedback Demo Deck. How To Use This For A Loom Review
info: |
  Generic 22-slide demo webinar for demonstrating the feedback protocol.
  Use this when teaching a teammate how to give slide-level revision notes.
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: Inter
  serif: Inter
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<style>
:root {
  --brand-primary: #2563eb;
  --brand-secondary: #f59e0b;
  --brand-accent: #ecfeff;
  --brand-dark: #0f172a;
  --brand-light: #fafaf7;
}

.slidev-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--brand-light);
  color: var(--brand-dark);
}

.slidev-vclick-hidden {
  opacity: 0 !important;
}
.slidev-vclick-target {
  transition: opacity 200ms ease;
}

.slidev-layout h1 {
  font-size: 4.5rem;
  font-weight: 900;
  color: var(--brand-primary);
  letter-spacing: -0.03em;
  line-height: 1.05;
}

.slidev-layout p, .slidev-layout li {
  font-size: 1.5rem;
  line-height: 1.6;
}

.slidev-layout strong {
  color: var(--brand-primary);
  font-weight: 700;
}

.brand-primary { color: var(--brand-primary); }
.brand-secondary { color: var(--brand-secondary); font-weight: 800; }
</style>

<!-- slide:cover-01 -->

<div class="absolute inset-0" style="background: radial-gradient(ellipse at top, #3b82f6 0%, #2563eb 40%, #1e3a8a 100%);"></div>

<div class="absolute inset-0 flex items-center justify-center px-12">
  <div class="text-center max-w-4xl">
    <div class="text-2xl mb-12" style="color: rgba(245, 158, 11, 0.9); letter-spacing: 0.3em; text-transform: uppercase; font-weight: 600;">
      Demo Webinar
    </div>
    <div class="font-black" style="font-size: 6rem; line-height: 0.95; color: white; letter-spacing: -0.04em;">
      Stop Burning Out.
    </div>
    <div class="font-black mt-4" style="font-size: 5rem; line-height: 1; color: #f59e0b; letter-spacing: -0.03em;">
      Start Compounding.
    </div>
    <div class="mt-16 text-xl" style="color: rgba(255,255,255,0.7);">
      A Founder Masterclass with Demo Presenter
    </div>
    <div class="mt-3 text-base" style="color: rgba(255,255,255,0.5); letter-spacing: 0.1em;">
      Tuesday at 8pm EST. Live on Zoom.
    </div>
  </div>
</div>

<div class="absolute" style="bottom: 4%; left: 50%; transform: translateX(-50%);">
  <div class="flex items-center gap-2" style="color: rgba(255,255,255,0.4); font-size: 0.875rem;">
    <span>Press</span>
    <kbd style="background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2);">Space</kbd>
    <span>to begin</span>
  </div>
</div>

<!--
HOOK: Demo deck cover slide. Tight on brand colors (blue + amber).
DEMO NOTE for reviewer: this is a fake webinar built to demonstrate the feedback protocol.
TIMING: 30 sec
TRANSITION: "Hey. Welcome in."
-->

---
layout: center
class: text-center
---

<!-- slide:welcome-02 -->

<div class="space-y-8">

<v-click>

<div class="text-3xl text-slate-600">
Hey. Welcome in.
</div>

</v-click>

<v-click>

<div class="font-black brand-primary" style="font-size: 4.5rem; line-height: 1; letter-spacing: -0.03em;">
I'm a Demo Presenter.
</div>

</v-click>

<v-click>

<div class="text-2xl text-slate-500 mt-6">
This is what a webinar slide deck looks like.
</div>

</v-click>

</div>

<!--
HOOK: Open calm. Direct address.
DEMO NOTE: pattern 1 = welcome with v-click reveals on plain text.
TIMING: 15 sec
TRANSITION: Credentials.
-->

---
layout: default
---

<!-- slide:creds-03 -->

# Why listen to me?

<v-clicks>

- 10 years building startups
- 3 exits, 1 IPO
- Mentored 200+ founders
- Burned out twice. Recovered both times.

</v-clicks>

<!--
HOOK: Credentials with v-clicks list reveal.
DEMO NOTE: pattern 2 = bullet list with progressive reveal.
TIMING: 25 sec
TRANSITION: "Tonight is going to be different."
-->

---
layout: center
class: text-center
---

<!-- slide:frame-04 -->

<div class="space-y-12">

<v-click>

<div class="text-3xl text-slate-500">
Tonight is going to be different.
</div>

</v-click>

<v-click>

<div class="font-black brand-secondary" style="font-size: 7rem; line-height: 1; letter-spacing: -0.04em;">
Burnout is over.
</div>

</v-click>

<v-click>

<div class="font-bold brand-primary" style="font-size: 3rem; line-height: 1.1; letter-spacing: -0.02em;">
Compounding starts right now.
</div>

</v-click>

</div>

<!--
HOOK: Big-impact frame statement. Hero typography.
DEMO NOTE: pattern 3 = three-beat reveal with hero typography. Test "I'm on slide 4. Change brand-secondary line to..." feedback.
TIMING: 25 sec
TRANSITION: Pop Quiz.
-->

---
layout: center
class: text-center
---

<!-- slide:popquiz-intro-05 -->

<div class="absolute inset-0" style="background: radial-gradient(ellipse at center, #3b82f6 0%, #2563eb 50%, #1e3a8a 100%);"></div>

<div class="absolute inset-0 flex items-center justify-center px-16">

<div class="text-center text-white max-w-4xl space-y-8">

<v-click>

<div style="color: rgba(245, 158, 11, 0.85); letter-spacing: 0.35em; text-transform: uppercase; font-size: 1.1rem; font-weight: 600;">
Quick Warm-up
</div>

</v-click>

<v-click>

<div class="font-black" style="font-size: 7.5rem; line-height: 1; color: #f59e0b; letter-spacing: -0.04em;">
Pop Quiz
</div>

</v-click>

<v-click>

<div class="text-3xl" style="line-height: 1.3;">
3 True or False questions about founder burnout.
</div>

</v-click>

<v-click>

<div class="inline-flex flex-wrap items-center justify-center gap-x-4 gap-y-2 mt-6 px-8 py-5 rounded-2xl" style="background: rgba(245, 158, 11, 0.15); border: 2px solid rgba(245, 158, 11, 0.45);">
  <span class="text-2xl">Reply</span>
  <span class="font-black" style="color: #f59e0b; font-size: 2rem;">T</span>
  <span class="text-xl" style="color: rgba(255,255,255,0.75);">for True</span>
  <span style="color: rgba(255,255,255,0.4); font-size: 1.5rem;">·</span>
  <span class="font-black" style="color: #f59e0b; font-size: 2rem;">F</span>
  <span class="text-xl" style="color: rgba(255,255,255,0.75);">for False</span>
  <span class="text-2xl">in the chat</span>
</div>

</v-click>

</div>

</div>

<!--
HOOK: Audience interaction begins.
DEMO NOTE: pattern 4 = section divider with gradient background + brand color hero text + pill CTA.
TIMING: 30 sec
TRANSITION: Q1.
-->

---
layout: center
class: text-center
---

<!-- slide:q1-setup-06 -->

<div class="space-y-10">

<v-click>

<div class="text-lg uppercase text-slate-500" style="letter-spacing: 0.25em;">
Question 1 of 3
</div>

</v-click>

<v-click>

<div class="font-black brand-primary" style="font-size: 4.5rem; line-height: 1; letter-spacing: -0.03em;">
True or False?
</div>

</v-click>

<v-click>

<div class="text-4xl text-slate-700 max-w-3xl mx-auto font-medium" style="line-height: 1.3;">
Burnout means you need a vacation.
</div>

</v-click>

<v-click>

<div class="text-xl text-slate-500 mt-10">
Type T or F in the chat.
</div>

</v-click>

</div>

<!--
HOOK: Pop quiz question setup.
DEMO NOTE: pattern 5 = centered text reveals. Test "I'm on slide 6. The question text is too long, shorten to X."
TIMING: 25 sec
TRANSITION: Reveal.
-->

---
layout: center
class: text-center
---

<!-- slide:q1-reveal-07 -->

<div class="space-y-10">

<v-click>

<div class="inline-block px-12 py-6 rounded-full" style="background: rgba(220, 38, 38, 0.1); border: 2px solid #dc2626;">
  <span class="font-black text-red-600" style="font-size: 6rem; letter-spacing: 0.05em;">FALSE</span>
</div>

</v-click>

<v-click>

<div class="text-2xl text-slate-700 max-w-3xl mx-auto" style="line-height: 1.55;">
Burnout means your <strong>operating cadence is wrong</strong>. A vacation pauses the cadence. It doesn't fix it.
</div>

</v-click>

<v-click>

<div class="text-3xl font-bold brand-primary max-w-3xl mx-auto" style="line-height: 1.25;">
You don't need rest. You need a different system.
</div>

</v-click>

</div>

<!--
HOOK: Pop quiz answer reveal with pill badge.
DEMO NOTE: pattern 6 = FALSE pill reveal + reframe content.
TIMING: 35 sec
TRANSITION: Q2.
-->

---
layout: center
class: text-center
---

<!-- slide:q2-setup-08 -->

<div class="space-y-10">

<v-click>

<div class="text-lg uppercase text-slate-500" style="letter-spacing: 0.25em;">
Question 2 of 3
</div>

</v-click>

<v-click>

<div class="font-black brand-primary" style="font-size: 4.5rem; line-height: 1; letter-spacing: -0.03em;">
True or False?
</div>

</v-click>

<v-click>

<div class="text-4xl text-slate-700 font-medium">
Burnout happens to weak founders.
</div>

</v-click>

<v-click>

<div class="text-xl text-slate-500 mt-10">
Type T or F in the chat.
</div>

</v-click>

</div>

<!--
DEMO NOTE: identical pattern to slide 6 to show the rhythm of setup-reveal pairs.
TIMING: 25 sec
TRANSITION: Reveal.
-->

---
layout: center
class: text-center
---

<!-- slide:q2-reveal-09 -->

<div class="space-y-10">

<v-click>

<div class="inline-block px-12 py-6 rounded-full" style="background: rgba(220, 38, 38, 0.1); border: 2px solid #dc2626;">
  <span class="font-black text-red-600" style="font-size: 6rem; letter-spacing: 0.05em;">FALSE</span>
</div>

</v-click>

<v-click>

<div class="text-2xl text-slate-700 max-w-3xl mx-auto" style="line-height: 1.55;">
Burnout happens to <strong>high-output founders running an inefficient system</strong>. The harder you push a broken system, the faster you break.
</div>

</v-click>

<v-click>

<div class="text-3xl font-bold brand-secondary mt-6" style="line-height: 1.3;">
Output is not the problem. Cadence is.
</div>

</v-click>

</div>

<!--
DEMO NOTE: pattern repeats. Good practice slide for feedback testing.
TIMING: 30 sec
TRANSITION: Q3.
-->

---
layout: center
class: text-center
---

<!-- slide:q3-reveal-10 -->

<div class="space-y-10">

<v-click>

<div class="text-lg uppercase text-slate-500" style="letter-spacing: 0.25em;">
Question 3 of 3
</div>

</v-click>

<v-click>

<div class="text-4xl text-slate-700 font-medium max-w-3xl mx-auto" style="line-height: 1.3;">
The fix for burnout is more discipline.
</div>

</v-click>

<v-click>

<div class="inline-block px-12 py-6 rounded-full mt-8" style="background: rgba(220, 38, 38, 0.1); border: 2px solid #dc2626;">
  <span class="font-black text-red-600" style="font-size: 6rem; letter-spacing: 0.05em;">FALSE</span>
</div>

</v-click>

<v-click>

<div class="text-2xl text-slate-700 max-w-3xl mx-auto mt-4" style="line-height: 1.55;">
More discipline applied to a broken system <strong>accelerates the burn</strong>. The fix is a better operating cadence, not more willpower.
</div>

</v-click>

</div>

<!--
DEMO NOTE: combined setup + reveal pattern on one slide (faster pacing variant).
TIMING: 35 sec
TRANSITION: Pain section.
-->

---
layout: center
class: text-center
---

<!-- slide:pain-opener-11 -->

<div class="absolute inset-0" style="background: radial-gradient(ellipse at center, #2a3447 0%, #1a2030 60%, #0a0d14 100%);"></div>

<div class="absolute inset-0 flex items-center justify-center px-16">

<div class="text-center max-w-4xl space-y-12">

<v-click>

<div style="color: rgba(245, 158, 11, 0.7); letter-spacing: 0.4em; text-transform: uppercase; font-size: 1rem; font-weight: 600;">
The pattern I watch every quarter
</div>

</v-click>

<v-click>

<div class="font-black" style="font-size: 5rem; line-height: 1.05; color: white; letter-spacing: -0.03em;">
Same broken cadence. Different founder.
</div>

</v-click>

<v-click>

<div class="text-xl mt-4" style="color: rgba(255,255,255,0.55); font-style: italic;">
Let me show you what it looks like before it becomes a crisis.
</div>

</v-click>

</div>

</div>

<!--
HOOK: Tone shift to pain section. Dark gradient.
DEMO NOTE: pattern 7 = pain section opener with dark gradient + amber accent.
TIMING: 18 sec
TRANSITION: Quiet questions.
-->

---
layout: default
---

<!-- slide:pain-questions-12 -->

<div class="h-full flex flex-col justify-center px-12 max-w-5xl mx-auto">

<div class="text-base uppercase text-slate-500 mb-6" style="letter-spacing: 0.3em; font-weight: 600;">
The questions you carry
</div>

<div class="font-black brand-primary mb-10" style="font-size: 2.75rem; line-height: 1.15; letter-spacing: -0.02em;">
Five things every burned-out founder thinks but rarely says.
</div>

<div class="space-y-3 text-xl text-slate-700">

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Am I building the right thing?</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Why does every win feel small and every loss feel huge?</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Why am I working 70 hours and still behind?</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Is the team carrying its weight or just protecting me?</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>If I stopped pushing tomorrow, would anything collapse?</span>
</div>

</v-click>

</div>

</div>

<!--
HOOK: List of internal questions every founder carries.
DEMO NOTE: pattern 8 = list with progressive v-click reveal + amber bullet markers.
TIMING: 50 sec
TRANSITION: Two paths.
-->

---
layout: two-cols
---

<!-- slide:two-paths-13 -->

<div class="h-full flex flex-col justify-center px-8">

<div class="text-base uppercase mb-6" style="letter-spacing: 0.35em; font-weight: 600; color: #dc2626;">
Path One
</div>

<div class="font-black brand-primary mb-8" style="font-size: 2.5rem; line-height: 1.15; letter-spacing: -0.02em;">
Push harder.
</div>

<div class="space-y-3 text-lg text-slate-700">

<v-click>

<div>· More hours.</div>

</v-click>

<v-click>

<div>· More discipline.</div>

</v-click>

<v-click>

<div>· More caffeine.</div>

</v-click>

<v-click>

<div>· Same broken cadence.</div>

</v-click>

</div>

</div>

::right::

<div class="h-full flex flex-col justify-center px-8" style="background: rgba(245, 158, 11, 0.08);">

<v-click>

<div class="text-base uppercase mb-6" style="letter-spacing: 0.35em; font-weight: 600; color: #f59e0b;">
Path Two
</div>

</v-click>

<v-click>

<div class="font-black brand-primary mb-8" style="font-size: 2.5rem; line-height: 1.15; letter-spacing: -0.02em;">
Fix the cadence.
</div>

</v-click>

<div class="space-y-3 text-lg text-slate-700">

<v-click>

<div>· Weekly compounding loops.</div>

</v-click>

<v-click>

<div>· One thing per week that compounds.</div>

</v-click>

<v-click>

<div>· The same hours. Different output.</div>

</v-click>

</div>

</div>

<!--
HOOK: Binary path comparison. Path 1 is the trap. Path 2 is the lift.
DEMO NOTE: pattern 9 = two-cols layout with red/amber color coding.
TIMING: 45 sec
TRANSITION: Mechanism reveal.
-->

---
layout: default
---

<!-- slide:mechanism-14 -->

<div class="h-full flex flex-col justify-center px-12 max-w-6xl mx-auto">

<div class="text-base uppercase text-slate-500 mb-4 text-center" style="letter-spacing: 0.35em; font-weight: 600;">
The Compounding Cadence System
</div>

<div class="font-black brand-primary mb-10 text-center" style="font-size: 3rem; line-height: 1.1; letter-spacing: -0.03em;">
Four loops, running weekly.
</div>

<div class="grid grid-cols-2 gap-5">

<v-click>

<div class="p-6 rounded-xl" style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(37, 99, 235, 0.02)); border-top: 4px solid #2563eb;">
  <div class="text-sm uppercase mb-2" style="letter-spacing: 0.2em; color: #2563eb; font-weight: 700;">Loop 1</div>
  <div class="text-2xl font-black brand-primary mb-2">Plan</div>
  <div class="text-base text-slate-600" style="line-height: 1.4;">One owner, one outcome, one week. No exceptions.</div>
</div>

</v-click>

<v-click>

<div class="p-6 rounded-xl" style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(37, 99, 235, 0.02)); border-top: 4px solid #2563eb;">
  <div class="text-sm uppercase mb-2" style="letter-spacing: 0.2em; color: #2563eb; font-weight: 700;">Loop 2</div>
  <div class="text-2xl font-black brand-primary mb-2">Ship</div>
  <div class="text-base text-slate-600" style="line-height: 1.4;">Output visible by Friday. Nothing carries to next week.</div>
</div>

</v-click>

<v-click>

<div class="p-6 rounded-xl" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(245, 158, 11, 0.02)); border-top: 4px solid #f59e0b;">
  <div class="text-sm uppercase mb-2" style="letter-spacing: 0.2em; color: #f59e0b; font-weight: 700;">Loop 3</div>
  <div class="text-2xl font-black brand-primary mb-2">Review</div>
  <div class="text-base text-slate-600" style="line-height: 1.4;">What worked, what didn't. 15 minutes. No blame.</div>
</div>

</v-click>

<v-click>

<div class="p-6 rounded-xl" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(245, 158, 11, 0.02)); border-top: 4px solid #f59e0b;">
  <div class="text-sm uppercase mb-2" style="letter-spacing: 0.2em; color: #f59e0b; font-weight: 700;">Loop 4</div>
  <div class="text-2xl font-black brand-primary mb-2">Compound</div>
  <div class="text-base text-slate-600" style="line-height: 1.4;">The lesson goes into the system, not the founder's head.</div>
</div>

</v-click>

</div>

</div>

<!--
HOOK: Mechanism reveal. Four-quadrant grid with v-click sequential reveal.
DEMO NOTE: pattern 10 = 2x2 grid mechanism reveal. Same template as Four-Pillar System in SupportED deck.
TIMING: 65 sec
TRANSITION: Data table.
-->

---
layout: default
---

<!-- slide:data-table-15 -->

<div class="h-full flex flex-col justify-center px-8 mx-auto" style="max-width: 920px;">

<div class="text-sm uppercase text-slate-500 mb-2" style="letter-spacing: 0.3em; font-weight: 600;">
What changes after 90 days
</div>

<div class="font-black brand-primary mb-6" style="font-size: 1.9rem; line-height: 1.15; letter-spacing: -0.02em;">
Average founder metrics, before and after.
</div>

<div class="overflow-hidden rounded-xl" style="border: 1px solid rgba(37, 99, 235, 0.15);">

<v-click>

<div class="grid grid-cols-3 gap-0" style="background: rgba(37, 99, 235, 0.06);">
  <div class="p-4 text-sm uppercase font-bold" style="letter-spacing: 0.15em; color: #2563eb;">Metric</div>
  <div class="p-4 text-sm uppercase font-bold text-center" style="letter-spacing: 0.15em; color: #dc2626;">Before</div>
  <div class="p-4 text-sm uppercase font-bold text-center" style="letter-spacing: 0.15em; color: #f59e0b;">After</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-0" style="border-top: 1px solid rgba(37, 99, 235, 0.1);">
  <div class="p-4 text-base text-slate-700">Hours per week</div>
  <div class="p-4 text-base text-center text-slate-600">72</div>
  <div class="p-4 text-base text-center font-bold brand-primary">48</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-0" style="border-top: 1px solid rgba(37, 99, 235, 0.1);">
  <div class="p-4 text-base text-slate-700">Shipped projects / quarter</div>
  <div class="p-4 text-base text-center text-slate-600">3</div>
  <div class="p-4 text-base text-center font-bold brand-primary">11</div>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-0" style="border-top: 1px solid rgba(37, 99, 235, 0.1); background: rgba(245, 158, 11, 0.08);">
  <div class="p-4 text-base font-bold text-slate-700">Founder energy (1-10)</div>
  <div class="p-4 text-base text-center text-slate-600">4</div>
  <div class="p-4 text-base text-center font-bold brand-secondary">8</div>
</div>

</v-click>

</div>

</div>

<!--
HOOK: Data table proof.
DEMO NOTE: pattern 11 = data table with progressive row reveal + highlighted final row.
TIMING: 40 sec
TRANSITION: Testimonial.
-->

---
layout: default
---

<!-- slide:testimonial-16 -->

<div class="h-full flex flex-col justify-center px-12 max-w-5xl mx-auto">

<div class="text-base uppercase text-slate-500 mb-3" style="letter-spacing: 0.3em; font-weight: 600;">
Sarah · Founder, AcmeCorp
</div>

<div class="font-black brand-primary mb-6" style="font-size: 2.5rem; line-height: 1.15; letter-spacing: -0.02em;">
Cut my hours in half. Doubled the output.
</div>

<div class="space-y-3 text-lg text-slate-700">

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Went from 72-hour weeks to 48.</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Shipped 11 projects last quarter. Up from 3.</span>
</div>

</v-click>

<v-click>

<div class="flex items-baseline gap-3">
  <span class="brand-secondary font-black text-2xl">·</span>
  <span>Team energy is the highest it's been in 2 years.</span>
</div>

</v-click>

<v-click>

<div class="p-4 rounded-xl mt-4" style="background: rgba(245, 158, 11, 0.15); border-left: 4px solid #f59e0b;">
  <div class="text-sm uppercase text-slate-600 mb-1" style="letter-spacing: 0.2em; font-weight: 700;">90-day result</div>
  <div class="font-black brand-secondary" style="font-size: 3rem; line-height: 1;">2x output</div>
</div>

</v-click>

</div>

</div>

<!--
HOOK: Generic testimonial proof.
DEMO NOTE: pattern 12 = testimonial with stat callout pill.
TIMING: 35 sec
TRANSITION: Offer intro.
-->

---
layout: center
class: text-center
---

<!-- slide:offer-intro-17 -->

<div class="absolute inset-0" style="background: radial-gradient(ellipse at center, #3b82f6 0%, #2563eb 50%, #1e3a8a 100%);"></div>

<div class="absolute inset-0 flex items-center justify-center px-16">

<div class="text-center max-w-4xl space-y-8">

<v-click>

<div style="color: rgba(245, 158, 11, 0.85); letter-spacing: 0.4em; text-transform: uppercase; font-size: 1rem; font-weight: 600;">
The Program
</div>

</v-click>

<v-click>

<div class="font-black" style="font-size: 6rem; line-height: 1; color: white; letter-spacing: -0.04em;">
The Cadence
</div>

</v-click>

<v-click>

<div class="font-black mt-4" style="font-size: 4rem; line-height: 1; color: #f59e0b; letter-spacing: -0.03em;">
$2,997
</div>

</v-click>

<v-click>

<div class="text-xl mt-4" style="color: rgba(255,255,255,0.7); line-height: 1.4;">
12-week implementation. Live weekly coaching. Compounding loops installed.
</div>

</v-click>

</div>

</div>

<!--
HOOK: Offer hero card.
DEMO NOTE: pattern 13 = offer reveal with gradient background + hero price.
TIMING: 25 sec
TRANSITION: Components.
-->

---
layout: default
---

<!-- slide:components-18 -->

<div class="h-full flex flex-col justify-center px-12 max-w-5xl mx-auto">

<div class="text-sm uppercase mb-3" style="letter-spacing: 0.3em; color: #f59e0b; font-weight: 700;">What you get</div>

<div class="font-black brand-primary mb-6" style="font-size: 2.25rem; line-height: 1.15; letter-spacing: -0.02em;">
12 weeks of implementation, not just teaching.
</div>

<div class="space-y-3 text-lg text-slate-700">

<v-click>

<div>· Weekly 1-on-1 coaching calls.</div>

</v-click>

<v-click>

<div>· The Cadence Operating Manual (PDF + Notion).</div>

</v-click>

<v-click>

<div>· 4-Loop installation in your existing tools.</div>

</v-click>

<v-click>

<div>· Async Slack support with your dedicated coach.</div>

</v-click>

<v-click>

<div>· 90-day energy + output baseline tracking.</div>

</v-click>

<v-click>

<div class="p-4 rounded-lg mt-6" style="background: rgba(245, 158, 11, 0.12); border-left: 4px solid #f59e0b;">
  <div class="text-xl font-black brand-primary">$2,997 paid in full</div>
</div>

</v-click>

</div>

</div>

<!--
HOOK: Components walk.
DEMO NOTE: pattern 14 = components list with price callout box.
TIMING: 45 sec
TRANSITION: Price reveal.
-->

---
layout: center
class: text-center
---

<!-- slide:guarantee-19 -->

<div class="space-y-10">

<v-click>

<div class="text-base uppercase text-slate-500" style="letter-spacing: 0.35em; font-weight: 600;">
The guarantee
</div>

</v-click>

<v-click>

<div class="font-black brand-primary max-w-3xl mx-auto" style="font-size: 3rem; line-height: 1.15; letter-spacing: -0.02em;">
If you complete the 12 weeks
</div>

</v-click>

<v-click>

<div class="font-black brand-secondary max-w-3xl mx-auto" style="font-size: 3.5rem; line-height: 1.1; letter-spacing: -0.03em;">
and don't ship 2x more in 90 days,
</div>

</v-click>

<v-click>

<div class="text-2xl font-bold brand-primary mt-4" style="line-height: 1.3;">
We refund every dollar. No questions.
</div>

</v-click>

</div>

<!--
HOOK: Risk reversal.
DEMO NOTE: pattern 15 = guarantee statement with three-beat build.
TIMING: 25 sec
TRANSITION: Two-paths close.
-->

---
layout: default
---

<!-- slide:close-paths-20 -->

<div class="h-full flex flex-col justify-center px-12 max-w-5xl mx-auto">

<div class="text-sm uppercase mb-3" style="letter-spacing: 0.3em; color: #dc2626; font-weight: 700;">Path One</div>

<div class="font-black brand-primary mb-6" style="font-size: 3rem; line-height: 1.1; letter-spacing: -0.03em;">
Keep grinding.
</div>

<v-click>

<div class="text-xl text-slate-700 max-w-3xl mb-10" style="line-height: 1.5;">
Hope the next sprint fixes it. Push harder. Burn brighter. Crash sooner.
</div>

</v-click>

<v-click>

<div class="text-sm uppercase mb-3" style="letter-spacing: 0.3em; color: #f59e0b; font-weight: 700;">Path Two</div>

</v-click>

<v-click>

<div class="font-black brand-primary mb-6" style="font-size: 3rem; line-height: 1.1; letter-spacing: -0.03em;">
Install the cadence.
</div>

</v-click>

<v-click>

<div class="text-2xl font-bold brand-secondary" style="line-height: 1.3;">
12 weeks. Same hours. Double the output.
</div>

</v-click>

</div>

<!--
HOOK: Binary close.
DEMO NOTE: pattern 16 = two-paths close in single-slide layout.
TIMING: 35 sec
TRANSITION: Final CTA.
-->

---
layout: end
class: text-center
---

<!-- slide:final-cta-21 -->

<div class="absolute inset-0" style="background: radial-gradient(ellipse at center, #3b82f6 0%, #2563eb 50%, #1e3a8a 100%);"></div>

<div class="absolute inset-0 flex items-center justify-center px-16">

<div class="text-center max-w-4xl space-y-10">

<v-click>

<div style="color: rgba(245, 158, 11, 0.85); letter-spacing: 0.4em; text-transform: uppercase; font-size: 1rem; font-weight: 600;">
Your next step
</div>

</v-click>

<v-click>

<div class="font-black" style="font-size: 6rem; line-height: 1; color: white; letter-spacing: -0.04em;">
Book your
</div>

</v-click>

<v-click>

<div class="font-black" style="font-size: 6rem; line-height: 1; color: #f59e0b; letter-spacing: -0.04em;">
strategy call.
</div>

</v-click>

<v-click>

<div class="text-2xl mt-8 max-w-3xl mx-auto" style="color: rgba(255,255,255,0.85); line-height: 1.4;">
demo-link.com/book
</div>

</v-click>

</div>

</div>

<!--
HOOK: Final CTA with layout: end.
DEMO NOTE: pattern 17 = final CTA on gradient background. Same as SupportED close slide 138.
TIMING: 15 sec
TRANSITION: End of demo deck.
-->

---
layout: center
class: text-center
---

<!-- slide:demo-howto-22 -->

<div class="space-y-8">

<div class="text-base uppercase text-slate-500" style="letter-spacing: 0.35em; font-weight: 600;">
This is the end of the demo deck
</div>

<div class="font-black brand-primary" style="font-size: 3rem; line-height: 1.15; letter-spacing: -0.02em;">
Now show your reviewer how to give feedback.
</div>

<div class="space-y-3 text-lg text-slate-700 max-w-3xl mx-auto text-left mt-6">

<div>· Open Loom or QuickTime and start recording your screen + voice.</div>
<div>· Open presenter mode at the URL with <code>/presenter/1</code>.</div>
<div>· Click through the deck end-to-end.</div>
<div>· When you hit a slide that needs a change, talk it back:</div>

<div class="p-4 rounded-lg italic" style="background: rgba(37, 99, 235, 0.05); border-left: 4px solid #2563eb;">
"I'm on slide 7. The line under FALSE is too long. Cut it to: 'Output is not the problem. Cadence is.'"
</div>

<div>· Slide number + the specific change you want. That's all.</div>

</div>

</div>

<!--
HOOK: Final how-to slide. This is the teaching layer for the demo Loom.
TIMING: 60 sec
TRANSITION: End of demo.
-->
