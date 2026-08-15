<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
const props = defineProps({ hours: { type: Number, default: 72 } })
// start a hair under the full window so it reads as already running
const remaining = ref(props.hours * 3600 - 3)
let timer = null
onMounted(() => { timer = setInterval(() => { if (remaining.value > 0) remaining.value-- }, 1000) })
onUnmounted(() => { if (timer) clearInterval(timer) })
const pad = (n) => String(n).padStart(2, '0')
const label = computed(() => {
  const s = remaining.value
  return `${pad(Math.floor(s / 3600))}:${pad(Math.floor((s % 3600) / 60))}:${pad(s % 60)}`
})
</script>

<template>
  <span class="tabular-nums">{{ label }}</span>
</template>
