---
layout: center
---

<!-- slide:findings-divider-01 -->

<div class="oa-ghostnum">03</div>

<div class="relative z-1 px-16" style="max-width: 56rem;">

  <div class="oa-eyebrow rust">Section 03 <span class="dim">· what the audit found</span></div>

  <div class="oa-h1 mt-3">What the audit found</div>

<v-clicks>

<div class="oa-lead mt-5">Run live on Monday August 3, against the synced GHL mirror and against the pages as they actually render in a browser.</div>

<div class="oa-meta mt-6">nothing in this section is an opinion. four findings, and every one of them moves a date.</div>

</v-clicks>

</div>

<div class="oa-footer">the audit · live capture, 2026-08-03</div>

<!--
HOOK: This next part is the audit, and it is the reason to trust everything after it.
BEATS:
  - "So that is the estate. Here is what I found when I actually went and looked at it on Monday."
  - (click) "Two places. The synced GHL mirror, so real counts and not a dashboard summary. And the live pages, loaded in a real browser, so what is actually there and not what should be there."
  - (click) "Nothing in this section is my opinion. There are four findings, and every single one of them moves a date in August. That is why the audit comes before the calendar and not after it."
TIMING: 20 sec
TRANSITION: "Here they are, in order of what they cost us."
-->

---
layout: default
---

<!-- slide:findings-map-02 -->

<div class="px-16 pt-9">

<div class="oa-eyebrow rust">The audit <span class="dim">· four findings, in order of cost</span></div>

<h2 class="oa-h2 mt-2">Four things are broken. <span class="oa-rust-t">All four are fixable.</span></h2>

<div class="mt-6 flex flex-col gap-2" style="max-width: 54rem;">
<v-clicks>

<div class="oa-row blocker"><span class="tag">01</span><span>There is no webinar registration page. Not a weak one. None.</span></div>

<div class="oa-row blocker"><span class="tag">02</span><span>The 47 dollar page answers a security challenge instead of a sales page.</span></div>

<div class="oa-row blocker"><span class="tag">03</span><span>Half the list cannot be mailed at all.</span></div>

<div class="oa-row blocker"><span class="tag">04</span><span>Nothing captures attribution at the moment a call gets booked.</span></div>

</v-clicks>
</div>

<div v-click class="oa-lead mt-6" style="max-width: 52rem;">Two of them move dates. One of them changes the target. One of them is the reason July cannot be scored.</div>

</div>

<div class="oa-footer">the audit · the four blockers</div>

<!--
HOOK: Four lines, no unpacking yet. This is the map so nobody wonders where we are.
BEATS:
  - (click) "One. There is no webinar registration page. Not a weak one. None."
  - (click) "Two. The forty seven dollar page answers a security challenge instead of a sales page."
  - (click) "Three. Half the list cannot be mailed at all."
  - (click) "Four. Nothing captures attribution at the moment a call gets booked."
  - (click) "Two of those move dates. One changes the target we set tonight. And one is the reason July cannot be scored, by either of us."
TIMING: 30 sec
TRANSITION: "Number one is the one that changed the calendar, so let me just show you it."
-->

---
layout: default
---

<!-- slide:findings-b1-identical-03 -->

<div class="px-14 pt-8">

<div class="oa-eyebrow rust">Blocker 01 <span class="dim">· three urls, captured monday</span></div>

<h2 class="oa-h2 mt-2">Three different URLs. <span class="oa-rust-t">One page.</span></h2>

<div class="mt-5 grid grid-cols-3 gap-4">
<v-clicks>

<div>
  <div class="oa-shot"><img src="/images/01_ap_application_funnel.png" alt="supportedtutoring.com home page" /></div>
  <div class="oa-shotcap">supportedtutoring.com/</div>
</div>

<div>
  <div class="oa-shot"><img src="/images/04_webinar_reg.png" alt="supportedtutoring.com/webinars serving the home page" /></div>
  <div class="oa-shotcap rust">supportedtutoring.com/webinars</div>
</div>

<div>
  <div class="oa-shot"><img src="/images/07_supported_home.png" alt="supportedtutoring.com/tested-offer serving the home page" /></div>
  <div class="oa-shotcap rust">supportedtutoring.com/tested-offer</div>
</div>

</v-clicks>
</div>

<div v-click class="mt-5">
  <div class="oa-callout rustline">Not similar pages. <b>Byte for byte the same page.</b> One checksum across all three captures.</div>
</div>

</div>

<div class="oa-footer">blocker 01 · the slugs serve the homepage</div>

