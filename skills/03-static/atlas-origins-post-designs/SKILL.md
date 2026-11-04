---
name: "atlas-origins-post-designs"
description: "Make Atlas Origins B2C carousels, incl. the intro series (Meet the molecule / accord / essential oil), in the flat reference style with three layouts: Fact Sheet, Recipe Card, Compare."
---

# Atlas Origins post designs (B2C carousels)

Use for any Atlas Origins (@atlasorigins.my) B2C carousel, above all the intro series that introduces one ingredient: a molecule, an accord or an essential oil. Also use for other Origins B2C explainers, picking one of the three styles below by topic or as Gerrick names it.

This skill replaces the visual system of `atlas-social-posts` for Origins B2C posts. That skill's white-first, gradient, lilac-accent rules apply to Atlas DSF and are NOT used here. Still reuse from `atlas-social-posts`: the Odoo content calendar (section 1), the copy hard rules (section 2), the Pexels photo capture and rembg cut-outs (sections 4 and 9), the render setup (section 10), and the hand-off to `/ship-content`.

Approved 11 Oct 2026 on the Hedione post (first in the intro series).

Task list: Topic, Style pick, Facts and copy, Art (doodles, cut-outs, map), Build, Render, QA, Approval, Hand off.

## 1. Pick the style

Three layouts, all from the same reference look (flat panels, highlighter tags, huge numbers, line-art that crosses slides). Pick by topic, or use the one Gerrick names:

| Style | Use for | Reference |
|---|---|---|
| **A. Fact Sheet** | Meet one ingredient: what it is, what it smells like, numbers, what it does, a science fact, how to try it | the "Tacos: What's inside?" set |
| **B. Recipe Card** | Make it yourself: an accord or blend formula, a DIY candle/soap/perfume, step-by-step | the "Ramen for the victory" set |
| **C. Compare** | X vs Y (natural vs synthetic, two grades, two oils), where an oil comes from, myth vs fact | the "Ramen or instant ramen?" set |

Default for a plain "intro" post is A. Rotate styles across the weekly series so the grid does not repeat.

## 2. Series rules (every intro-series post, every style)

- **Series tag:** a yellow rectangle with black text on the cover, top-right, straight (no tilt), never moved:
  `Meet the molecule` / `Meet the accord` / `Meet the essential oil` (match the ingredient type). No number.
  Position: right 70px, top 90px. Style: `background:#F6CE45; color:#141414; font:600 30px/1 'Inter Tight'; padding:9px 15px 11px; letter-spacing:-.3px`.
  Non-series Origins posts skip the tag.
- **Cover name:** the ingredient name in lemon yellow, Inter Tight 500, about 200px, letter-spacing -3px, followed by a colon, with the hook line under it in white bold. Size the name down only if it would cross the 70px side margin.
- **Wordmark:** "ATLAS ORIGINS™" in Jost 600, 26px, letter-spacing 2.1px, small ™ (11px, top-aligned), bottom-right (right 64px, bottom 78px). White on green or dark photo, green on light or yellow.
- **Mascot:** the lemon-drop character (yellow drop with dot eyes and a smile) on the cover and the CTA slide. It waves on the CTA.
- **CTA wording:** `Follow for a new ingredient every week` (or molecule/accord/oil when the whole run is one type), plus `Save for your next blend`.

## 3. Look

**Flat colour only. No gradients anywhere** (backgrounds, shapes, type).

| Token | Hex | Use |
|---|---|---|
| Origins green | `#2D5C43` | hero panels (cover, stats, CTA), green tags, key words on light |
| Lemon yellow | `#F6CE45` | second panel colour, highlighter tags, ingredient name, key words on green |
| Warm light grey | `#EEEDE8` | reading panels |
| Ink | `#141414` | text and line-art on light and yellow |
| White | `#FFFFFF` | text and line-art on green, white tags |

- Panels alternate so neighbours never match: e.g. green, light, green, yellow, light, green.
- **Rectangles only.** Tags, stickers, CTAs and boxes are all sharp-cornered rectangles. No ovals, pills or rounded cards. The only circles allowed are drawn objects (photo rings, diagram dots, orbs in a doodle).
- Tags may tilt 1.5 to 4 degrees for a hand-placed feel, except the series tag.

## 4. Type (Inter Tight; built for a quick glance while swiping)

Install: `npm i @fontsource/inter-tight@5.0.20` in `/home/claude/render` (Jost is already there for the wordmark).

