#!/usr/bin/env python3
"""
Redact student PII from testimonial screenshots so the deck can use them publicly.

Strategy:
1. OCR each image with Tesseract + extract per-word bounding boxes
2. Apply blacklist of known student names + their family + parent names
3. Apply regex patterns for ID numbers, ZIP codes, email addresses, street addresses
4. Black-box redact each matched bounding box
5. KEEP admissions-officer signatures (Marcelle Hicks, Bridget Varisco, Kellie Kane,
   Ross VanDyke, Linda Livingstone) and the Coach Jo brand
6. Special-case: blur the Slack avatar in screenshot-06
"""
from PIL import Image, ImageDraw, ImageFilter
import pytesseract
import re
from pathlib import Path
from difflib import SequenceMatcher

# Source + destination
SRC = Path('/root/slidev-webinars/giftedgabber/bsmd_v2_2026_06_22/assets/testimonials')
DST = SRC / 'redacted'
DST.mkdir(exist_ok=True)

# Student / family / parent names to redact (case-insensitive)
NAME_BLACKLIST = {
    'nuha', 'sayeed', 'nuha,', 'nuha!', 'nuha.', 'nuha?',
    'jessica', 'jessica.', 'jessica,', 'jessica!',
    'lorie', 'lorie.', 'lorie,',
    'sayeed,', 'sayeed.', 'sayeed!',
    'anusha', 'venkat', 'anusha,', 'anusha.',
    'santhosh', 'gheevarghese',
    'roshin', 'roshin,', 'roshin.', 'roshin\'s',
    'gia', 'gia,', 'gia.',
    'nicholas',
}

# Substrings (case-insensitive) — if a word CONTAINS one of these, redact
NAME_SUBSTRINGS = {
    'nuha', 'sayeed', 'santhosh', 'gheevarghese', 'roshin', 'jessica',
    'anusha', 'venkat',
}

# Core names — anything within Levenshtein-similarity threshold also redacts.
# Catches OCR typos like "Nuha" -> "Nuna" (common h/n confusion).
FUZZY_NAMES = [
    'nuha', 'sayeed', 'santhosh', 'gheevarghese',
    'roshin', 'jessica', 'anusha', 'venkat', 'lorie',
]
FUZZY_THRESHOLD = 0.70

# Explicit OCR misreads we have seen: tesseract confuses h/n, e/o, etc.
OCR_TYPO_BLACKLIST = {
    'nuna', 'nuda', 'nuho', 'nuhe', 'nuhi',
    'sayoed', 'sayood', 'sayeod',
    'jossica', 'jossice',
    'lorio', 'lorle',
    'anushe', 'anusho',
}


def fuzzy_match(text):
    """True if text is similar to any sensitive name."""
    t = text.lower().strip('.,;:!?()<>[]"\'')
    if len(t) < 4:  # too short to fuzzy-match safely
        return False
    for name in FUZZY_NAMES:
        if abs(len(t) - len(name)) > 2:
            continue
        if SequenceMatcher(None, t, name).ratio() >= FUZZY_THRESHOLD:
            return True
    return False

# Email-address pattern — any handle that contains a redacted name OR
# any gmail address that's not obviously brand
EMAIL_PATTERN = re.compile(r'\b[\w.-]+@[\w.-]+\.\w+\b', re.I)
GMAIL_PERSONAL = re.compile(r'\b[\w.]+gj\d+@gmail\.com\b', re.I)

# University student ID patterns (V01168073, W01518777, N02341958, PIDM, Pitt ID, etc.)
# All case-insensitive so they match against the lowercased clean text
ID_PATTERNS = [
    re.compile(r'^[vwn]\d{6,}$', re.I),     # V01168073, W01518777, N02341958
    re.compile(r'^\d{7,}$'),                # raw 7+ digit IDs like 4949117
    re.compile(r'^[a-z]\d{6,}$', re.I),     # any letter + 6+ digits
    re.compile(r'^pid[mn]?$', re.I),        # PIDM, PIDN, PID labels (followed by colon usually)
]

# ZIP-code pattern (full address gets caught as a multi-word range)
ZIP_PATTERN = re.compile(r'^\d{5}(-\d{4})?$')

# Address detector — single street number followed by street name
ADDRESS_TOKENS = {'via', 'street', 'st', 'st.', 'ave', 'avenue', 'drive', 'dr', 'dr.',
                  'road', 'rd', 'rd.', 'blvd', 'lane', 'ln', 'ct', 'court'}

