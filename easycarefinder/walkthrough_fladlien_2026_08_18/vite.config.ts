import { defineConfig } from 'vite'

// Rule 18: Slidev's rolldown PRODUCTION build resolves leading-slash public paths
// (e.g. <img src="/images/..."> or `image: /images/...` frontmatter) as fs imports and
// fails with "resolves outside of Vite server.fs.allow". The dev server runs clean; only
// `slidev build` (and therefore the Vercel deploy) trips. Relax fs.allow so both succeed.
export default defineConfig({
  server: { fs: { strict: false, allow: ['.', '..'] } },
})
