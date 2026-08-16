<script setup>
/**
 * Live countdown to the offer deadline, for use on slides.
 *
 * 🔴 THE DEADLINE IS AN ABSOLUTE UTC INSTANT, NOT A LOCAL TIME.
 * "Midnight ET on 31 August" is 2026-09-01T03:59:59Z, because America/New_York is
 * UTC-4 during EDT. If this were written as a local Date string it would compute
 * differently on the presenter's laptop than on a viewer's, and a countdown that
 * disagrees with the email is worse than no countdown at all.
 *
 * 🔴 IT DEGRADES. Past the deadline it shows the closed state rather than negative
 * numbers, so a replay viewer never sees "-3 days".
 *
 * 🔴 LIVE-SCREENSHARE SAFE. One text node updates per second inside a fixed-width
 * tabular-nums box. Nothing reflows, nothing animates, the repaint region is a few
 * hundred pixels. This is the one moving thing in the deck and it is deliberate.
 */
import { ref, onMounted, onUnmounted, computed } from 'vue'

const props = defineProps({
  // 31 Aug 2026, 23:59:59 America/New_York (EDT, UTC-4) === 1 Sep 2026, 03:59:59 UTC
  deadline: { type: String, default: '2026-09-01T03:59:59Z' },
  label: { type: String, default: 'Your $500 credit expires in' },
  closedLabel: { type: String, default: 'This window has closed' },
  compact: { type: Boolean, default: false },
})

const now = ref(Date.now())
let timer = null
onMounted(() => { timer = setInterval(() => { now.value = Date.now() }, 1000) })
onUnmounted(() => { if (timer) clearInterval(timer) })

const target = computed(() => new Date(props.deadline).getTime())
const left = computed(() => Math.max(0, target.value - now.value))
const over = computed(() => left.value <= 0)

const pad = (n) => String(n).padStart(2, '0')
const parts = computed(() => {
  const s = Math.floor(left.value / 1000)
  return {
    d: Math.floor(s / 86400),
    h: pad(Math.floor((s % 86400) / 3600)),
    m: pad(Math.floor((s % 3600) / 60)),
    s: pad(s % 60),
  }
})
</script>

<template>
  <div class="sp-countdown" :class="{ compact, over }">
    <div class="sp-countdown-label">{{ over ? closedLabel : label }}</div>
    <div v-if="!over" class="sp-countdown-clock">
      <span class="unit"><b>{{ parts.d }}</b><i>days</i></span>
      <span class="sep">:</span>
      <span class="unit"><b>{{ parts.h }}</b><i>hrs</i></span>
      <span class="sep">:</span>
      <span class="unit"><b>{{ parts.m }}</b><i>min</i></span>
      <span class="sep">:</span>
      <span class="unit"><b>{{ parts.s }}</b><i>sec</i></span>
    </div>
    <div class="sp-countdown-foot">Midnight ET, Monday 31 August</div>
  </div>
</template>

<style scoped>
.sp-countdown {
  display: inline-flex; flex-direction: column; align-items: center; gap: .55rem;
  border: 2px solid var(--gold); border-radius: 16px;
  background: rgba(197, 165, 90, .12);
  padding: 1.15rem 2rem 1rem;
}
.sp-countdown-label {
  font-family: var(--body); font-weight: 700; font-size: var(--t-label);
  letter-spacing: .12em; text-transform: uppercase; color: var(--goldi);
}
:is(.night, .ink) .sp-countdown-label { color: var(--goldl); }
.sp-countdown-clock { display: flex; align-items: flex-end; gap: .35rem; }
.unit { display: flex; flex-direction: column; align-items: center; min-width: 3.1ch; }
.unit b {
  font-family: var(--display); font-weight: 900; font-size: var(--t-stat);
  line-height: .95; font-variant-numeric: tabular-nums; color: var(--navy);
}
:is(.night, .ink) .unit b { color: #fff; }
.unit i {
  font-family: var(--body); font-style: normal; font-weight: 700;
  font-size: var(--t-micro); letter-spacing: .1em; text-transform: uppercase;
  color: var(--fogd); margin-top: .2rem;
}
:is(.night, .ink) .unit i { color: var(--onnavy2); }
.sep {
  font-family: var(--display); font-weight: 900; font-size: var(--t-stat);
  line-height: .95; color: var(--gold); padding-bottom: 1.1rem;
}
.sp-countdown-foot {
  font-family: var(--body); font-weight: 700; font-size: var(--t-micro);
  color: var(--fogd);
}
:is(.night, .ink) .sp-countdown-foot { color: var(--onnavy2); }

.compact .unit b, .compact .sep { font-size: var(--t-h2); }
.compact { padding: .7rem 1.3rem .6rem; }

.over { border-color: var(--fog); background: transparent; }
</style>
