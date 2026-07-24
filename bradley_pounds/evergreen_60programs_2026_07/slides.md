---
theme: default
title: 60+ Programs for High-Earning First-Time Buyers
titleTemplate: '%s'
favicon: /favicon.png
info: |
  Bradley Pounds / HomeBuyerSchool.com -- EVERGREEN "shorty" webinar (on-demand replay cut).
  Self-running / narrated. ~22 min target (band 20-25) vs the 60-90 min live.
  Funnel: cold FB (Housing Special Ad Category, broad-only) -> registration -> on-demand webinar -> BOOK A CALL -> high-ticket homebuyer coaching.
  Offer: FREE STRATEGY CALL (soft, book-a-call). No priced stack / guarantee / hard scarcity.
  SKELETON ONLY -- Rule 14: slide copy is NOT written until the script (built from the big-webinar transcript) is blessed.
  Outline source of truth: ./_EVERGREEN_STRUCTURE.md
  Source live deck: ./assets/source_images/ (78 slides / 107 images) + scratchpad brad_slides.pdf/.txt
class: text-center
highlighter: shiki
lineNumbers: false
# Rule 12: pin colorSchema so OS dark mode cannot flip the light design.
colorSchema: light
drawings:
  # Evergreen self-running replay: no live annotation needed.
  persist: false
transition: slide-left
mdc: true
fonts:
  # Body = Poppins (all weights). Display = Anton/Oswald, loaded via @import in style.css.
  sans: Poppins
  provider: google
  weights: '400,500,600,700,800,900'
layout: cover
---

<!--
  STYLE: cross-slide brand + component CSS lives UNSCOPED in the co-located ./style.css (Rule 7).
  Slidev auto-loads it. Class prefix: .hbs-* (HomeBuyerSchool). Do NOT move brand classes into this
  scoped <style> block -- they would break on slides 2+ (Rule 7).
  The <style> block below carries ONLY the Rule 3 force-hide (safe as scoped-or-not; duplicated in style.css too).
-->

<style>
/* Rule 3: force full-hide before click (default Slidev leaves content faded-gray). */
.slidev-vclick-hidden { opacity: 0 !important; }
.slidev-vclick-target { transition: opacity 240ms ease, transform 240ms ease; }
</style>

<!-- slide:op-01-cover -->

<div class="absolute inset-0">
  <img src="/images/concept/c01_horizon_home.png" class="hbs-bleed" />
  <div class="hbs-scrim"></div>
</div>

<img src="/images/brad/img-021_t.png" class="hbs-logo" style="left:2.2rem; right:auto;" />

<div class="absolute right-8 bottom-0 h-[90%] w-[33%] z-20" v-motion :initial="{ opacity: 0, x: 40 }" :enter="{ opacity: 1, x: 0, transition: { delay: 320 } }">
  <img src="/images/brad/img-019_cut.png" class="h-full w-full object-contain object-bottom" style="filter: drop-shadow(0 12px 34px rgba(1,25,55,0.5));" />
</div>

<div class="absolute left-0 top-0 h-full w-[60%] flex flex-col justify-center pl-16 pr-6 z-10">
  <div class="hbs-eyebrow hbs-eyebrow-light" v-motion :initial="{ opacity: 0, y: 20 }" :enter="{ opacity: 1, y: 0, transition: { delay: 100 } }">Unlock your first home</div>
  <h1 class="text-white" style="font-size: 3.7rem;" v-motion :initial="{ opacity: 0, y: 28 }" :enter="{ opacity: 1, y: 0, transition: { delay: 220 } }">Programs for high-earning first-time buyers</h1>
  <p class="hbs-lead-light mt-6" style="text-shadow: 0 2px 12px rgba(1,25,55,0.9); font-weight:600;" v-motion :initial="{ opacity: 0 }" :enter="{ opacity: 1, transition: { delay: 520 } }">Bradley Pounds &middot; HomeBuyerSchool.com</p>
</div>

<div class="hbs-foot hbs-fineprint hbs-fineprint-light z-30">Educational purposes only, not a commitment to lend. Equal Housing Opportunity.</div>

<!--
O1 COVER / FRAME (~40s). TEMPO: FRAME, let it breathe.
SAY: Appreciate you being here. My name's Bradley Pounds, and over the next twenty minutes or so I'm going to share everything I know about helping higher earners take advantage of programs you've probably never even heard of. Programs built to help you buy your first home, or your first home in a long time. Now if you've been telling yourself a story that this kind of help is only for really low-income folks, that there's nothing out there for somebody like you who works hard and makes good money, I am really, really excited to prove you wrong. You'll never be so happy to be wrong as you're about to be. So grab a pen, because you're going to want to take some notes.
COMPLIANCE: educational promise only; "Unlock" appears only as on-slide eyebrow, never spoken.
-->

---
src: ./opening.md
---

---
src: ./teaching.md
---

---
src: ./teaching_tour.md
---

---
src: ./recap_momentum.md
---

---
src: ./offer.md
---

---
src: ./close.md
---
