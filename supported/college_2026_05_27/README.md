# SupportED College Webinar. Wed 2026-05-27 Launch

## Status
GATE_2_PREVIEW

## Target live date
2026-05-27 20:00 EST (Wed). Recurring weekly Wed cadence after launch week.

## Presenter
Dr. Joe Sebestyen (live, Riverside).

## Source script
`/root/ai-os/06_Clients/supported/strategy/college_promo_2026_05_15/webinar_v3_full_script_reference_2026_05_17.md`

Canonical Google Doc: `https://docs.google.com/document/d/1teXURa2ADuPQpzaQ8IjdxcULX4icJIHx-vee-n6nVLw/edit`

## Foundational VSL alignment (Rule 14)
SupportED does not yet have a separate VSL script. The webinar v3 script serves as the foundational reference because: (a) F6 docs locked, (b) mechanism named (Four-Pillar System), (c) core arguments stress-tested across 14 sections, (d) em-dash zero verified, (e) Pass 2 per-block QC complete 2026-05-16/17. Treating as Rule 14 documented exception. Separate VSL build queued post-launch.

## Deck URLs
- Production: https://supported.slides.funnelfuturist.com/college
- Preview: pending first Vercel deploy
- Presenter mode: append `?presenter=1` to production URL

## Title
"AP Is Over. The Real Game Starts Now." (launch week. Recurring weeks rotate topic but keep "Parent Masterclass" wrapper.)

## Offer architecture
- Hero: AcceptED Senior Sprint at $6,997 (rising 11/12)
- Secondary: AcceptED College Blueprint at $9,997
- Premium: Premium Pathway at $18,997

## Audience
Rising 11 + rising 12 parents (cold-primary. existing clients invited inline.)

## Word count + slide target
Script: ~7,300 spoken words. Slide formula: words / 30 = ~243 target slides. Section ratios per Fladlien 400-slide hack:
- Opening (10-15%): 24-36 slides
- Teaching (40-50%): 97-122 slides
- Offer (25-35%): 61-85 slides
- Close (5-10%): 12-24 slides

## QC log
- Pass 1 (block-by-block copy QC): script PASS 2026-05-17 (em-dash zero, 6-Pillar mapped, Aha Stack threaded, mechanism reconciled)
- Pass 2 (slide-by-slide functional QC): pending after Opening section build
- Pass 3 (live deck): pending Vercel preview

## Asset registry
`SELECT * FROM cs.slidev_asset_registry WHERE client_id = (SELECT id FROM core.clients WHERE slug = 'supported') AND deck_slug = 'college_2026_05_27';`

## Cloudinary folder
`funnelfuturist/slidev/supported/college_2026_05_27/`

## Section file map
- `slides.md`. Entry + cover slide + src: includes
- `opening.md`. Fladlien sections 1-3 (Pop Quiz + Pain + Why Listen). Currently being built.
- `teaching.md`. Fladlien sections 4-5 (Mechanisms + Demo). Pending.
- `recap_momentum.md`. Fladlien sections 6-7. Pending.
- `offer.md`. Fladlien sections 8-12. Pending.
- `close.md`. Fladlien sections 13-14 + FAQ + CTA. Pending.

## Notes
- Recurring webinar format (not "Webinar 1 of 4"). Close embeds weekly cadence.
- 1435 spine integrated into Section 2 (Pain) and Section 5 (Mechanism 2).
- Two-case dichotomy (Family 1 / Family 2) is the load-bearing pain example.
- Verbatim attribution applied 3x (Sections 3, 7, 10): "Joe's spent 16 years inside the American education system. We've worked with over 30 families through college admissions specifically, and hundreds more across our AP and tutoring programs."
- [VERIFY] tags pending: Samiksha testimonial (Joe Slack confirmation), Andrew testimonial (mom's signed release), UIUC family, guarantee contract language.