| Role | Spec |
|---|---|
| Slide title | 700, 92 to 112px, line-height .96, **letter-spacing 0** (bold titles need the air) |
| Light subtitle under a title | 300, 44 to 56px, letter-spacing -1.5px ("to your blend", "a soft whisper of") |
| Big numbers | 700, 270 to 330px, **letter-spacing -10 to -12px** (keep numbers tight) |
| Tags | 600, 38 to 52px, letter-spacing -.3px, padding 10px 18px 13px |
| Body | 400, 30px/1.34, letter-spacing -.3px, 2 to 3 lines per block, key words in 600 green (on light/yellow) or 600 yellow (on green) |
| Diagram labels | 400, 24px |
| Sources | 400, 19px, 75% opacity, near the bottom |

Highlight the main idea of each slide with ONE device: a tag ("Usual dose?"), or a yellow highlighter block behind one word in the title. For the block, put the word in its own `display:inline-block` span (`background:#F6CE45; line-height:1; padding:2px 16px 12px; margin:10px 0 6px -16px; transform:rotate(-1.5deg)`) so it never paints over the line above.

## 5. Safe margins

Keep all text at least 60 to 100px from every edge so it clears Instagram's username header and the like/comment/caption bar:
- top elements start at 90 to 96px
- side text starts at 70px
- bottom text (sources, CTA tags) ends by about 1270px
Art and photos may run off the edges on purpose; text never does.

## 6. Art

- **Line-art doodles do most of the work.** Hand-drawn feel: single 5px stroke, round caps and joins, no fill. White on green, ink on light and yellow. Draw them as SVG for each subject (flowers, leaves, bottles, droppers, noses, brains, molecules as circles). No AI images, no clip-art.
- **At least one piece of art crosses a slide edge** (a branch from cover into slide 2, a dotted droplet trail into the CTA, a pipette hanging across two slides). Build the carousel as one wide panorama so this lines up when swiping (section 8).
- **Photo cut-outs, sparingly** (1 or 2 per post): transparent PNGs from Pexels via rembg, either inside a 4px ink ring circle (Style A/B) or large on the CTA. Style B may use one full-bleed photo panel (see below).
- **1 to 2 simple diagrams per carousel** that explain the idea (before/after dots, nose → receptor → brain, a 3 to 4 step flow).
- Facts always carry a tiny source line.

## 7. Slide plans

### A. Fact Sheet (6 slides) — the approved Hedione post
1. **Cover (green):** series tag; big line-art of the source material (e.g. jasmine branch) across the top, running into slide 2; yellow name + white bold hook ("Hedione: why perfume glows"); one-line teaser; mascot.
2. **Meet it (light):** green tag "Meet <name>"; 2 short body blocks (origin story, chemical name / nickname); right column "Smells like" (bold) + light subtitle + 3 to 4 stacked yellow tags (notes); ringed cut-out of a related material; source.
3. **Numbers (green):** 1 to 2 question tags ("Usual dose?" white, "The record?" yellow) each over a huge white number and one body line; small white doodle; sources.
4. **What it does (yellow):** bold title + light subtitle; before/after diagram with "Without" (white tag) and "With <name>" (green tag); one body line. Keep the title, diagram and body as one balanced group.
5. **Smell science (light):** green tag; title with one yellow highlighter word; 3-step diagram; 2-line body; source; dotted trail starting toward slide 6.
6. **CTA (green):** "Now you're ready to try it!"; yellow tag "How to start"; usage line; dropper cut-out; waving mascot; outline rectangle "Save for your next blend"; white rectangle "Follow for a new ingredient every week".

### B. Recipe Card (5 to 6 slides)
1. **Cover (light):** series tag (if part of the series); bold title + light subtitle ("Fig accord / for beginners"); three ringed cut-out circles of the raw materials in a row, the middle one biggest with a yellow ring, each with a small green name tag; one teaser line; mascot.
2. **Hero photo (full-bleed photo panel):** one Pexels photo as the whole slide (hands with dropper, blotters, beaker; no faces), darkened with a flat `rgba(0,0,0,.35)` layer (no gradient); a yellow tag with the recipe name; white light subtitle ("the formula").
3. **You'll need (yellow), two columns:** left "You'll need:" bold, then the ingredient list in ink 28px with the star line in a white box; right "Step by step:" with numbered black-on-white tags ("1 - Blend", "2 - Rest", "3 - Test") each followed by 1 to 2 body lines. This slide can span two panels if the list is long.
4. **Why it works (light):** a simple diagram (top/heart/base pyramid or a 3-step flow) with tags.
5. **CTA (light or green):** a pun headline on a yellow highlighter block ("it was fig-tastic"), white rectangle tags with ink text ("Show us your blend", "Tag @atlasorigins.my"), mascot.
No personal names or handles from real people; if showing "makers", use the mascot or hands only.

