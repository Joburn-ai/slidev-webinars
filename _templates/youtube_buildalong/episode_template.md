---
theme: default
title: Episode NN · [Title]
info: |
  Joburn Build-Along · Episode NN
  Format: 6-slot recurring template (Hook · Topic · Build 1 · Whiteboard · Build 2 · Recap).
  Drawing primary: drauu (press the toolbar pen icon). Big whiteboard moments: switch OBS to iPad scene.
class: text-center
highlighter: shiki
lineNumbers: false
colorSchema: light
drawings:
  persist: true
  syncAll: false
transition: slide-left
mdc: true
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<!-- ============================================================
     SLOT 1 / 6 · COLD-OPEN HOOK
     Time: 5-10s. Promise + curiosity gap.
     Voice: confident, slightly contrarian, no "hey guys welcome back."
     ============================================================ -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow">Joburn · Build-Along · EP NN</div>

<h1 style="font-size: 4.5rem; color: white; line-height: 1;">
[The hook headline]<br/>
<span class="ff-orange">[in &lt;30 minutes].</span>
</h1>

<p style="font-size: 1.4rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 50rem; margin-left:auto; margin-right:auto;">
[One sentence promise. What they will have when this video ends.]
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOBURN · JOHN COBURN
</div>

</div>

<!--
HOOK NOTES (presenter):
- 5-10s on this slide. Don't define yet. Lean into curiosity.
- Read the headline. Read the sub. Beat. Click forward.
- Camera scene: SLIDES + CAM CORNER. Loud-and-confident pose.
-->

---

<!-- ============================================================
     SLOT 2 / 6 · TOPIC CARD
     What they'll have at the end. Set expectation.
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-16 py-12">

<div class="ff-bar"></div>

<div class="section-tag">EPISODE NN</div>

<h1 style="font-size: 3.5rem; margin-top: 1rem;">[Episode title].</h1>

<div class="rule-thin"></div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>
<div class="section-tag navy">WHAT YOU&apos;LL BUILD</div>
<ul style="margin-top: 1rem; font-size: 1.15rem;">
<li>[Concrete artifact 1]</li>
<li>[Concrete artifact 2]</li>
<li>[Concrete artifact 3]</li>
</ul>
</div>

<div>
<div class="section-tag gold">PREREQS</div>
<ul style="margin-top: 1rem; font-size: 1.15rem;">
<li>[Tool / version]</li>
<li>[Tool / version]</li>
<li>[Account / key (free tier OK)]</li>
</ul>
</div>

</div>

<div class="absolute bottom-8 left-16 fig-caption">FIG. 1 · EPISODE OVERVIEW</div>

</div>

<!--
TOPIC NOTES:
- 20-30s. Walk left column then right.
- Camera scene: SLIDES + LARGE CAM (talking head moment).
- Don't oversell. State the artifact in operator terms.
-->

---

<!-- ============================================================
     SLOT 3 / 6 · BUILD PHASE 1 (Steps 1-3 of N)
     Code-along. Monaco editor live. Magic Move for state transitions.
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-12 py-10">

<div class="ff-bar"></div>

<div class="flex items-center gap-4 mb-2">
<div class="section-tag">PHASE 01</div>
<span class="step-counter"><span class="num">STEP 01</span> · [step name]</span>
</div>

<h2 style="font-size: 2.4rem; margin-top: 0.5rem;">[What we&apos;re doing in this phase].</h2>

<div class="rule-thin"></div>

<div class="code-frame mt-4">
<div class="frame-label">// LIVE EDIT · type along</div>

```ts {monaco}
// [Live editable code block. Replace this with the actual code
//  the viewer will type. Monaco gives full editing, TS types,
//  syntax highlighting. Keep this block small enough to read at
//  1080p: ~12-18 lines max.]
function diagnose(data: WeeklyMetrics): Diagnostic {
  return {
    seen: data.summarize(),
    means: data.interpret(),
    nextLever: pickPriorityLever(data),
  }
}
```

</div>

</div>

<!--
BUILD 1 NOTES:
- 4-7 min. Talk as you type. Each function = a beat.
- Use Shiki Magic Move for code state transitions when worth it.
- Camera scene: SLIDES + CAM CORNER (lean in, low energy talking head).
- If you mistype, leave it. Edit later in Descript.
-->

---

<!-- ============================================================
     SLOT 4 / 6 · WHITEBOARD BREAK
     Zoom out from code. Diagram the concept.
     Default: drauu annotation on this slide.
     Big moment: OBS scene switch to iPad whiteboard.
     ============================================================ -->