<!--
HOOK: The most persuasive thirty seconds in the deck. Let the pictures do the arguing.
BEATS:
  - (click) "That is the SupportED homepage."
  - (click) "That is slash webinars."
  - (click) "And that is slash tested offer."
  - "Three different addresses. Same picture, three times."
  - (click) "They are not similar pages. They are byte for byte the same page, one checksum across all three captures. Those slugs do not exist, so the site quietly hands back the homepage instead of a 404. Which is worse than a 404, because nothing looks broken."
TIMING: 35 sec. Hold two full seconds after the callout before you speak again.
TRANSITION: "Which means one specific thing for the calendar."
-->

---
layout: center
---

<!-- slide:findings-b1-consequence-04 -->

<div class="px-14" style="max-width: 54rem;">

<div class="oa-eyebrow rust">Blocker 01 <span class="dim">· what it costs us</span></div>

<h2 class="oa-h2 mt-2">There was nothing to open.</h2>

<div v-click class="mt-6">
  <div class="oa-heroCard rustline">
    <div class="k">the plan said: open registration mon aug 17</div>
    <div class="v">A page that does not exist cannot open. Anyone who followed that link landed on the homepage with no form, no date and no event.</div>
  </div>
</div>

<div class="mt-4 flex flex-col gap-2">
<v-clicks>

<div class="oa-row ruling"><span class="tag">Fix</span><span>The registration page gets built Mon Aug 10 to Fri Aug 14. That is the entire reason a build week exists in this plan.</span></div>

<div class="oa-row ruling"><span class="tag">Cost</span><span>Registration runway drops to 9 days, Aug 17 into the webinar on Aug 26. Tight, workable, and not compressible again.</span></div>

</v-clicks>
</div>

</div>

<div class="oa-footer">blocker 01 · build lands aug 10 to 14</div>

<!--
HOOK: Level voice. This is a fact with a date attached, not a complaint.
BEATS:
  - "So when the plan said open registration Monday August 17, there was nothing to open."
  - (click) "A page that does not exist cannot open. Anyone who followed that link landed on the homepage. No form, no date, no event."
  - (click) "So the build moves forward, not back. The registration page gets built August 10 through 14. That is the whole reason there is a build week in this plan."
  - (click) "And it costs us runway. Registration is 9 days, the 17th into the webinar on the 26th. That is tight but workable, and I do not want to compress it a second time."
TIMING: 35 sec
TRANSITION: "Second blocker, and this one only bites us if we spend money."
-->

---
layout: default
---

<!-- slide:findings-b2-checkpoint-05 -->

<div class="px-14 pt-8">

<div class="oa-eyebrow rust">Blocker 02 <span class="dim">· the low ticket page, captured monday</span></div>

<h2 class="oa-h2 mt-2">The 47 dollar page answers <span class="oa-rust-t">a challenge.</span></h2>

<div class="mt-5 grid grid-cols-5 gap-6 items-start">

  <div class="col-span-2">
    <div class="oa-shot"><img src="/images/02_lt_gameplan_47.png" alt="Vercel Security Checkpoint served on the game plan page" /></div>
    <div class="oa-shotcap rust">gameplan.supportedtutoring.com · 403</div>
  </div>

  <div class="col-span-3 flex flex-col gap-2">
  <v-clicks>

  <div class="oa-row blocker"><span class="tag">What</span><span>A Vercel Security Checkpoint. A 403 to a real browser, from a non-residential IP.</span></div>

  <div class="oa-row blocker"><span class="tag">Who</span><span>A parent on a home connection most likely clears it. Link scanners and automated monitoring do not.</span></div>

  <div class="oa-row fix"><span class="tag">Fix</span><span>Load it from a home connection and confirm it before any cold spend. It blocks the cold lane, not the list lane.</span></div>

  </v-clicks>
  </div>

</div>

</div>

<div class="oa-footer">blocker 02 · verify from a residential connection first</div>

<!--
HOOK: A real risk with a cheap test in front of it. Do not overstate this one.
BEATS:
  - "That is what our forty seven dollar page served me on Monday."
  - (click) "A Vercel Security Checkpoint. A 403, to a real browser, from a non-residential IP."
  - (click) "A parent on a home connection most likely clears that challenge and never sees it. But link scanners, inbox previewers and any automated monitoring do not clear it. They get the 403. So we could be paying for clicks into a page that half the plumbing thinks is dead."
  - (click) "The rule is simple. Somebody loads it from a home connection and confirms it, before one dollar of cold spend. It blocks the cold lane. It does not block the list lane."
TIMING: 40 sec
TRANSITION: "Third blocker. This is the one that changes the target we set tonight."
-->

---
layout: default
---

