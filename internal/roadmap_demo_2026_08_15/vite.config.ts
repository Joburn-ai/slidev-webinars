import { defineConfig } from 'vite'

// Rule 18: slidev's rolldown PRODUCTION build treats a leading-slash public path
// as a filesystem import and fails with "resolves outside of Vite server.fs.allow".
// The dev server runs clean, so this only bites on the Vercel deploy.
export default defineConfig({ server: { fs: { strict: false, allow: ['.', '..'] } } })
