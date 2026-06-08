---
theme: default
title: "Brandon × FF · The Path to Cohort 1"
info: |
  brandon launch — the simple critical path.
  not the finish line. the starting line.
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
  serif: 'Crimson Pro'
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
---

<style>
:root {
  --ff-bg: #0A0F1C;
  --ff-bg-elevated: #111827;
  --ff-bg-card: #0F172A;
  --ff-navy: #1E293B;
  --ff-cream: #F5F1E8;
  --ff-cyan: #22D3EE;
  --ff-cyan-dim: #0E7490;
  --ff-green: #10B981;
  --ff-green-dim: #047857;
  --ff-orange: #FB923C;
  --ff-orange-dim: #C2410C;
  --ff-amber: #FBBF24;
  --ff-gray-300: #CBD5E1;
  --ff-gray-400: #94A3B8;
  --ff-gray-500: #64748B;
  --ff-rule: #1F2937;
  --ff-text: #E2E8F0;
  --ff-text-mute: #94A3B8;
  --ff-text-dim: #64748B;
}

* { box-sizing: border-box; }

html, body, #app {
  background: var(--ff-bg) !important;
  color: var(--ff-text);
  font-family: 'Inter', -apple-system, sans-serif;
  font-feature-settings: 'ss01', 'ss02', 'cv11';
}

.slidev-layout {
  background: var(--ff-bg) !important;
  padding: 3.5rem 4.5rem;
  position: relative;
}

/* Subtle grid background pattern */
.slidev-layout::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(34, 211, 238, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(34, 211, 238, 0.025) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
  z-index: 0;
}

.slidev-layout > * { position: relative; z-index: 1; }

/* Typography */
h1 {
  font-family: 'Crimson Pro', Georgia, serif;
  font-weight: 700;
  color: var(--ff-cream);
  letter-spacing: -0.025em;
  line-height: 1.05;
}

h2, h3 {
  color: var(--ff-cream);
  font-weight: 600;
  letter-spacing: -0.01em;
}

/* Brand mark — top right corner */
.brand-mark {
  position: absolute;
  top: 1.75rem;
  right: 2rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  z-index: 10;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ff-text-mute);
  font-weight: 600;
}

.ff-mark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border: 1.5px solid var(--ff-cyan);
  border-radius: 50%;
  font-family: 'Crimson Pro', serif;
  font-weight: 700;
  font-size: 0.7rem;
  letter-spacing: 0.02em;
  color: var(--ff-cyan);
  background: linear-gradient(135deg, rgba(34, 211, 238, 0.08), rgba(34, 211, 238, 0.02));
}

.brand-mark .x {
  color: var(--ff-text-dim);
  font-weight: 400;
}

.brand-mark .ff {
  color: var(--ff-cyan);
}

.brand-mark .bw {
  color: var(--ff-cream);
}

/* Slide footer tag */
.footer-tag {
  position: absolute;
  bottom: 1.5rem;
  left: 2rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.65rem;
  color: var(--ff-text-dim);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 500;
  z-index: 10;
}

.footer-tag .dot {
  width: 4px;
  height: 4px;
  background: var(--ff-cyan);
  border-radius: 50%;
}

.slide-number {
  position: absolute;
  bottom: 1.5rem;
  right: 2rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  color: var(--ff-text-dim);
  letter-spacing: 0.1em;
  z-index: 10;
}

/* Eyebrow */
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 0.7rem;
  color: var(--ff-cyan);
  font-weight: 700;
  margin-bottom: 1.25rem;
}

.eyebrow::before {
  content: '';
  width: 24px;
  height: 1px;
  background: var(--ff-cyan);
  display: block;
}

/* Color utilities */
.cyan { color: var(--ff-cyan); }
.green { color: var(--ff-green); }
.orange { color: var(--ff-orange); }
.amber { color: var(--ff-amber); }
.cream { color: var(--ff-cream); }
.mute { color: var(--ff-text-mute); }
.dim { color: var(--ff-text-dim); }

