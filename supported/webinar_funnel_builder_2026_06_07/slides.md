---
theme: default
title: Webinar Funnel Builder · SupportED
info: |
  Internal team memo. How the Roadmap + Workshop funnel works, the framing, and the assets available.
  SupportED / AcceptED · June 2026.
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: dark
drawings:
  persist: false
transition: fade
mdc: true
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '300,400,500,600,700'
layout: cover
---

<!-- slide:cover-01 -->

<div class="absolute inset-0 flex flex-col justify-center px-20">
<div class="max-w-4xl">

<span class="wfb-eyebrow gold">SupportED / AcceptED · internal team memo</span>

<h1 style="font-size: 3.5rem;">The Roadmap + Workshop Funnel</h1>

<p class="wfb-mute" style="font-size: 1.35rem; margin-top: 1.4rem; max-width: 42rem;">
How leads flow from ad to enrollment, the framing per entry, and the assets you already have to run it.
</p>

<p v-click class="wfb-teal" style="margin-top: 1.6rem; font-size: 1.05rem;">
Two entry paths. One destination. The live workshop.
</p>

</div>
</div>

<div class="wfb-footer">Webinar Funnel Builder · v1 · June 2026</div>

---
layout: center
---

<!-- slide:big-idea-02 -->

<span class="wfb-eyebrow teal">the big idea</span>

<h2 style="font-size: 2.3rem; margin-bottom: 2.2rem;">Three steps. Each one earns the next.</h2>

<div class="wfb-grid wfb-g3" style="max-width: 64rem; margin: 0 auto;">
<div class="wfb-card blue" v-click>
<h3>1 · The Roadmap</h3>
<p>The value hook. A free, personalized diagnostic that pulls them in and tells us who is serious.</p>
</div>
<div class="wfb-card" v-click>
<h3>2 · The Workshop</h3>
<p>The indoctrination engine. We pop misconceptions, aha-stack, and build trust live.</p>
</div>
<div class="wfb-card gold" v-click>
<h3>3 · The Call</h3>
<p>The close. Diagnose live, then present AcceptED, the Complete Pathway.</p>
</div>
</div>

<p v-click class="wfb-mute" style="margin-top: 2rem; font-size: 1.05rem;">
Every ad sells the <span class="wfb-teal">next step</span>, never the program.
</p>

---
layout: center
class: text-center
---

<!-- slide:flowchart-03 -->

<span class="wfb-eyebrow gold">how it works · the full flow</span>

```mermaid {theme: 'dark', scale: 0.62}
flowchart LR
  classDef road fill:#10243f,stroke:#5aa6f0,color:#eef3fa,rx:8,ry:8
  classDef web fill:#0f2b29,stroke:#38b6a6,color:#eef3fa,rx:8,ry:8
  classDef conv fill:#2a2310,stroke:#d6a94a,color:#ffffff,rx:8,ry:8
  A1[Ads]:::road --> A2[Free Roadmap]:::road
  A2 --> A3[Book a Call]:::road
  A2 --> A4[Auto-register]:::road
  B1[Ads]:::web --> B2[Register]:::web --> B3["Get Roadmap<br/>free + $27 VIP"]:::web --> B4["Confirm<br/>+ show-up"]:::web
  A4 --> W[Live Workshop]:::conv
  B4 --> W
  A3 --> C[Strategy Call]:::conv
  W --> C
  C --> E[AcceptED]:::conv
```

<div class="wfb-grid wfb-g3" style="max-width: 60rem; margin: 1.4rem auto 0;">
<div v-click><span class="wfb-pill blue">Path A</span> <span class="wfb-mute" style="font-size:0.85rem;"> roadmap-first</span></div>
<div v-click><span class="wfb-pill">Path B</span> <span class="wfb-mute" style="font-size:0.85rem;"> workshop-first</span></div>
<div v-click><span class="wfb-pill gold">Both converge</span> <span class="wfb-mute" style="font-size:0.85rem;"> at the workshop</span></div>
</div>

---
layout: center
---

<!-- slide:path-a-04 -->