<div class="absolute inset-0 px-16 py-12" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="section-tag gold">FIG. 2 · WHY THIS WORKS</div>

<h2 style="font-size: 2.6rem; margin-top: 1rem;">Why are we doing it <span class="ff-cyan">this way</span>?</h2>

<div class="rule-thin"></div>

<div class="whiteboard-scene mt-8" style="min-height: 320px;">
[ DRAW ON THIS SLIDE WITH DRAUU<br/><br/>
OR SWITCH OBS TO IPAD SCENE FOR FULL WHITEBOARD ]
</div>

<div class="fig-caption mt-4">PRESENTER: PRESS PEN ICON OR HOTKEY OBS SCENE 3</div>

</div>

<!--
WHITEBOARD NOTES:
- 2-4 min. Step away from the code mentally.
- If drauu: enable pen, annotate on this slide. Diagram the concept.
- If iPad: hotkey OBS scene 3 (iPad fullscreen + cam corner). Draw freely.
- Decision rule: drauu for arrows/circles on existing diagram. iPad for from-scratch ideation.
- Return to slide deck when done.
-->

---

<!-- ============================================================
     SLOT 5 / 6 · BUILD PHASE 2 (Steps 4-N)
     Back to code. Apply what the whiteboard explained.
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-12 py-10">

<div class="ff-bar"></div>

<div class="flex items-center gap-4 mb-2">
<div class="section-tag">PHASE 02</div>
<span class="step-counter"><span class="num">STEP 04</span> · [step name]</span>
</div>

<h2 style="font-size: 2.4rem; margin-top: 0.5rem;">[Applying what we just diagrammed].</h2>

<div class="rule-thin"></div>

<div class="code-frame mt-4">
<div class="frame-label">// MAGIC MOVE · watch this evolve</div>

````md magic-move
```ts
// State 1: naive
const result = data.map(d => d.value)
```

```ts
// State 2: filtered
const result = data
  .filter(d => d.weekOf === thisWeek)
  .map(d => d.value)
```

```ts
// State 3: with the lever applied
const result = data
  .filter(d => d.weekOf === thisWeek)
  .map(d => applyLever(d))
  .reduce(intoDiagnostic, BLANK)
```
````

</div>

</div>

<!--
BUILD 2 NOTES:
- 5-8 min. Connect back to the whiteboard concept.
- Magic Move shines here. Each click = one logical transformation.
- Camera scene: SLIDES + CAM CORNER.
-->

---

<!-- ============================================================
     SLOT 6 / 6 · RECAP + CTA
     What they built. One pin. Next episode tease.
     ============================================================ -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center px-16 py-12">

<div class="ff-bar"></div>

<div class="ff-eyebrow" style="color: rgba(255,255,255,0.65);">RECAP · EPISODE NN</div>

<h1 style="font-size: 3.5rem; color: white;">You just built <span class="ff-orange">[the artifact]</span>.</h1>

<div style="height: 1px; background: rgba(255,255,255,0.2); margin: 1.5rem 0 2rem;"></div>

<div class="grid grid-cols-2 gap-12">

<div>
<div class="section-tag gold" style="background: rgba(212,184,90,0.1);">WHAT YOU NOW HAVE</div>
<ul style="margin-top: 1rem; color: rgba(255,255,255,0.92); font-size: 1.15rem;">
<li>[Artifact 1 in operator terms]</li>
<li>[Artifact 2]</li>
<li>[Artifact 3]</li>
</ul>
</div>

<div>
<div class="cta-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.3); color: white;">
<div class="section-tag gold" style="margin-bottom: 0.75rem;">NEXT EPISODE</div>
<p style="font-size: 1.25rem; color: white; margin: 0;">[Tease the next build]</p>
<p style="font-size: 0.9rem; color: rgba(255,255,255,0.65); margin-top: 0.75rem;">Subscribe so you don&apos;t miss it.</p>
</div>
</div>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOBURN.COM · BUILD-ALONG SERIES
</div>

</div>

<!--
RECAP NOTES:
- 30-45s. Camera scene: CAM ONLY (close eye contact, sign-off energy).
- Read "you just built [artifact]". Beat. Read the three bullets.
- Read the next-episode tease. One CTA: subscribe. Nothing else.
- Stop recording AFTER you've been still for 2 full seconds (Descript needs the room).
-->