/* Cards */
.card {
  background: var(--ff-bg-card);
  border: 1px solid var(--ff-rule);
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.card-cyan { border-left: 3px solid var(--ff-cyan); }
.card-orange { border-left: 3px solid var(--ff-orange); }
.card-green { border-left: 3px solid var(--ff-green); }
.card-amber { border-left: 3px solid var(--ff-amber); }

.kicker {
  font-size: 1.05rem;
  color: var(--ff-text-mute);
  line-height: 1.55;
}

/* Funnel diagram - custom */
.funnel-wrap {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.funnel-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.8rem;
  align-items: stretch;
  position: relative;
}

.funnel-stage {
  background: var(--ff-bg-card);
  border: 1px solid var(--ff-rule);
  border-radius: 0.6rem;
  padding: 0.85rem 0.85rem;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  min-height: 95px;
}

.funnel-stage .num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: var(--ff-text-dim);
  letter-spacing: 0.15em;
  font-weight: 600;
}

.funnel-stage .label {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--ff-cream);
  line-height: 1.2;
}

.funnel-stage .meta {
  font-size: 0.75rem;
  color: var(--ff-text-mute);
  line-height: 1.4;
  margin-top: auto;
}

.funnel-stage.built {
  border-left: 3px solid var(--ff-green);
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, var(--ff-bg-card) 60%);
}
.funnel-stage.built::after {
  content: '✓ built';
  position: absolute;
  top: 0.65rem;
  right: 0.65rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.55rem;
  color: var(--ff-green);
  letter-spacing: 0.1em;
  font-weight: 700;
  text-transform: uppercase;
}

.funnel-stage.tobuild {
  border-left: 3px solid var(--ff-orange);
  background: linear-gradient(135deg, rgba(251, 146, 60, 0.10) 0%, var(--ff-bg-card) 60%);
}
.funnel-stage.tobuild::after {
  content: '○ build';
  position: absolute;
  top: 0.65rem;
  right: 0.65rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.55rem;
  color: var(--ff-orange);
  letter-spacing: 0.1em;
  font-weight: 700;
  text-transform: uppercase;
}

.funnel-stage.live {
  border-left: 3px solid var(--ff-cyan);
  background: linear-gradient(135deg, rgba(34, 211, 238, 0.08) 0%, var(--ff-bg-card) 60%);
}
.funnel-stage.live::after {
  content: '◆ live';
  position: absolute;
  top: 0.65rem;
  right: 0.65rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.55rem;
  color: var(--ff-cyan);
  letter-spacing: 0.1em;
  font-weight: 700;
  text-transform: uppercase;
}

/* Arrows between stages */
.arrow-right::after {
  content: '→';
  position: absolute;
  right: -0.65rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ff-cyan);
  font-size: 1.1rem;
  font-weight: 300;
  z-index: 5;
}

.arrow-down-snake {
  position: relative;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding-right: 0.5rem;
  height: 1.5rem;
  margin: 0.25rem 0;
}

.arrow-down-snake::after {
  content: '↓';
  color: var(--ff-cyan);
  font-size: 1.2rem;
  font-weight: 300;
}

/* Stat */
.big-stat {
  font-family: 'Crimson Pro', serif;
  font-size: 4.5rem;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.02em;
}

/* DM script bubble */
.dm-bubble {
  background: var(--ff-bg-card);
  border-radius: 1.25rem;
  padding: 1rem 1.25rem;
  position: relative;
  max-width: 90%;
  font-size: 0.92rem;
  line-height: 1.55;
  margin-bottom: 0.75rem;
}

.dm-bubble.inbound {
  background: var(--ff-navy);
  color: var(--ff-text);
  margin-right: auto;
  border-bottom-left-radius: 0.25rem;
}

.dm-bubble.outbound {
  background: linear-gradient(135deg, var(--ff-cyan-dim), var(--ff-cyan));
  color: var(--ff-bg);
  margin-left: auto;
  border-bottom-right-radius: 0.25rem;
  font-weight: 500;
}

.dm-label {
  font-size: 0.65rem;
  color: var(--ff-text-dim);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  font-weight: 600;
  margin-bottom: 0.25rem;
  display: block;
}

/* Table */
table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 0.9rem;
  background: var(--ff-bg-card);
  border-radius: 0.6rem;
  overflow: hidden;
}

th {
  text-align: left;
  padding: 0.85rem 1.1rem;
  background: var(--ff-navy);
  color: var(--ff-cyan);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.7rem;
  font-weight: 700;
  border-bottom: 1px solid var(--ff-rule);
}

td {
  padding: 0.85rem 1.1rem;
  border-bottom: 1px solid var(--ff-rule);
  vertical-align: top;
  font-size: 0.92rem;
}

