"""Build an AI video prompt from a shot plan, in the fixed Atlas order, and check it before any money is spent.

Usage:
    python3 shot.py plan.json            print the prompt, the checks and the cost estimate
    python3 shot.py plan.json --json     same, as JSON (for scripts)

A plan is JSON (see ../templates/ for ready ones):
{
  "name": "ORIGINS_UGC_LATE_T4",
  "model": "google/veo-3.1-lite", "seconds": 6, "aspect": "9:16", "resolution": "720p", "audio": true,
  "look": "natural window light, slightly warm, shot on a phone, real home, lived-in",
  "character": {"who": "Malaysian Chinese woman, mid 20s", "face": "...", "hair": "...", "wardrobe": "..."},
  "shots": [
    {"t": [0, 3], "framing": "medium close-up", "angle": "eye level", "move": "locked-off",
     "lens": "phone wide lens", "setting": "...", "action": "...", "line": "Sorry I'm late, traffic was crazy!",
     "delivery": "fast, a little out of breath", "sfx": "car keys dropped on a table"},
    {"t": [3, 6], "cut": "hard cut", ...}
  ],
  "ambient": "quiet apartment room tone",
  "music": "none",
  "keep": ["no phones in frame"]
}
"""
import json, sys

# The only camera moves we use. One per shot. Anything else is a warning.
MOVES = {
    'locked-off': 'locked-off camera on a tripod, no camera movement',
    'slow push-in': 'slow, continuous dolly push-in',
    'slow pull-out': 'slow, continuous dolly pull-out',
    'pan left': 'slow pan left', 'pan right': 'slow pan right',
    'tilt up': 'slow tilt up', 'tilt down': 'slow tilt down',
    'tracking': 'smooth tracking shot moving alongside the subject',
    'orbit': 'slow 90-degree orbit around the subject',
    'crane up': 'slow crane up', 'crane down': 'slow crane down',
    'handheld': 'gentle handheld camera, natural small sway',
    'top-down': 'locked-off top-down overhead camera',
    'pov': 'first-person point-of-view shot from the subject\'s eyes',
    'macro slide': 'slow macro slider move across the object',
    'whip pan': 'fast whip pan',
    'snap zoom': 'quick snap zoom in',
}
FRAMINGS = ['extreme wide', 'wide', 'full shot', 'medium wide', 'medium', 'medium close-up', 'close-up',
            'extreme close-up', 'macro', 'over-the-shoulder', 'two-shot', 'insert']
ANGLES = ['eye level', 'low angle', 'high angle', 'top-down', 'dutch angle', 'worm\'s-eye', 'bird\'s-eye']

# Failures we have already paid for (ugc-video/README.md). Added to every prompt.
HOUSE_KEEP = [
    'every person has exactly two arms and two hands',
    'no on-screen text, no subtitles, no captions',
    'no logos, no brand names, no readable labels',
]
WORDS_PER_SEC = 2.8          # faster than this and the line eats the punchline time
PRICE_PER_SEC = {            # US$ per second, last checked 4 Nov 2026; run list_models for today's price
    ('google/veo-3.1-lite', True): 0.05, ('google/veo-3.1-lite', False): 0.03,
    ('minimax/hailuo-3-max', False): 0.05, ('kwaivgi/kling-v3.0-std', False): 0.084,
}
CALL_CAP = 0.50              # connector cap per call


def cap(t):
    return t[:1].upper() + t[1:]


def ts(x):
    return f'00:{int(x):02d}'


