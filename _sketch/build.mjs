/**
 * Build every diagram in ./diagrams into ./out as SVG, then rasterise to PNG with
 * the playwright chromium already on this box (no rsvg/inkscape installed).
 */
import { readdirSync, mkdirSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });

const files = readdirSync(join(here, "diagrams")).filter((f) => f.endsWith(".mjs"));
const built = [];
for (const f of files) {
  const mod = await import(join(here, "diagrams", f));
  // a file exports either one diagram (name + render) or several named ones
  const diagrams = mod.name && mod.render
    ? [mod]
    : Object.values(mod).filter((d) => d && d.name && d.render);
  for (const d of diagrams) {
    const svg = d.render();
    const p = join(outDir, `${d.name}.svg`);
    writeFileSync(p, svg);
    built.push({ name: d.name, path: p, bytes: svg.length });
    console.log(`built ${d.name}.svg  ${svg.length} bytes`);
  }
}
writeFileSync(join(outDir, "_manifest.json"), JSON.stringify(built, null, 2));
