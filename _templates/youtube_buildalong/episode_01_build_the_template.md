---
theme: default
title: Episode 01 · Build a Slidev YouTube Template in 30 Minutes
info: |
  Joburn Build-Along · Episode 01
  Meta-episode: we build the very template this series uses, on camera, with the template.
  Format: 6 slots (Hook · Topic · Build 1 · Whiteboard · Build 2 · Recap).
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
     SLOT 1 / 6 · HOOK
     ============================================================ -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center items-center px-12">

<div class="ff-bar"></div>

<div class="max-w-5xl text-center">

<div class="ff-eyebrow">Joburn · Build-Along · EP 01</div>

<h1 style="font-size: 4.5rem; color: white; line-height: 1;">
The template that builds<br/>
<span class="ff-orange">an entire YouTube series.</span>
</h1>

<p style="font-size: 1.4rem; color: rgba(255,255,255,0.85); margin-top: 1.5rem; max-width: 50rem; margin-left:auto; margin-right:auto;">
In the next 30 minutes, I&apos;m going to build the Slidev template that produces this exact video. And every video after it. We&apos;re filming with it. While we build it.
</p>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOBURN · JOHN COBURN
</div>

</div>

<!--
HOOK SCRIPT:
"The template that builds an entire YouTube series. In the next 30 minutes
I'm going to build the Slidev template that produces this exact video.
And every video after it. We're filming with it. While we build it."

5-10 seconds. Confident pace. Don't smile. The headline carries the energy.
Camera: SLIDES + CAM CORNER.
-->

---

<!-- ============================================================
     SLOT 2 / 6 · TOPIC
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-16 py-12">

<div class="ff-bar"></div>

<div class="section-tag">EPISODE 01</div>

<h1 style="font-size: 3.5rem; margin-top: 1rem;">Build the build-along template.</h1>

<div class="rule-thin"></div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>
<div class="section-tag navy">WHAT YOU&apos;LL HAVE</div>
<ul style="margin-top: 1rem; font-size: 1.15rem;">
<li>A 6-slot Slidev deck template</li>
<li>5 reusable Vue layouts (Hook / Topic / BuildPhase / Whiteboard / Recap)</li>
<li>An OBS scene config doc that pairs with the deck</li>
<li>A drawing-surface policy you stop relitigating</li>
</ul>
</div>

<div>
<div class="section-tag gold">PREREQS</div>
<ul style="margin-top: 1rem; font-size: 1.15rem;">
<li>Node 20+</li>
<li>Slidev (<code>npx slidev</code>)</li>
<li>OBS Studio installed</li>
<li>A pen-capable input (mouse, trackpad, or stylus)</li>
</ul>
</div>

</div>

<div class="absolute bottom-8 left-16 fig-caption">FIG. 1 · EPISODE 01 OVERVIEW</div>

</div>

<!--
TOPIC SCRIPT:
"Episode 01: build the build-along template. By the end, you have a 6-slot
Slidev deck, five reusable Vue layouts, an OBS scene config that pairs with
the deck, and a drawing-surface policy you stop relitigating. Prereqs are
trivial. Node, Slidev, OBS, anything that draws."

20-30s. Walk left then right column. Camera: SLIDES + LARGE CAM.
-->

---

<!-- ============================================================
     SLOT 3 / 6 · BUILD PHASE 1 · The 6-slot structure
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-12 py-10">

<div class="ff-bar"></div>

<div class="flex items-center gap-4 mb-2">
<div class="section-tag">PHASE 01</div>
<span class="step-counter"><span class="num">STEP 01</span> · scaffold the deck</span>
</div>

<h2 style="font-size: 2.4rem; margin-top: 0.5rem;">Six slots. Each one has one job.</h2>

<div class="rule-thin"></div>

<div class="code-frame mt-4">
<div class="frame-label">// slides.md · the spine</div>

```md {monaco}
---
theme: default
title: Episode NN · [title]
drawings: { persist: true }
mdc: true
---

# Slot 1 · Hook            (5-10s · curiosity gap)
---
# Slot 2 · Topic           (20-30s · what they'll have)
---
# Slot 3 · Build Phase 1   (4-7min · code-along, steps 1-3)
---
# Slot 4 · Whiteboard      (2-4min · drauu OR iPad scene)
---
# Slot 5 · Build Phase 2   (5-8min · code-along, steps 4-N)
---
# Slot 6 · Recap + CTA     (30-45s · 3 bullets + next ep tease)
```

</div>

</div>

<!--
BUILD 1 SCRIPT:
"Six slots. Each one has one job. The hook owns 5-10 seconds and creates
a curiosity gap. The topic card shows what they'll have at the end. Build
phase 1 covers steps 1-3 of whatever we're making, 4-7 minutes. Whiteboard
break, 2-4 minutes, where we step away from code. Build phase 2, steps 4-N,
5-8 minutes. Recap, 30-45 seconds. Three bullets and one CTA: subscribe.
That's it. That's the entire format."

Type each comment block live as you talk. Don't pre-fill.
Camera: SLIDES + CAM CORNER.
-->

---

<!-- ============================================================
     SLOT 4 / 6 · WHITEBOARD · Why these 6 slots
     ============================================================ -->

<div class="absolute inset-0 px-16 py-12" style="background: var(--ff-warm);">

<div class="ff-bar"></div>

<div class="section-tag gold">FIG. 2 · WHY SIX SLOTS</div>

<h2 style="font-size: 2.6rem; margin-top: 1rem;">Six is the <span class="ff-cyan">attention budget</span>.</h2>

<div class="rule-thin"></div>

