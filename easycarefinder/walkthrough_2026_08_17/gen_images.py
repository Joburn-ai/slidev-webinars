#!/usr/bin/env python3
"""Concept imagery for the ECF walkthrough deck. Gemini 3 Pro Image, 16:9, no text ever rendered."""
import os, json, base64, urllib.request, re, concurrent.futures as cf
ENV="/root/ai-os/.env"; OUT="public/images"
os.makedirs(OUT, exist_ok=True)
def env(k):
    m=re.search(r"^%s=(.*)$"%re.escape(k), open(ENV).read(), re.M)
    return m.group(1).strip().strip('"').strip("'") if m else os.environ.get(k)

# Market Archetype 1 register, held across every frame.
LOOK=("Editorial documentary photograph, natural available light, warm and slightly desaturated. "
 "Calm, unhurried, generous negative space, one clear subject. Photojournalism, not advertising. "
 "Muted palette that sits beside deep forest green #1D5C4D, warm gold #A87910 and cream #FBF7F1. "
 "STRICTLY NO text, NO words, NO letters, NO numbers, NO signage, NO house numbers, NO street signs, "
 "NO number plates, NO logos, NO watermark. NO stock-photo smiling, NO glossy retouching, "
 "NO medical or clinical objects, NO wheelchairs, NO hospital, NO scrubs, NO pill bottles. "
 "16:9 horizontal. Leave the left third or the lower third quiet so text can sit over it later.")

SHOTS={
 "c01_four_doors":"Four ordinary residential front doors photographed as a quiet typology, side by side, each slightly different in colour and era, warm daylight. Nobody in frame. Calm and orderly.",
 "c02_kitchen_table":"An empty kitchen table in an ordinary Northern California house, late warm afternoon light through a window. Two mugs, a legal pad, a set of keys. Nobody in frame.",
 "c03_phone_dusk":"A kitchen counter at dusk, one warm lamp, a phone face down beside a notepad with handwriting on it. The rest of the room falling into shadow. Nobody in frame.",
 "c04_form_wall":"An abstract quiet still life suggesting a barrier: a plain closed door with a small frosted glass panel, dim hallway, one light behind it. Nobody in frame.",
 "c05_broken_map":"A folded paper road map lying open on a wooden table, worn at the creases, one corner torn, warm side light. Nobody in frame. No readable place names.",
 "c06_home_help":"An ordinary domestic kitchen mid morning, a kettle, a folded tea towel, a chair pulled slightly out from the table. Lived in and calm. Nobody in frame.",
 "c07_independent_apt":"The exterior walkway of a small low rise apartment building, potted plants outside two of the doors, warm late light, mature tree. Nobody in frame. No numbers on the doors.",
 "c08_large_community":"A long wide carpeted corridor in a large building, evenly spaced identical doors receding into the distance, soft institutional daylight. Nobody in frame. Slightly impersonal.",
 "c09_small_home_street":"A 1970s single storey ranch house on an ordinary quiet suburban street in inland Northern California, mature oak, wide driveway, watered lawn, photographed straight on at about 7am. Completely unremarkable and residential. Nobody in frame.",
 "c10_invisible_street":"An ordinary residential street at dusk seen from the middle of the road, five modest houses, one porch light on, everything else quiet and unlit. Nobody in frame.",
 "c11_two_doors_same_street":"Two ordinary front porches on the same suburban street photographed from the pavement, near identical in size and era, one with a chair and a plant, the other bare. Warm flat morning light. Nobody in frame.",
 "c13_shortlist_table":"Three printed sheets of paper fanned out on a plain wooden kitchen table beside a mug, warm window light. Nobody in frame. No readable text on the pages.",
}
def gen(item):
    slug,scene=item
    dst=f"{OUT}/{slug}.png"
    if os.path.exists(dst) and os.path.getsize(dst)>20000: return slug,"cached"
    url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent?key={env('GOOGLE_AI_API_KEY')}"
    body={"contents":[{"parts":[{"text":f"{LOOK} SCENE: {scene}"}]}],
          "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"16:9"}}}
    try:
        j=json.load(urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(body).encode(),
            headers={"Content-Type":"application/json"},method="POST"),timeout=420))
        for c in j.get("candidates",[]):
            for p in c.get("content",{}).get("parts",[]):
                d=p.get("inlineData") or p.get("inline_data")
                if d and d.get("data"):
                    open(dst,"wb").write(base64.b64decode(d["data"])); return slug,"ok"
        return slug,"NO IMAGE"
    except Exception as e: return slug,f"FAIL {str(e)[:90]}"
with cf.ThreadPoolExecutor(max_workers=4) as ex:
    for s,st in ex.map(gen, SHOTS.items()): print(f"  {s:28} {st}")