tr:last-child td { border-bottom: none; }

/* Legend chip */
.chip {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.25rem 0.7rem;
  border-radius: 999px;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: var(--ff-bg-card);
  border: 1px solid var(--ff-rule);
}

.chip-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

/* Highlighted callout */
.callout {
  background: linear-gradient(135deg, rgba(34, 211, 238, 0.08) 0%, rgba(16, 185, 129, 0.06) 100%);
  border: 1px solid var(--ff-rule);
  border-left: 3px solid var(--ff-cyan);
  border-radius: 0.6rem;
  padding: 1.25rem 1.5rem;
}

/* Numbered list */
.num-list { counter-reset: numlist; list-style: none; padding: 0; }
.num-list li {
  counter-increment: numlist;
  padding-left: 2.5rem;
  margin-bottom: 1rem;
  position: relative;
  line-height: 1.55;
}
.num-list li::before {
  content: counter(numlist, decimal-leading-zero);
  position: absolute;
  left: 0;
  top: 0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: var(--ff-cyan);
  font-weight: 700;
  letter-spacing: 0.05em;
}
</style>

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<div class="absolute inset-0 flex flex-col justify-center px-20">

<span class="eyebrow">Brandon launch · the path forward</span>

<h1 style="font-size: 5rem; line-height: 1.0; max-width: 30ch;">
This isn't the <span class="orange">finish line</span>.<br/>
It's the <span class="cyan">starting line</span>.
</h1>

<p class="kicker" style="margin-top: 2.5rem; max-width: 40rem; font-size: 1.35rem;">
Cohort 1 is the <span class="cream">first test</span>. Not the destination. We launch fast, learn what breaks, then move into ads + DM ads so the system runs.
</p>

<div style="margin-top: 3rem; display: flex; gap: 0.75rem; align-items: center;">
  <span class="chip"><span class="chip-dot" style="background: var(--ff-green);"></span>most of it is built</span>
  <span class="chip"><span class="chip-dot" style="background: var(--ff-orange);"></span>3 things left</span>
  <span class="chip"><span class="chip-dot" style="background: var(--ff-cyan);"></span>application form unlocks everything</span>
</div>

</div>

<div class="footer-tag"><span class="dot"></span>2026-06-08 · brandon × ff · the simple version</div>
<div class="slide-number">01 / 08</div>

<!--
Reframe: this isn't finish-line syndrome, it's start-line momentum.
Cohort 1 is one test. Then ads + DM ads + the back-end. That's the real game.
-->

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">The funnel · one diagram</span>

<h1 style="font-size: 2.4rem; margin-bottom: 1.5rem;">
The <span class="cyan">whole machine</span>, on one screen.
</h1>

<div class="funnel-wrap">

<div class="funnel-row">
  <div class="funnel-stage built arrow-right">
    <span class="num">01</span>
    <span class="label">Origin Story Sequence</span>
    <span class="meta">8 IG-story frames · in your voice · ready to post</span>
  </div>
  <div class="funnel-stage live arrow-right">
    <span class="num">02</span>
    <span class="label">DMs + Sticker Replies</span>
    <span class="meta">audience engages · you reply warm · we sort</span>
  </div>
  <div class="funnel-stage tobuild arrow-right">
    <span class="num">03</span>
    <span class="label">ManyChat Soft Bridge</span>
    <span class="meta">auto-reply · plant the waitlist invite</span>
  </div>
  <div class="funnel-stage tobuild">
    <span class="num">04</span>
    <span class="label">Application Form</span>
    <span class="meta">= the waitlist · deep diagnostic · this is the unlock</span>
  </div>
</div>

<div class="arrow-down-snake"></div>

<div class="funnel-row">
  <div class="funnel-stage tobuild arrow-right">
    <span class="num">05</span>
    <span class="label">Mini Sage VSL</span>
    <span class="meta">3-5 min · "here's how it works when you join"</span>
  </div>
  <div class="funnel-stage live arrow-right">
    <span class="num">06</span>
    <span class="label">Sales Call w/ Brandon</span>
    <span class="meta">already-warm · 30 min · pick the right 5</span>
  </div>
  <div class="funnel-stage built arrow-right">
    <span class="num">07</span>
    <span class="label">Cohort 1 · the TEST</span>
    <span class="meta">5 founder clients · 90 days · learn what works</span>
  </div>
  <div class="funnel-stage" style="border-left: 3px solid var(--ff-amber); background: linear-gradient(135deg, rgba(251, 191, 36, 0.06) 0%, var(--ff-bg-card) 60%);">
    <span class="num">08</span>
    <span class="label" style="color: var(--ff-amber);">Ads + DM Ads + Back-End</span>
    <span class="meta">the real game starts here</span>
  </div>
