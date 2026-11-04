---
name: atlas-remix
description: Turn one reference (a competitor or cross-industry post, ad, carousel, reel or UGC video, or our own winner) into a batch of on-brand Atlas variants across hooks, colours and formats, ready for approval. Use for remix, iterate, make variations, make versions of this, or more like this winner.
---

# Atlas remix (one idea in, many on-brand variants out)

Read `context/atlas-brand-context.md` first.

Gerrick finds or picks an idea. This skill does everything after that: works out why it works, rebuilds it in the Atlas voice, and makes the variations (hooks, colours, formats) so nobody redoes each one by hand.

It is the iteration layer. It does not replace the making skills; it feeds them:

| Output | Made with |
|---|---|
| Static ad (Origins) | `skills/03-static/ad-library` (`ad_library.py`, `vary` block) |
| Carousel or post | `atlas-origins-post-designs` (Origins B2C) or `atlas-social-posts` (DSF) |
| Reel, b-roll, UGC | `ai-ugc-production` for UGC, `video-direction` for every prompt, then `explainer-reel` or the UGC edit in `skills/04-video/ugc-video` |
| Hooks and lines | `atlas-script-lab` |
| Publishing / ads | `ship-content` (organic), `atlas-ads-manager` (paid) |

Task list: Breakdown, Translate, Variant plan, Produce, Contact sheet, Approval, Log and hand off.

## 1. Inputs

- **The reference:** an image, a video file, a link, a `stash` item, or one of our live ads (by name, e.g. `MEME_H1_SAFFRON`).
- **Account:** Atlas Origins (default for ads) or Atlas DSF.
- **How many:** default one batch = 3 hooks x 3 colours of the static (9) plus 1 video if the reference is a video.

Ask once (AskUserQuestion) only for what is missing. If the reference can't be seen (a link that won't load), ask for a screenshot or the file rather than guessing what it shows.

## 2. Breakdown (why it works)

Write `breakdown.md` in the run folder (`/home/claude/remix/<YYYY-MM-DD>-<slug>/`):

- **Situation:** the moment in the buyer's life it speaks to
- **Hook:** the first line or first frame, and the mechanism (flipped belief, search bar, callout, "nobody ...", trend audio)
- **Format:** layout or shot table (for video: time, framing, angle, move, action, line, sound, using the `video-direction` vocabulary)
- **Proof and visual:** what makes it believable
- **Why it works:** one sentence
- **Family:** which ad library family it belongs to (1 Search intent to 7 Offer). If none fits, say so: that's a new family or template.

Keep the structure, never the wording. No sentence, joke or tagline from the reference goes into our version (Gerrick's rule: AI is bad at reiterating copy; we copy skeletons, not words). Cross-industry references are the point: a car-parts ad's structure rebuilt for perfume beats a perfume ad copied.

## 3. Translate into Atlas

- Load `atlas-script-lab` for the hooks: one situation, 5 hooks in the buyer's own words, pick the best 3 (more if Gerrick asks).
- Origins buyer focus: people already buying perfume oils who want easy bases, plus mass-market "anyone can smell expensive". Products are the punchline, Smelly is the mascot.
- Prices, offers and proof must be real: take prices from origins.atlasdsf.com, never invent reviews, sales counts or deadlines.
- Brand voice: plain, warm, a little cheeky for Origins; measured for DSF; publicist voice ("the team at Atlas") for DSF company posts. No em dashes anywhere.

## 4. Variant plan (change one thing at a time)

Write `variants.md` as a table before making anything. Axes, in this order of value:

1. **Hook** (biggest effect): 3 to 5 per situation
2. **Format:** static, carousel, reel, UGC skit (same hook across formats)
3. **Proof or visual:** a number, a product close-up, a reaction
4. **Colour** (smallest effect, cheapest to test)

Each test ad set changes one axis only, so a winner tells us why it won. Colours by brand:
- **Origins ads:** white, saffron `#D8A23F`, rose `#E2A091`; green `#22473A` only on the meme template. Never grey.
- **Origins B2C carousels:** the flat green and lemon system in `atlas-origins-post-designs`; colour variants = swap which panel colour leads the cover.
- **Atlas DSF:** the white-first, green-gradient system in `atlas-social-posts`, one accent (saffron or rose clay) on one page only.

Names: `FAMILYCODE_H#_FORMAT` (e.g. `MEME_H4_ROSE`, `UGC_H2_LATE`). Check the creative tracker and `specs.json` first so a new hook never reuses a live H number.

## 5. Produce

**Static ads.** Work in `skills/03-static/ad-library/` of the pulled repo. Add one spec with `code`, `h_start` and a `vary` block of hooks and colours, then:
```
python3 ad_library.py new.json out/ --dry     # list the names first
python3 ad_library.py new.json out/           # render every variant + _contact_sheet.png
```
Setup and product cut-outs are at the top of `ad_library.py`. If the reference's layout has no template yet, build it as a new template function next to the others (same lockup, CTA, margins), rebuild the reference near pixel for pixel with only words, products and colours changed, and add its family to the README.

**Carousels.** Run the matching carousel skill with the translated angle; make each colour variant from the same copy.

**Video and UGC.** Load `video-direction` (and `ai-ugc-production` for UGC: brief, three hooks with the body held constant, short test first, QC rubric). Breakdown shot table, then a shot plan per hook, run `shot.py`, show cost, generate, QC. Same hook as the static so the two can be compared.

## 6. Approval (one click)

Send one contact sheet (all variants, names under each) and the caption or line for each hook. Then one AskUserQuestion, multiSelect: which variants go live. Short bullets only; Gerrick approves, he doesn't plan.

## 7. Log and hand off

- Append approved static specs to `skills/03-static/ad-library/specs.json` and commit.
- Add each approved ad to the creative tracker in the Paid Ads Plan doc (name, family, hook, colour, date).
- Paid: hand to `atlas-ads-manager` for the Test campaign. Organic: hand to `ship-content`.
- Save any new template, shot plan that worked, or lesson (what failed and the fix) back into this repo (the skill it belongs to, or `video-direction/templates/`) and commit, so the library grows every run.

## Standard rules (every variant)

- Mark + ATLAS ORIGINS lockup, large, centred at the top (Origins).
- Text at least 70px from every edge; never grey backgrounds; only the headline bold on social posts.
- One green CTA with the real price, origins.atlasdsf.com in bold, Shopee and TikTok Shop as a small secondary line. Ad links go to the website.
- Smelly or AI personas only: never real people, celebrities, creators' faces or other brands' characters. AI video gets the platform's AI label and stays a skit, never a fake testimonial.
