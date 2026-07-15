import { defineConfig } from 'vite'

// Rule 18: rolldown production build resolves leading-slash public paths as fs imports.
// Relax fs.allow so `slidev build` (and the Vercel deploy) succeed like the dev server does.
export default defineConfig({
  server: { fs: { strict: false, allow: ['.', '..'] } },
})
