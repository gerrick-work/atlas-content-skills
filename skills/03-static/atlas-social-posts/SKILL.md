---
name: "atlas-social-posts"
description: "Make Atlas DSF or Atlas Origins static posts and carousels from the Odoo content calendar, in the approved Atlas brand system (white-first, forest-green gradients, cut-out imagery), rendered to Meta-ready 4:5 images. Use whenever Gerrick asks for a post, carousel, static, this week's posts or the next post from the calendar."
---

# Atlas social posts (static posts and carousels)

Use whenever Gerrick asks for a post, carousel, static, "this week's posts" or "the next post from the calendar" for Atlas DSF (B2B: @atlasdsf.my, LinkedIn) or Atlas Origins (B2C: @atlasorigins.my).

This skill is the Atlas brand identity (approved 9 Oct 2026). Orange is not part of the brand. The old "Atlas Brand Kit" Design System artifact was a demo: ignore it.

Output: a Design canvas for review, plus 1080 x 1350 JPGs and a caption per post. Then hand off to `/ship-content` to schedule. Use the task list: Topic, Copy, Photos and cut-outs, Design, Render, Approval, Hand off.

## 1. Topic (Odoo is the master calendar)

- Odoo project "Atlas Content Calendar" (project id 5) on atlas-dsf.odoo.com.
  - One task per post, named `[DSF] ...` or `[Origins] ...`, due on its posting day (Mon/Wed/Fri).
  - Stages: Planned, Drafting, Design, Ready to post, Posted, Parked.
  - Tags: account, pillar, "Check first".
- Read Odoo through Claude in Chrome (read the chrome-browser skill first). The cloud workspace can't reach Odoo.
  1. Open a new tab at atlas-dsf.odoo.com.
  2. Run this read-only call:
     ```js
     const rpc=async(model,method,args,kwargs)=>(await (await fetch('/web/dataset/call_kw',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jsonrpc:'2.0',method:'call',params:{model,method,args,kwargs}})})).json()).result;
     window.__cal=await rpc('project.task','search_read',[[['project_id','=',5]]],{fields:['name','date_deadline','stage_id','tag_ids','description'],order:'date_deadline asc'});
     ```
  3. Read it back in slices of about 800 characters; longer returns are truncated.
  4. Strip the HTML tags from `description`.
