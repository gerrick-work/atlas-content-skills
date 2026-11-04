"""Atlas Origins ad library: four reusable static ad templates (1080x1350, 4:5).

Usage:
    python3 ad_library.py specs.json OUT_DIR          render every ad (variants expanded)
    python3 ad_library.py specs.json OUT_DIR --dry    list the ads a spec file expands to, render nothing
    python3 ad_library.py specs.json OUT_DIR --only MEME_H3   render only names starting with this

Each spec in specs.json picks a template ("search", "problems", "meme", "presenter")
and fills its copy slots. Change the words, products, prices or colour; the layout,
logo lockup, CTA style and safe margins stay standard.

Variants (added 4 Nov 2026): one spec can fan out into many ads. Give it a "code"
(MEME, SEARCH, PROBLEMS, BUT) and a "vary" block instead of a single name:

    {"code":"MEME","family":"Emotional / relatable","template":"meme",
     "images":["879","938","956"],"cta":"Grab all 3 for RM33.70","link":"/oils",
     "h_start":2,
     "vary":{"hooks":[{"quote":"Perfume is only for<br>rich people","setup":"Me with RM35:"},
                      {"quote":"Smelling expensive<br>costs a fortune","setup":"Me with RM35:"}],
             "bg":["saffron","rose","white"]}}

That makes 2 hooks x 3 colours = 6 ads named MEME_H2_SAFFRON ... MEME_H3_WHITE.
Each hook entry can override any slot (quote, setup, images, cta, problems...).
Hooks are numbered from h_start (default 1) so new hooks never reuse a live H number.

Setup (once per machine):
    cd WORK && npm i @fontsource/inter-tight@5.0.20 @fontsource/jost @fontsource/caveat playwright@1.56.1
    npx playwright install chromium
    pip install pillow numpy
Product cut-outs: fetch_product(id) downloads https://origins.atlasdsf.com/web/image/product.template/<id>/image_1024
and removes the white background. Bottles photo: Canva design DAHY1XhiEuE ("SHOPEE"), page 4, crop (52,252,582,702).
"""
import itertools, json, os, sys, subprocess

WORK = os.environ.get('ADLIB_WORK', '/home/claude/render')
FONTS_DIR = f'{WORK}/node_modules/@fontsource'
CUT = f'{WORK}/cut'
HERE = os.path.dirname(os.path.abspath(__file__))

# Brand tokens (Atlas Origins)
G = '#2D5C43'          # Origins green: CTA button and logo only
INK = '#141414'
BG = {'white': '#FFFFFF', 'green': '#22473A', 'saffron': '#D8A23F', 'rose': '#E2A091'}  # never grey
DARK_BG_OK = {'meme'}  # only the meme template is built to read on dark green
MARK = open(os.path.join(HERE, 'mark_path.txt')).read()  # corporate "A" mark, viewBox 136 248 1328 1104


def fi(w):
    return (f"@font-face{{font-family:'IT';font-weight:{w};"
            f"src:url('file://{FONTS_DIR}/inter-tight/files/inter-tight-latin-{w}-normal.woff2')}}")


CSS = (f"@font-face{{font-family:'Jost';font-weight:600;src:url('file://{FONTS_DIR}/jost/files/jost-latin-600-normal.woff2')}}"
       f"@font-face{{font-family:'Cav';font-weight:600;src:url('file://{FONTS_DIR}/caveat/files/caveat-latin-600-normal.woff2')}}"
       + ''.join(fi(w) for w in (300, 400, 500, 600, 700)) + """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:IT;color:#141414}
.c{position:relative;width:1080px;height:1350px;overflow:hidden}
.abs{position:absolute}
.wm{font:600 24px Jost;letter-spacing:2px}
.wm sup{font-size:10px;vertical-align:top;margin-left:2px}
""")


def bg_of(s, default='white'):
    """Background colour for a spec. Green only where the template was designed for it; never grey."""
    name = s.get('bg', default)
    if name not in BG:
        raise ValueError(f"{s.get('name')}: bg '{name}' is not one of {sorted(BG)}")
    if name == 'green' and s['template'] not in DARK_BG_OK:
        raise ValueError(f"{s.get('name')}: green background only works on the meme template")
    return BG[name]


# ---------- shared parts ----------
def lockup(c, h=60, fs=40):
    """Corporate mark + ATLAS ORIGINS. Always large, centred at the top (rule from 3 Nov 2026)."""
    return (f'<div class="abs" style="left:0;right:0;top:84px;text-align:center;z-index:9">'
            f'<span style="display:inline-flex;align-items:center;gap:{int(h*.32)}px;white-space:nowrap">'
            f'<svg height="{h}" viewBox="136 248 1328 1104"><path fill="{c}" d="{MARK}"/></svg>'
            f'<span class="wm" style="color:{c};font-size:{fs}px">ATLAS ORIGINS<sup>&trade;</sup></span></span></div>')


