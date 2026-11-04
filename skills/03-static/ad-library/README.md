# Atlas Origins Ad Library

Every Atlas Origins ad belongs to one **family**. The family says what the ad is trying to do, which buyer it talks to, and where it goes in the ad account. A new ad is made by picking a family, picking its template, and writing new copy into the template's slots. The layout, logo, CTA and colours stay standard.

New ideas and iterations go through the `atlas-remix` skill, which breaks a reference down, writes the hooks and fans one spec out into variants here. Video prompts follow the `video-direction` skill.

## The families

| Family | Job of the ad | Buyer it talks to | Template | Campaign slot |
| --- | --- | --- | --- | --- |
| 1. Search intent | Show we are the answer to something they already want | Already looking ("how to make my own perfume") | `search` | Test, then Scale |
| 2. Problem to solution | Name their frustrations, then show the fix | Feels the problem, doesn't know the fix | `problems` | Test, then Scale |
| 3. Emotional / relatable | Make them laugh or feel seen, so the brand sticks | Never thought about DIY perfume | `meme` (Smelly hugging products) | Test; best for cold audiences and TikTok |
| 4. Product spotlight | One product, one benefit, one price | Curious, comparing shops | `presenter` (Smelly presenting) | Test, then Scale |
| 5. Education / how to use | Teach one thing; the product is the tool | Curious beginners | carousel, `atlas-origins-post-designs` skill | Organic first; winners become ads |
| 6. Proof | Real buyers or creators using it | Comparing, needs trust | affiliate or customer video (Spark ad) | Test (TikTok first) |
| 7. Offer / urgency | A real voucher, bundle or free shipping | Visited the shop, didn't buy | static with the offer as the headline | Retarget only |

Families 5 to 7 have no static template yet. Proof and offers must be real: no invented reviews, sales counts or fake deadlines.

## Copy formulas (fill the slots)

**1. Search intent** (`search`)
- `query`: the exact words a buyer types. Examples: "how to make my own perfume", "perfume that smells like pandan", "where to buy fragrance oil malaysia", "perfume ingredients for beginners".
- `hero`: the product shot that answers it (bottles, kit, one oil).
- `cta`: action + lowest real price ("Make your own, from RM9.90").

**2. Problem to solution** (`problems`)
- `problems`: 5 short complaints in the buyer's own words, 27 characters max each (the renderer refuses longer ones). Bank: "Everyone smells the same", "Niche perfume costs a bomb", "No idea where to start", "Big bottles, big commitment", "Classes are pricey", "Scent fades by lunch" (only with a product that fixes it), "Shopee sellers all look the same".
- `images`: 2 products that answer them.
- `cta`: "Try it from RM__".

**3. Emotional / relatable** (`meme`)
- `quote`: a common saying or belief, flipped. Pattern: "You can't ___" then show you can. Examples: "You can't make a signature scent", "Perfume is only for rich people", "Smelling expensive costs a fortune".
- `setup`: the punchline lead-in ("Me with RM35:").
- `images`: 3 products Smelly is hugging.
- `bg`: `saffron`, `rose` or `green` (test colours as separate ads).

**4. Product spotlight** (`presenter`)
- `quote`: a limit or "nobody" statement ("Nobody smells like dessert").
- `pivot`: "But.."
- `image`: the one product.
- `caption`: what it does for them; `accent`: one handwritten word to finish it ("deliciously.").
- `cta`: "Try it now, RM__".

## Variants (one spec, many ads)

Since 4 Nov 2026 a spec can fan out. Give it a `code` (MEME, SEARCH, PROBLEMS, BUT), an `h_start` (the next unused hook number) and a `vary` block:

- `vary.hooks`: a list; each entry overrides any slots (quote, setup, query, problems, images, cta...). Numbered H{h_start}, H{h_start+1}...
- `vary.bg`: a list of colours. Every template takes `white`, `saffron` and `rose`; `green` works on `meme` only. Grey is refused.

3 hooks x 3 colours = 9 ads, named `MEME_H2_SAFFRON` and so on. See `examples/variants-example.json` (15 ads from 2 specs). The renderer refuses duplicate names, problem lines over 27 characters, grey, and green on templates that can't take it. Every multi-ad render also writes `_contact_sheet.png` for one-look approval.

Test one axis at a time (hooks first, then format, then colour) so a winner says why it won.

## Standard rules (every ad)

- Large corporate mark + ATLAS ORIGINS, centred at the top.
- Backgrounds white, or saffron / rose / green for test variants. Never grey.
- One green CTA button with the real website price, origins.atlasdsf.com in bold under it, "also on Shopee and TikTok Shop" as a small secondary line. Ad links always go to the website.
- Smelly is the mascot. Never real people, celebrities or other brands' characters.
- Text kept 70px or more from the edges; no em dashes.
- Name: `FAMILYCODE_H#_FORMAT`, e.g. `MEME_H2_SAFFRON`. Log every new ad in the creative tracker in the Paid Ads Plan doc.

## How to make a new ad

1. Add a spec to a new JSON file (single ad: `name`; many: `code` + `h_start` + `vary`).
2. `python3 ad_library.py new.json out/ --dry` to list the names, then without `--dry` to render (setup steps are at the top of `ad_library.py`). `--only MEME_H3` renders just those.
3. Check the contact sheet, get approval, append the approved specs to `specs.json`, slot them into the Test campaign per the Paid Ads Plan.

## Files

- `ad_library.py`: the four templates, the variant expander, the contact sheet and the renderer
- `specs.json`: every live ad, by family (the live set from 3 Nov 2026)
- `examples/variants-example.json`: an example batch (not live)
- `mark_path.txt`: the corporate "A" mark as a vector path
