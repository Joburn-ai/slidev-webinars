---
theme: default
title: 60+ Programs for High-Earning First-Time Buyers (Evergreen)
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
  # TODO: confirm against ./_ASSET_REFERENCE_SHEET.md brand kit before build.
  sans: Inter
  serif: Crimson Pro
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

<!-- slide:cover-01 -->

<div class="absolute inset-0 hbs-cover flex flex-col justify-center items-center px-16">
  <!-- TODO(bless): cover copy from _EVERGREEN_STRUCTURE.md O1. <=7 visible words; notes carry script. -->
  <!-- Placeholder only -- do not treat as final copy. -->
  <div class="hbs-eyebrow">Evergreen on-demand replay</div>
  <h1 class="text-5xl max-w-4xl">[COVER HEADLINE -- fill from O1 after bless]</h1>
  <p class="text-lg mt-10 hbs-quiet">with Bradley Pounds &middot; HomeBuyerSchool.com</p>
</div>

<!--
TODO(Rule 14): SAY-script for the cover is written AFTER the shorty script is blessed
(script = compressed cut of the big-webinar transcript per ./_EVERGREEN_STRUCTURE.md).
This deck is SKELETON only until then.
-->

---
src: ./opening.md
---

---
src: ./teaching.md
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
