# Active initiatives (max 3)

Each: goal, KPI, deliverables, dates, read date, scale or kill rule, status. Status lines are dated and honest ("not checked" when not checked).

## 1. Paid ads test 1: Origins static product cards (Meta)

- Goal: find which ad family brings website buyers from outside Shopee.
- KPI: website orders and cost per order (ceiling RM15.65, break-even RM31.30); secondary link CTR and landing-page views.
- Live set: Meta campaign ORI_META_TRAFFIC_HOBBYIST_NOV26, RM40/day, 4 Nov 00:00 to 11 Nov 00:00 MYT (max ~RM280). Ads: SEARCH_H1_STATIC, PROBLEMS_H1_STATIC, MEME_H1_SAFFRON, MEME_H1_ROSE, BUT_H1_STATIC, linking to origins.atlasdsf.com/oils with UTM tags. TikTok ads not running.
- Watched daily by the "Atlas ads watcher" scheduled task (8:42am), which owns the day-by-day rules and the Atlas Origins Ads Dashboard (https://claude.ai/artifact/F2MhoWFSdvg2pqr99Uhmse). The Director reads its results; it does not re-check Ads Manager.
- Known gap: no Meta pixel, so Meta can't see sales; orders are matched in Odoo by UTM.
- Decide: 10 to 11 Nov. Winner gets fanned out with `atlas-remix` (3 new hooks on the winning family, held to one colour), losers off.
- Status 4 Nov 2026: day 1 live; results not read by the Director yet.
- Status 5 Nov 2026: under-delivering. Day 1 spent RM2.08 of RM40 (~5%), 507 impressions, 4 link clicks (all BUT_H1_STATIC), 2 landing page views, 0 website orders; 5 Nov RM0.02 by 8:42am (ads watcher dashboard). Cause not checked. At this pace the 10 Nov verdict has no data. Proposed to Gerrick: fix delivery inside the RM40/day cap and move the end date to keep 7 full days (max RM280 unchanged). Note logged on Odoo task 503.
- Status 6 Nov 2026: Gerrick has not answered the delivery fix; no change made. Ads watcher dashboard last updated 5 Nov 8:47am; today's 8:42am result not posted by 9:13am (not checked further). Odoo: first paid website order S00243, 5 Nov 22:28, Amber 3g + delivery RM17.80, paid by DuitNow QR, customer not a test account, no UTM, so it can't be credited to the ads. Checkout works end to end.

## 2. Shopee Discovery Kit launch

- Goal: lift Shopee AOV and give ads a better product to push (kit floor RM45.90 vs RM33 AOV).
- KPI: kit orders, Shopee AOV, ad ROAS on the kit (break-even ~1.65).
- Deliverables: new listing (3 Nov 2026), standalone Shopee ad, max RM100.
- Read: 10 Nov; decide 17 Nov.
- Rule: keep the ad if ROAS ≥ 2 at RM100 spent; otherwise fold the kit into Shop GMV Max and stop the standalone ad.
- Status 4 Nov 2026: listing and ad approved 3 Nov; live status not checked.
- Status 5 Nov 2026: live status still not checked. Odoo shows 1 Shopee order on 4 Nov (RM11.73), 0 so far on 5 Nov; no kit order visible.
- Status 6 Nov 2026: 1 Shopee order 5 Nov (RM94.62, contents not checked for a kit). Ad live status still not checked.

## 3. TikTok base for Atlas Origins

- Goal: give TikTok Shop a steady base. No organic videos means no trust for ad viewers and no reason for creators to join, so TikTok Shop has fallen to 1 or 2 orders a week.
- KPI: TikTok Shop orders per week (W42 peak 9); posts shipped; profile-to-shop taps.
- Deliverables: shop-linked TikTok renamed to Atlas Origins; 1 post a day (decided 4 Nov 2026); creator outreach reopens once 7 posts are up.
- Read: 18 Nov (2 weeks of posting).
- Rule: if posting holds 7/7 days and orders don't move by 25 Nov, the constraint is the offer or the shop page, not content; re-diagnose.
- Status 4 Nov 2026: cadence decided; rename and first posts not done; no TikTok posting skill in the repo yet. Decision card on the CEO Desk (task 531): how posts go up (A: Claude uploads via TikTok Studio after his tap, recommended; B: he posts from his phone), and whether the rename is done.
- Status 5 Nov 2026: card 531 still unanswered; 0 posts up. TikTok Shop 0 orders 3 to 5 Nov (Odoo).
- Status 6 Nov 2026: card 531 still unanswered (day 3), 0 posts up, TikTok Shop 0 orders 3 to 6 Nov. Brief for the first 3 posts drafted (execution/briefs/2026-11-06-tiktok-first-3-posts.md); no video made, no spend. Asked Gerrick in chat to pick the route; recommended B (he posts from his phone from files we send) to start today, since the cloud run can't reach his computer for TikTok Studio.
