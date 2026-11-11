# Brief: ads test 2, winning chat ad sent to Shopee (drafted 9 Nov 2026, NOT approved)

Status: draft. Needs Gerrick's yes (spend + destination change). Nothing launched.

Initiative: 1. Paid ads test (Meta)
Deliverable: 1 ad set, the CHAT_H1_SCREENSHOT creative unchanged (plus BUT_H1_STATIC as the only backup), link changed from origins.atlasdsf.com/oils to the Atlas Origins Shopee shop. No new creative this week.
Skill: skills/05-ship-and-ads/atlas-ads-manager (the Origins campaign sits in an ad account the Meta connector can't read, so the link swap is done in Ads Manager by Gerrick from steps we send, or by a desktop-linked session)
Channel and placement: Meta (Facebook and Instagram), same audience as test 1 (Hobbyist)
Buyer and angle: people already buying perfume oils who want easy bases; "chat screenshot" angle, oils from RM9.90 (check the live Shopee price before launch)
Product and real price: Shopee shop front; live prices from Shopee, not this file
Constraints: RM20/day, 12 to 18 Nov 2026 MYT, max RM140 (moved 10 Nov from 10 to 16 Nov so 11.11 is outside the test). Single variable vs test 1: destination (website -> Shopee). No vouchers (9 Oct rule).
Done means: ad shows "Active" in Ads Manager with the Shopee link, screenshot sent
Read date and rule: day 3 (14 Nov) red flag check, decide 19 Nov. Keep if Shopee orders on ad days beat the same weekdays before 11.11 by at least RM20/day (break-even at ROAS 1.65 needs ~RM33/day extra sales); off if not.
Known weakness: the 11.11 lift can spill into 12 Nov; compare against the same weekdays before 11.11. Shopee doesn't pass UTM to Odoo; use Shopee Business Insights traffic source if it shows outside traffic (not checked).

Why: test 1 to 7 Nov: RM64.42 spent, 501 link clicks (RM0.13 each), 267 landing views, 0 website orders. Ads bring people; the website doesn't close. Shopee closes (3 orders RM413.50 on 8 to 9 Nov, first Discovery Kit order S00274).
Website fix (FPX online banking, asked 8 Nov) stays open in parallel; once it's live, website traffic gets re-tested.

## Link-swap steps for Gerrick (added 11 Nov 2026, about 5 minutes, only after his yes)

1. Ads Manager, campaign ORI_META_TRAFFIC_HOBBYIST_NOV26 (all ads show Ended since 11 Nov).
2. Tick the ad set, Duplicate, into the same campaign. Name it TEST2_SHOPEE_NOV26.
3. In the new ad set: Daily budget RM20. Schedule start 12 Nov 2026 00:00, end 19 Nov 2026 00:00 (Malaysia time). Audience unchanged.
4. Keep only 2 ads on: CHAT_H1_SCREENSHOT and BUT_H1_STATIC. Turn the other 4 off.
5. In each of the 2 ads, change Website URL to the Atlas Origins Shopee shop link (https://shopee.com.my/shop/202452044, open it on your phone first to check it lands on the shop) and keep the UTM tail as utm_source=meta&utm_medium=paid&utm_campaign=ORI_TEST2_NOV26.
6. Publish. Screenshot the ad set showing "Active" or "Scheduled" and send it here.
