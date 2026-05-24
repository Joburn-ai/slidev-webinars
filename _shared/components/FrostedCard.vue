<template>
  <div class="frosted-card" :class="variant">
    <slot />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  variant?: 'light' | 'dark' | 'auto'
}>()
</script>

<style scoped>
.frosted-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: inset 0 0 0 9999px rgba(0, 0, 0, 0.25);
  color: white;
}
.frosted-card.light {
  background: rgba(255, 255, 255, 0.7);
  box-shadow: inset 0 0 0 9999px rgba(255, 255, 255, 0.1);
  color: #111;
  border: 1px solid rgba(0, 0, 0, 0.08);
}
.frosted-card.dark {
  background: rgba(0, 0, 0, 0.5);
}
</style>
