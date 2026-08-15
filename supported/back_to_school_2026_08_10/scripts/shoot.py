"""QC screenshots of the built deck.

    python3 scripts/shoot.py 24,38,67

🔴 SHOOTS THE OPENING STATE OF EACH SLIDE, WHICH IS DELIBERATE.

Slidev's `/<slide>/<clicks>` route is NOT reliable here: `/24/4` does not resolve to
slide 24 at click 4, it lands elsewhere entirely (verified 2026-08-15 — `.slidev-page-24`
is absent from the DOM at that URL). An earlier version of this script used it, silently
fell through, and produced screenshots that looked like slides with missing content.

The opening state is the honest thing to QC anyway: v-click content is present in the DOM
with `opacity: 0`, so it already RESERVES its layout space. If a slide is well composed at
click 0 it is well composed at full reveal. To check a reveal, drive it by hand.
"""
import asyncio, sys
from playwright.async_api import async_playwright

CHROME = ('/root/.cache/ms-playwright/chromium_headless_shell-1228/'
          'chrome-headless-shell-linux64/chrome-headless-shell')
PORT = 8930
WANT = [int(x) for x in sys.argv[1].split(',')]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=1)
        for n in WANT:
            await pg.goto(f'http://localhost:{PORT}/{n}', wait_until='networkidle')
            await pg.wait_for_timeout(900)
            # fail loudly rather than screenshotting a 404 that looks like a blank slide
            ok = await pg.evaluate(f"() => !!document.querySelector('.slidev-page-{n}')")
            if not ok:
                print(f'  !! slide {n}: .slidev-page-{n} not in DOM — NOT a valid route')
            await pg.screenshot(path=f'qc/s{n:03d}.png')
            print(f'shot {n}' + ('' if ok else '  (SUSPECT)'))
        await b.close()

asyncio.run(main())