def cta(t, ink=INK, stack=False):
    """Green button (offer + real price), website in bold under it, Shopee/TikTok as a small secondary line."""
    return (f'<span style="display:inline-block;position:relative;z-index:7;background:{G};color:#fff;font:600 38px/1 IT;'
            f'letter-spacing:-.4px;padding:24px 34px 27px;white-space:nowrap;box-shadow:0 10px 24px rgba(0,0,0,.18)">{t} &rarr;</span>'
            f'<div style="position:relative;z-index:7;margin-top:14px;font:400 22px/1.2 IT;color:{ink};white-space:nowrap">'
            f'<span style="font:700 27px IT">origins.atlasdsf.com</span>{"<br>" if stack else "&nbsp;&nbsp;"}'
            f'also on Shopee and TikTok Shop</div>')


def img(src, x, y, w, rot=0, z=2):
    path = src if src.startswith('/') else f'{CUT}/{src}.png'
    return (f'<img class="abs" src="file://{path}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);'
            f'z-index:{z};filter:drop-shadow(0 18px 22px rgba(0,0,0,.22))">')


def smelly(pose):
    """Smelly, the Atlas Origins mascot. pose: 'hug' (body; arms drawn separately on top) or 'present'."""
    if pose == 'hug':
        return f'''<svg class="abs" style="left:150px;top:540px;z-index:1" width="800" height="900" viewBox="0 0 800 900">
<g stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none">
<path d="M40,900 C10,620 30,300 150,170 C260,50 470,10 600,80 C720,145 770,260 760,400 C750,560 770,760 770,900" fill="#fff"/>
<circle cx="440" cy="210" r="26" fill="{INK}" stroke="none"/><circle cx="590" cy="200" r="26" fill="{INK}" stroke="none"/>
</g></svg>'''
    return f'''<svg class="abs" style="left:90px;top:370px;z-index:1" width="560" height="620" viewBox="0 0 560 620">
<g stroke="{INK}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none">
<path d="M60,600 C30,440 50,260 130,170 C200,95 320,85 380,150 C440,215 450,330 430,450 C415,540 420,580 430,600 Z" fill="#fff"/>
<circle cx="250" cy="215" r="17" fill="{INK}" stroke="none"/><circle cx="340" cy="210" r="17" fill="{INK}" stroke="none"/>
<path d="M265,262 Q290,282 318,262"/><path d="M410,300 C450,250 480,190 505,130"/><path d="M430,430 C455,430 475,436 495,446"/>
<path d="M505,130 l-4,-34 M505,130 l18,-28 M505,130 l30,-12 M505,130 l32,10"/>
<path d="M495,446 l14,-28 M495,446 l24,-12 M495,446 l24,8 M495,446 l8,24"/></g></svg>'''


# ---------- templates ----------
def t_search(s):
    """FAMILY: Search intent. Slots: query, hero (image), cta. Optional bg: white, saffron, rose."""
    return f'''<div class="c" style="background:{bg_of(s)}">{lockup(G)}
<div class="abs" style="left:0;right:0;top:282px;text-align:center;font:700 64px/1 IT;letter-spacing:-2.6px">{s.get("label_top","the search:")}</div>
<div class="abs" style="left:214px;width:641px;top:415px;height:80px;background:#fff;border:2.5px solid {INK};border-radius:5px;display:flex;align-items:center">
<svg class="abs" style="left:24px" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" stroke-linecap="round"><circle cx="10" cy="10" r="7"/><path d="M15.5 15.5 21 21"/></svg>
<div style="margin-left:122px;font:400 33px IT;letter-spacing:-.4px">{s["query"]}</div></div>
<div class="abs" style="left:0;right:0;top:572px;text-align:center;font:700 64px/1 IT;letter-spacing:-2.6px">{s.get("label_bottom","the solution:")}</div>
{img(s["hero"], 300, 650, 480)}
<div class="abs" style="left:0;right:0;top:1095px;text-align:center">{cta(s["cta"])}</div></div>'''


