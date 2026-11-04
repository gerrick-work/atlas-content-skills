---
name: "atlas-growth-loop"
description: "Run the Atlas Origins growth loop: hunt cross-industry winning content and offers, shortlist for Gerrick's review, produce daily posts, measure, promote winners to paid ads, and repeat."
---

# Atlas growth loop

One repeatable weekly loop for Atlas Origins (B2C, TikTok first, Instagram and Facebook second). It does not copy fragrance content. It finds winning **structures** in unrelated niches, strips them to their skeleton, and rebuilds them for Origins. Gerrick directs the creative; everything else runs on its own.

Every ad is a **creative x an offer**. Part 1 finds creatives, Part 2 finds offers. Both share one measurement layer and one winners library.

This skill orchestrates the existing skills. It never duplicates them:
- `atlas-content-engine`: Odoo library (Knowledge article 72), content calendar (project 5), recycle rules (section 7), ad cut (section 7b), add a guide (section 8)
- `atlas-script-lab`: hook, angle, body and CTA for every piece
- `explainer-reel`: premium video pipeline (US$1 cap per reel)
- `hypit` (Hypit skill): low-cost video pipeline (free local voice, own or stock footage, word-timed captions), and cloning a reference video's timing
- `atlas-origins-post-designs`: static carousels and posts
- `tiktok-caption-and-sound`: captions, hashtags, sounds
- `ship-content`: publishing to Meta after approval
- `small-business:ad-manager`: reading ad results and making approved ad changes

## Weekly rhythm

| When | Stage | Gerrick's time |
|---|---|---|
| Monday morning | 1 Hunt + 2 Shortlist (scheduled task) | none |
| Monday | 3 Review gate | about 30 min |
| Every day | 4 Produce, 5 Ship | approve each day's batch |
| Rolling, 72h after each post | 6 Measure | none |
| Sunday | 7 Winner selection (Gerrick picks what can drive sales) + scorecard | about 20 min |
| Monday | 8 Paid launch (new test ad set) + 9 Offer loop | approve spend |

**Cadence: 1 to 3 reels and 1 to 2 statics every day** (14 to 35 pieces a week). Volume never lowers the bar: the content engine quality gate (section 4) applies to every piece.

**Production cost control.** At this volume, premium reels add up (US$1 each through `explainer-reel`, so up to about US$21 a week at 3 a day). Default daily mix: 1 premium reel (`explainer-reel`) plus the rest as low-cost reels (`hypit` with the free local voice, own footage or stock) and statics. Track weekly generation spend on the scorecard and ask before going above US$10 a week.

Use the task list: one task per stage.

## 1. Hunt (cross-industry, measured, low-cost)

**Niches.** Rotate 5 or 6 each week, all outside fragrance. Prefer sellers of boring, technical or low-ticket things, because they have to win on structure: car parts and car care, plumbing and home repair, tax and accounting services, skincare and haircare, coffee and tea, cooking tools, pet products, supplements, stationery, DIY and hobby kits, phone repair, cleaning products. Log which niches were used so they rotate.

**Pipeline: collect, then tag in bulk with Jev, then Claude reviews the top candidates.** No Apify (it needs a subscription Gerrick does not want).

### Step A: collect

**Primary: ScrapeCreators API** (pay as you go, credits never expire, about 1 credit per request; reachable from the cloud workspace, so the scheduled Monday run works without Gerrick's computer). The API key lives in the workspace as the environment variable `SCRAPECREATORS_API_KEY`; never print it or write it into files. Check the balance at the start of each run and report credits used on the scorecard. Endpoints used:

| Need | Endpoint | Winner signal to capture |
|---|---|---|
| Organic TikTok per niche | `/v1/tiktok/search/keyword`, `/v1/tiktok/search/hashtag` | views, likes, shares, saves, author |
| Outlier ratio | `/v3/tiktok/profile/videos` for each candidate's creator | views divided by the creator's median views over recent posts; keep 10x or higher |
| What was said | `/v1/tiktok/video/transcript` (top candidates only) | spoken script for the beat breakdown |
| Paid TikTok structures | `/v1/tiktok/ad-library/search` | ad run length, reach where given |
| Static layouts | `/v1/pinterest/search` (carousel, infographic, poster, packaging per niche) | saves relative to the account's typical pin |
| Paid structures and offers on Meta | `/v1/facebook/adLibrary/search/ads` (Malaysia) | ads running 30 days or more |

Budget per weekly hunt: about 150 to 250 credits (6 niches). Stop and ask if a run would pass 400 credits. Read the endpoint docs (docs.scrapecreators.com) for exact parameters and per-endpoint costs before the first call of each kind; cached results are free.

**Free fallback: Claude in Chrome on Gerrick's computer** (read the `chrome-browser` skill first) for TikTok Creative Center Top Ads (filter Malaysia and each niche's industry; capture CTR, likes and rank in industry), TikTok and Pinterest search pages, and Meta Ad Library. Extract with page JavaScript into a CSV. Use this when credits run low or an endpoint fails. Creative Center has no API route, so it is always collected this way when used.