<div class="whiteboard-scene mt-8" style="min-height: 320px;">
[ DRAW THE ATTENTION CURVE WITH DRAUU ·<br/><br/>
HOOK SPIKES · TOPIC PRIMES · BUILD 1 DEPTH · WHITEBOARD RESETS · BUILD 2 PEAKS · RECAP CLOSES ]
</div>

<div class="fig-caption mt-4">PRESS THE PEN ICON · DRAW THE CURVE LIVE</div>

</div>

<!--
WHITEBOARD SCRIPT:
"Six is the attention budget. Not five, not seven. Five and the recap eats
half the runtime. Seven and you lose them at slot 5. Six gives you one
hook, two real teaching beats, one cognitive break in the middle, and a
clean close. Let me draw the attention curve."

Press the pen icon. Draw a sine-wave-ish curve, label peaks (hook, build 1
end, build 2 climax) and valley (whiteboard break = intentional reset).

2-4 min. The drawing IS the teach. Don't rush it.
Camera: SLIDES + CAM CORNER (or scene 3 if iPad).
-->

---

<!-- ============================================================
     SLOT 5 / 6 · BUILD PHASE 2 · Layouts + OBS config
     ============================================================ -->

<div class="grid-paper absolute inset-0 px-12 py-10">

<div class="ff-bar"></div>

<div class="flex items-center gap-4 mb-2">
<div class="section-tag">PHASE 02</div>
<span class="step-counter"><span class="num">STEP 04</span> · layouts + scenes</span>
</div>

<h2 style="font-size: 2.4rem; margin-top: 0.5rem;">Each slot becomes a Vue layout. Each layout pairs with an OBS scene.</h2>

<div class="rule-thin"></div>

<div class="code-frame mt-4">
<div class="frame-label">// obs-scene-policy.md · what camera, when</div>

````md magic-move
```md
// Slot 1 · Hook       → Scene A (slides + cam corner)
// Slot 2 · Topic      → Scene B (slides + large cam)
// Slot 3 · Build 1    → Scene A
// Slot 4 · Whiteboard → Scene C (iPad fullscreen)  OR drauu in place
// Slot 5 · Build 2    → Scene A
// Slot 6 · Recap      → Scene D (cam only)
```

```md
// HOTKEYS (OBS Studio · Settings · Hotkeys)
// Scene A · Cmd+1   (default; lean back to it between slots)
// Scene B · Cmd+2   (only for slot 2; talking-head expectation-set)
// Scene C · Cmd+3   (only when whiteboard is the work)
// Scene D · Cmd+4   (only for slot 6; sign-off intimacy)
```

```md
// DRAWING POLICY (do not relitigate per episode)
// Quick annotation on existing diagram        → drauu in slide
// Persistent diagram (saves between recordings)→ slidev-addon-tldraw
// From-scratch ideation, sustained whiteboard → iPad + Sidecar + tldraw web
// Default for Joburn build-along: drauu in slot 4. iPad only on demand.
```
````

</div>

</div>

<!--
BUILD 2 SCRIPT:
"Each slot becomes a Vue layout in the layouts folder. Each layout pairs
with one OBS scene. I'm going to show you the scene-to-slot map, the OBS
hotkeys you bind once and never touch again, and the drawing-surface
policy that means you stop wasting brain cycles on it mid-recording."

Click through the magic-move sequence. Each click reveals one block.
5-8 min. Take your time on the drawing policy block.
Camera: SLIDES + CAM CORNER.
-->

---

<!-- ============================================================
     SLOT 6 / 6 · RECAP
     ============================================================ -->

<div class="absolute inset-0 ff-navy-bg flex flex-col justify-center px-16 py-12">

<div class="ff-bar"></div>

<div class="ff-eyebrow" style="color: rgba(255,255,255,0.65);">RECAP · EPISODE 01</div>

<h1 style="font-size: 3.5rem; color: white;">You just built <span class="ff-orange">the format</span>.</h1>

<div style="height: 1px; background: rgba(255,255,255,0.2); margin: 1.5rem 0 2rem;"></div>

<div class="grid grid-cols-2 gap-12">

<div>
<div class="section-tag gold" style="background: rgba(212,184,90,0.1);">WHAT YOU NOW HAVE</div>
<ul style="margin-top: 1rem; color: rgba(255,255,255,0.92); font-size: 1.15rem;">
<li>A 6-slot Slidev deck you can refill in 90 minutes</li>
<li>Five Vue layouts you never rebuild</li>
<li>An OBS scene map with hotkeys</li>
<li>A drawing-surface policy that ends the debate</li>
</ul>
</div>

<div>
<div class="cta-card" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.3); color: white;">
<div class="section-tag gold" style="margin-bottom: 0.75rem;">NEXT EPISODE</div>
<p style="font-size: 1.25rem; color: white; margin: 0;">We use the template to build a Growth Starter diagnostic in 30 minutes.</p>
<p style="font-size: 0.9rem; color: rgba(255,255,255,0.65); margin-top: 0.75rem;">Subscribe so you don&apos;t miss it.</p>
</div>
</div>

</div>

<div class="absolute bottom-8 left-0 right-0 text-center" style="color: rgba(255,255,255,0.4); font-size: 0.7rem; letter-spacing: 0.25em; font-family: 'JetBrains Mono', monospace;">
JOBURN.COM · BUILD-ALONG SERIES
</div>

</div>

<!--
RECAP SCRIPT:
"You just built the format. You have a 6-slot Slidev deck you can refill
in 90 minutes. Five Vue layouts you never have to rebuild. An OBS scene
map with hotkeys. And a drawing-surface policy that ends the debate.
Next episode, we use the template to build a Growth Starter diagnostic
in 30 minutes. Subscribe so you don't miss it."

Camera: CAM ONLY (Scene D). Eye contact. Confident close. Hold the
final beat 2 full seconds before cutting.
-->