<!-- slide:findings-b3-suppression-06 -->

<div class="px-16 pt-9">

<div class="oa-eyebrow rust">Blocker 03 <span class="dim">· the list, one number at a time</span></div>

<h2 class="oa-h2 mt-2">Half the list <span class="oa-rust-t">cannot be mailed.</span></h2>

<div class="mt-7 grid grid-cols-4 gap-4">
<v-clicks>

<div class="oa-stat"><div class="lbl">Total contacts</div><div class="val">14,639</div></div>

<div class="oa-stat"><div class="lbl">Unsubscribed</div><div class="val rust">4,975 <span class="oa-mute-t" style="font-size: 0.95rem;">34%</span></div></div>

<div class="oa-stat"><div class="lbl">Bounced</div><div class="val rust">2,363 <span class="oa-mute-t" style="font-size: 0.95rem;">16%</span></div></div>

<div class="oa-stat"><div class="lbl">Marked dnc</div><div class="val rust">321 <span class="oa-mute-t" style="font-size: 0.95rem;">2%</span></div></div>

</v-clicks>
</div>

<div v-click class="mt-8" style="max-width: 52rem;">
  <div class="oa-lead">That is not a worry about deliverability. It is a record of what has already happened to this domain.</div>
  <div class="oa-meta mt-5">counted from marketing.ghl_contacts, synced 2026-08-02. every figure is a count, not an estimate.</div>
</div>

</div>

<div class="oa-footer">blocker 03 · suppression, by category</div>

<!--
HOOK: ZOOM. Say every digit out loud. The unrounded number is the proof.
BEATS:
  - (click) "14,639 contacts in the file. That is the number everybody quotes, me included until Monday."
  - (click) "4,975 of them are unsubscribed. Thirty four percent."
  - (click) "2,363 have hard bounced. Sixteen percent."
  - (click) "321 are marked do not contact."
  - (click) "That is not a worry about deliverability in the future. It is a record of what has already happened to this domain, and the mail providers hold that same record."
TIMING: 40 sec
TRANSITION: "Dedupe the overlap and you get the one number the month gets planned against."
-->

---
layout: center
class: text-center
---

<!-- slide:findings-b3-ceiling-07 -->

<div class="mx-auto" style="max-width: 46rem;">

<div class="oa-eyebrow gold">Blocker 03 <span class="dim">· the real audience</span></div>

<h2 class="oa-h2 mt-3">Deduped, it is exactly half.</h2>

<div class="mt-6 grid grid-cols-2 gap-4">
<v-clicks>

<div class="oa-stat"><div class="lbl">Any suppression, deduped</div><div class="val rust">7,344</div></div>

<div class="oa-stat"><div class="lbl">Share of the file</div><div class="val rust">50%</div></div>

</v-clicks>
</div>

<div v-click class="mt-4">
  <div class="oa-stat hero"><div class="lbl">Mailable ceiling</div><div class="val gold" style="font-size: 3.4rem;">7,293</div></div>
</div>

<div v-click class="oa-meta mt-5">every august target gets built on this number.</div>

</div>

<div class="oa-footer">blocker 03 · mailable ceiling 7,293</div>

<!--
HOOK: STOP here. One number, and the whole month gets planned against it.
BEATS:
  - "Contacts sit in more than one of those buckets, so dedupe it."
  - (click) "7,344 suppressed, once the overlap is stripped out."
  - (click) "Exactly fifty percent of the file."
  - (click) "Which leaves 7,293 addresses we can legally and safely mail. That is the ceiling. Not the target. The ceiling."
  - (click) "So every August target gets built on that number. Forecast off 14,639 and we are forecasting off an audience that does not exist."
TIMING: 30 sec. Let 7,293 sit on screen before you click on.
TRANSITION: "And it gets thinner than that."
-->

---
layout: default
---

<!-- slide:findings-b3-tags-08 -->

<div class="px-16 pt-9">

<div class="oa-eyebrow rust">Blocker 03 <span class="dim">· and the engagement data is not real</span></div>

<h2 class="oa-h2 mt-2">The tags do not survive <span class="oa-rust-t">one minute of arithmetic.</span></h2>

<div class="mt-6 flex flex-col gap-2" style="max-width: 54rem;">
<v-clicks>

<div class="oa-row blocker"><span class="tag">Thin</span><span>Of the 7,293 mailable, only 671 carry any engager tag at all. That is 4.6%.</span></div>

<div class="oa-row blocker"><span class="tag">Odd</span><span>The 7 day, 30 day, 60 day and 90 day engaged tags all sit at exactly 1,687.</span></div>