</div>

</div>

<p style="margin-top: 1.25rem; text-align: center; font-size: 0.85rem;">
<span class="chip"><span class="chip-dot" style="background: var(--ff-green);"></span>built</span>
<span class="chip" style="margin-left: 0.4rem;"><span class="chip-dot" style="background: var(--ff-cyan);"></span>live workflow</span>
<span class="chip" style="margin-left: 0.4rem;"><span class="chip-dot" style="background: var(--ff-orange);"></span>build this week</span>
<span class="chip" style="margin-left: 0.4rem;"><span class="chip-dot" style="background: var(--ff-amber);"></span>after cohort 1</span>
</p>

<div class="footer-tag"><span class="dot"></span>8 stages · 3 things to build · then we run</div>
<div class="slide-number">02 / 08</div>

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">The DM game · how the soft bridge works</span>

<h1 style="font-size: 2.2rem; margin-bottom: 1.5rem;">
Story reply <span class="cyan">→</span> ManyChat <span class="cyan">→</span> waitlist invite.<br/>
<span class="mute" style="font-size: 1.4rem; font-weight: 400;">Same conversation. Just smoother.</span>
</h1>

<div class="grid grid-cols-2 gap-8">

<div>
<h3 style="color: var(--ff-orange); margin-bottom: 1rem; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase;">The conversation arc</h3>

<div class="dm-bubble inbound">
<span class="dm-label">audience reply via story sticker</span>
"my biggest question is how to actually stay consistent with cutting when life is busy"
</div>

<div class="dm-bubble outbound">
<span class="dm-label" style="color: rgba(0,0,0,0.55);">manychat (or you) replies</span>
"hey thanks so much for replying. i'm literally getting hundreds of these and trying to take my time going through them.
<br/><br/>
quick one. would you be open to joining a waitlist? as i go through all this i'm building something behind the scenes to help on a deeper level. takes 3 min to fill out, asks about your current situation."
</div>

<div class="dm-bubble inbound">
"yeah send it"
</div>

<div class="dm-bubble outbound" style="background: linear-gradient(135deg, var(--ff-green-dim), var(--ff-green));">
<span class="dm-label" style="color: rgba(0,0,0,0.55);">manychat sends the form link</span>
"perfect. here's the link → [application form]
<br/><br/>
i'll be in touch within 24h once i review."
</div>
</div>

<div>
<h3 style="color: var(--ff-cyan); margin-bottom: 1rem; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase;">Why this works</h3>

<div class="callout" style="margin-bottom: 1rem;">
<strong class="cream">Soft bridge, not a pitch.</strong>
<p style="font-size: 0.9rem; margin-top: 0.5rem; color: var(--ff-text-mute);">
You're not selling. You're saying "I'm overwhelmed, want to go deeper?" That's a permission ask, not a sales push.
</p>
</div>

<div class="callout" style="margin-bottom: 1rem; border-left-color: var(--ff-orange);">
<strong class="cream">ManyChat saves your sanity.</strong>
<p style="font-size: 0.9rem; margin-top: 0.5rem; color: var(--ff-text-mute);">
You're already overloaded. ManyChat handles the first reply + sends the form link. You only enter the convo when someone replies back warm.
</p>
</div>

<div class="callout" style="border-left-color: var(--ff-green);">
<strong class="cream">Form = sorted waitlist.</strong>
<p style="font-size: 0.9rem; margin-top: 0.5rem; color: var(--ff-text-mute);">
Every reply becomes a deep-diagnostic application. You pick the 5 that fit. Everyone else gets the Mini VSL + nurture for cohort 2.
</p>
</div>
</div>

</div>

<div class="footer-tag"><span class="dot"></span>the application form is the single biggest unlock</div>
<div class="slide-number">03 / 08</div>

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">What's already built ✓</span>

<h1 style="font-size: 2.2rem; margin-bottom: 1.5rem;">
You're not starting from scratch.
</h1>