def build(p):
    warn, shots = [], p['shots']
    secs = p.get('seconds', 6)
    # timing
    if shots[0]['t'][0] != 0:
        warn.append('first shot should start at 0')
    for a, b in zip(shots, shots[1:]):
        if a['t'][1] != b['t'][0]:
            warn.append(f'gap or overlap between {a["t"]} and {b["t"]}')
    if shots[-1]['t'][1] != secs:
        warn.append(f'shots end at {shots[-1]["t"][1]}s but the clip is {secs}s')
    if len(shots) > 3:
        warn.append(f'{len(shots)} shots in one generation; more than 3 usually gets merged or skipped')

    lines = []
    head = (f'A single {secs}-second {p.get("aspect", "9:16")} vertical video made of {len(shots)} shot'
            f'{"s" if len(shots) > 1 else ""}. Look: {p["look"]}.')
    lines.append(head)
    ch = p.get('character')
    if ch:
        desc = '; '.join(f'{v}' for k, v in ch.items() if v)
        lines.append(f'Character (the same person, same face, same hair in every shot): {desc}.')
    for i, s in enumerate(shots):
        d = s['t'][1] - s['t'][0]
        move = s.get('move', 'locked-off')
        if move not in MOVES:
            warn.append(f'shot {i+1}: move "{move}" is not in the fixed list; it may be ignored')
        if s.get('framing') not in FRAMINGS:
            warn.append(f'shot {i+1}: framing "{s.get("framing")}" is not in the fixed list')
        if s.get('angle') and s['angle'] not in ANGLES:
            warn.append(f'shot {i+1}: angle "{s["angle"]}" is not in the fixed list')
        if d < 1.5:
            warn.append(f'shot {i+1} is {d}s; under 1.5s the model tends to drop it')
        text = ' '.join(str(s.get(k, '')) for k in ('action', 'setting')).lower()
        if 'selfie' in text and any(w in text for w in ('both hands', 'two hands', 'claps', 'hands up', 'arms')):
            warn.append(f'shot {i+1}: selfie plus a two-handed gesture makes a third arm; put the phone on a tripod')
        if any(w in text for w in ('towards the camera', 'toward the camera', 'approaches the camera', 'walks into the camera')) and move != 'locked-off':
            warn.append(f'shot {i+1}: subject moving at the camera fights the camera move; lock the camera or drop the walk')

        cam = MOVES.get(move, move)
        seg = [f'[{ts(s["t"][0])}-{ts(s["t"][1])}]']
        if i > 0:
            seg.append(f'{s.get("cut", "Hard cut").capitalize()} to:')
        seg.append(f'{s["framing"].capitalize()}, {s.get("angle", "eye level")}, {cam}'
                   f'{", " + s["lens"] if s.get("lens") else ""}.')
        seg.append(cap(s['setting']) + '.' if s.get('setting') else '')
        seg.append(cap(s['action']) + '.')
        if s.get('line'):
            words = len(s['line'].split())
            if words > WORDS_PER_SEC * d:
                warn.append(f'shot {i+1}: {words} words in {d}s is too many to say; cut the line')
            deliv = s.get('delivery', 'natural')
            seg.append(f'{s.get("speaker", "They")} say{"" if s.get("speaker","They")=="They" else "s"}, {deliv}, all within {d - 0.5:g} seconds: "{s["line"]}"')
        if s.get('sfx'):
            seg.append(f'SFX: {s["sfx"]}.')
        lines.append(' '.join(x for x in seg if x))

    audio = [f'Ambient noise: {p["ambient"]}.' if p.get('ambient') else '',
             f'Music: {p.get("music", "none")}.']
    lines.append(' '.join(a for a in audio if a))
    keep = HOUSE_KEEP + p.get('keep', [])
    lines.append('Keep: ' + '; '.join(keep) + '.')
    prompt = '\n'.join(lines)

    model = p.get('model', 'google/veo-3.1-lite')
    rate = PRICE_PER_SEC.get((model, bool(p.get('audio', True))))
    cost = round(rate * secs, 2) if rate else None
    if cost is None:
        warn.append(f'no saved price for {model}; check list_models before generating')
    elif model == 'google/veo-3.1-lite' and p.get('audio', True) and secs > 6:
        warn.append('Veo with audio over 6s trips the connector\'s US$0.50 cap (it estimates high); keep it at 6s')
    elif cost > CALL_CAP:
        warn.append(f'estimated US${cost} is over the US${CALL_CAP} per-call cap; shorten the clip')
    return {'name': p.get('name'), 'model': model, 'seconds': secs, 'aspect': p.get('aspect', '9:16'),
            'resolution': p.get('resolution', '720p'), 'generate_audio': bool(p.get('audio', True)),
            'estimated_cost_usd': cost, 'warnings': warn, 'prompt': prompt}


if __name__ == '__main__':
    r = build(json.load(open(sys.argv[1])))
    if '--json' in sys.argv:
        print(json.dumps(r, indent=1, ensure_ascii=False))
    else:
        print(r['prompt']); print()
        print(f"model {r['model']} | {r['seconds']}s {r['aspect']} {r['resolution']} | audio {r['generate_audio']} | est US${r['estimated_cost_usd']}")
        print('CHECKS: ' + ('all clear' if not r['warnings'] else '\n - ' + '\n - '.join(r['warnings'])))
