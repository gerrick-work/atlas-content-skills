# Atlas Creative Tastebook (context file, read before any creative work)

Set 11 Nov 2026. Gerrick signed off the week 1 batch (16 to 22 Nov drafts) as "up to expectations and up to standard". This file is the permanent standard: every new post, carousel, reel storyboard, ad and LinkedIn image starts from one of the patterns below and follows the house style. When a skill file says otherwise, the newer dated rule wins; the colour rule is the 5 Nov 2026 one.

- Visual tastebook (all reference slides, tap to enlarge): https://claude.ai/artifact/HGt2sno2xtueia8cH5JkiH
- Reference images in the repo: context/tastebook/img/<ID>.jpg (720px wide previews)
- Atlas Rulebook still applies: https://claude.ai/artifact/PvNDXemVAigEKxPrHWi1Q7

## How the batch was made (repeat this exactly)

1. Plan the week from the marketing plan, then split into lanes: Origins carousels, Origins reels and Trial Reels, Origins ads, Atlas DSF posts, personal LinkedIn. One agent per lane, all reading one shared brief.
2. Hooks come from Gerrick's Taste Bank 4 and 5 ratings (list below). One idea per post, a different explainer layout per post.
3. Imagery: ONLY stock photos plus our own HTML/CSS/SVG editing. No AI image generation, no Canva generation. Pexels first (scrape https://www.pexels.com/search/<query>/?orientation=portrait with the Firecrawl scrape tool, formats ["links"], ids are in images.pexels.com/photos/<id>/ links), Unsplash second. Download with curl at w=1350. Look at every photo before using it.
4. Icons: the 3D icon library (skills/03-static/icon-library, Fluent Emoji 3D). Never draw icons.
5. Real products and prices: product photos from https://origins.atlasdsf.com/web/image/product.template/<id>/image_1024 cut out with numpy; names and prices from Odoo product.template or the live shop. Never invent a price.
6. Render HTML with Playwright and Chrome (Inter Tight from @fontsource, await document.fonts.ready), JPG quality 92. Feed 1080x1350, reels 1080x1920, LinkedIn 1080x1350, article cover 1920x1080.
7. Look at every slide, then a contact sheet per lane. Fix overflow, clipping, edge margins, cut-out halos, dead space and rule breaks before Gerrick sees anything.
8. Put everything on one review page (approve / change / reject per post, comment per slide). Gerrick only judges quality.

## House style

### Imagery
- Stock photos (Pexels first, then Unsplash) plus our own HTML/CSS/SVG editing. No AI images in this style.
- Hands, bodies from behind and crops. No faces, no readable labels of other brands, nothing orange-heavy.
- Photos as cut-outs, circle crops with a gradient ring, arches, or photos that fade into the ground. Full-bleed only when the photo is the background.
- Mix bright, nature, lab and unexpected scenes. Not everything dark or woody.
- Icons come from the 3D library (Fluent Emoji 3D). Never Claude-drawn icons.

### Layout
- Every headline centred, with the kicker above and the sub-line below centred too.
- Big bold headline (Inter Tight 700, slightly wider spacing), one plain sub-line, few words per slide.
- One idea per slide. Add slides instead of cramming.
- Dense, not empty: orbs, rings and diagrams fill space with a purpose.
- Text at least 70px from every edge. On TikTok frames keep the top 220px, bottom 380px and right 160px clear.
- No boxes behind text. Use white glow on black text or dark shadow on white text.
- Corporate A mark at the bottom right of every creative, one mark only.

### Colour
- White first. Warm gradients from white into saffron #D8A23F (DSF and some Origins) or rose clay #E2A091 (Origins).
- Soft orbs with gradient edges in saffron, rose and pearl white give the shapes character.
- Forest green #2C463A only on the CTA pill. Never a background, never decoration.
- Black rectangles for tags (MYTH, FACT, QUIZ, SCENT, product name). Tags are rectangles; only CTA buttons are pills.

### Diagrams
- 1 or 2 per carousel, drawn in HTML/SVG: line chart, pyramid, step-down flow, timeline dots, bars, Gantt bars, spoke, chevrons, A/B/C quiz, icon flow.
- Rotate the layout so no two posts in a week share one.

### Copy
- Hooks from the Taste Bank 4 and 5 ratings: real problems, strange-but-true facts, plot twists, direct punchlines.
- Plain words a non-native reader gets at once. No em dashes. No invented numbers, reviews or customers.
- Origins: warm and a little cheeky, CTA "Make your own smell" with the live lowest price and origins.atlasdsf.com.
- DSF: publicist voice ("the team at Atlas"), product development and manufacturing first, fragrance second, AI third.

## Pattern catalogue (the variety to keep rotating)

### Origins carousels

**O1. Problem to 3-step fix** (reference: ORI-C1; slides: ORI-C1_1, ORI-C1_2, ORI-C1_3, ORI-C1_4, ORI-C1_5)
- Use it for: A real everyday mistake with a fix people can use today.
- 1. Cover: the problem as a blunt statement, sub-line is the twist ("Everyone else doesn't.")
- 2. Slide 2: why it happens, shown as a simple drawn line chart plus one 3D icon (nose)
- 3. Slide 3: the consequence, made funny and local ("Now the whole lift knows")
- 4. Slide 4: step-down flow diagram, 3 numbered steps, short bold step title plus one plain line
- 5. CTA: "Make your own smell." with the real lowest price, pill button, Shopee and TikTok Shop as a small line
- Why it works: Starts from a pain the reader already has, explains it like to a 10 year old, then hands over a fix. Only then sells.

**O2. Story timeline with a plot twist** (reference: ORI-C2; slides: ORI-C2_1, ORI-C2_2, ORI-C2_3, ORI-C2_4, ORI-C2_5, ORI-C2_6)
- Use it for: Ingredient stories that should land on a real shop product.
- 1. Cover: the strangest true fact as the headline, photo in a circle crop with a gradient ring
- 2. Build the story with one fact per slide (where the oil sits, how long it takes)
- 3. Timeline slide: dots on a line, Year 0 / Year 15+ / Then / Today
- 4. "Plot twist." slide with two 3D icons and an arrow (tree to lab)
- 5. Land on the smell itself, then the product tag (black rectangle name, white rectangle price)
- 6. CTA headline plays on the hook ("Smell it. Skip the smuggling.")
- Why it works: Storytelling mode Gerrick asked for: curiosity first, the trade is not obvious until late, the twist makes it memorable.

**O3. Myth vs fact plus test it yourself** (reference: ORI-C3; slides: ORI-C3_1, ORI-C3_2, ORI-C3_3, ORI-C3_4, ORI-C3_5, ORI-C3_6)
- Use it for: Correcting a habit almost everyone has.
- 1. Cover: the habit and its cost, one hand-and-bottle photo bleeding off the edge
- 2. Myth vs fact slide: struck-through myth, rectangle MYTH and FACT tags, 3D cross and tick
- 3. Explain with a simple pyramid diagram (top, heart, base)
- 4. "Do this instead" numbered list beside a circle photo
- 5. Engagement slide: a test they can run ("Rubbed vs Left alone") with two orbs, ask them to comment
- 6. CTA slide
- Why it works: Gives proof the reader can check on their own wrist, which builds trust better than a claim.

**O4. Money breakdown bars** (reference: ORI-C4; slides: ORI-C4_1, ORI-C4_2, ORI-C4_3, ORI-C4_4, ORI-C4_5)
- Use it for: Price and value angles: why make your own.
- 1. Cover: the provocative claim ("The liquid is the cheapest part")
- 2. "Say you pay RM500." with four 3D icons in soft orbs (bottle and box, ads, shop, brand profit)
- 3. Bars slide: rough ranges only, a small footnote says they are rough industry ranges
- 4. Big number slide: "RM15 to RM40" with one photo
- 5. CTA: "Make your own smell from RM9.50. Skip the ads and the shop."
- Why it works: Uses only defensible ranges ("roughly"), never a fake exact figure, then turns the number into the reason to buy.

**O5. Quick quiz with answer slide** (reference: ORI-C5; slides: ORI-C5_1, ORI-C5_2, ORI-C5_3, ORI-C5_4, ORI-C5_5)
- Use it for: Busting a myth people repeat in shops.
- 1. Cover: myth headline on a full-bleed photo, rectangle QUICK QUIZ tag, "Swipe for the answer"
- 2. Quiz slide: A / B / C options in circles
- 3. Answer slide: wrong options struck through, right one filled black with a 3D tick
- 4. How-to slide: three-step icon flow (tired nose, fresh air, smell again)
- 5. CTA slide
- Why it works: A quiz makes people stop and guess, which drives swipes and saves.

**O6. Checklist plus comment-keyword lead magnet** (reference: ORI-C6; slides: ORI-C6_1, ORI-C6_2, ORI-C6_3, ORI-C6_4, ORI-C6_5)
- Use it for: "How to" posts people save, and collecting leads in comments.
- 1. Cover: plain question headline, "A 6 point checklist. Save it."
- 2. Checklist slides: photo fades into the ground at the top, 3 points per slide, one 3D icon per point
- 3. Local touch ("Malaysia is not an air-con shop")
- 4. Bridge slide: "Can't find one? Make a smell nobody else has." with a price tag rectangle
- 5. Last slide: "Comment SCENT" in a big black rectangle, then the pill CTA
- Why it works: Useful enough to save, and the keyword turns comments into leads.

### TikTok and Reels

**R1. Relatable scene with dry humour** (reference: ORI-R1; slides: ORI-R1_1, ORI-R1_2, ORI-R1_3, ORI-R1_5)
- Use it for: Turning a fact into a situation everyone has lived.
- 1. Frame 1 is the hook, readable in under 1 second, one key word underlined in rose clay
- 2. Move the story into a real place (the lift, 14 floors, 4 colleagues)
- 3. Text effects only: black text with white glow or white text with dark shadow, never a box
- 4. End frame: the fix plus "or make a smell that is yours", ATLAS ORIGINS and the pill URL
- 5. Keep text clear of the top 220px, bottom 380px and right 160px (TikTok buttons)
- Why it works: Dry humour plus a true fact. Faceless: hands, objects, places.

**R2. Nature and science openers** (reference: ORI-R2 / R3 / R5; slides: ORI-R2_1, ORI-R3_1, ORI-R5_1, ORI-R5_2)
- Use it for: Strange-but-true hooks (smuggled trees, musk blindness, sweat bacteria).
- 1. Bright, unexpected stock photo that is not a perfume bottle (forest, gym towel, petri dish)
- 2. Big centred hook, 3 to 5 lines, one word underlined
- 3. Gross-in-a-good-way is welcome ("The bacteria eating it do.")
- 4. Mix nature, lab and everyday scenes so the feed is not all dark and woody
- Why it works: Lead with curiosity and land on smell. The trade is not obvious at first, which is what Gerrick rated 5/5.

**R3. Money reveal story** (reference: ORI-R4; slides: ORI-R4_1, ORI-R4_2, ORI-R4_3, ORI-R4_4, ORI-R4_5)
- Use it for: Video twin of the money breakdown carousel.
- 1. Fancy bottle in hand, hook on the word "liquid"
- 2. One cost per frame: glass, box, heavy cap; the famous face, the ad, the shop shelf
- 3. Turn: "The smell itself is the small part."
- 4. End on white: "Make your own smell. Perfume materials from RM9.50."
- Why it works: Each frame adds one thing you are paying for, so the reveal builds.

**R4. Unhinged Gen Z skit** (reference: ORI-R6; slides: ORI-R6_1, ORI-R6_2, ORI-R6_3, ORI-R6_4, ORI-R6_5)
- Use it for: Mass-market TikTok fun, not perfume-making process.
- 1. Calm on-screen text while something goes wrong ("Everything is going perfectly.")
- 2. Deadpan captions: "Confidence: high." / "The shelf is fine. We love a shelf."
- 3. Land the point on a clean end frame: "Buying blind is a risk. Make your own smell."
- Why it works: The mismatch between text and picture is the joke. Still ends on the product reason.

### Ads

**A1. Chat screenshot** (reference: CHAT_H2 / H3 / H4; slides: CHAT_H2_STATIC_1, CHAT_H3_STATIC_1, CHAT_H4_STATIC_1, CHAT_H4_STORY_1)
- Use it for: The ad family that won test 1 on clicks. One problem per ad.
- 1. ATLAS ORIGINS lockup top centre, problem headline under it
- 2. Generic friends chat ("Bestie"), lower-case casual lines, no real names, no fake reviews
- 3. Ingredient cut-outs in a row (rose, coffee bean, cotton candy, jasmine, bergamot) with a 4+1 FREE rectangle tag
- 4. Green pill CTA with the real price ("Try the kit, RM49.90"), Shopee line under it
- 5. Make a 1080x1920 twin of the best one for Stories and TikTok
- Why it works: Looks native in a feed, speaks the buyer's own words, and the price is upfront.

**A2. Your problems, our solution** (reference: PROBLEMS_H2 / H3; slides: PROBLEMS_H2_STATIC_1, PROBLEMS_H3_STATIC_1)
- Use it for: Stacking 5 complaints in the buyer's words.
- 1. ad_library "problems" template
- 2. 5 speech bubbles, each under 27 characters, written like a real complaint
- 3. Right column: two ingredient cut-outs and the pill CTA
- Why it works: Readers find their own complaint in the list, so it qualifies them fast.

**A3. Native stock photo** (reference: STOCK_H1; slides: STOCK_H1_STATIC_1)
- Use it for: A bright candid photo that does not look like an ad at first.
- 1. Bright hand-and-bottle photo, no face, no readable brand
- 2. One bold problem headline with a white glow, no box
- 3. Ingredient row and the 4+1 FREE tag over the photo, pill CTA with the price
- Why it works: Feels like a post, not an ad, until the CTA.

### Atlas DSF (B2B)

**D1. Hurdles explainer** (reference: DSF-P1; slides: DSF-P1_1, DSF-P1_2, DSF-P1_3, DSF-P1_4, DSF-P1_5, DSF-P1_6, DSF-P1_7)
- Use it for: Thought leadership on why launches stall.
- 1. Small saffron kicker label above every headline (PRODUCT DEVELOPMENT, HURDLE 1...)
- 2. Cover: cut-out hand on a saffron orb with a soft glow
- 3. Myth/fact with white and saffron orbs
- 4. Hurdle slides: photo fades into white at the top, headline sits on the fade, takeaway line in saffron-brown
- 5. Diagrams: Gantt-style bars ("The launch waits for the longest bar"), spoke diagram with the A mark in the centre
- 6. CTA: the core Atlas line plus the pill "Enquire: link in bio"
- Why it works: Professional, publicist voice, product development first. Every slide teaches one hurdle with one picture.

**D2. Seasonal gifting offer** (reference: DSF-P2; slides: DSF-P2_1, DSF-P2_2, DSF-P2_3, DSF-P2_4, DSF-P2_5, DSF-P2_6)
- Use it for: Corporate gifting and any offer with real numbers.
- 1. Cover: gift boxes cut out over a saffron glow, the contrast line ("not another generic hamper")
- 2. Numbered list in saffron orbs under a fading photo
- 3. Big number bars for real minimums (100 and 500 units)
- 4. Chevron timelines comparing two routes
- 5. Generic vs yours comparison with a white orb and a saffron orb
- 6. CTA: WhatsApp-first, list the three things to send
- Why it works: Honest numbers and a clear route make it easy for HR or an agency to say yes.

**D3. Process steps plus lead offer** (reference: DSF-P3; slides: DSF-P3_1, DSF-P3_2, DSF-P3_3, DSF-P3_4, DSF-P3_5, DSF-P3_6, DSF-P3_7)
- Use it for: Showing how working with Atlas runs, end to end.
- 1. Vertical numbered path of all seven steps on one slide
- 2. Then two steps per slide with a photo or two simple illustrations
- 3. Lead offer as three orbs: 1 kg, Free, Paid, with the plain condition under it
- 4. CTA: "Have a product idea? Send us the brief."
- Why it works: Removes the unknowns for a first-time founder and states the offer plainly.

### LinkedIn

**L1. Personal post images** (reference: GER-L1..3 / SHI-L1..3 / ART-1; slides: GER-L1_1, GER-L2_1, GER-L3_1, SHI-L1_1, SHI-L2_1, SHI-L3_1, ART-1_1)
- Use it for: One image per personal post, a set look per person.
- 1. Gerrick: saffron corner glows, rounded photo card on top (laptop, hands), headline under it
- 2. Shirley: rose clay glows, arch-shaped photo of hands and materials, headline on top
- 3. Small kicker (AI AND SMELL, MAKING AND MATERIALS), name and title line at the bottom, A mark bottom right
- 4. Article cover 1920x1080: title left, photo card right
- 5. Post text first person, plain active sentences, placeholders like [SHIRLEY: ...] where only they know the story
- Why it works: Each person is recognisable in the feed, different from the company look, and still faceless.

## Hooks that met the standard

- You stop smelling your own perfume in minutes. Everyone else doesn't.
- Sandalwood is so valuable people smuggle the trees.
- Rubbing your wrists burns off the best part of your perfume.
- The liquid is the cheapest part of a designer perfume.
- Smelling coffee beans doesn't reset your nose.
- How to choose your signature scent
- Some people physically can't smell your perfume.
- Your sweat doesn't smell. The bacteria eating it do.
- Everything is going perfectly. (falling bottle skit)
- Ads: Tired of smelling like everyone? / RM480 for one bottle? / No idea where to start? / You smell like everyone else
- DSF: Most first launches stall at the factory, not at the idea. / A scent made for your company, not another generic hamper. / From brief to finished product, step by step.
- LinkedIn: A computer has no nose. / Two people. A long list of jobs. / Both 23. Built from scratch. / Every material comes with a paper. I read it. / A good oil can still arrive badly.

Unused hooks still rated 4 or 5 in the Taste Bank: the most expensive wood only smells good after it gets sick; petrichor is made by bacteria; some 'sexy' perfumes smell a little like sweat; ancient Egyptians embalmed with a resin in your perfume; iris roots dried for years; long-lasting perfume tips; the secret to smelling good all day.

## Fix before shipping (known issues in the reference batch)
- ORI-R1 frame 4: The stock bottle shows a readable designer label. Swap the photo before it ships; other brands' labels are out.
- ORI-R1 frame 2: Text sits on a busy lift panel. Pick a calmer photo or a stronger glow so it reads in under a second.
- ORI-R2 frame 4 (not shown): A blurred face sits in the background. Faces are out even when blurred.

## Change log
- 11 Nov 2026: tastebook created from the week 1 batch, after these edits Gerrick asked for on the same day: pill-shaped CTA buttons, every headline centred, corporate A mark bottom right on every creative, 3D library icons in place of drawn icons.