- Chrome unreachable? Read the published "Atlas Content Calendar" artifact (https://claude.ai/artifact/75GVNpMEmfC8tj9xt494TW) with the Artifact tool instead. Its DATA rows hold date, account, pillar, format, angle (`a`), CTA (`c`) and check-first (`chk`). Say that Odoo itself wasn't re-checked.
- Each description holds Account, Channel, Pillar, Format, Post type, Angle and CTA. Build the post from the Angle and CTA. If the planned format is a reel, say so and offer `/explainer-reel`.
- Default pick: the next tasks in Planned by date. A topic or date the user names wins.
- "Check first" posts need the fact, stock or permission confirmed before the copy states it. Ask, or write around it and flag it.
- Writing to Odoo needs a yes.

## 2. Copy

**Start with the angle.** Load the `atlas-script-lab` skill with the Skill tool and run it with the topic, account, format (carousel or static), platform and the task's funnel tag (TOFU, MOFU or BOFU). Save its angle brief as `angle.md` beside the post's files. It sets the segment, lead hook and two alternates, the carousel framework, the proof points and the CTA. The rules below still apply on top of it.

- **Cover:** the lead hook's on-screen line is the headline and its visual is the cover image or cut-out. The headline must not caption the image.
- **Slide 2:** the on-ramp. It continues the cover's premise, never a brand introduction.
- **Body slides:** follow the framework the brief names.
- **Last slide:** the CTA from the brief. Use a comment keyword only when the brief marks its offer as live or manual DM; otherwise use the brief's fallback.

- **Atlas DSF:** thought leadership. Professional, warm and plain, for brand owners and founders; never B2C tips.
  - Messaging order: product development and manufacturing first, fragrance second, AI third.
- **Atlas Origins:** friendly smell science and making. Say what a material does before what it is.
- **Carousel:** 5 to 7 slides.
  - Slide 1 is the hero: a headline of 8 words or fewer if possible, plus one supporting line.
  - Body slides: one idea each, 25 words or fewer.
  - Last slide: the CTA from `angle.md` (the Odoo task's CTA, matched to the funnel role and checked against the live offers).
- **Static:** headline, supporting line, CTA.
- **Hard rules:**
  - No em dashes anywhere; rewrite the sentence instead.
  - No invented stats. Verify each fact with a web source and list sources in the reply.
  - Never expand "DSF".
  - No faces (hands are fine).
  - No prices or client names unless Gerrick gives them.
  - No trademarked material names (Iso E Super, Hedione and the like) on generic diagrams; use generic ones such as linalool.
- **Caption:** for DSF, LinkedIn-first (3 to 5 short paragraphs, up to 4 hashtags). For Origins, shorter for Instagram. The first line restates the hook idea in a fresh sentence, and the CTA repeats just before the hashtags.
- **Edit pass:** run the lab's AI-tells check (section 9 of atlas-script-lab) over every slide and the caption.

## 3. Colour system: white first, forest green as the brand

**Size:** design at 1080 x 1350 (4:5). Instagram via Business Suite rejects anything taller and auto-crops 3:4.

**Primary colour is pure white `#FFFFFF`.** It is the ground of the middle slides. Forest green is the brand colour and must be obvious on every post.

**Font colours: black, white or Atlas green, nothing else** (except on the one accent page).
- Black `#111111`: body copy on white only. Headlines are never black.
- White `#FFFFFF`: on green grounds and dark photo areas.
- Atlas green `#2C463A`: headlines, labels, small text and the wordmark on white.
- Pick by contrast with what is directly behind the text. Contrast 4.5:1 or better (white on the accent colours fails).

**Forest green, always with a gradient.** Forest and black look alike at a glance, so green has to carry area to read as the brand. Every green fill, panel, card, pill or large headline is a gradient, never flat.
- Gradients run from forest toward lighter green or toward white:
  - lighter green: deep `#1F3429` → forest `#2C463A` → jade `#4F7A60` → mist `#86AE94`
  - to white: forest `#2C463A` → `#5E8A70` → `#C9DCCF` → white `#FFFFFF`
- The dark end sits behind white type so it stays readable; the light end runs away from the text. Mist and the pale tints only appear at the far edge, never as a big pastel area (pastel stays under 30% of a slide).
- Small text (body, labels, captions) stays solid `#2C463A`; gradients on small text look blurry.
- Darken photos for white text with black (`rgba(0,0,0,..)`) or the green photo grade, never a flat green overlay.

**Where green goes on every post (the standard mix):**
- **Cover: forest to lighter green.** A full green ground, `linear-gradient(165deg, #1F3429 0%, #2C463A 40%, #4F7A60 78%, #7FA88D 100%)`, with white headline, label, body and wordmark. Pills on it are white with green text. Cut-outs on green get a deeper shadow, `drop-shadow(0 30px 40px rgba(20,40,30,.35))`. Every post opens green, so the grid reads as Atlas.
- **CTA slide: forest to white.** `linear-gradient(180deg, #22382E 0%, #2C463A 34%, #5E8A70 52%, #C9DCCF 68%, #FFFFFF 82%)`, with white type in the green top and cut-outs sitting on the white bottom; wordmark in green.
- **White slides: gradient headlines and green pills.** Headlines over about 80px use `background: linear-gradient(100deg, #1F3429 0%, #2C463A 45%, #5E8A70 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent` with `color: #2C463A` as the fallback. Pills use `linear-gradient(135deg, #2C463A, #5E8A70)` with white text.
- **Stat and diagram slides: green marks the answer.** The key card, orb or element (the Atlas number, the original scent, where Atlas sits) gets `linear-gradient(160deg, #22382E 0%, #2C463A 35%, #4F7A60 75%, #86AE94 100%)` with white type and `box-shadow: 0 24px 50px rgba(44,70,58,.35)`. Everything else on the slide stays white or neutral; arrows and chevrons pointing to it are forest.
- **Field photos (when a photo is the background): green photo grade.** `filter: grayscale(1) contrast(1.25) brightness(.95)` on the img, then a `#2C463A` layer with `mix-blend-mode: lighten` and a `#DDE6E0` layer with `mix-blend-mode: multiply` over it. Shadows go forest, highlights stay white. Field slides only, not every photo.
- A single static post: the cover rule applies (green ground), or a white post with a gradient headline plus one green-gradient element.
- No green border or frame around the slide.

**One accent page per post.**
- A bright contrasting colour may appear on ONE slide of a carousel only, on the slide that carries the single most important line of copy. Every other slide uses only white, black, green and photography.
- Account accents:
  - Atlas DSF: signal lime `#D4F53C`
  - Atlas Origins: bright lilac `#B9A4FF`
- Ways to use it on that page (pick one):
  - Preferred: a forest gradient ground (`linear-gradient(170deg, #1F3429 0%, #2C463A 45%, #4F7A60 100%)`) with white type, the accent on the key phrase and the label. Lime and lilac look strongest against forest.
  - A highlighter band behind the key phrase on a white slide: put the phrase on its own line (`<br>` before it), give the headline `line-height: 1.08`, and paint the band as `background: linear-gradient(180deg, transparent 14%, <accent> 14%, <accent> 94%, transparent 94%)` with `padding: 0 14px; margin-left: -14px; box-decoration-break: clone`. A plain background on a wrapped span paints over the line above.
  - The hero object in a diagram.
- A single static post may use its accent once, or not at all.
- Never orange. Never two accents in one post.

**Fill the frame (no large empty areas).** Every slide is carried by at least one of:
- a green gradient ground
- a full-bleed photo that fades into white behind the type (for example `linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.85) 55%, #FFFFFF 70%)`)
- a large transparent cut-out (at least 35 to 45% of the slide) with a soft shadow
- a diagram built from cut-outs and characterful shapes
- headline type set big (88 to 130px) so it fills its block
- No more than about 25% of a slide may be empty white.

**Other gradients:** photo fades into white, soft neutral grounds (`#FFFFFF` to `#F1F2F1`), or a light grey floor shadow under cut-outs.

**Shapes need character.** Gradient edges, an inner highlight and a soft drop shadow, so they read as objects, never flat circles.
- Neutral glass orb: `background: radial-gradient(circle at 35% 30%, #FFFFFF 0%, #F6F7F6 28%, #DCDFDD 68%, #C4C9C6 100%); box-shadow: 0 24px 48px rgba(0,0,0,.14), inset 0 -10px 24px rgba(0,0,0,.06)`.
- Green orb (the answer): `radial-gradient(circle at 35% 30%, #86AE94 0%, #4F7A60 35%, #2C463A 70%, #1F3429 100%)` with `box-shadow: 0 24px 48px rgba(44,70,58,.35)`.
- Blotter strip: a 70px-wide white rounded rectangle, `linear-gradient(90deg, #FFFFFF, #FAFAF8 60%, #EEEFEC)` with a soft shadow and a faint amber tint at the dipped tip.
- On the accent page only, the hero shape may use the accent: `radial-gradient(circle at 35% 30%, #FFFFFF 0%, <accent> 45%, <accent darker 15%> 100%)`.

## 4. Images: transparent cut-outs first

- Photos that illustrate an object or a concept (bottles, droppers, blotters, raw materials, soap, a car, a hand holding a tool) are used as **transparent no-background cut-outs**, on white or green grounds with a soft shadow (`filter: drop-shadow(0 30px 40px rgba(0,0,0,.18))` on white).
- This applies above all to diagrams: the cut-outs are the parts of the diagram.
- Use a full photo with its background only when the photo is meant to BE the background (a Field slide), graded green or faded into white.
- Make cut-outs in the workspace with rembg (one-time setup; the model downloads from GitHub and works through the proxy):
  ```bash
  pip install --break-system-packages -q "rembg[cpu]"
  python3 - <<'EOF'
  from rembg import remove, new_session
  from PIL import Image
  s = new_session('isnet-general-use')
  for src, out in [('photos/x.jpg', 'cut/x.png')]:
      o = remove(Image.open(src), session=s)
      o.crop(o.getbbox()).save(out)   # trim to the object
  EOF
  ```
- Check every cut-out on white before using it: no leftover background halos or ghost fragments (crop them away, for example by finding where the alpha rows of the real object start), no clipped edges on the object (a hand cut at the wrist is fine if it runs off the slide edge). Photos with a plain, contrasting background cut out cleanly; skip ones where a coloured wall tints the skin.
- Keep cut-outs clear of text: no arm or object runs under a headline.
- Cut-outs are PNG with alpha; upload them as canvas assets like photos.

## 5. Type

- Headline: Jost 700. Only the headline is bold. Green gradient on white, white on green.
- Body: Mulish 400. Black on white, white on green.
- Labels: Jost 400 uppercase, letter-spacing 4px, solid green on white or white on green and photos.
- Big numbers: Jost 300.
- Wordmark: "ATLAS DSF" or "ATLAS ORIGINS" in Jost 600, 26px, letter-spacing 2.1px, with a small ™ (11px, top-aligned), green on white, white on green.
  - ALWAYS bottom-right (right 64px, bottom 50 to 60px), nowhere else. Keep that corner clear; content blocks sit at bottom 150px or higher.

**Never:**
- headers or footers, slide counters or dots
- decorative lines or borders
- emoji
- flat clip-art
- AI-generated photos
- large empty areas
- flat green

**Shape language:** rounded corners 20 to 32px, pill tags (green-gradient pills with white text on white slides; white pills with green text on green slides).

## 6. Diagrams (1 to 2 in every carousel)

- Explain at least one idea with a simple diagram.
- Good forms:
  - cutaway
  - scale or spectrum
  - before and after
  - 3 to 4 step flow
  - two-axis positioning map
  - cluster versus outlier
- Build from transparent cut-outs plus separate HTML elements (glass orbs, white rounded cards with soft shadows, forest chevrons or arrows from CSS triangles or stroke SVG). The element that is the answer is green (section 3).
- Labels at least 24px, Jost or Mulish 400, black or green; five labels or fewer.
- Proven examples:
  - two glass bottles with few vs many oil orbs (concentration)
  - six brand orbs funnelling into two library orbs into one "similar scents" pill
  - an axis map with a neutral stock-scent cluster vs one green original orb
  - two white date cards joined by a chevron, each with a bottle cut-out (deadlines)
  - four numbered blotter strips with chevrons (a step flow)
  - shrinking orbs above blotters labelled Now, 1 hour, Tomorrow (change over time)

## 7. Bento cards: statistics comparison only

- Use bento ONLY to compare numbers side by side; never a whole post or a list of dates.
- Maximum 3 cards per slide.
- On white: neutral cards `#FFFFFF` with `box-shadow: 0 18px 44px rgba(0,0,0,.10)` and a 1px `rgba(0,0,0,.06)` border, radius 28; the key card takes the green answer gradient with white type. Over a photo: `rgba(255,255,255,.82)` with `backdrop-filter: blur(14px)`.
- Content per card: a big Jost 300 number and a short Mulish label. A cut-out can sit inside a card when it illustrates the number.

## 8. Two design languages: alternate the lead per account

- **A. Field:** a full-bleed photo that is meant to be the background, graded green or faded into white, with type low on the slide.
- **B. Cut-out:** white or green grounds carried by large transparent cut-outs, characterful shapes and diagrams.
- Both languages open on a green cover (or a green-graded Field photo) and close on the forest-to-white CTA.
- A carousel can borrow slides from the other language, but the hero follows the lead.
- Consecutive posts on the same account switch the lead.

## 9. Photos (Pexels, through Chrome)

- Royalty-free only: Pexels, then Unsplash. Real materials, hands, bottles, labs. No faces, no other brands' readable labels, nothing orange-dominant. For cut-outs, prefer subjects shot on a plain background.
- The workspace can't reach Pexels. In a new Chrome tab:
  1. Search `pexels.com/search/<query>/?orientation=portrait`.
  2. Collect ids with `[...new Set([...document.querySelectorAll('article a[href*="/photo/"]')].map(a=>(a.getAttribute('href').match(/(\d+)\/?$/)||[])[1]))]`.
  3. Preview a contact grid from `images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&w=200&h=266&fit=crop`.
  4. Capture each pick at full size: load `...&cs=tinysrgb&w=1080&h=1440&fit=crop` into a fixed `<img>` 1080 x 1440 at left:0, then take two `computer screenshot` calls with `save_to_disk` and scale 1 (the files land in the workspace), with the img at top 0 and at top -(1440 - viewport height).
  5. Stitch with PIL: crop x 0 to 1080, using the screenshot-to-CSS ratio `screenshot_width / innerWidth`.
  6. Cut out the ones used as objects (section 4), then upload photos and cut-outs as canvas assets.
- Chrome unreachable: reuse photos already in the workspace and say so.
- List the Pexels ids as sources.

## 10. Build, render, approve

1. **Canvas:** a Design canvas, one 1080 x 1350 artboard per slide, one row per post, with captions as stickies. Build without a design system: don't install or follow the old "Atlas Brand Kit" demo. This skill is the brand identity.
2. **Render to JPG in the workspace:**
   - Setup in `/home/claude/render`: `npm init -y && PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm i playwright@1.56.1 @fontsource/jost@5.0.18 @fontsource/mulish@5.0.20`. Use playwright 1.56.1; it matches the preinstalled Chromium 1194, and older versions fail.
   - Easiest: keep each slide's body as a Python template with image placeholders, and build two outputs from it: standalone HTML with `file://` images and local `@font-face` (for Playwright), and the canvas `.dc.html` with `/_blob/<id>` images.
   - Or convert `.dc.html` directly. `render.mjs <srcDir> <outDir> <names...>`, for each file:
     - removes the `support.js` script, the Google Fonts link and the `x-dc` script block
     - maps every `/_blob/<id>` to the local photo or cut-out file
     - injects `@font-face` rules pointing at `node_modules/@fontsource/{jost,mulish}/files/*-latin-<w>-normal.woff2` plus `x-dc,helmet{display:contents}`
   - Open each page at viewport 1080 x 1350, await `document.fonts.ready`, and screenshot the 1080 x 1350 clip.
   - Convert to JPG at quality 93 with PIL.
   - Save into `/home/claude/posts/<date>/`. Chrome uploads accept workspace paths only, not `/mnt/user-data/outputs`.
3. **QA:** build a contact sheet and look at it. Check:
   - the cover is green (or green-graded), the CTA fades forest to white, and green is obvious on every slide
   - no flat green anywhere; every green fill or large headline is a gradient; the dark end sits behind white text
   - white grounds on the middle slides; font colours only black, white or green (plus the accent page)
   - the accent colour appears on exactly one slide at most, on the key line
   - object and diagram images are clean transparent cut-outs; full photos only where they are the background
   - no slide more than about 25% empty white, no big pastel areas
   - subject visible in each photo; no other brands' text
   - nothing overflowing or clipped; no cut-out under text; wordmark corner clear
   - no em dashes or orange; only headlines at weight 700
   - 1 to 2 diagrams per carousel, at most 3 bento cards per slide
   Fix and re-render.
4. **Approval:** SendUserFile the contact sheet and use SendUserMessage for the captions plus the angle brief's hook, two alternates and CTA. Ask with AskUserQuestion:
   - approve, change, or hold
   - timing: calendar date at 8:30pm, now, or another time
   - placements: Facebook plus Instagram, or Instagram only
5. **Hand off:** run `/ship-content` with the JPG paths in slide order, the caption, the account, the date/time, and the funnel role and CTA keyword from `angle.md`. After it confirms, offer to move the Odoo tasks to "Ready to post".