<div class="oa-row blocker"><span class="tag">Why</span><span>Four different windows cannot return one identical number, and the newest email tag in the system is dated 2026-05-22. That is a one time bulk stamp, not a rolling calculation.</span></div>

</v-clicks>
</div>

<div v-click class="mt-5">
  <div class="oa-callout rustline">So the genuinely engaged core is <b>unknown.</b> The Aug 6 send is how we find out.</div>
</div>

</div>

<div class="oa-footer">blocker 03 · the engager tags are a bulk stamp</div>

<!--
HOOK: The arithmetic does the arguing. State it flat and let it land.
BEATS:
  - (click) "Of those 7,293, only 671 carry any engager tag at all. Four point six percent."
  - (click) "And here is the part that gave it away. Seven day engaged, thirty day, sixty day, ninety day. All four sit at exactly 1,687."
  - (click) "Four different windows cannot return one identical number. And the newest email tag anywhere in that system is dated May 22. So that is a one time bulk stamp somebody ran once, not a rolling calculation."
  - (click) "Which means the genuinely engaged core is unknown tonight. I do not have it and I am not going to invent a number for it. The August 6 send is how we find out."
TIMING: 40 sec
TRANSITION: "So here is the ruling that comes out of blocker three."
-->

---
layout: center
---

<!-- slide:findings-b3-ruling-09 -->

<div class="px-14" style="max-width: 52rem;">

<div class="oa-eyebrow gold">Blocker 03 <span class="dim">· the ruling</span></div>

<h2 class="oa-h2 mt-2">Build the target off <span class="oa-gold-t">7,293.</span> Never off 14,639.</h2>

<div v-click class="mt-6">
  <div class="oa-callout">The first job in August is not converting attention. <b>It is re-earning it.</b></div>
</div>

<div class="mt-4 flex flex-col gap-2">
<v-clicks>

<div class="oa-row ruling"><span class="tag">Aug 5-9</span><span>A deliverability ramp goes in front of the promo. No promotional sends that week.</span></div>

<div class="oa-row ruling"><span class="tag">Gate</span><span>We only leave that week on bounce under 2% on the Aug 6 send. If it is not clean, the list gets fixed before anything else ships.</span></div>

</v-clicks>
</div>

</div>

<div class="oa-footer">blocker 03 · ramp first, gated on bounce under 2 percent</div>

<!--
HOOK: A gold beat. This is a ruling, and it protects everything after it.
BEATS:
  - "So the ruling. We build the August target off 7,293, never off 14,639. Any forecast off the big number is fiction, and it will make a good month look like a failure."
  - (click) "And the first job this month is not converting attention. It is re-earning it. A file with a sixteen percent bounce history does not get blasted."
  - (click) "So a deliverability ramp goes in front of the promotion, August 5 through 9. No promotional sends at all that week. That week exists so the following four weeks land in an inbox."
  - (click) "And it has a gate. We only leave that week if bounce comes in under two percent on the August 6 send. If it is not clean, we fix the list before anything else ships, webinar promo included."
TIMING: 40 sec
TRANSITION: "Fourth blocker. This is the one I care about most, because it decides whether we can score August at all."
-->

---
layout: default
---

<!-- slide:findings-b4-attribution-10 -->

<div class="px-16 pt-8">

<div class="oa-eyebrow rust">Blocker 04 <span class="dim">· why july showed zero email attribution</span></div>

<h2 class="oa-h2 mt-2">The email motion is invisible <span class="oa-rust-t">by design.</span></h2>

<div class="mt-5 flex flex-col gap-2" style="max-width: 54rem;">
<v-clicks>

<div class="oa-row fix"><span class="tag">Works</span><span>The UTM is on the link. supportedtutoring.com/book-consultation-college433868?utm_source=email exists and fires.</span></div>

<div class="oa-row blocker"><span class="tag">Breaks</span><span>GHL stamps source and UTMs on the contact record at creation. A list member from 2024 who books off an email keeps their 2024 source forever.</span></div>

<div class="oa-row blocker"><span class="tag">Blind</span><span>marketing.ghl_appointments holds 0 rows for every client. Appointments were never added to the sync, so no booking count and no show rate is verifiable at all.</span></div>

<div class="oa-row blocker"><span class="tag">Stale</span><span>ghl_payments has written no row since 2026-04-21, while the sync log keeps reporting success.</span></div>

</v-clicks>
</div>

<div v-click class="oa-meta mt-4">not the automation, and not the team. the field is doing exactly what it was built to do.</div>

</div>

<div class="oa-footer">blocker 04 · attribution is stamped at creation, not at booking</div>

