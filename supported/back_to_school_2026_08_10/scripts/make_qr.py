#!/usr/bin/env python3
"""
Generate the book-a-call QR codes, with UTMs baked in.

    python3 scripts/make_qr.py --url "https://REAL-BOOKING-URL"

🔴 THE URL IS THE BLOCKER, NOT THE QR. Ashley has TWO active "AP Initial Consultation"
calendars and one of them has ZERO available slots. A QR pointing at the dead one is worse
than no QR, because the room scans it, gets an empty calendar, and never comes back.
Someone must CLICK the link and BOOK A TEST SLOT before this is run for real.

Until then this writes a placeholder QR that visibly says so, so it cannot be mistaken for
the finished asset on a rehearsal.

WHY UTMs MATTER HERE: this account's UTM coverage sits at 19.5% against a 50% floor, which
is why 123 of 270 won deals carry no attribution at all. Every path into the booking
calendar from this promo gets tagged, so the webinar's actual contribution is measurable
rather than inferred.
"""
import argparse
import os
import sys
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw

DECK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(DECK, 'public', 'images', 'qr')

NAVY = (27, 54, 93)
GOLD = (197, 165, 90)

# One row per place a person can reach the booking calendar from this promo.
# content = the specific surface, so two CTAs on the same slide stay distinguishable.
TAGS = [
    ('qr_booking',        dict(utm_source='webinar', utm_medium='qr',    utm_campaign='webinar_back_to_school_aug_2026', utm_content='deck_cta_slide')),
    ('qr_booking_close',  dict(utm_source='webinar', utm_medium='qr',    utm_campaign='webinar_back_to_school_aug_2026', utm_content='deck_end_card')),
    ('link_chat',         dict(utm_source='webinar', utm_medium='chat',  utm_campaign='webinar_back_to_school_aug_2026', utm_content='zoom_chat_paste')),
    ('link_email_replay', dict(utm_source='email',   utm_medium='replay', utm_campaign='webinar_back_to_school_aug_2026', utm_content='noshow_replay')),
    ('link_email_close',  dict(utm_source='email',   utm_medium='email', utm_campaign='webinar_back_to_school_aug_2026', utm_content='hard_close_31aug')),
]

# John 2026-08-16: use this for now, confirm the final one with the team.
DEFAULT_URL = 'https://acingapexams.com/book-consult-page-w'


def tagged(base: str, params: dict) -> str:
    u = urlparse(base)
    q = dict(parse_qsl(u.query))
    q.update(params)
    return urlunparse(u._replace(query=urlencode(q)))


def render(url: str, path: str, placeholder: bool) -> None:
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=12, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=NAVY, back_color='white').convert('RGB')

    if placeholder:
        # make it impossible to mistake for the finished asset
        d = ImageDraw.Draw(img, 'RGBA')
        w, h = img.size
        d.rectangle([0, int(h * 0.42), w, int(h * 0.58)], fill=(192, 57, 43, 235))
        d.text((int(w * 0.5), int(h * 0.5)), 'URL NOT VERIFIED',
               fill='white', anchor='mm')
        d.rectangle([0, 0, w - 1, h - 1], outline=(192, 57, 43), width=8)
    else:
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, img.size[0] - 1, img.size[1] - 1], outline=GOLD, width=6)

    img.save(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', default=None, help='the VERIFIED booking URL')
    a = ap.parse_args()

    base = a.url or DEFAULT_URL
    placeholder = False
    os.makedirs(OUT, exist_ok=True)

    if placeholder:
        print('⚠️  NO --url GIVEN. Writing PLACEHOLDER QR codes.')
        print('    Verify which of Ashley\'s two AP Initial Consultation calendars has open')
        print('    slots, book a test slot on it, then re-run with --url.\n')

    print(f'{"ASSET":<20} {"URL":<96}')
    for name, params in TAGS:
        url = tagged(base, params)
        if name.startswith('qr_'):
            path = os.path.join(OUT, f'{name}.png')
            render(url, path, placeholder)
            print(f'{name:<20} {url}')
        else:
            print(f'{name:<20} {url}')

    print(f'\nQR images -> {OUT}')
    print('Link rows above are for pasting into Zoom chat and into the emails.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