<span class="wfb-eyebrow blue">Path A · Roadmap-first</span>

<h2 style="font-size: 2rem; margin-bottom: 1.8rem;">They come for the roadmap. We auto-register them for the workshop.</h2>

<div style="max-width: 56rem; margin: 0 auto; text-align: left;">
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">1</span><div><b>Ad</b> sells the free roadmap. The roadmap is the hook.</div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">2</span><div><b>Free Roadmap</b> opt-in. Personalized diagnostic delivered. <span class="wfb-pill">"normally $47, free now"</span></div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">3</span><div>They <b>book a strategy call</b> AND get <b class="wfb-teal">auto-registered for the workshop</b> to indoctrinate further.</div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">4</span><div><b>Attend the workshop</b> → strategy call → AcceptED.</div>
</div>
</div>

---
layout: center
---

<!-- slide:path-b-05 -->

<span class="wfb-eyebrow teal">Path B · Workshop-first &nbsp;(the assumptive one)</span>

<h2 style="font-size: 2rem; margin-bottom: 1.8rem;">They register for the workshop. The roadmap is the second commitment on the way in.</h2>

<div style="max-width: 56rem; margin: 0 auto; text-align: left;">
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">1</span><div><b>Ad</b> sells the Roadmap Workshop.</div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">2</span><div><b>Register</b> for the workshop (the opt-in).</div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">3</span><div>Next page: <b>get your custom roadmap</b> — free, with an optional <b class="wfb-gold">$27 VIP bump</b>. A second commitment.</div>
</div>
<div style="display:flex; align-items:center; gap:1rem; margin:0.9rem 0;" v-click>
<span class="wfb-step">4</span><div><b>Confirmation</b> (confetti + show-up incentive) → workshop → call → AcceptED.</div>
</div>
</div>

---
layout: center
---

<!-- slide:framing-06 -->

<span class="wfb-eyebrow gold">the framing · meet them where they entered</span>

<h2 style="font-size: 2rem; margin-bottom: 1.8rem;">Same destination, different angle of approach.</h2>

<div class="wfb-grid wfb-g2" style="max-width: 60rem; margin: 0 auto;">
<div class="wfb-card blue" v-click>
<h3>Roadmap-first</h3>
<p>They already raised their hand for value. Framing: <span class="wfb-mute">"you got the roadmap, now come see exactly how to use it live."</span> Warm, value-continuation.</p>
</div>
<div class="wfb-card" v-click>
<h3>Workshop-first</h3>
<p>They committed to a live event. Framing: <span class="wfb-mute">"before the workshop, lock in your custom roadmap so you get the most out of it."</span> Assumptive, prep-driven.</p>
</div>
</div>

<p v-click class="wfb-mute" style="margin-top: 1.8rem;">
One <span class="wfb-teal">indoctrination + reminder sequence</span> (email + SMS) runs across both, adapting the opening line to where they came from.
</p>

---
layout: center
---

<!-- slide:positioning-07 -->

<span class="wfb-eyebrow teal">why people say yes · the positioning</span>

<h2 style="font-size: 2rem; margin-bottom: 1.8rem;">Three pillars. This is what makes us different.</h2>

<div class="wfb-grid wfb-g3" style="max-width: 64rem; margin: 0 auto;">
<div class="wfb-card" v-click>
<h3>Academic company first</h3>
<p>We do AP / SAT / ACT tutoring <b>in house</b>. Most advisors only touch essays and activities, then send you elsewhere.</p>
</div>
<div class="wfb-card gold" v-click>
<h3>The Complete Pathway + Ivy</h3>
<p>Coaching + AP + tutoring <b>under one roof</b>. Empowerly, Crimson, Zenith charge ~$30k to advise only. We do the whole thing.</p>
</div>
<div class="wfb-card blue" v-click>
<h3>Transparent pricing</h3>
<p><b>$3,800&ndash;$9,997 shown upfront.</b> "I hate that nobody gives you a range." Leads stop bouncing on a hidden number.</p>
</div>
</div>

---
layout: center
---

<!-- slide:assets-08 -->

<span class="wfb-eyebrow gold">assets available · what you already have</span>