### C. Compare (5 to 6 slides)
1. **Cover (green):** series tag (if part of the series); the name or question in yellow + white bold hook; a large white line-art graphic that doubles as a chart (e.g. bars made of drips, blotter strips at different heights) running off the bottom.
2. **The question (light):** green tag with the question ("Natural or synthetic?"), 4 to 5 lines of body with key words in 600; an illustration hanging from the top edge across into slide 3 (pipette with yellow drips, a flower on a stem).
3. **Side 1 (light):** grey world map (`#D6D5D0` land) with the origin country filled green; green tilted tag with the name and a small white sub-label (country); 4 to 5 body lines with key words in 600.
4. **Side 2 (light):** same layout as slide 3, other side. If it is not about places, swap the map for a doodle of each side.
5. **CTA (green):** big white bold closing line ("Now you can smell the difference!"), the hanging illustration coming in from the top, wordmark.

Maps: `npm i world-atlas@2.0.2 d3-geo@3.1.0 topojson-client@3.1.0` in `/home/claude/render`, then `node map.mjs <Country name> <w> <h> <zoom>` prints `{land, hi}` SVG path strings (Natural Earth projection, centred on the country). Draw `land` in `#D6D5D0` and `hi` in green.

```js
// /home/claude/render/map.mjs
import {geoNaturalEarth1, geoPath, geoCentroid} from 'd3-geo';
import {feature} from 'topojson-client';
import {createRequire} from 'module';
const require=createRequire(import.meta.url);
const world=require('world-atlas/countries-110m.json');
const [name,w,h,zoom]=[process.argv[2],+process.argv[3]||900,+process.argv[4]||600,+process.argv[5]||2.2];
const fc=feature(world,world.objects.countries);
const hi=fc.features.find(f=>f.properties.name===name);
if(!hi){console.error('not found');process.exit(1)}
const proj=geoNaturalEarth1().fitSize([w,h],fc);
proj.scale(proj.scale()*zoom);
const c=proj(geoCentroid(hi)); proj.translate([proj.translate()[0]+w/2-c[0],proj.translate()[1]+h/2-c[1]]);
const p=geoPath(proj);
console.log(JSON.stringify({land:p(fc), hi:p(hi)}));
```

## 8. Build and render (panorama, then slice)

Build ONE HTML page `N x 1080` wide by 1350 tall. Each slide is an absolutely positioned 1080 x 1350 panel at `left = i*1080`. All line-art lives in one full-width SVG on top; art that crosses a slide edge is drawn twice through per-slide clip paths so it switches colour at the edge (white on green, ink on light).

Base CSS and helpers (Python template; fonts from `/home/claude/render/node_modules/@fontsource`):