Save everything per run to `hunt/<YYYY-MM-DD>/` as CSV: link, niche, platform, caption or on-screen text, duration or slide count, metrics, creator, and the cover image (download immediately; cover URLs expire within hours). Raw views alone never qualify a post: a big account's average post is not a winning structure. Never quote captions, lyrics or slogans verbatim anywhere downstream.

**Also reuse what exists.** The 16 Oct scan (`tiktok_ad_wall_3326_ads.csv`, 3,326 product ads, already tagged) covers many non-fragrance categories. Re-rank it on CTR alone within each category (the earlier 60/40 CTR and likes score overweighted likes), and mine its non-fragrance winners before spending new credits.

### Step B: tag in bulk (Jev)

Use the OpenRouter `batch_generate` tool with model `typesafe/jev-router`, temperature 0, one CSV chunk per call, on Gerrick's computer (CSV in `~/Atlas/OpenRouter Outputs/hunt/<date>/`). System prompt: answer immediately; return only one line of compact JSON with keys:
- `category`
- `format` (talking_head, voiceover_broll, text_on_screen, demo, before_after, listicle, skit, slideshow_carousel, static_poster, ugc_review, other)
- `hook_type` (question, bold_claim, problem_callout, pov_relatable, before_after, demo_result, price_shock, curiosity_gap, social_proof, urgency_scarcity, promo_discount, storytime, comparison, tutorial_howto, trend_meme, none_visible)
- `angle` (transformation, price_value, convenience, status_luxury, health_safety, novelty, emotional_gift, authority_expert, community_trend, other)
- `cta` (shop_basket, link_in_bio, comment_keyword, dm_whatsapp, limited_offer, follow_save, none)
- `offer` (none, free_shipping, bundle, bogo, free_gift, discount, sample, cod, other)
- `keywords` (up to 5 topic keywords, English)
- `hook_summary` (max 12 English words, own paraphrase, never quoting)
- `confidence` (0 to 1)

State the estimated OpenRouter cost before running; it is usually cents. Jev only classifies; it does not judge visuals or write.

### Step C: review (Claude)

Rank by the winner signal, take the top 30 to 40, and look at each one properly: cover image, frames and transcript where available (Hypit can download and transcribe; if a download is blocked, say so and work from the cover, transcript and tags).

## 2. Shortlist (structure cards)

Produce 15 to 20 structure cards, roughly 60% video and 40% static. Each card:

- Source link, niche, platform, and the measured evidence (outlier ratio, CTR rank, run length or saves)
- Jev tags: format, hook type, angle, CTA, offer, keywords
- **Hook mechanic** (what it does, e.g. hidden-markup reveal, wrong-way demo, "I tested X so you don't have to"), not its wording
- **Beat sequence**: hook, tension, proof device, payoff, CTA, with rough timings
- **Visual devices**: text placement, cut rhythm, props, layout grid (for statics)
- **Why it worked**: written as interpretation, labelled as such
- **Atlas Origins transplant**: one-line pitch of our version, the atom it would use (content engine atom bank), and the format
- Funnel role: Discover, Trust or Convert

Transplant example: a mechanic saying "the part your dealer charges RM800 for costs RM40" is a hidden-markup reveal. The Origins version: "that RM500 bottle is mostly one molecule you can buy for RM12.90". Check against guardrails (no named brands, no designer comparisons).

Present the cards as one page (an artifact) with the cover images and links.

## 3. Review gate (Gerrick, AI assisted)

Ask with AskUserQuestion (multi-select) which cards to run, and collect his direction notes per pick (tone, twist, what to avoid). At this cadence he usually picks 10 to 15. Offer one AI suggestion per card for how to push it further, but his call decides.

Approved structures are saved to the library: add each as an entry in **Guide S: Cross-industry structures** (child of Knowledge article 72, codes S01, S02, ...), following content engine section 8. Each structure can be reused with new atoms, which multiplies the library.

