---
name: video-direction
description: Fixed rules for directing AI video (Veo, Kling, Hailuo on OpenRouter): shot plan, framing, camera move, lens, dialogue and audio, built into a checked prompt. Use before every AI video generation, including UGC skits, product b-roll and reel clips.
---

# Video direction (shot and camera prompting)

The one way Atlas writes prompts for AI video. Every other video skill (`explainer-reel`, `atlas-remix`, `hypit`, UGC skits) loads this before it spends money on a generation.

The idea: a director never says "make a nice video". They say what the frame is, where the camera sits, how it moves, what happens, what is heard. The model obeys the same way. Vague prompts get random camera work; slotted prompts get the shot you asked for.

Tools (beside this file in the repo; copies in the appendices in case the repo isn't pulled):
- `shot.py` (Appendix A): turns a shot plan (JSON) into the prompt, in the fixed order, and checks it (timing, move list, words per second, third-arm risk, price cap)
- Templates (Appendix B): ready shot plans to copy (`ugc-skit-2shot.json`, `product-hero.json`). They live in `templates/` beside this file.

## 1. The formula (always this order)

**Camera first, style last.** Put mood words first and they override the camera.

1. **Header:** length, aspect, number of shots, overall look (light, place, how it was "filmed")
2. **Character block:** the same face, hair and clothes written once and reused for every shot (age, face shape, freckles, brows, hair length and parting, "worn down in both shots", outfit)
3. **One segment per shot,** timestamped `[00:00-00:03]`, each in this order:
   framing, angle, camera move, lens, then setting, then action, then the spoken line, then SFX
4. **Cut** written between shots ("Hard cut to:"). Two shots in one generation keep the same face across the cut.
5. **Audio last:** `Ambient noise:` and `Music:` (usually none; music goes on in the edit)
6. **Keep line:** the short "no" list for failures we have actually seen (added automatically)

## 2. The fixed vocabulary

Use only these words. `shot.py` warns on anything else.

**Framing** (what the viewer feels)

| Framing | Use it for |
|---|---|
| wide / extreme wide | where we are; a reveal |
| full shot, medium wide | body language, a whole action at a table |
| medium | talking plus hands (most UGC) |
| medium close-up | a reaction, a line delivered to camera (the hook shot) |
| close-up | emotion, smelling a wrist |
| extreme close-up, macro | a drop, a texture, a cap twisting (product proof) |
| over-the-shoulder | "I'm watching her do it" POV of a friend |
| insert | a hand doing one thing, cut into a sequence |

**Angle:** eye level (default, honest), low angle (makes the product heroic), high angle (small, relatable, "me at 2am"), top-down (flat lay, mixing on a table), dutch angle (chaos, comedy only).

**Camera moves** (one per shot, never two)

| Move | Use it for |
|---|---|
| locked-off | UGC and comedy. Default. Real people film on a tripod or prop the phone |
| slow push-in | build tension, "wait for it", the product moment |
| slow pull-out | the reveal ("she made all of these herself") |
| pan left / right, tilt up / down | follow a line of bottles, bottle to face |
| tracking | walk-and-talk |
| orbit | premium product hero, max 90 degrees |
| crane up / down | opening or closing beat |
| handheld | vlog energy. Never with a selfie or a two-handed gesture |
| top-down | process from above |
| pov | "you" doing it (dropping oil, opening the box) |
| macro slide | slow glide past bottles or droplets |
| whip pan, snap zoom | comedy beat, the punchline cut |

**Lens:** "phone wide lens" (UGC, looks real), "35mm" (natural, cinematic), "85mm, shallow depth of field" (portrait, blurry background), "100mm macro" (drops and textures).

## 3. Hard rules (learned the expensive way)

- One subject, one action, one camera move per shot. If you wrote two moves, delete one.
- Never let the subject walk toward the camera while the camera moves; lock the camera instead.
- Max 3 shots per generation, each at least 1.5 seconds. 6 seconds = 2 shots is the sweet spot.
- Spoken lines in double quotes, with speed ("says fast, all within two seconds"). Max about 2.8 words per second, or the line eats the punchline.
- No "handheld selfie" with any two-handed action: the model adds a third arm. Use "phone on a tripod, camera never visible".
- Describe what IS there first; use "no ..." only for failures we've seen (phones in frame, labels, bags and sunglasses carrying over).
- Products: AI can't draw our real bottles or labels. Show generic amber dropper bottles, glass, droplets, and put the real product in the static end card. If the video tool accepts a start image, use the real product photo as the first frame.
- Real people: AI personas only, never a real person, celebrity or creator's face. Skits only, never presented as a real customer review. Tick the AI-generated label on TikTok and Meta.
- Explainer reels stay faceless (hands only), per `explainer-reel`.

## 4. Remixing a reference video

When Gerrick sends a video to copy the structure of:

1. Break it into a shot table: time, framing, angle, move, what happens, line, sound. (Watch it frame by frame if the file is here; otherwise ask for the file or a screen recording.)
2. Keep the timing, framing and moves. These are why it works.
3. Swap the person, place, product and line for Atlas (Origins: mass market, everyday people, the product as the punchline).
4. Write it as a shot plan and run `shot.py`.

## 5. Workflow (every generation)

1. **Plan:** copy the closest template into the run folder as `plan.json` and fill it.
2. **Check:** `python3 shot.py plan.json`. Fix every warning before going on.
3. **Price:** run the OpenRouter `list_models` once per session for today's video prices. Defaults: `google/veo-3.1-lite` (US$0.05/s with audio, US$0.03/s silent; with audio keep it at 6s or the connector's US$0.50 cap trips), `minimax/hailuo-3-max` or `kwaivgi/kling-v3.0-std` when Veo can't do a motion.
4. **Approve:** show Gerrick the shot table (not the raw prompt) and the cost in one short message; one yes covers up to 3 takes of that plan.
5. **Generate:** OpenRouter `generate_video` with the prompt and the settings `shot.py` printed. Log each take (file, cost, what went wrong) in `takes.md`.
6. **QC every take** before showing it: hand and arm count in every frame, same face across the cut, lip sync, text and labels, objects appearing from nowhere, warping background. Fix the prompt for the specific failure (add one "Keep" item), never rewrite everything.
7. **Edit:** captions (TikTok Sans 600, white, soft shadow), light grain, 2.2s end card with the mark + ATLAS ORIGINS lockup, the real price CTA and origins.atlasdsf.com. Render with the `video-making` skill rules.

