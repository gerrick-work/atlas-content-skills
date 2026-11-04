---
name: "atlas-content-engine"
description: "Plan, write, recycle and load batches of Atlas educational content (TikTok first) from the atom x format x hook library in Odoo Knowledge; also adds new guides and atoms."
---

# Atlas content engine

A delivery system, not a brainstorm. Every post is a **recipe**: one **atom** (a teachable truth) x one **format** (Guide F, F01 to F30) x one **hook** (Guide H, H01 to H60) x one **channel cut**. The engine never invents a topic from nothing; it combines approved parts, writes, checks, and loads to Odoo.

## 0. Where everything lives (Odoo, atlas-dsf.odoo.com)

- Knowledge > **Atlas Content Engine** (article 72): quality bar, guardrails, guide index
  - **Playbook: how the engine runs** (73)
  - **Guide F: 30 educational formats** (74)
  - **Guide H: 60+ hooks** (75)
  - **Atom bank (the facts)** (76)
  - **Guide A: What wins and loses in TikTok ads** (77): rules A01 to A10 from a 3,326-ad scan, the ad-cutting recipe and the loser checklist
  - any newer `Guide <letter>: ...` children (read them all; each multiplies the library)
- Project **Atlas Content Calendar** (project id 5): the ledger. Stages: Planned 27, Drafting 28, Design 29, Ready to post 30, Posted 31, Parked 32. Engine tasks are named `[TikTok · Carousel] <hook>` / `[TikTok · Reel] <hook>` and carry tags `TikTok` + `Carousel`/`Reel` + funnel + brand + `Hook: <family>` (+ `Check first`), with the recipe code in the description.

Read the Knowledge articles fresh at the start of every run (they change). Access Odoo through Claude in Chrome with JSON-RPC to `/web/dataset/call_kw` (`knowledge.article` / `project.task` `search_read`, `create`, `write`). For bulk data, write a JSON file in the scratchpad, inject a file input into the Odoo tab (`document.createElement('input')`, type file, an aria-label), find it with the Chrome `find` tool, push the file with `file_upload` (scratchpad paths work), and read it in page JS with `files[0].text()`. Never paste large payloads into a tool call.

## 1. Modes

| Request | Mode |
| --- | --- |
| "Fill / plan the calendar", "next week's posts" | **Plan + write + load** (sections 2 to 6) |
| "Recycle", "what worked", "repurpose winners" | **Recycle** (section 7) |
| "Make an ad from this post", "boost the winners" | **Ad cut** (section 7b) |
| A new poster, swipe file, data scan or guide | **Add a guide** (section 8) |
| New facts, comment questions, bench notes | **Add atoms** (section 9) |

Ask once (AskUserQuestion) only for what is genuinely missing: date range, cadence, and what happens to existing planned tasks (default: move them to Parked, never delete).

## 2. Assign recipes (code, not vibes)

Pull every existing engine task first so nothing repeats. Assign with a script in the scratchpad:
- 80% mass-market atoms (aud C/H), 20% niche (M/F).
- Same atom not within 10 days; an atom x format pair never repeats within 90 days.
- Formats: reel-type formats for reels, carousel-type for carousels (Guide F "Best as"); spread usage evenly.
- Hook family: one that fits the format (Guide H "Matching hooks to formats"); no family three posts in a row.
- Schedule any "part 2" a post's CTA promised before filling new slots.
- Default cadence: TikTok 1 carousel (1:00pm MYT) + 1 reel (8:30pm MYT) a day.

## 3. Write

For more than ~15 posts, split into batches of ~27 and run parallel writer agents with one shared brief, then review a sample yourself. Each post:
- Spine: **Problem > Explanation > Example > Takeaway**, one CTA.
- `hook` (on-screen, 7 words or fewer, blank filled with the specific detail) + 2 alternate hooks from other families (saved for reposts and ad variants).
- Carousel: 6 to 8 slides, slide 1 works alone, one idea per slide, one diagram slide.
- Reel: 15 to 30 s, faceless, no voice-over, on-screen text + music; beats with timestamps; open loop by 2 s, blunt answer by 5 s, pattern break, stakes line.
- Caption: first line restates the hook differently, CTA again, 4 to 6 hashtags (organic).
- Voice: a person slightly too obsessed with smell, Malaysian flavour, TikTok-simple, never cheap. Load `atlas-script-lab` for the AI-tell edit pass and CTA rules.