<div class="grid grid-cols-3 gap-4">

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ Origin Story Sequence</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
8 IG-story frames, your @beefcakemaxxing voice. Two versions (essay + documentary). Soft CTA + Question sticker. Day-X anchor.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ VSL Script v1</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
~7 min, essay-voice register. Ready when you want to record. Refine to v2 after WHISPER replies come in.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ Audience + Voice Locked</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
40K maxxing + 42K wellness verified. Voice DNA locked per surface. Phoenix dual-account roles mapped.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ MSA + Contract</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
PandaDoc-ready V2 with Phoenix's revisions baked in. Sign + pay = green light.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ Email Sequences (drafts)</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
WHISPER 1-5 in his voice. TEASE + SHOUT structured. We send, you reply to inbound only.
</p>
</div>

<div class="card card-green">
<div style="font-weight: 700; color: var(--ff-green); margin-bottom: 0.4rem; font-size: 0.95rem;">✓ Waitlist Page Copy</div>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5;">
Long-form copy in essay voice. Build deploy in parallel with form. Live before TEASE opens.
</p>
</div>

</div>

<div class="callout" style="margin-top: 1.5rem;">
<p style="font-size: 1rem; color: var(--ff-cream);">
<strong class="cyan">6 of 9 components shipped.</strong> The remaining 3 are <span class="orange">infra</span>, not creative — and infra moves fast when the brief is clean.
</p>
</div>

<div class="footer-tag"><span class="dot"></span>~70% shipped · the last bit is mechanical</div>
<div class="slide-number">04 / 08</div>

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">What's left · 3 builds. that's it.</span>

<h1 style="font-size: 2.2rem; margin-bottom: 1.5rem;">
The actual finish line is <span class="orange">three things</span>.
</h1>

<div class="grid grid-cols-3 gap-5">

<div class="card card-orange" style="position: relative;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: var(--ff-orange); letter-spacing: 0.15em; font-weight: 700;">01 / FF BUILDS</div>
<h3 style="margin: 0.5rem 0 0.75rem; font-size: 1.2rem; color: var(--ff-cream);">ManyChat Soft Bridge</h3>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.55;">
Auto-reply to story replies + DM keywords. Plant the waitlist invite. Send the form link when they opt in.
</p>
<p style="font-size: 0.75rem; color: var(--ff-text-dim); margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px dashed var(--ff-rule);">
~1 day to build. Live before stories post.
</p>
</div>

<div class="card card-orange" style="position: relative; border-left-width: 4px;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: var(--ff-orange); letter-spacing: 0.15em; font-weight: 700;">02 / FF BUILDS</div>
<h3 style="margin: 0.5rem 0 0.75rem; font-size: 1.2rem; color: var(--ff-cream);">Application Form</h3>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.55;">
10-Q deep diagnostic. Current situation, biggest blockers, what they've tried, commitment level. Doubles as the waitlist.
</p>
<p style="font-size: 0.75rem; color: var(--ff-cyan); margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px dashed var(--ff-rule); font-weight: 600;">
THE single biggest unlock. Ships first.
</p>
</div>

<div class="card card-orange" style="position: relative;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: var(--ff-orange); letter-spacing: 0.15em; font-weight: 700;">03 / JOHN RECORDS</div>
<h3 style="margin: 0.5rem 0 0.75rem; font-size: 1.2rem; color: var(--ff-cream);">Mini Sage VSL</h3>
<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.55;">
3-5 min, Brandon's voice. "Here's what happens when you join." Indoctrination, not pitch. Triggers post-application.
</p>
<p style="font-size: 0.75rem; color: var(--ff-text-dim); margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px dashed var(--ff-rule);">
After Brandon finishes offer ramp-up docs.
</p>
</div>

</div>

<div style="margin-top: 1.5rem; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

<div class="card" style="background: linear-gradient(135deg, rgba(251, 146, 60, 0.06) 0%, var(--ff-bg-card) 100%); border-left: 3px solid var(--ff-orange);">
<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
<span style="color: var(--ff-orange); font-weight: 700; font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase;">Brandon · do this</span>
</div>
<ul class="num-list" style="margin: 0;">
<li><strong class="cream">Finish offer ramp-up docs</strong> · today / tomorrow</li>
<li><strong class="cream">Post the Origin sequence</strong> · once ManyChat is wired</li>
<li><strong class="cream">Reply warm to inbound</strong> · don't pitch, just sort</li>
</ul>
</div>