```python
R='/home/claude/render/node_modules/@fontsource'
W,H=1080,1350
G,Y,LT,K='#2D5C43','#F6CE45','#EEEDE8','#141414'
def fi(w,st='normal'):
    return f"@font-face{{font-family:'IT';font-weight:{w};font-style:{st};src:url('file://{R}/inter-tight/files/inter-tight-latin-{w}-{st}.woff2')}}"
fonts=f"@font-face{{font-family:'Jost';font-weight:600;src:url('file://{R}/jost/files/jost-latin-600-normal.woff2')}}"+''.join(fi(w) for w in (300,400,500,600,700))
CSS=fonts+"""
*{margin:0;padding:0;box-sizing:border-box}
.sl{position:absolute;top:0;width:1080px;height:1350px;overflow:hidden}
.abs{position:absolute}
.h{font-family:IT;font-weight:700;line-height:.96;letter-spacing:0}
.lite{font-family:IT;font-weight:300;line-height:1;letter-spacing:-1.5px}
.b{font:400 30px/1.34 IT;letter-spacing:-.3px}
.src{font:400 19px/1.3 IT;opacity:.75}
.tag{display:inline-block;font:600 44px/1 IT;padding:10px 18px 13px;letter-spacing:-.3px}
.wm{position:absolute;bottom:78px;font:600 26px Jost;letter-spacing:2.1px}
.wm sup{font-size:11px;vertical-align:top;margin-left:2px}
.co{position:absolute;filter:drop-shadow(0 22px 26px rgba(0,0,0,.22))}
"""
X=lambda i:i*W
wm=lambda i,c:f'<div class="wm" style="left:{X(i)+W-330}px;color:{c}">ATLAS ORIGINS<sup>™</sup></div>'
series=lambda kind:f'<div class="abs" style="left:0;width:{W}px;top:90px;text-align:right;padding-right:70px;z-index:3"><span class="tag" style="background:{Y};color:{K};font-size:30px;padding:9px 15px 11px">Meet the {kind}</span></div>'
def clip(i): return f'<clipPath id="c{i}"><rect x="{X(i)}" y="0" width="{W}" height="{H}"/></clipPath>'
def inslide(i,c,body,sw=5):
    return f'<g clip-path="url(#c{i})" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</g>'
def droplet_char(x,y,s,fill=Y,wave=False):  # the lemon-drop mascot
    arm='M-44,30 C-70,22 -78,0 -70,-14' if wave else 'M-44,34 C-62,44 -70,58 -64,70'
    return f'''<g transform="translate({x},{y}) scale({s})" stroke="{K}" stroke-width="{4/s:.1f}" stroke-linecap="round" stroke-linejoin="round">
<path d="{arm}" fill="none"/><path d="M44,34 C62,44 70,58 64,70" fill="none"/>
<path d="M0,-78 C26,-40 48,-8 48,28 A48,48 0 1 1 -48,28 C-48,-8 -26,-40 0,-78 Z" fill="{fill}"/>
<circle cx="-15" cy="22" r="5" fill="{K}"/><circle cx="15" cy="22" r="5" fill="{K}"/>
<path d="M-12,42 Q0,54 12,42" fill="none"/>
<path d="M-26,-8 C-30,6 -32,14 -30,22" fill="none" stroke="#fff" stroke-opacity=".8"/></g>'''
# place the mascot: <svg class="abs" style="left:..;top:.." width="220" height="250" viewBox="-110 -110 220 250">{droplet_char(0,0,1.2)}</svg>
```

Useful doodle helpers (draw inside an `inslide` group):
- flower `(cx,cy,r,rot)`: 5 petals, each `M0,0 C r*.5,-r*.2 r*.62,-r*.82 r*.06,-r C -r*.5,-r*.92 -r*.5,-r*.3 0,0` rotated by i*72, a centre circle r*.12, and 5 short stamen lines with dot tips.
- leaf `(x,y,l,rot)`: `M0,0 C l*.3,-l*.32 l*.75,-l*.3 l,0 C l*.75,l*.3 l*.3,l*.32 0,0 M0,0 L l*.85,0`.
- curved arrow: a cubic path plus a two-line head at the end point.
- dotted trail: a path with `stroke-dasharray="2 22" stroke-width="7"`.

Render with Playwright 1.56.1 (`/home/claude/render/pano.mjs`):

```js
import { chromium } from 'playwright';
const [src,out,n]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080*+n,height:1350}});
await p.goto(`file://${src}`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:`${out}/pano.png`,clip:{x:0,y:0,width:1080*+n,height:1350}});
for(let i=0;i<+n;i++) await p.screenshot({path:`${out}/s${i+1}.png`,clip:{x:1080*i,y:0,width:1080,height:1350}});
await b.close();
```

`node pano.mjs <html> <outDir> <N>`, then convert each slice to JPG at quality 93 as `01_<name>.jpg` ... in `/home/claude/posts/<date>-<name>/`. Also save a small panorama (`pano_small.jpg`) and a 3-across contact sheet.

## 9. QA (look at the contact sheet and the panorama)

- flat colours only; no gradients anywhere
- series tag yellow rectangle, top-right, straight, correct type word, no number
- ingredient name yellow on the cover; titles at letter-spacing 0, numbers tight
- rectangles only; no ovals or rounded pills
- all text inside the safe margins; wordmark bottom-right and clear
- at least one doodle crosses a slide edge and lines up across the cut
- 1 to 2 diagrams; neighbouring slides never share a background colour
- body blocks 3 lines or fewer; every fact has a source line
- no em dashes, no orange, no faces, no other brands' readable labels, no invented stats
Fix and re-render.

## 10. Caption

Instagram-first, short: a hook line naming the ingredient, 2 to 3 short lines on what it does and one fact, the try-it line, "Save this, and follow for a new ingredient every week.", then up to 4 hashtags (e.g. #perfumery #aromachemicals #DIYperfume #fragranceoil). No em dashes.

Then approval and hand-off exactly as in `atlas-social-posts` section 10 (approve / change / hold, timing, placements, then `/ship-content`).