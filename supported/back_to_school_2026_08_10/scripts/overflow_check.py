"""Geometry sweep: does any element escape its slide frame?

    python3 scripts/overflow_check.py [port]

🔴 WHY NOT scrollWidth. Slidev's slide container is `overflow: hidden`, so text that runs
past the edge is CLIPPED, not scrolled — scrollWidth never exceeds clientWidth and an
assertion built on it goes green over a visibly broken frame. This compares each element's
BOUNDING BOX against the slide container's box instead, which is what the eye sees.

Run it after ANY font or type-scale change: swapping a face changes glyph metrics, so
headlines that fitted yesterday can clip today.
"""
import asyncio, sys
sys.path.insert(0, 'scripts')
from deck_gate import read_deck

CHROME = ('/root/.cache/ms-playwright/chromium_headless_shell-1228/'
          'chrome-headless-shell-linux64/chrome-headless-shell')
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8912
N = len(read_deck())

from playwright.async_api import async_playwright

async def main():
    bad = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1280, 'height': 720})
        for n in range(1, N + 1):
            await pg.goto(f'http://localhost:{PORT}/{n}', wait_until='domcontentloaded')
            await pg.wait_for_timeout(220)
            res = await pg.evaluate(f"""async () => {{
              await document.fonts.ready;
              const page = document.querySelector('.slidev-page-{n}');
              if (!page) return null;
              const L = page.querySelector('.slidev-layout') || page;
              const lb = L.getBoundingClientRect();
              const out = [];
              L.querySelectorAll('*').forEach(el => {{
                const r = el.getBoundingClientRect();
                if (!r.width || !r.height) return;
                const cs = getComputedStyle(el);
                if (cs.position === 'absolute' || cs.position === 'fixed') return;
                const dx = Math.max(0, Math.round(r.right - lb.right), Math.round(lb.left - r.left));
                const dy = Math.max(0, Math.round(r.bottom - lb.bottom), Math.round(lb.top - r.top));
                if (dx > 2 || dy > 2) {{
                  out.push({{tag: el.tagName.toLowerCase(), cls: (el.className||'').toString().slice(0,42),
                             dx, dy, txt: (el.innerText||'').trim().replace(/\\s+/g,' ').slice(0,48)}});
                }}
              }});
              // keep only the deepest offenders, parents inherit their child's overflow
              return out.filter(o => o.txt).slice(0, 3);
            }}""")
            if res:
                bad.append((n, res))
        await b.close()
    if not bad:
        print(f'✅ geometry clean across {N} slides — nothing escapes its frame')
        return 0
    print(f'❌ {len(bad)} slides with content outside the frame:')
    for n, items in bad:
        for it in items:
            print(f"  slide {n:>3}  +{it['dx']}px x / +{it['dy']}px y  <{it['tag']} {it['cls']}>  {it['txt']!r}")
    return 1

sys.exit(asyncio.run(main()))