<!--
HOOK: Educational beat. Joe has to understand this mechanism or he keeps asking a question the data cannot answer.
BEATS:
  - "Neither July window showed a single email attributed booking. Here is why, and it is not the automation."
  - (click) "The UTM is on the link. That booking link with utm source equals email exists and it fires correctly. That part works."
  - (click) "But GHL stamps source and UTMs onto the contact record at creation. So a list member from 2024 who books off our email keeps their 2024 source forever. The email that earned the booking can never get credit for it."
  - (click) "Then it gets worse. Appointments were never added to the sync at all. Zero rows, for every client. So no booking count and no show rate is verifiable by anybody, me included."
  - (click) "And payments have not written a row since April 21, while the sync log keeps reporting success. That one is just quietly wrong."
  - (click) "So it is not the automation and it is not the team. That field is doing exactly what it was built to do. We were asking it the wrong question."
TIMING: 50 sec
TRANSITION: "Three fixes, and the first one has a hard date on it."
-->

---
layout: default
---

<!-- slide:findings-b4-fix-11 -->

<div class="px-16 pt-9">

<div class="oa-eyebrow">Blocker 04 <span class="dim">· the fix, in three moves</span></div>

<h2 class="oa-h2 mt-2">Attribution becomes <span class="oa-teal-t">a query.</span></h2>

<div class="mt-6 flex flex-col gap-2" style="max-width: 54rem;">
<v-clicks>

<div class="oa-row fix"><span class="tag">Aug 6</span><span>A hidden UTM field on the booking form, written per booking. Before the first send, or August is as unmeasurable as July.</span></div>

<div class="oa-row fix"><span class="tag">MVP2</span><span>An append only attribution_touches table. Every touch is its own row, so first touch, last touch or any touch is a question we ask, never a column we overwrite.</span></div>

<div class="oa-row fix"><span class="tag">August</span><span>Appointments get added to the sync and payments get unstuck. The appointments table already exists. It is just empty.</span></div>

</v-clicks>
</div>

<div v-click class="mt-5">
  <div class="oa-callout">One rule underneath all three: <b>capture at the event, never stamp on the record.</b></div>
</div>

</div>

<div class="oa-footer">blocker 04 · capture at the event</div>

<!--
HOOK: The mechanism, with dates on it. Show the shape, do not sell it.
BEATS:
  - (click) "First, before the August 6 send goes out, a hidden UTM field on the booking form that writes per booking. Not per contact. Per booking. If that is not live by Thursday, August is exactly as unmeasurable as July and we have this same conversation in September."
  - (click) "Second, with MVP2, an append only attribution touches table. Every touch is its own row. Then first touch, last touch or any touch is a question we ask of the data, instead of a column somebody overwrote in 2024."
  - (click) "Third, still in August, appointments get added to the sync and payments get unstuck. The appointments table already exists. It is just empty, which is why nobody caught it."
  - (click) "One rule sits under all three. Capture at the event, never stamp on the record. Get that right once and we stop guessing for good."
TIMING: 45 sec
TRANSITION: "One last honest thing before we get to August."
-->

---
layout: center
---

<!-- slide:findings-honesty-12 -->

<div class="px-14" style="max-width: 52rem;">

<div class="oa-eyebrow rust">One more honest thing <span class="dim">· then august</span></div>

<h2 class="oa-h2 mt-2">6 of 18 July opportunities <span class="oa-rust-t">disagree with themselves.</span></h2>

<div v-click class="mt-6">
  <div class="oa-heroCard rustline">
    <div class="k">stamped won_at, sitting in a stage that is not won</div>
    <div class="v">Same six deals, two fields, two different answers. Neither field is lying. They were written by different actions at different times.</div>
  </div>
</div>

<div v-click class="mt-4">
  <div class="oa-callout rustline">A revenue figure from one field will not match the other. <b>Name the field, or do not quote the number.</b></div>
</div>

</div>

<div class="oa-footer">honesty · say which field you counted</div>

<!--
HOOK: Deliberately flat and unafraid. Volunteering this is what makes every other number in the deck credible.
BEATS:
  - "Last thing on the audit, and I would rather you hear it from me than find it later."
  - (click) "Six of the eighteen July opportunities are stamped won at, while sitting in a stage that is not won. Same six deals, two fields, two different answers. Neither field is lying. They were written by different actions at different times."
  - (click) "So any revenue number quoted off one of those fields will not match the other one. The rule from here is that we name the field we counted, or we do not quote the number at all. That applies to me first."
TIMING: 30 sec
TRANSITION: "That is the audit. Four blockers, all four with a date on them. Now August, week by week."
-->