<div class="card" style="background: linear-gradient(135deg, rgba(34, 211, 238, 0.05) 0%, var(--ff-bg-card) 100%); border-left: 3px solid var(--ff-cyan);">
<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
<span style="color: var(--ff-cyan); font-weight: 700; font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase;">FF · we handle</span>
</div>
<ul class="num-list" style="margin: 0;">
<li><strong class="cream">ManyChat flows</strong> · live before stories post</li>
<li><strong class="cream">Application form</strong> · the unlock — ships first</li>
<li><strong class="cream">Mini VSL production</strong> · right after offer docs land</li>
</ul>
</div>

</div>

<div class="footer-tag"><span class="dot"></span>3 builds · 3 days · then we ship</div>
<div class="slide-number">05 / 08</div>

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">This week · the critical path</span>

<h1 style="font-size: 2.2rem; margin-bottom: 1.5rem;">
From today forward. <span class="cyan">No mystery.</span>
</h1>

<table>
<thead>
<tr>
<th style="width: 20%;">When</th>
<th style="width: 40%;">Brandon</th>
<th style="width: 40%;">Funnel Futurist</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong class="cream">Today</strong><br/><span class="dim" style="font-size: 0.75rem;">Sun Jun 8</span></td>
<td>Finish offer ramp-up docs · review Origin sequence final</td>
<td>Build ManyChat flows · scaffold application form</td>
</tr>
<tr>
<td><strong class="cream">Mon-Tue</strong><br/><span class="dim" style="font-size: 0.75rem;">Jun 9-10</span></td>
<td>Post Origin Story Sequence · reply warm to inbound</td>
<td>Application form live · ManyChat live · WHISPER emails fire</td>
</tr>
<tr>
<td><strong class="cream">Wed-Thu</strong><br/><span class="dim" style="font-size: 0.75rem;">Jun 11-12</span></td>
<td>Record Mini Sage VSL with John · keep DMs warm</td>
<td>Mini VSL deployed · ManyChat routes warm leads to it</td>
</tr>
<tr>
<td><strong class="cream">Fri-Sun</strong><br/><span class="dim" style="font-size: 0.75rem;">Jun 13-15</span></td>
<td>WHISPER continues · sort warm threads · review applications</td>
<td>Daily data analysis · refine VSL v2 prep · TEASE opens Mon</td>
</tr>
<tr style="background: linear-gradient(90deg, rgba(34, 211, 238, 0.05) 0%, transparent 100%);">
<td><strong class="cyan">Week of Jun 16</strong></td>
<td>TEASE → SHOUT cadence · sales calls with the warm 5-10</td>
<td>Email cadence · waitlist mgmt · call scheduling</td>
</tr>
<tr style="background: linear-gradient(90deg, rgba(16, 185, 129, 0.08) 0%, transparent 100%);">
<td><strong class="green">Week of Jun 30</strong><br/><span class="dim" style="font-size: 0.75rem;">cohort 1 starts</span></td>
<td>Onboard 5 founders · run Execution Launch Calls</td>
<td>Onboarding sequences fire · retention monitoring</td>
</tr>
</tbody>
</table>

<div class="callout" style="margin-top: 1.25rem;">
<p style="font-size: 0.95rem; color: var(--ff-cream); margin: 0;">
<strong>Floor: 3 days to ManyChat + form live.</strong> Ceiling: cohort 1 day 1 the week of Jun 30. <span class="mute">Everything between is conversations, not construction.</span>
</p>
</div>

<div class="footer-tag"><span class="dot"></span>~3 weeks to first founder client</div>
<div class="slide-number">06 / 08</div>

---
layout: default
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<span class="eyebrow">After cohort 1 · the real game begins</span>

<h1 style="font-size: 2.2rem; margin-bottom: 1.5rem;">
Cohort 1 is the <span class="orange">test</span>.<br/>
The system <span class="cyan">starts after</span>.
</h1>

<div class="grid grid-cols-2 gap-8">

<div>

<h3 style="color: var(--ff-cyan); font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 1rem;">
The phases
</h3>