<h2 style="font-size: 2rem; margin-bottom: 1.6rem;">Most of this is built. Here is the inventory.</h2>

<div class="wfb-grid wfb-g2" style="max-width: 64rem; margin: 0 auto; text-align: left;">
<div class="wfb-card blue" v-click>
<h3>Creative + copy</h3>
<ul style="margin:0; padding:0;">
<li class="wfb-li">Roadmap ads <b>recording runbook</b> (in Drive, ready for Joe)</li>
<li class="wfb-li">New college ads + new AP ads (recorded, clean audio)</li>
<li class="wfb-li">Copy-brain RAG: winning hooks, openers, bodies</li>
</ul>
</div>
<div class="wfb-card" v-click>
<h3>Funnel + automation</h3>
<ul style="margin:0; padding:0;">
<li class="wfb-li">Live roadmap quiz + college application funnels</li>
<li class="wfb-li">Roadmap auto-generation (GHL automation)</li>
<li class="wfb-li">Auto-register + indoctrination nurture (proven template)</li>
</ul>
</div>
</div>

---
layout: center
---

<!-- slide:assets-09 -->

<span class="wfb-eyebrow gold">assets available · tracking + the workshop</span>

<div class="wfb-grid wfb-g2" style="max-width: 64rem; margin: 1rem auto 0; text-align: left;">
<div class="wfb-card green" v-click>
<h3>Tracking</h3>
<ul style="margin:0; padding:0;">
<li class="wfb-li">Meta pixel + CAPI live (optimize for <b>Lead</b>)</li>
<li class="wfb-li">AP lead notifications fixed and firing</li>
<li class="wfb-li">Per-funnel spend, leads, and CPL visible</li>
</ul>
</div>
<div class="wfb-card gold" v-click>
<h3>The workshop</h3>
<ul style="margin:0; padding:0;">
<li class="wfb-li">"College Acceptance Roadmap Workshop" (working name)</li>
<li class="wfb-li">Short VSL for indoctrination (modeled on the proven one)</li>
<li class="wfb-li">Slidev deck, Fladlien-standardized, built from the script</li>
</ul>
</div>
</div>

<p v-click class="wfb-mute" style="margin-top: 1.6rem; font-size: 0.95rem;">
Gaps we are closing: the GHL email load, the registration → CAPI event, and the final workshop script.
</p>

---
layout: center
---

<!-- slide:roles-10 -->

<span class="wfb-eyebrow teal">who owns what</span>

<h2 style="font-size: 2rem; margin-bottom: 1.8rem;">Clear lanes, no overlap.</h2>

<div class="wfb-grid wfb-g2" style="max-width: 62rem; margin: 0 auto; text-align: left;">
<div class="wfb-card blue" v-click>
<h3>Marketing + Ops</h3>
<p>Ads live and tracked. Pages built simple. GHL automation, auto-register, nurture, CAPI.</p>
</div>
<div class="wfb-card gold" v-click>
<h3>Joe</h3>
<p>Record ads clean (QC before sending). Run the live workshop and crush it.</p>
</div>
<div class="wfb-card" v-click>
<h3>Sales</h3>
<p>Work registrants + roadmap leads. Run the strategy calls. Close AcceptED.</p>
</div>
<div class="wfb-card green" v-click>
<h3>Everyone</h3>
<p>Keep the funnel congruent. One message, ad to call. The roadmap is always the hook.</p>
</div>
</div>

---
layout: center
class: text-center
---

<!-- slide:close-11 -->

<span class="wfb-eyebrow gold">the standard</span>

<h2 style="font-size: 2.4rem; max-width: 50rem; margin: 0 auto 1.6rem;">
The roadmap pulls them in. The workshop earns the trust. The call closes.
</h2>

<p v-click class="wfb-mute" style="font-size: 1.1rem; max-width: 44rem; margin: 0 auto;">
Keep the pages simple, the copy sharp, and the next step obvious. We test one thing at a time and scale what wins.
</p>

<div class="wfb-footer">SupportED / AcceptED · Webinar Funnel Builder · build #1</div>