def t_problems(s):
    """FAMILY: Problem to solution. Slots: problems (5 short lines, <=27 chars), images (2), cta. Optional bg."""
    for p in s['problems']:
        if len(p) > 27:
            raise ValueError(f"{s.get('name')}: problem line over 27 characters: '{p}'")

    def bub(t, x, y, side):
        tail = (f'<div style="position:absolute;bottom:-15px;{"left:40px" if side=="l" else "right:40px"};width:0;height:0;'
                f'border-left:15px solid transparent;border-right:15px solid transparent;border-top:16px solid {INK}"></div>')
        return (f'<div class="abs" style="left:{x}px;top:{y}px;background:#fff;border:2.5px solid {INK};border-radius:24px;'
                f'font:400 33px/1 IT;letter-spacing:-.3px;padding:24px 26px 27px;white-space:nowrap">{t}{tail}</div>')
    pos = [(40, 470, 'l'), (10, 620, 'r'), (70, 770, 'l'), (40, 920, 'r'), (120, 1070, 'l')]
    bubbles = ''.join(bub(t, *p) for t, p in zip(s['problems'], pos))
    i1, i2 = s['images']
    return f'''<div class="c" style="background:{bg_of(s)}">{lockup(G)}
<div class="abs" style="left:506px;top:196px;width:1.5px;height:1100px;background:#555"></div>
<div class="abs" style="left:0;width:506px;top:210px;text-align:center;font:700 86px/.84 IT;letter-spacing:-4px">your<br><span style="color:{G}">problems</span></div>
<div class="abs" style="left:506px;width:574px;top:210px;text-align:center;font:700 86px/.84 IT;letter-spacing:-4px">our<br>
<span style="position:relative;color:{G}">solution<svg class="abs" style="left:-22px;top:-18px;overflow:visible" width="340" height="110" viewBox="0 0 340 110">
<path d="M40,26 C110,-4 280,0 330,40 C358,66 318,104 190,106 C66,108 -6,86 4,56 C12,34 58,20 150,14 L200,22" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></svg></span></div>
{bubbles}{img(i1, 545, 600, 330)}{img(i2, 790, 800, 230, 0, 3)}
<div class="abs" style="left:506px;right:0;top:1090px;text-align:center">{cta(s["cta"], stack=True)}</div></div>'''


def t_meme(s):
    """FAMILY: Emotional / relatable humour. Slots: quote (2 lines, use <br>), setup, images (3), cta, bg."""
    bg = bg_of(s, 'saffron')
    ink = '#fff' if s.get('bg') == 'green' else INK
    logo = '#fff' if s.get('bg') == 'green' else G
    a, b, c = s['images']
    return f'''<div class="c" style="background:{bg}">{lockup(logo)}
<div class="abs" style="left:40px;right:40px;top:200px;text-align:center;color:{ink};font:700 82px/1.12 IT;letter-spacing:-1.5px">&ldquo;{s["quote"]}&rdquo;</div>
<div class="abs" style="left:0;right:0;top:450px;text-align:center;color:{ink};font:600 40px IT;letter-spacing:-.6px">{s["setup"]}</div>
{smelly('hug')}
<svg class="abs" style="left:150px;top:440px;z-index:6" width="800" height="900" viewBox="0 0 800 900"><g stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"><path d="M60,430 C20,560 120,650 300,665"/><path d="M745,420 C790,560 680,650 500,665"/></g><ellipse cx="305" cy="665" rx="44" ry="30" fill="{INK}"/><ellipse cx="495" cy="667" rx="44" ry="30" fill="{INK}"/></svg>
{img(a, 235, 800, 290, -10, 3)}{img(b, 405, 775, 285, 0, 4)}{img(c, 625, 810, 245, 10, 3)}
<div class="abs" style="left:0;right:0;top:1160px;text-align:center;z-index:8">{cta(s["cta"])}</div></div>'''
# the website line sits on Smelly's white body, so it stays black on every background


def t_presenter(s):
    """FAMILY: Product spotlight. Slots: quote, image, caption (use <br>), accent (one handwritten word), cta. Optional bg."""
    return f'''<div class="c" style="background:{bg_of(s)}">{lockup(G)}
<div class="abs" style="left:0;right:0;top:200px;text-align:center;font:600 64px/1 IT;letter-spacing:-1.2px;color:#2b2b2b">&ldquo;{s["quote"]}&rdquo;</div>
<div class="abs" style="left:176px;top:340px;font:600 42px IT;letter-spacing:-.6px;color:#2b2b2b">{s.get("pivot","But..")}</div>
{smelly('present')}{img(s["image"], 600, 300, 440)}
<div class="abs" style="left:560px;width:500px;top:1010px;text-align:center;font:400 32px/1.25 IT;letter-spacing:-.4px;color:#2b2b2b">{s["caption"]} <span style="font:600 46px Cav;color:{G}">{s["accent"]}</span></div>
<div class="abs" style="left:540px;width:540px;top:1150px;text-align:center">{cta(s["cta"], stack=True)}</div></div>'''


