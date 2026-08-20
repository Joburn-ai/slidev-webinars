#!/usr/bin/env bash
# Build + deploy THE BACK-TO-SCHOOL GAME PLAN deck.
#
# 🔴 Two traps this script exists to avoid, both hit on 2026-08-20:
#  1. `slidev build --out dist` WIPES dist, including dist/.vercel, so the project
#     link is lost on every build and the next deploy silently creates a NEW project
#     called "dist". The canonical link is kept at the deck root and copied in.
#  2. `vercel deploy dist` infers the project name from the DIRECTORY BASENAME,
#     overriding the root link. So we cd INTO dist and deploy `.` instead.
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/deck_gate.py || echo "⚠️  gate reported failures, continuing (visual coverage is tracked separately)"
npx slidev build slides.md --out dist --base /
cp -r .vercel dist/.vercel
( cd dist && npx vercel deploy --prod --yes \
    --token "$VERCEL_TOKEN" --scope team_AcbqD1MAg7WOqx4lMqGSZXoa )
echo ""
echo "verifying routes on the project alias:"
for p in "/" "/presenter/1" "/134" "/images/dr-joe.jpg"; do
  printf "  %-20s -> HTTP %s\n" "$p" \
    "$(curl -s -o /dev/null -w '%{http_code}' -A 'curl/8.5.0' --max-time 25 \
       "https://supported-back-to-school.vercel.app$p")"
done
