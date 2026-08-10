#!/usr/bin/env python3
"""
Brad Pounds / HomeBuyerSchool evergreen-webinar image runner.

Re-paletted fork of build_doc_images/runner.py. LOCKED to the HomeBuyerSchool
orange/navy brand so every generated concept image reads as ONE visual system
(the #1 fix John flagged: past decks were weak/inconsistent on imagery).

Style is bold editorial flat-vector, cinematic composition, NO photorealism,
NO human faces in detail (silhouettes / back-views only -> avoids the
testimonial-face rule + uncanny valley), NO text/logos in the image.

Usage:
    python3 runner_supported.py --config images_config_supported.json --out ../../public/images/concept/
"""

import argparse, base64, json, os, sys, time
from pathlib import Path
from urllib import error as urllib_error
from urllib import request as urllib_request

ROOT_ENV = Path("/root/ai-os/.env")
DEFAULT_MODEL = "gemini-3-pro-image-preview"

# LOCKED Brad brand preamble -- baked into every prompt so the set is one system.
STYLE_PREAMBLE = (
    "Bold editorial flat-vector illustration for a premium, calm, academically "
    "credible American education brand serving parents of high-school AP students. "
    "Cinematic composition with one clear focal point and generous negative space. "
    "LOCKED PALETTE, use only these: deep navy #1B365D, warm gold #C5A55A, "
    "soft cream #E8E0D0, near-black #111111, white. "
    "NO photorealism. NO detailed human faces, use silhouettes, back-views or "
    "three-quarter-away framing only. NO text, NO letterforms, NO numbers, NO logos "
    "anywhere in the image. Flat vector shapes, subtle grain, confident and quiet, "
    "never cartoonish and never corporate-stock. "
)


def load_api_key() -> str:
    if not ROOT_ENV.exists():
        sys.exit(f"FATAL: root .env not found at {ROOT_ENV}")
    for raw in ROOT_ENV.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        if key.strip() == "GEMINI_API_KEY":
            return val.strip().strip('"').strip("'")
    sys.exit("FATAL: GEMINI_API_KEY not found in root .env")


def generate_image(api_key: str, prompt: str, model: str) -> bytes:
    endpoint = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]},
    }
    req = urllib_request.Request(
        f"{endpoint}?key={api_key}",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib_request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib_error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")[:600]
        raise RuntimeError(f"HTTP {e.code}: {err}")
    for part in payload.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError(f"No image in response: {json.dumps(payload)[:300]}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    if not args.config.exists():
        sys.exit(f"FATAL: config not found at {args.config}")
    config = json.loads(args.config.read_text())
    model = os.environ.get("GEMINI_IMAGE_MODEL", config.get("model", DEFAULT_MODEL))
    images = config.get("images", [])
    if not images:
        sys.exit("FATAL: no images in config")
    args.out.mkdir(parents=True, exist_ok=True)
    api_key = load_api_key()
    print(f"model: {model}\nimages: {len(images)}\noutput: {args.out}\n")
    generated, skipped, failed = [], [], []
    for spec in images:
        slug = spec["slug"]
        out_path = args.out / f"{slug}.png"
        if out_path.exists():
            print(f"[skip] {out_path.name}")
            skipped.append(slug); continue
        prompt = STYLE_PREAMBLE + spec["concept"]
        print(f"[gen ] {out_path.name} ... ", end="", flush=True)
        try:
            out_path.write_bytes(generate_image(api_key, prompt, model))
            print(f"ok ({out_path.stat().st_size // 1024} KB)")
            generated.append(slug)
        except Exception as exc:
            print(f"FAILED -- {exc}")
            failed.append((slug, str(exc)))
        time.sleep(1)
    print(f"\nsummary -- gen={len(generated)} skip={len(skipped)} fail={len(failed)}")
    for slug, err in failed:
        print(f"  X {slug}: {err[:160]}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