TEMPLATES = {'search': t_search, 'problems': t_problems, 'meme': t_meme, 'presenter': t_presenter}


# ---------- variants ----------
def expand(specs):
    """Turn specs with a "vary" block into one spec per hook x colour. Plain specs pass through unchanged."""
    out = []
    for s in specs:
        v = s.get('vary')
        if not v:
            out.append(s)
            continue
        base = {k: val for k, val in s.items() if k not in ('vary', 'code', 'h_start')}
        hooks = v.get('hooks') or [{}]
        bgs = v.get('bg') or [s.get('bg')]
        h0 = s.get('h_start', 1)
        for (hi, hook), bg in itertools.product(enumerate(hooks), bgs):
            spec = {**base, **hook}
            if bg:
                spec['bg'] = bg
            fmt = bg.upper() if bg else 'STATIC'
            spec['name'] = f"{s['code']}_H{h0 + hi}_{fmt}"
            out.append(spec)
    names = [x['name'] for x in out]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise ValueError(f'duplicate ad names: {sorted(dupes)} (raise h_start so new hooks get new numbers)')
    return out


def contact_sheet(pngs, out_path, cols=4):
    """One overview image of every rendered ad with its name, for quick approval."""
    from PIL import Image, ImageDraw
    tw, th, pad, lab = 324, 405, 24, 34
    rows = (len(pngs) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (tw + pad) + pad, rows * (th + lab + pad) + pad), '#FFFFFF')
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(pngs):
        x = pad + (i % cols) * (tw + pad); y = pad + (i // cols) * (th + lab + pad)
        sheet.paste(Image.open(p).convert('RGB').resize((tw, th)), (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline='#141414')
        d.text((x, y + th + 8), os.path.splitext(os.path.basename(p))[0], fill='#141414')
    sheet.save(out_path)
    return out_path


def fetch_product(pid):
    """Download a product photo from the Origins shop and cut out its white background into CUT/<pid>.png."""
    from PIL import Image, ImageDraw, ImageFilter
    import numpy as np
    os.makedirs(CUT, exist_ok=True)
    raw = f'{CUT}/{pid}_raw.png'
    subprocess.run(['curl', '-s', '-m', '30', '-o', raw,
                    f'https://origins.atlasdsf.com/web/image/product.template/{pid}/image_1024'], check=True)
    im = Image.open(raw).convert('RGB'); w, h = im.size; t = im.copy()
    for p in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1), (w//2, 0), (w//2, h-1), (0, h//2), (w-1, h//2)]:
        if sum(t.getpixel(p)) > 705:
            ImageDraw.floodfill(t, p, (255, 0, 255), thresh=28)
    a = np.array(t); bg = (a[:, :, 0] == 255) & (a[:, :, 1] == 0) & (a[:, :, 2] == 255)
    out = im.convert('RGBA'); out.putalpha(Image.fromarray(np.where(bg, 0, 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2)))
    out.save(f'{CUT}/{pid}.png')


def render(specs, out_dir):
    os.makedirs(out_dir, exist_ok=True); html_dir = os.path.join(out_dir, 'html'); os.makedirs(html_dir, exist_ok=True)
    jobs = []
    for s in specs:
        body = TEMPLATES[s['template']](s)
        p = os.path.join(html_dir, s['name'] + '.html')
        open(p, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
        jobs.append([p, os.path.join(out_dir, s['name'] + '.png')])
    js = f'''import {{ chromium }} from '{WORK}/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch({{args:['--allow-file-access-from-files']}});
for (const [src, out] of jobs) {{ const p = await b.newPage({{viewport:{{width:1080,height:1350}}}});
await p.goto('file://' + src); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await p.screenshot({{path: out, clip:{{x:0,y:0,width:1080,height:1350}}}}); await p.close(); }}
await b.close();'''
    jsf = os.path.join(out_dir, '_shot.mjs'); open(jsf, 'w').write(js)
    subprocess.run(['node', jsf], check=True)
    pngs = [j[1] for j in jobs]
    if len(pngs) > 1:
        contact_sheet(pngs, os.path.join(out_dir, '_contact_sheet.png'))
    return pngs


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    specs = expand(json.load(open(args[0])))
    if only:
        specs = [s for s in specs if s['name'].startswith(only)]
    for s in specs:          # validate every slot before spending time on a render
        TEMPLATES[s['template']](s)
    if '--dry' in sys.argv:
        print('\n'.join(s['name'] for s in specs)); print(f'{len(specs)} ads')
    else:
        print(render(specs, args[1]))