Stop after 3 failed takes of one plan and tell Gerrick what keeps failing; the idea may need a different shot, not a fourth roll.

## 6. Recipes (shot plans that work)

| Recipe | Shots | Use |
|---|---|---|
| UGC skit (setup, punchline) | 2: medium close-up line to camera, hard cut to the truth | memes, "Sorry I'm late" type trends |
| Product proof | 1: macro, slow push-in, one drop | b-roll, ad hook shot |
| Hands-only process | 2: top-down mixing, insert of the drop | explainer reels |
| POV | 1: pov, hands opening a box or dropping oil | "you" ads, unboxing |
| Before / after | 2: same framing and move, only the situation changes | problem to solution |
| Reaction | 2: insert of the action, close-up of the face reacting | "smell this" moments |

Templates for the first two are in Appendix B. Save every plan that produced a usable take into `templates/` with a short name and commit, so the library grows.

## Appendix A: shot.py

```python
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
```

## Appendix B: templates

`ugc-skit-2shot.json`
```json
{
 "name": "ORIGINS_UGC_LATE_T4",
 "model": "google/veo-3.1-lite", "seconds": 6, "aspect": "9:16", "resolution": "720p", "audio": true,
 "look": "real Malaysian apartment, natural window light, slightly warm, looks filmed on a phone, casual and unpolished",
 "character": {
  "who": "Malaysian Chinese woman, about 25",
  "face": "round face, light freckles across the nose, straight dark brows",
  "hair": "shoulder-length straight black hair, middle parting, worn down in both shots",
  "wardrobe": "plain oversized cream t-shirt"
 },
 "shots": [
  {"t": [0, 3], "framing": "medium close-up", "angle": "eye level", "move": "locked-off", "lens": "phone wide lens",
   "setting": "she stands just inside her front door, phone on a tripod in front of her, camera never visible",
   "action": "she rushes in, slightly out of breath, and apologises to someone off camera",
   "speaker": "She", "line": "Sorry I'm late, traffic was crazy!", "delivery": "fast and breathless"},
  {"t": [3, 6], "cut": "hard cut", "framing": "medium", "angle": "eye level", "move": "locked-off", "lens": "phone wide lens",
   "setting": "the same woman at her kitchen table, no bag and no sunglasses",
   "action": "she happily drips oil from small amber dropper bottles into a glass beaker, completely absorbed, smiling to herself",
   "sfx": "soft glass clinks"}
 ],
 "ambient": "quiet apartment room tone",
 "music": "none",
 "keep": ["no phones in frame", "no bag and no sunglasses in the second shot"]
}
```

`product-hero.json`
```json
{
 "name": "ORIGINS_BROLL_DROPPER",
 "model": "google/veo-3.1-lite", "seconds": 4, "aspect": "9:16", "resolution": "720p", "audio": false,
 "look": "bright clean daylight, white marble counter, soft shadows, premium but natural",
 "shots": [
  {"t": [0, 4], "framing": "macro", "angle": "eye level", "move": "slow push-in", "lens": "100mm macro lens, shallow depth of field",
   "setting": "a small amber glass dropper bottle on a white marble counter",
   "action": "a single golden drop falls from the dropper tip into a clear glass vial, a tiny ripple, only hands visible, no faces"}
 ],
 "keep": ["no faces"]
}
```