<ul class="num-list">
<li>
<strong class="cream">Launch cohort 1.</strong> Take 5. Stress-test the offer. Find what breaks.
<span class="mute" style="font-size: 0.85rem; display: block; margin-top: 0.25rem;">→ proof + testimonials + offer refinement</span>
</li>
<li>
<strong class="cream">Run cohort 2 fast.</strong> Don't over-saturate the warm list. Pace it. Light it back up.
<span class="mute" style="font-size: 0.85rem; display: block; margin-top: 0.25rem;">→ slightly higher pricing · social proof active</span>
</li>
<li>
<strong class="amber">Switch on ads + DM ads.</strong> The warm list runs out. Cold + lookalike traffic feeds the funnel.
<span class="mute" style="font-size: 0.85rem; display: block; margin-top: 0.25rem;">→ continuous flow · CPL/CAC tuning · scale</span>
</li>
<li>
<strong class="cream">Stack the back-end.</strong> Lower-tier offer for non-buyers. Continuity for cohort grads. Higher-tier for builders.
<span class="mute" style="font-size: 0.85rem; display: block; margin-top: 0.25rem;">→ the recurring revenue that compounds</span>
</li>
</ul>

</div>

<div>

<div class="card card-amber" style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.08) 0%, var(--ff-bg-card) 60%);">
<h3 style="color: var(--ff-amber); font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase; margin: 0 0 1rem;">
What we're really building
</h3>

<p style="font-size: 1rem; color: var(--ff-cream); line-height: 1.5; margin-bottom: 1rem;">
Not a cohort spreadsheet. A <strong class="cyan">recurring back-end</strong> with a paid-traffic engine bolted to the front of it.
</p>

<div style="background: var(--ff-bg); border-radius: 0.4rem; padding: 1rem; margin-bottom: 0.75rem;">
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--ff-text-dim); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">The economic shape</div>
<div style="font-size: 0.92rem; line-height: 1.7;">
<div><span class="cyan">→</span> <strong class="cream">Front-end:</strong> <span class="mute">Execution Install (high-ticket cohort)</span></div>
<div><span class="cyan">→</span> <strong class="cream">Back-end:</strong> <span class="mute">Continuity + lower-tier nurture</span></div>
<div><span class="cyan">→</span> <strong class="cream">Traffic:</strong> <span class="mute">Organic + DM ads + retargeting</span></div>
<div><span class="cyan">→</span> <strong class="cream">Audience:</strong> <span class="mute">Grows weekly with the engine running</span></div>
</div>
</div>

<p style="font-size: 0.85rem; color: var(--ff-text-mute); line-height: 1.5; margin: 0;">
Get the front working. Then the back-end compounds without your attention. That's the version of this we're heading toward.
</p>
</div>

</div>

</div>

<div class="footer-tag"><span class="dot"></span>cohort 1 is the proof · the engine is the prize</div>
<div class="slide-number">07 / 08</div>

---
layout: cover
class: text-center
---

<div class="brand-mark">
  <span class="ff-mark">FF</span>
  <span class="bw">Beefcake Wellness</span>
  <span class="x">×</span>
  <span class="ff">Funnel Futurist</span>
</div>

<div class="absolute inset-0 flex flex-col justify-center px-20 text-center">

<span class="eyebrow" style="margin: 0 auto;">One question</span>

<h1 style="font-size: 4.5rem; line-height: 1.05; margin: 2rem auto;">
What's <span class="orange">in the way</span><br/>right now?
</h1>

<p class="kicker" style="max-width: 36rem; margin: 0 auto; font-size: 1.3rem;">
Not the whole launch. Just the <span class="cyan">next thing on your list</span>.
</p>

<p class="kicker" style="max-width: 36rem; margin: 1.25rem auto 0; font-size: 1rem;">
Drop it in your launch Slack channel. We move it within 4 hours.
</p>

<div class="callout" style="margin: 3rem auto 0; max-width: 40rem; text-align: left;">
<p style="font-size: 0.95rem; color: var(--ff-cream); margin: 0;">
<strong class="cyan">Don't optimize.</strong> Don't perfect. Don't wait for the perfect post.
<br/><br/>
<strong>Cohort 1 isn't the destination.</strong> It's the <strong class="green">first iteration of a system</strong> we're going to run for the next 12 months.
<br/><br/>
The faster we launch, the faster we learn what breaks, the faster the real engine turns on.
</p>
</div>

</div>

<div class="footer-tag"><span class="dot"></span>brandon × ff · let's fucking go</div>
<div class="slide-number">08 / 08</div>