Create one Odoo task per post in the Atlas Content Calendar (project 5) with tag `Loop` and the structure code in the description.

## 4. Produce

For each approved card:
1. `atlas-script-lab` writes the angle brief from the structure card and Gerrick's notes.
2. Video: `explainer-reel` for the daily premium reel; `hypit` for the low-cost reels and for structures that depend on word-timed cuts or captions.
3. Static: `atlas-origins-post-designs`. Pinterest pins are **layout references only**. Rebuild the layout in our own design, or send a written brief to an OpenRouter image model (Gerrick's standing preference). Never reuse the pin image.
4. `tiktok-caption-and-sound` for caption and sound.
5. Run the content engine quality gate and guardrails.

**Originality rule (hard):** never reuse another creator's footage, images, music or exact wording. Take the structure only. Copies get accounts flagged.

Send each day's batch to Gerrick as soon as it is ready, so he can redirect early.

## 5. Ship

- Instagram and Facebook: hand off to `ship-content` (its own approval gate applies).
- TikTok: manual upload for now. Give Gerrick the file and caption in plain chat text (no code block). Auto-posting needs a TikTok business API setup; only build that if he asks.
- Move the Odoo task to Posted and record the post URL.

## 6. Measure (72 hours after posting)

Pull each post's numbers: ScrapeCreators `/v2/tiktok/video` (or `/v3/tiktok/profile/videos` for the whole account) for our own TikTok posts, Claude in Chrome on our TikTok and Instagram analytics pages for hold and completion rates, or numbers Gerrick pastes or exports.

Score organic posts on:
- **Share + save rate per view** (primary)
- 3-second hold rate and completion rate when available
- Profile visits, shop clicks and product page views when available (the strongest sales signals)

Rank within the last 14 days of posts. Top 20% = Winner, bottom 20% = Flop, the rest Middle. Then apply content engine section 7 (recycle rules). Tag the Odoo task.

**Feed it back.** Write the result onto the structure's Guide S entry: uses, wins, flops. Next week's shortlist favours structure types with a higher win rate and drops a structure after 3 flops. Losers are logged too; the library learns from both.

## 7. Sunday winner selection (Gerrick)

Show the week's Winners with their numbers and a one-line note on sales potential for each (shop clicks, comment intent such as "where to buy", whether a live offer fits). Gerrick picks the ones he thinks can drive sales; only his picks go to paid. Cut each pick with content engine section 7b (15 seconds or less, offer or strongest claim in the first 2 seconds, 2 or fewer hashtags, its two saved alternate hooks as variants).

## 8. Paid campaigns

### Unit economics (recalculate when prices, fees or packaging change)

| | Single sample RM12.90 | Starter of 3 materials (about RM38.70) |
|---|---|---|
| Platform fees 22 to 28% | RM2.84 to 3.61 | RM8.51 to 10.84 |
| Product COGS (RM0.60 to 1.00 per 3g) | RM0.60 to 1.00 | RM1.80 to 3.00 |
| Packaging | to fill in | to fill in |
| **Break-even cost per purchase** | **about RM8 to 9, minus packaging** | **about RM25 to 28, minus packaging** |

A single RM12.90 sample leaves almost no room to buy a customer. Paid ads should therefore sell the **starter bundle or a basket offer** (Part 2), not the single sample, unless repeat purchase data shows the sample pays back later. Track average order value weekly.

### Where the money goes (RM250 a week, separate from the RM1,000 a month on Shopee)

- **TikTok paid ads: not yet.** TikTok Shop sales ads now run only as GMV Max, whose platform minimum is about US$50 a day, with US$100 to 200 a day and roughly US$1,000 of learning spend recommended. That is above this budget. TikTok growth comes from organic volume plus **affiliates** (commission only, no upfront spend, and already proven: affiliate reposts earned over RM1,000 since July). Revisit GMV Max when paid budget reaches about RM3,000 a month.
- **Meta: the testing and scaling ground**, because it allows small daily budgets.

### Meta structure: campaign > ad set > ad

- **Campaign** = the goal and who controls the budget. Use the Sales objective (or Traffic if no purchase tracking is available, see below).
- **Ad set** = one **angle** (the reason someone buys, e.g. price reveal, gift, make-your-own). Broad targeting: Malaysia, adults, no interest stacking. Advantage+ placements.
- **Ad** = one creative (a cut of an organic winner) plus copy and CTA.

Two campaigns only:

1. **TEST (ABO: budget set per ad set)**: 2 ad sets live at a time, about RM12 a day each (about RM170 a week). Each ad set holds 3 creatives on the same angle. A new ad set launches each Monday from Gerrick's Sunday picks; the weakest live ad set is switched off to make room.
2. **WINNERS (CBO or Advantage+: budget set at campaign level)**: about RM10 a day (about RM70 a week). Proven ads are moved in **by post ID** so their likes and comments carry over. Until the first winner exists, this budget stays in TEST.

At this spend, Meta will not exit its learning phase; that is expected. Judge on the rules below, not on Meta's learning status.

**Naming:** `ORIG_TEST_<week>` / `AS_<angle>` / `AD_<structure code>_<hook variant>`, e.g. `ORIG_TEST_W43 / AS_price-reveal / AD_S07_h2`. The scorecard maps every ad back to its Guide S structure.

### Tracking sales

Meta cannot see Shopee or TikTok Shop sales on its own. In order of preference:
1. **Shopee Collaborative Ads (CPAS)** from Shopee Seller Centre, which reports Shopee sales back to Meta (available in Malaysia since 2022). Check eligibility in Seller Centre before the first launch.
2. Otherwise a **Traffic** campaign to the Shopee listing, with a **unique Shopee voucher code per ad set** so sales can be matched.
3. **Click-to-WhatsApp** as a test lane (the 16 Oct scan found WhatsApp CTAs among the strongest), closed by hand on the WhatsApp Business line.

### Rules

- **Judge** an ad set after about 5 days or RM60 of spend, whichever comes first.
- **Kill** an ad that spends 2x the break-even cost per purchase with no sale. With a sale, give it 2 or 3 more days, then kill it if cost per purchase stays above break-even. Switch off an ad set when 2 of its 3 ads fail.
- **Scale** an ad with cost per purchase at or under break-even across at least 3 purchases: move it into WINNERS by post ID. Raise budgets by at most 20% every 2 days; never more than 50% at once.
- **Refresh** WINNERS with new proven ads weekly; winners fatigue.
- Every launch, budget change, boost or move needs Gerrick's explicit yes. Read results through `small-business:ad-manager`, Meta Ads Manager or exported reports.

## 9. Offer loop (Part 2)

Same cross-industry method, applied to offers.

**Hunt.** Long-running ads in Meta Ad Library (ScrapeCreators `/v1/facebook/adLibrary/search/ads`) and top listings on Shopee and TikTok Shop in other categories (coffee, tea, skincare, snacks, hobby kits, razors), tagged with Jev's `offer` field. Patterns to look for: sample-to-full-size credit, starter kit ladder (1, 3, 5 materials), bundle discount, free gift above a basket threshold, refill or subscription, build-your-own kit, try-before-you-buy.

**Offer card:** source and evidence, the mechanic, the Atlas Origins version, and checks:
- Margin at our COGS and 22 to 28% fees, against break-even cost per purchase (section 8)
- Fulfilment: can we pack and ship it at volume
- Compliance: labelling and claims (IFRA, GHS) for anything new we sell
- Platform rules on Shopee and TikTok Shop

**Test.** Gerrick approves an offer and makes it live in the shop. Test one offer at a time, on the current best creative (the control), so the result belongs to the offer. Change only one variable per test: new creatives run on the current best offer, new offers on the current best creative.

An offer appears in captions and CTAs only after Gerrick confirms it is live (content engine guardrail).

## 10. Weekly scorecard (Sunday)

One page:
- Posts shipped vs target (reels and statics), and the week's Winners, Middles, Flops
- Structure library win rates (best and worst structure types)
- Paid: spend, purchases, cost per purchase vs break-even, average order value, what was killed, kept or scaled
- Affiliate reposts and affiliate sales
- Offer test status
- Spend: OpenRouter generation, Jev tagging, ScrapeCreators credits used and remaining
- Next week's niches

## Hard rules

- No em dashes anywhere. Warm, plain wording.
- Never spend (scraping credits, AI generation, ads) without an approved estimate. Never publish without approval.
- Never copy another creator's assets or wording; structure only. Never quote captions or lyrics verbatim.
- Origins guardrails from `atlas-content-engine` and `atlas-script-lab` apply to every piece.
- Keep Gerrick's part to the Monday review, the Sunday winner pick and approvals. Do all technical setup yourself.