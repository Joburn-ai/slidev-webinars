"""Build slides_v8_short.md from slides_v8.md by removing the three named script cuts.

The three cuts come from SHOOT_constraint_roadmap_vsl_2026_08_09.md -> WORD COUNT AND RUNTIME.
Slide LABELS (the <!-- slide:NN --> comments), not route indices.
  cut 1: 18, 19, 20  -- the three "it is no longer as simple as" strikes
  cut 2: 29, 30, 31  -- the most agencies / coaches / consultants triplet
  cut 3: 89, 90      -- "that's our way of saying thank you" + "you showed up for you"
"""
import re, sys

SRC = "/root/slidev-webinars/internal/roadmap_vsl_2026_08_05/slides_v8.md"
DST = "/root/slidev-webinars/internal/roadmap_vsl_2026_08_05/slides_v8_short.md"
CUTS = ["18", "19", "20", "29", "30", "31", "89", "90"]

text = open(SRC).read()

# Slide boundaries: a line "---" immediately followed by a frontmatter key.
# Split keeps the delimiter at the START of each following chunk.
parts = re.split(r"\n(?=---\n(?:layout|class|clicks|transition|level|hide|routeAlias):)", text)
print(f"parsed {len(parts)} blocks (block 0 = the deck frontmatter + title slide)")

def label_of(block):
    m = re.search(r"<!--\s*slide:(\d+)", block)
    return m.group(1) if m else None

labels = [label_of(b) for b in parts]
missing = [c for c in CUTS if c not in labels]
if missing:
    sys.exit(f"ABORT: labels not found, refusing to guess: {missing}")

# count spoken words in the blocks we are about to remove
def spoken_words(block):
    total = 0
    for m in re.finditer(r'SPOKEN:\s*"(.*?)"', block, re.S):
        total += len(m.group(1).split())
    return total

removed_words = 0
kept = []
for b, lab in zip(parts, labels):
    if lab in CUTS:
        w = spoken_words(b)
        removed_words += w
        print(f"  - cutting slide label {lab}  ({w} spoken words)")
        continue
    kept.append(b)

out = "\n".join(kept)

# MANDATORY repair: slide 32's kicker reads "AND YES, AI" -- it continues the triplet that
# cut 2 just removed. Left alone it is an orphaned conjunction.
before = out
out = out.replace(
    '<div class="rt-kicker">AND YES, AI</div>',
    '<div class="rt-kicker">AND AI</div>',
)
if out == before:
    sys.exit("ABORT: could not find the 'AND YES, AI' kicker to repair")

open(DST, "w").write(out)

total_before = sum(spoken_words(b) for b in parts)
print(f"\nslides: {len(parts)-0} -> {len(kept)}  (removed {len(parts)-len(kept)})")
print(f"spoken words: {total_before} -> {total_before - removed_words}  (cut {removed_words})")
for wpm in (165, 180, 195):
    s = (total_before - removed_words) / wpm * 60
    o = total_before / wpm * 60
    print(f"  at {wpm} wpm: full {int(o//60)}:{int(o%60):02d}  ->  short {int(s//60)}:{int(s%60):02d}")
print(f"\nwrote {DST}")
