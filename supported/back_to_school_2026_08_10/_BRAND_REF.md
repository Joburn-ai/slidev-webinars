# BRAND REFERENCE — SupportED Tutoring

**Built 2026-08-16 from the live site, the VSL render pipeline and this deck's build.**
Per `deck_production` §4.2. Read before designing any SupportED asset.

## Palette — fills and type tokens are DIFFERENT tokens

| Token | Hex | Job | Verified |
|---|---|---|---|
| navy | `#1B365D` | the shout ground | white on it = 12.12:1 |
| ink | `#111111` | darkest ground | |
| cream | `#E8E0D0` | warm light ground | |
| wash | `#F5F6F8` | card ground | navy on it = 11.21:1 |
| **gold FILL** | `#C5A55A` | rules, borders, the gold ground, chip stroke | 🔴 **fill only** |
| gold TYPE on light | `#8A6D2B` | gold text on white/cream | 4.88:1 |
| gold TYPE on dark | `#D8BC77` | gold text on navy/photo | 6.57:1 |
| red fill / type | `#C0392B` / `#A32B20` | trap, loss, FALSE | type 6.00:1 on its tint |
| green fill / type | `#1E8449` / `#14663A` | correct, TRUE, the win | type 6.16:1 on its tint |
| fog border | `#8494A6` | 1px borders | 3.10:1, clears WCAG 1.4.11 |
| fog type | `#4A5765` | secondary type | 7.39:1 |

🔴 **`#C5A55A` fails WCAG AA in BOTH directions** — white on it is 2.36:1 and it on white is
2.36:1. It is a FILL. Gold text takes `--goldi` on light grounds and `--goldl` on dark.
🔴 **Gold ground carries NAVY or INK type, never white.**

## Typefaces — matched to the render pipeline, not chosen

**Display: Merriweather. Body: Manrope.** Not a preference: the VSL scene frames placed
full-bleed through the deck were RENDERED in these, so anything else makes every placed
frame read as spliced in from another deck.

Source of truth: `06_Clients/supported/05_assets_and_deliverables/vsl_v3_render/assets/fonts/`

Cut as static instances, self-hosted, 73KB total. Display is instanced at **opsz=96** (a
real display cut) and never set below 2.80rem. Manrope's weight axis **maxes at 800** —
`font-weight: 900` on a sans element is unbuildable.

## Imagery register

**Polished-direct**, with flat-vector concept plates. Never photorealistic-generated people.

- `concept/c01-c10` — flat editorial illustration, text-free, on-palette. The house look.
- `vsl/*` and `scene/*` — finished 1920x1080 frames from the VSL render, own typography,
  used FULL-BLEED with no overlay. Scene crops are 1920x861 (caption band removed).
- `uni/*` — real product screenshots, PII-redacted.

## Proof assets, with compliance status

| Asset | Status |
|---|---|
| `proof/reviews_band_456.png` | ✅ rating + count only, no names |
| `proof/team_band.png` | ✅ real team page crop, roles only, no claims |
| `students/{Nabila,Laura,Avery}` | ✅ the ENTIRE cleared name set |
| `students/` others (6) | ❌ not cleared |
| `proof/wall_of_love` + Senja wall | ❌ names ~10 uncleared families, hard claims |
| `proof/ap_section_..._breakthroughs` | ❌ names Taylor, Aleeza, Payton, Christian, David |
| `ads/*` (12) | ❌ paid-ad creative: $47 CTA, uncleared student |
| `_quarantine/joe-conf.AI-GENERATED.png` | ❌ AI-generated photo of a real person |

## 🔴 Their own published disclaimer — this binds every claim

From supportedtutoring.com:

> "SupportED Tutoring is an independent test preparation and education services provider and
> is **not affiliated with, sponsored by, or endorsed by the College Board** or any other
> testing organization or educational institution. **Individual results vary and are not
> guaranteed.**"

Consequences: never "College Board certified" (say **certified AP teacher**); never promise
a score. One coach IS a verifiable **AP Calculus Reader** — that is a real credential and it
belongs to one person, not to "our coaches".

## Real credentials worth using

- 14 coaches, each a subject specialist (supportedtutoring.com/supported-team)
- Coach Nicholas: **AP Calculus Reader** — has scored the real exam
- Dr. Joe Sebestyen: Doctorate in Educational Leadership
- 456 reviews
