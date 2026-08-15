"""QC screenshots. Derives each slide's real click count so the shot shows the
FINAL state of the slide, not the opening state.

    python3 scripts/shoot.py 1,17,26,40
"""
import asyncio, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_gate import read_deck
from playwright.async_api import async_playwright

slides = read_deck()
# clicks = number of reveal steps. <v-click> counts 1; <v-clicks> counts its list items.
def clicks_for(body):
    n = len(re.findall(r'<v-click(?![s])', body))
    for blk in re.findall(r'<v-clicks>(.*?)</v-clicks>', body, re.S):
        n += len(re.findall(r'(?m)^\s*[-*]\s+\S', blk)) or len(re.findall(r'<div', blk))
    return n

WANT = [int(x) for x in sys.argv[1].split(',')]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(
            executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-linux64/chrome-headless-shell',
            args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=1)
        for n in WANT:
            c = clicks_for(slides[n - 1][2]) if n - 1 < len(slides) else 0
            url = f'http://localhost:8901/{n}/{c}' if c else f'http://localhost:8901/{n}'
            await pg.goto(url, wait_until='networkidle')
            await pg.wait_for_timeout(1000)
            body = await pg.inner_text('body')
            if '404' in body[:60]:
                await pg.goto(f'http://localhost:8901/{n}', wait_until='networkidle')
                await pg.wait_for_timeout(800)
            await pg.screenshot(path=f'qc/s{n:03d}.png')
            print(f'shot {n} (clicks={c})')
        await b.close()

asyncio.run(main())