## 4. Quality gate (reject and rewrite if any fails)

1. One specific, surprising detail (molecule, number, mechanism, real scene).
2. One small problem solved; one takeaway.
3. Something to do or check today.
4. Sounds like a person, not a brand.

Guardrails: no em dashes; no brand or famous perfume names; no health scares; safe handling on screen; no religion or ethnicity angles; no shaming dupes or private label; never reveal stock, suppliers or tools; faceless; CTAs only to offers that are live (no kits, bundles, drops or lead magnets until Gerrick confirms they exist; a "DM us LAUNCH" answered by hand is fine). Any `CF` atom or new number: verify with a search or tag `Check first`. Illustrative numbers are labelled as examples on screen.

From Guide A (apply to organic posts too): never compare the scent to designer, luxury or niche perfumes (A06); no empty "long-lasting, smells amazing" claim (A07); no fake scarcity or deadlines (A09).

Script checks: JSON parses, no em or en dashes, slide and beat counts in range, hook length, AI-tell word list.

## 5. Load to Odoo

- Move superseded Planned tasks in the date range to Parked (never delete).
- Create one task per post: `date_deadline` in UTC (1:00pm MYT = 05:00, 8:30pm MYT = 12:30), tags as in section 0 (create missing tags first), description HTML with: recipe code, atom, hook + alternates, problem/explanation/example/takeaway/try-today, slide or beat table, music, CTA, caption, hashtags, check-before-posting list, sources.
- Read back: count per day, no gaps, no duplicate names.

## 6. Report

One short message: range covered, count, what needs checking before posting, and anything the CTAs promised that must be scheduled. No step recap.

## 7. Recycle (weekly, once posts have 7 days of data)

Gerrick supplies the numbers (TikTok views, saves, shares, watch-through) or they are read from the account. Rank within each format:
- **Winner** (top 20%): IG cut + affiliate repost pack within a week; same atom in 2 new formats within 30 days; repost with an alternate hook after 45 days; flag as ad candidate (then section 7b).
- **Middle**: same atom once more with a new hook family.
- **Flop** (bottom 20%): change hook first, then format; park the atom after 3 flops.
- **Comments**: each real question becomes a new atom (F07 or F20).

A recycle always changes at least one part of the recipe; never repost an identical video. Log outcomes on the task (stage + a `Winner`/`Flop` tag).

## 7b. Ad cut (from an organic winner)

Follow Guide A, "How to cut an ad": 15 seconds or less; the real offer or the strongest claim in the first 2 seconds; call to action is a WhatsApp message or shop link, never "comment a word"; 2 or fewer hashtags; the post's two saved alternate hooks become the A/B variants; run the Guide A loser checklist before it goes into Ads Manager. Offers must be ones Gerrick has confirmed are live; if none, lead with the result and flag "no offer". Remember the scan measured clicks on paid ads, not sales and not organic performance.

## 8. Add a guide

When Gerrick shares a poster, swipe file or data scan: transcribe or summarise it faithfully (keep numbering and categories, state the evidence and its limits), give it a code letter, add an Atlas example per item and a when-to-use note, create it as a child of article 72, and add its row to the index table on article 72. Tell him in one line how it changes capacity (e.g. a 20-item CTA guide multiplies recipes by up to 20).

## 9. Add atoms

Append to the Atom bank (article 76) with the next ID; never renumber. Fields: pillar, audience, truth, surprising detail, example, try today, sells, status (V or CF). Atom test: if the detail could be written by someone who has never smelled a raw material, rewrite it.