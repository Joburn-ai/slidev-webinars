---
theme: default
title: AP Is Over. The Real Game Starts Now.
info: |
  SupportED Tutoring Parent Masterclass.
  Wed 2026-05-27, 8pm EST. Dr. Joe Sebestyen, live.
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
  mono: JetBrains Mono
  weights: '300,400,500,600,700,800,900'
layout: cover
background: 'https://res.cloudinary.com/dby8dt6md/image/upload/v1779640657/slidev/supported/_brand/other/dr_joseph.png'
---

<style>
:root {
  --brand-primary: #1B365D;
  --brand-secondary: #C5A55A;
  --brand-accent: #E8E0D0;
  --brand-dark: #0f172a;
  --brand-light: #fafaf7;
}

.slidev-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--brand-light);
  color: var(--brand-dark);
}

.slidev-layout h1 {
  font-size: 4.5rem;
  font-weight: 900;
  color: var(--brand-primary);
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-bottom: 1.5rem;
}

.slidev-layout h2 {
  font-size: 3rem;
  font-weight: 800;
  color: var(--brand-primary);
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
}

.slidev-layout p, .slidev-layout li {
  font-size: 1.5rem;
  line-height: 1.55;
  color: var(--brand-dark);
}

.slidev-layout li {
  margin-bottom: 0.75rem;
}

.slidev-layout strong {
  color: var(--brand-primary);
  font-weight: 700;
}

/* Force v-click hidden state to be FULLY invisible (not faded). */
.slidev-vclick-hidden {
  opacity: 0 !important;
}

.slidev-vclick-target {
  transition: opacity 200ms ease;
}

/* Brand utility classes. */
.gold {
  color: var(--brand-secondary);
  font-weight: 800;
}
.navy {
  color: var(--brand-primary);
}
.cream-bg {
  background: var(--brand-accent);
}
.serif {
  font-family: 'Crimson Pro', 'Source Serif Pro', Georgia, serif;
}

/* Frosted card for hero overlays. */
.frosted {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(27, 54, 93, 0.1);
  border-radius: 20px;
  padding: 3rem 4rem;
  box-shadow: 0 20px 60px -10px rgba(27, 54, 93, 0.25);
}

.frosted-dark {
  background: rgba(15, 23, 42, 0.7);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(197, 165, 90, 0.2);
  border-radius: 20px;
  padding: 3rem 4rem;
  color: white;
}

/* Callouts. */
.callout-info {
  background: rgba(59, 130, 246, 0.08);
  border-left: 4px solid #3b82f6;
  padding: 1.25rem 1.5rem;
  border-radius: 0.5rem;
}
.callout-success {
  background: rgba(22, 163, 74, 0.08);
  border-left: 4px solid #16a34a;
  padding: 1.25rem 1.5rem;
  border-radius: 0.5rem;
}
.callout-warning {
  background: rgba(245, 158, 11, 0.08);
  border-left: 4px solid #f59e0b;
  padding: 1.25rem 1.5rem;
  border-radius: 0.5rem;
}
.callout-danger {
  background: rgba(220, 38, 38, 0.08);
  border-left: 4px solid #dc2626;
  padding: 1.25rem 1.5rem;
  border-radius: 0.5rem;
}

/* Section divider gradient. */
.section-gradient {
  background: linear-gradient(135deg, var(--brand-primary) 0%, #2a4a7a 50%, #1B365D 100%);
  color: white;
}

/* Logo watermark on every non-cover slide. */
.slidev-layout:not(.slidev-layout-cover):not(.slidev-layout-end)::after {
  content: '';
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  width: 140px;
  height: 40px;
  background: url('https://res.cloudinary.com/dby8dt6md/image/upload/v1779640658/slidev/supported/_brand/brand/supported_logo_with_name.png') no-repeat right center;
  background-size: contain;
  opacity: 0.65;
  z-index: 100;
  pointer-events: none;
}
</style>

<!-- slide:cover-01 -->

<div class="absolute inset-0 bg-black/50"></div>

<div class="absolute inset-0 flex items-center justify-center px-12">
  <div class="frosted-dark max-w-3xl text-center">
    <div class="text-2xl mb-4 opacity-80" style="letter-spacing: 0.15em; text-transform: uppercase;">
      Parent Masterclass
    </div>
    <div class="font-black mb-6" style="font-size: 5rem; line-height: 0.95; color: white;">
      AP Is Over.
    </div>
    <div class="text-5xl gold font-bold">
      The Real Game Starts Now.
    </div>
    <div class="mt-12 text-xl opacity-75">
      With Dr. Joe Sebestyen, Founder of SupportED Tutoring
    </div>
    <div class="mt-2 text-base opacity-60">
      Wednesday May 27, 2026  ·  8pm EST  ·  Live on Riverside
    </div>
  </div>
</div>

<!--
HOOK: Hold the cover slide silently for 5 seconds. Let the room settle.
BEATS:
  - Eyes on camera
  - "Hey. Welcome in."
TIMING: 30 sec on this slide
TRANSITION: Click to first content slide.
-->

---
src: ./opening.md
---
