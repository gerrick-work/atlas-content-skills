# Brief: website cart leak (draft, 7 Nov 2026)

Initiative: 1. Paid ads test 1 (Meta, website)
Problem: Meta ads now bring shoppers who add to cart, but none pay. Odoo, 6 Nov 00:11 to 7 Nov 09:13: 4 website carts tagged ORI_NOV26 (1 meta/paid, 3 ig/social), 13 items, about RM175, all still draft, all "Public user" (none filled in the details form). 0 paid website orders from ads.
Constraint (AARRR): Revenue. Acquisition works (5 Nov: RM11.90 spend, 94 link clicks, about RM0.13 a click, per ads watcher). Shoppers drop between cart and the details form.

## Checkout walk, 7 Nov 9:15am MYT (iPhone 13 emulation, nothing paid)

- /oils lists 87 products. The first one, Agarwood 3g, shows on the page but can't be added ("unavailable"). Others tested (Amber, Ambroxan, Arabian Oud Base, Bergamot and 7 more) add fine.
- Cart works. Sticky green "Checkout" bar works but sits over the "sign up for RM8 off WELCOME5" box.
- Cart shows "Delivery from RM4.90"; top banner says free delivery over RM100 (FREESHIP100). Ad carts were RM21.90 to RM77.40, so the free-delivery line is out of reach for every one of them.
- Details page: guest checkout allowed, 8 fields (name, email, phone, street, apartment, city, postcode, state). Payment step not walked.
- Test carts from this walk are S00257, S00258, S00259 (UTM source "test_director"). Exclude them. The 4 x RM12.90 carts at 13:00 on 6 Nov with no UTM look like a test too (not checked).

## Proposed fix (needs Gerrick's yes, changes price to buyer)

A. Free West Malaysia delivery over RM35 until the test verdict (11 Nov), on the Odoo delivery method "West Malaysia delivery" (free_over RM35), plus the top banner changed to say so. Cost only lands on orders that pay: RM4.90 each. Margin at RM35 is still well above cost (materials and packaging about RM1 to 1.20 per bottle). Not a Shopee voucher, so the 9 Oct "no margin-compressing Shopee campaigns" rule is not touched, but it is a discount and needs his yes.
B. Change nothing; judge the test on 10 Nov by carts and clicks, not orders.

Free without approval (Director will raise with Gerrick as ops items, not change): unpublish or restock Agarwood 3g on the website; move the WELCOME5 box above the sticky bar.

Read: 10 Nov with the ads verdict. Success: 1 or more paid website orders tagged ORI_NOV26 by 10 Nov.
Cause is not proven. Shipping cost is the likeliest cart-stage blocker we can change today; the other common one (people browsing, not ready) can't be fixed with settings.

## Update 8 Nov 2026: payment step walked (iPhone 13 emulation, nothing paid)

- Address form saves, then goes straight to /shop/payment. Delivery (RM4.90) is added there, so a RM12.90 item shows as RM17.80 for the first time on the payment page.
- Payment options: Debit / credit card, GrabPay, DuitNow QR, Apple Pay (coming soon). **No FPX online banking.** "Pay now" stays grey until a method is picked.
- Real shoppers since the last run: S00260 (chatgpt.com, RM30.80) reached the payment page and left without a payment attempt; S00266 (no UTM, RM60.50) saved details and stopped before delivery; S00262 (meta/paid, RM25.80) never filled details. No payment transaction since S00243.
- Test carts from this walk: S00267, S00268 (UTM source test_director, partner TEST Claude Director). Exclude.

Proposal (needs Gerrick's yes): A. switch on FPX online banking on the website payment provider (his login; which provider runs the card/GrabPay/DuitNow methods not checked, payment settings are off-limits to the Odoo connector) and send Odoo's cart reminder email to S00260 and S00266. B. change nothing; judge 10 Nov on clicks and carts.
Cause still not proven. Most ad carts never reach the details form; FPX only helps the few who reach payment.