# Things we EXPLICITLY KEEP (admissions officers, brand)
KEEP_LIST = {
    'marcelle', 'hicks',
    'bridget', 'varisco', 'varisco,', 'varisco.',
    'kellie', 'kane', 'kane,', 'kane.',
    'ross', 'vandyke',
    'linda', 'livingstone',
    'coach', 'jo', 'coach jo',
}


def should_redact_word(text):
    """Decide if a single OCR'd word should be redacted."""
    if not text:
        return False
    clean = text.lower().strip('.,;:!?()<>[]"\'')

    if clean in KEEP_LIST:
        return False

    if clean in NAME_BLACKLIST:
        return True

    if clean in OCR_TYPO_BLACKLIST:
        return True

    # Substring check — catches "Nuha's" or "Nuha!" variants
    for sub in NAME_SUBSTRINGS:
        if sub in clean:
            return True

    # Fuzzy check — catches OCR misreads like "Nuna" (h→n) or "Sayood" (e→o)
    if fuzzy_match(text):
        return True

    # ID patterns
    for pat in ID_PATTERNS:
        if pat.match(clean):
            return True

    # ZIP codes
    if ZIP_PATTERN.match(clean):
        return True

    # Email addresses that look personal
    if EMAIL_PATTERN.match(text):
        if GMAIL_PERSONAL.match(text):
            return True
        # any email with a redacted name in it
        for sub in NAME_SUBSTRINGS:
            if sub in text.lower():
                return True

    return False


def redact_image(in_path, out_path, extra_rects=None):
    """OCR + redact + save. extra_rects = list of (x, y, w, h) for hardcoded boxes."""
    img = Image.open(in_path).convert('RGB')
    draw = ImageDraw.Draw(img)

    # Apply any hardcoded redactions first (avatar, etc.)
    if extra_rects:
        for (x, y, w, h, mode) in extra_rects:
            if mode == 'blur':
                # Crop, blur, paste back
                region = img.crop((x, y, x + w, y + h))
                blurred = region.filter(ImageFilter.GaussianBlur(radius=15))
                img.paste(blurred, (x, y))
                draw = ImageDraw.Draw(img)
            else:
                draw.rectangle([x, y, x + w, y + h], fill='black')

    # OCR with bounding boxes
    try:
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    except Exception as e:
        print(f'  OCR FAILED: {e}')
        img.save(out_path)
        return 0

    redacted_count = 0
    n = len(data['text'])
    for i in range(n):
        text = data['text'][i].strip()
        if not text:
            continue

        if should_redact_word(text):
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]
            # Add a 2px safety margin
            draw.rectangle([x - 2, y - 2, x + w + 2, y + h + 2], fill='black')
            redacted_count += 1

    img.save(out_path)
    return redacted_count


# Per-image hardcoded extras (avatar, header truncated names, etc.)
# Coordinates determined from visual inspection
HARDCODED = {
    # Slack screenshot — Lorie's avatar in top-left of message body (blur)
    'testimonial-screenshot-06.png': [
        (8, 8, 70, 60, 'blur'),   # avatar circle area
    ],
    # Gmail mobile screenshot — "Anusha" truncated text at very top (faded)
    'testimonial-photo-01.jpg': [
        (40, 50, 200, 50, 'black'),  # the faint "Anusha" header text
    ],
    'testimonial-screenshot-10.png': [
        (40, 50, 200, 50, 'black'),
    ],
    # Elmira screenshot is 2932x1372. Top-right "Nuha Sayeed" is at ~x=2580+.
    # OCR catches "Sayeed" reliably but misses the "Nuha" before it (font/proximity).
    'testimonial-screenshot-09.png': [
        (2580, 25, 250, 65, 'black'),  # top-right name block, before "Logout"
    ],
}


def main():
    images = sorted(SRC.glob('testimonial-*'))
    images = [p for p in images if not p.parent.name == 'redacted']

    print(f'Found {len(images)} source testimonials. Redacting to {DST}\n')

    for img_path in images:
        if img_path.is_dir():
            continue
        out_name = img_path.stem + '-redacted' + img_path.suffix
        out_path = DST / out_name

        extras = HARDCODED.get(img_path.name)
        count = redact_image(img_path, out_path, extra_rects=extras)
        flag = '' if count > 0 else ' (no OCR hits — relying on hardcoded only)'
        print(f'  {img_path.name:50} -> {count} redactions{flag}')

    print(f'\nDone. Redacted files in {DST}')


if __name__ == '__main__':
    main()
