# Roadmap VSL v6 — build + deploy

```bash
cd /root/slidev-webinars
npx slidev build internal/roadmap_vsl_2026_08_05/slides_v6.md --base / --out dist-rv6
cp internal/roadmap_vsl_2026_08_05/vercel.json internal/roadmap_vsl_2026_08_05/dist-rv6/
cd internal/roadmap_vsl_2026_08_05/dist-rv6
npx vercel --prod --yes --token "$VERCEL_TOKEN" --scope team_AcbqD1MAg7WOqx4lMqGSZXoa
```

**LIVE: https://roadmap-vsl-v6.vercel.app**

## 🔴 Two gotchas that cost time on 2026-08-09

**1. `--out` is relative to the SLIDES FILE, not your cwd.** `dist-rv6` lands in
`internal/roadmap_vsl_2026_08_05/`, not the repo root. Looking in the wrong place makes a
successful build look like it produced nothing.

**2. Slidev emits `_redirects` (Netlify), NOT a Vercel rewrite.** Without `vercel.json`, every
deep link (`/14`, `/52?clicks=5`) returns **404** while still rendering, because the SPA router
takes over client-side. **Images load, status is 404, and `curl /` returns 200** — so all three
naive checks pass while shared slide links are broken. The `vercel.json` here fixes it; copy it
into `dist-rv6/` on every deploy.
