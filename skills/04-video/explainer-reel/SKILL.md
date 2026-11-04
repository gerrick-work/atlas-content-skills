---
name: "explainer-reel"
description: "Make a polished vertical explainer reel for Atlas DSF or Atlas Origins from a topic: provocative script, AI b-roll and voice via OpenRouter (max US$1 per reel), diagram moments, HyperFrames render, then /ship-content."
---

# Explainer reel

One linear pipeline: 10 stages, 3 approval gates. Every stage writes a file into the run folder, so a stopped run resumes from the last file that exists. Do not skip or reorder stages. Use the task list: one task per stage.

Run folder: `/home/claude/reels/<YYYY-MM-DD>-<slug>/` with `src/`, `scripts/`, `project/{clips,img,fonts,audio,assets/vendor}`, `out/`.

## Budget (hard rule)

- **US$1.00 maximum per reel**, across every OpenRouter call (video, image, voice, re-rolls).
- Keep `budget.md` in the run folder: one line per call (tool, model, cost from the tool result) and a running total. Check it before every paid call. If the next call would pass US$1, stop generating and fill the gap with a diagram moment or a Pexels clip (Appendix A).
- Before planning, run `list_models` for video, image and audio to get today's prices; models and prices change.
- Default mix that fits: 4 AI video clips (about US$0.48), 3 AI images (about US$0.14), per-line voice (about US$0.02), leaving room for one or two re-rolls.

## Tools, picked per job (never one repo for everything)

| Job | Default | Notes |
|---|---|---|
| Hero b-roll clips | OpenRouter `generate_video`, `google/veo-3.1-lite`, 4s, 720p, 9:16, no audio (US$0.03/s) | Cheapest good-looking option. `minimax/hailuo-3-max` 480p (US$0.05/s) or `kwaivgi/kling-v3.0-std` (US$0.084/s) when Veo struggles with a motion |
| Cut-out objects for diagrams | OpenRouter `generate_image`, `black-forest-labs/flux.2-pro` (about US$0.045), prompt "isolated on a pure flat white background, no shadow" | Cut out in the workspace with an edge flood-fill (Stage 5). `tencent/hy-image-v3.5-preview` is the near-free fallback |
| Voice | OpenRouter `text_to_speech`, `elevenlabs/eleven-flash-v2.5`, voice `sarah`, mp3, **one call per script line** | Per-line calls give exact caption timing and cost about a cent in total. Gemini TTS only returns raw pcm, which the connector cannot save, so skip it. Kokoro (local, free, Appendix B) is the fallback |
| Diagrams, numbers, end card | HyperFrames HTML + GSAP | Never AI-generated |
| Music | `music.py` (Stage 7), generated locally | Free |
| Stock fallback | Pexels through Chrome (Appendix A) | Only when the budget is spent or AI can't do the shot |
| Optional looks | Lemo-Opuscar style cards (MIT, github.com/lemomo-ai/lemo-opuscar) for diagram moments; our own continuous-take mode (Stage 4) | Never use onetake (noncommercial licence) |

OpenRouter files land on Gerrick's Mac in `~/Atlas/OpenRouter Outputs/{videos,images,audio}`. Bring them into the workspace with `device_stage_files`. If that folder isn't connected, call `device_request_folder_access` for `~/Atlas/OpenRouter Outputs` once and tell Gerrick to tap Allow.

## House rules (Atlas DSF and Atlas Origins)

- **Format:** 1080x1920, 30fps, 35 to 50s.
- **Faceless:** never Gerrick's face or voice. AI hands are fine. Prompt every clip with "only hands visible, no faces, no text, no logos, no labels".
- **No real brands:** no recognisable bottles, logos, currency designs or competitor products. Money is "plain paper money with no visible currency design".
- **Type:**
  - Jost, the brand typeface, copied from npm `@fontsource/jost@5.0.18` (`files/jost-latin-{300,400,700}-normal.woff2`) into `project/fonts/`.
  - Headlines Jost 700; everything else Jost 400; big numbers Jost 300.
  - White type.
- **Colour (the Atlas brand identity, approved 9 Oct 2026; the atlas-social-posts skill holds the full system):**
  - Type is white, black or Atlas green `#2C463A` only.
  - Forest green is always a gradient, never flat: deep `#1F3429` → forest `#2C463A` → jade `#4F7A60` → mist `#86AE94`, or forest → white.
  - Prompt AI clips toward "deep forest green and cream tones" so they sit in the brand palette.
  - One bright accent per reel, on the single most important word or number only: DSF signal lime `#D4F53C`, Origins bright lilac `#B9A4FF`. Everything else is white or mist.
  - NO orange anywhere. Ignore the old "Atlas Brand Kit" artifact; it was a demo.
- **End card:**
  - The account's wordmark (`ATLAS DSF™` or `ATLAS ORIGINS™`), the tagline, and the CTA from `angle.md` as one short line. Use `Follow @atlasdsf.my` or `Follow @atlasorigins.my` only when the CTA is a follow.
  - The CTA is also the last voice line.
  - Set over a forest gradient (`linear-gradient(165deg, #1F3429 0%, #2C463A 40%, #4F7A60 78%, #7FA88D 100%)`).
  - The wordmark appears on the end card only, because the Reels UI covers the corners.
- **No em dashes anywhere:** script, on-screen text, caption.
- **Never on screen:**
  - header bars, footers, progress bars
  - grid backgrounds, monospace labels, subtitle bands
  - large empty areas: diagrams fill y 250 to 1150 with big objects and big numbers
  - After the hook, the on-screen type IS the caption: it mirrors the voice line by line. During the hook (the first 3s), the on-screen text complements the voice instead of repeating it.
- **Claims:** read `/areas/atlas-positioning.md` and `/areas/the-bench.md`. Only claims Atlas can defend today. No locations, no invented figures or third parties.

## Gates (ask once each, AskUserQuestion)

1. Script approval. Skip only if the user said "just make it".
2. Spend approval: show the shot list with model, seconds and estimated cost per paid call, plus the total against US$1. Skip only if the user said "just make it".
3. Publish approval: held by `/ship-content`.

If the user is unattended, stop at the gate, deliver what exists, and say what is waiting.

## Stage 1. Brief -> `brief.md`

Collect the topic and angle, account (Atlas DSF or Atlas Origins), post date and time (Asia/Kuala_Lumpur), platforms, length, funnel role (Discover, Trust or Convert; TOFU, MOFU or BOFU on the task) and CTA. If it comes from the Odoo content calendar (project "Atlas Content Calendar", id 5), read the task's Angle, CTA and funnel tag through Chrome, as the atlas-social-posts skill describes. Read the memory files atlas-positioning, the-bench, atlas-identity, social-accounts and marketing-os. Ask only for what is missing, in one AskUserQuestion.

## Stage 2. Angle, claims ledger and script -> `angle.md`, `claims.md`, `script.json`, `hooks-alt.json`

1. **Angle.** Load the `atlas-script-lab` skill with the Skill tool and run it with the brief (format: reel). Save its angle brief as `angle.md`. It must pass the lab's stimulation check (section 6b): a hook that opens a loop or picks a fight, a blunt answer by second 5, a pattern break near the middle, and a stakes line. If it reads like a gentle tip, send it back.
2. Write `claims.md`: every factual statement the video will make, each with its source (a memory file line, or a web URL). No source, no claim.
3. Fact-check with a subagent: spawn one general-purpose Agent with only `claims.md` and the sources. Ask it to mark each claim supported, overstated or unsupported, with a reason. Fix or cut anything not supported, and update `angle.md` if a proof point falls away.
4. Script shape (about 100 to 120 words), following the reel spine in `angle.md`:
   - Hook in the first 2s. Its visual is the first AI clip.
   - On-ramp, mechanism (2 to 3 lines), pattern break, stakes, payoff, CTA as the final line.
   - One idea per line; each line becomes one voice call.
   - Spell acronyms with spaces for the voice ("Atlas D S F"). Spell keywords so the voice says them clearly and the screen shows them in capitals ("comment launch" spoken, `Comment LAUNCH` on screen).
5. Write `script.json`: `[{"say": "...", "screen": ["..."], "hl": [1], "pause": 0.3}, ...]`.
   - `screen` is 2 to 4 lines, about 20 characters each; split lines explicitly so no word is orphaned.
   - `hl` marks the one line set as a 104px headline (short punch lines only).
   - Hook lines: `screen` holds the lab's on-screen anchor, which complements `say` rather than repeating it. Every later line mirrors `say`.
6. Write `hooks-alt.json` with the two alternate hooks as replacement opening lines (same format, plus a `"visual"` note each) for later variant renders; don't render them now.
7. Gate 1: show `angle.md` (hook, alternates, CTA) and the script together.

## Stage 3. Voiceover -> `project/audio/vo.wav`, `vo.json`

One `text_to_speech` call per script line (`elevenlabs/eleven-flash-v2.5`, voice `sarah`, mp3), run in parallel. Stage the files, then join them with exact timings:

```python
# scripts/vo_join.py  usage: python3 -I vo_join.py script.json file1.mp3 file2.mp3 ...  (files in script order)
import json, subprocess, sys, numpy as np
lines = json.load(open(sys.argv[1])); files = sys.argv[2:]; assert len(files) == len(lines)
SR = 48000; t = 0.25; chunks = [np.zeros(int(0.25 * SR))]; meta = []
for f, ln in zip(files, lines):
    a = np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout, np.float32).astype(float)
    idx = np.where(np.abs(a) > 0.02 * np.abs(a).max())[0]; a = a[max(0, idx[0]-480): idx[-1]+2400]
    d = len(a) / SR; meta.append({"say": ln["say"], "start": round(t,3), "end": round(t+d,3)})
    p = ln.get("pause", 0.3); chunks += [a, np.zeros(int(p*SR))]; t += d + p
x = np.concatenate(chunks); x = x / np.abs(x).max() * 0.89; x.astype(np.float32).tofile('vo_raw.f32')
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','vo_raw.f32','-af',
  'highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=7',
  '-ar','48000','-ac','2','project/audio/vo.wav'], check=True)
json.dump({"duration": round(t,3), "lines": meta}, open('project/audio/vo.json','w'), indent=1)
for m in meta: print(f'{m["start"]:6.2f}-{m["end"]:6.2f}  {m["say"]}')
```

Never generate the whole script as one voice file: it has no clean pauses and captions can't be synced to it. Total voice length should be the video length minus about 2.5s for the end card hold.

## Stage 4. Shot plan -> `shots.md`, Gate 2

Mix three kinds of shot. A reel that is all one kind looks templated.

- **AI clips (3 to 5):** the hook, any physical action (cutting, splitting, pouring, breaking), the founder POV. Each prompt names the action, the light ("deep forest green and warm gold"), "vertical", "only hands visible, no faces, no text, no logos, no labels". Every clip must show something happening, never a static product turntable.
- **Diagram moments (2 to 3), built in HTML:** the big number (count-up, the reel's one accent colour), the mechanism (bars, stacks, splits) using the AI cut-outs as objects, and a product moment (hero cut-out + one UI card). Orbs and backgrounds have character (gradient edges, glow), never flat.
- **End card.**

Rules:
- **Cuts:** one shot per voice line, cut on the line's start time from `vo.json`.
- **Hook:** hard cuts only, first two shots under 2.7s each.
- **After the hook:** 0.45s crossfades and a slow push-in on every shot (scale 1.00 to 1.075).
- **Pattern break:** the shot under the pattern-break line changes register (graphic to footage, or a sudden close-up).
- **Poster (frame 0):** the hook clip with the title at the top over a top scrim.
- **Optional continuous-take mode:** instead of crossfades between diagram moments, carry one object from beat to beat on one camera canvas (write `carry-plan.md`: beat, object, what it becomes; flag any beat change where nothing carries). Use it when Gerrick asks for a "one take" feel.

List every paid call in `shots.md` with model, seconds and estimated cost, total it against US$1, and run Gate 2.

## Stage 5. Generate -> `src/`

1. Run the video calls (`wait_minutes: 1`; resume with `video_status` if one returns a job id) and the image calls in parallel. Log each cost in `budget.md`.
2. Stage everything with `device_stage_files` and copy into `src/` with short names (`v_hook.mp4`, `i_bottle.jpg`).
3. Contact-sheet every clip (`fps=1.5,scale=180:-1,tile=6x1`) and read it. Re-roll a clip only if it shows a face, readable text, a logo or a broken object, and only if the budget allows.
4. Cut out the images (an edge flood-fill keeps white glass and highlights inside the object):

```python
# python3 -I, run per image
import numpy as np; from PIL import Image, ImageFilter; from collections import deque
im = Image.open('src/i_bottle.jpg').convert('RGB'); a = np.asarray(im).astype(int); H, W, _ = a.shape
d = np.abs(255 - a).max(axis=2); bg = np.zeros((H, W), bool); q = deque()
for x in range(W): q += [(0, x), (H-1, x)]
for y in range(H): q += [(y, 0), (y, W-1)]
while q:
    y, x = q.popleft()
    if 0 <= y < H and 0 <= x < W and not bg[y, x] and d[y, x] < 22:
        bg[y, x] = True; q.extend([(y+1, x), (y-1, x), (y, x+1), (y, x-1)])
al = Image.fromarray(np.where(bg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
out = im.copy(); out.putalpha(al); out.crop(out.getbbox()).save('project/img/i_bottle.png')
```

## Stage 6. Trim and grade -> `project/clips/`

Grade once in FFmpeg; HyperFrames' WebGL grading is too slow on a 2-core workspace. AI clips come in at 720x1280, 24fps, 4s; upscale, sharpen, grade and retime in one pass. `scripts/prep.py`, run as `python3 prep.py clips.json`:

```python
import json, subprocess, sys
BASE=("eq=contrast=1.06:saturation=0.9:gamma=0.98,"
 "curves=r='0/0.012 0.25/0.232 0.75/0.765 1/0.985':g='0/0.03 0.25/0.252 0.75/0.762 1/0.988':b='0/0.026 0.25/0.244 0.75/0.752 1/0.972'")
for c in json.load(open(sys.argv[1])):
    slow=c.get("slow",1.0); pre=f"setpts=PTS*{slow},minterpolate=fps=30:mi_mode=blend," if slow!=1 else ""
    vf=f"{pre}fps=30,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,unsharp=5:5:0.5,{BASE}" + (f",{c['post']}" if c.get("post") else "") + ",format=yuv420p"
    subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",str(c["in"]),"-i",f"src/{c['src']}","-t",str(c["len"]),"-vf",vf,"-an",
      "-c:v","libx264","-crf","16","-g","15","-movflags","+faststart",f"project/clips/{c['name']}.mp4"],check=True); print("ok",c["name"])
```

- `clips.json`: `[{"name":"s0","src":"v_hook.mp4","in":0.0,"len":2.6,"slow":1.0,"post":""}]`; `len` = shot length + 0.6s.
- A 4s clip covers a line up to about 3.3s. For longer lines use `slow` (1.3 to 1.45 works for slow-motion actions), or reuse the clip's other half for a second line.
- `post` fixes: dark shots `curves=all='0/0 0.06/0.04 0.25/0.46 1/1'`; loud colour `eq=saturation=0.78`; end-card footage `eq=brightness=-0.03`.
- Read a contact sheet of all graded clips before moving on.

## Stage 7. Music bed -> `project/audio/music-bed.wav`

An ambient pad, pluck arpeggio and soft pulse, ducked under the voice, with a soft swell into each section change (up to 6: hook end, pattern break, stakes, payoff). Run `python3 music.py project/audio/vo.wav project/audio/music-bed.wav <duration> "<swell times>"`:

```python
import sys, subprocess, numpy as np, soundfile as sf
vo_path, out, dur = sys.argv[1], sys.argv[2], float(sys.argv[3])
swells = [float(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 and sys.argv[4] else []
SR = 48000; N = int(SR * dur); rng = np.random.default_rng(7); mix = np.zeros((N, 2))
midi = lambda n: 440 * 2 ** ((n - 69) / 12)
CH = [[47, 54, 57, 61, 62], [43, 50, 54, 57, 59], [42, 50, 54, 57, 62], [45, 52, 57, 59, 61]]; BAR = 5.0; BEAT = 60 / 96
def add(sig, at, pan=0.5):
    s0 = int(at * SR); s1 = min(N, s0 + len(sig))
    if s0 < 0 or s1 <= s0: return
    mix[s0:s1, 0] += sig[: s1 - s0] * pan; mix[s0:s1, 1] += sig[: s1 - s0] * (1 - pan)
for ci in range(int(dur // BAR) + 1):
    tt = np.arange(int(7.2 * SR)) / SR; env = (np.clip(tt / 1.3, 0, 1) * np.clip((7.2 - tt) / 1.6, 0, 1)) ** 1.5
    for n in CH[ci % 4][1:]:
        for det, pan in ((-0.07, 0.8), (0, 0.5), (0.07, 0.2)):
            f = midi(n) * 2 ** (det / 12); ph = rng.uniform(0, 6.28)
            add(sum(np.sin(2 * np.pi * f * h * tt + ph * h) / h ** 1.6 for h in range(1, 7)) * env * 0.022, max(0, ci * BAR - 0.6), pan)
pat = [3, 1, 4, 2, 3, 1, 4, 0]; at = 3.8; k = 0
while at < dur - 7.8:
    f = midi(CH[int(at // BAR) % 4][pat[k % 8]] + 24); tt = np.arange(int(0.9 * SR)) / SR
    add((np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt)) * np.exp(-tt / 0.16) * 0.035, at, 0.3 if k % 2 else 0.7); at += BEAT / 2; k += 1
at = 11.1
while at < dur - 7.8:
    tt = np.arange(int(0.35 * SR)) / SR; add(np.sin(2 * np.pi * np.cumsum(46 + 70 * np.exp(-tt / 0.03)) / SR) * np.exp(-tt / 0.12) * 0.16, at); at += BEAT
def reverb(x, seed):
    n = int(2.4 * SR); ir = np.random.default_rng(seed).standard_normal(n) * np.exp(-np.arange(n) / SR / 0.48); ir /= np.sqrt((ir ** 2).sum())
    m = 1 << (len(x) + n - 1).bit_length(); return np.fft.irfft(np.fft.rfft(x, m) * np.fft.rfft(ir, m), m)[: len(x)]
mix[:, 0] += 0.35 * reverb(mix[:, 0], 1); mix[:, 1] += 0.35 * reverb(mix[:, 1], 2)
t = np.arange(N) / SR; mix *= (np.clip(t, 0, 1) * np.clip((dur - t) / 2.5, 0, 1))[:, None]
v, vsr = sf.read(vo_path); v = v.mean(axis=1) if v.ndim > 1 else v; h = int(0.01 * vsr)
e = np.array([np.sqrt(np.mean(v[i:i + h] ** 2)) for i in range(0, len(v) - h, h)]); e /= e.max(); sm = np.zeros_like(e)
for i in range(len(e)): p = sm[i - 1] if i else 0; sm[i] = p + (0.25 if e[i] > p else 0.03) * (e[i] - p)
mix *= np.interp(t, np.arange(len(sm)) * 0.01, 1 - 0.5 * np.clip(sm * 2.2, 0, 1), right=1.0)[:, None]
for sc in swells:
    tt = np.arange(int(0.7 * SR)) / SR; nz = np.convolve(rng.standard_normal(len(tt)), np.ones(24) / 24, "same")
    add(nz * np.sin(np.pi * tt / 0.7) ** 2 * 0.25, sc - 0.45)
sf.write("bed_raw.wav", (mix / np.abs(mix).max() * 0.5).astype(np.float32), SR)
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", "bed_raw.wav", "-af", "loudnorm=I=-30:TP=-6:LRA=11", "-ar", "48000", out], check=True)
```

Voice at -15 LUFS plus the bed at -30 LUFS mixes to about -15 LUFS, which is right for Reels.

## Stage 8. Build the composition -> `project/index.html`

Setup (Chrome for Testing downloads are blocked, so use the npm Chromium):

```bash
cd /home/claude/reels && npm i hyperframes@0.8.140 gsap @sparticuz/chromium @fontsource/jost@5.0.18
node -e "require('@sparticuz/chromium').default.executablePath().then(console.log)"   # prints /tmp/chromium
export HYPERFRAMES_BROWSER_PATH=/tmp/chromium
```

Clone `heygen-com/hyperframes` once and read `skills/hyperframes-core/SKILL.md` before writing HTML. Write the composition from a Python builder (`scripts/build.py`) that reads `vo.json` and `script.json`, so edits are data, not hand-edited HTML. Copy GSAP from `node_modules/gsap/dist/gsap.min.js` into `assets/vendor/`; CDNs are blocked.

Structure that works:
- **Root:** `<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-duration="D">`, background `#000`.
- **Video shots:** an untimed wrapper `<div class="shot" id="wS">` (it gets the push-in scale and fade-in opacity) holding a timed `<video class="clip media" muted playsinline data-start data-duration src>` plus a bottom scrim (forest `rgba(31,52,41,.82)` to transparent, 1000px). Never put `data-start` on both. The outgoing shot stays until the incoming fade finishes. Add a top scrim when text sits at the top.
- **Diagram shots:** a timed `<div class="clip gfx">` holding one inner `.gin` node; animate `.gin` and its children, never the `.clip` itself. Background is a forest gradient plus one or two characterful orbs.
- **Motion:** animate transforms only (x, y, scale, rotation, opacity). `top`, `left`, `width` and `height` tweens fail lint (`gsap_non_transform_motion`); set sizes in CSS and use `scaleX`/`scaleY` with a `transformOrigin`.
- **Text groups:** timed `<div class="t clip">` holding `<span class="ln">` lines.
  - In: `{opacity:0, y:34, filter:'blur(14px)'}` to settled over 0.65s `expo.out`, staggered 0.2s per line. Hook lines snap in (0.12s).
  - Out: 0.22s `power2.in` just before the next line.
- **Type scale:** headline 104px / 700 / -0.03em; body 62px / 400; big number 400px / 300 / -0.055em with a count-up from a tweened object in `onUpdate`.
- **Safe zone for the Reels UI:** x 76 to 956, y 250 to 1450. Bottom text block at `bottom: 470px`.
- **Poster:** a timed clip at `data-start="0" data-duration="0.034"` with a top scrim and the title.
- **Audio:** `<audio id="vo">` and `<audio id="bed">`. Each needs an `id`, or the render is silent.
- **Timeline:** one paused `gsap.timeline`, registered last as `window.__timelines["main"]`. Use a seeded PRNG only. Add `immediateRender:true` to the first `fromTo` on a target and `immediateRender:false` to later ones.

## Stage 9. QA (before and after the full render)

1. `npx hyperframes lint` with 0 errors.
2. `npx hyperframes snapshot --at <every shot midpoint> --no-end --describe false`, then read `snapshots/contact-sheet*.jpg`. Fix before rendering:
   - orphaned words, or text over a face, hand action or product
   - weak contrast on bright footage, or dark shots where the subject is invisible
   - a diagram that leaves a large empty area (scale it up to fill y 250 to 1150)
   - labels overlapping each other or hidden under another layer
   - the accent colour used in more than one moment
   - a poster title over the main subject
   - any orange, em dash, flat green, readable AI text or logo, or bold text other than headlines
3. Render: `npx hyperframes render -o out/master.mp4 -f 30 -q delivery -w 2` in the background (about 3 to 7 minutes), then wait for the notification.
4. Verify: 1080x1920 at 30fps; integrated loudness about -15 LUFS; voice offset 0 ms (cross-correlate the `vo.wav` envelope against the render's audio).

## Stage 10. Deliver and hand off

1. Encode into `out/` (under `/home/claude`; Chrome uploads accept workspace paths only):
   - **Chat copy:** `-crf 19`, under 30 MB for SendUserFile.
   - **Upload copy:** `-crf 23 -maxrate 1500k -bufsize 3000k -b:a 128k`, under 10 MB for the Chrome upload.
   - **Cover:** a JPG of frame 0.
   - Send the chat copy and the cover.
2. Caption, following the lab's caption rule: the hook idea in a fresh sentence, one proof line, the brand line, the CTA, then 5 hashtags. Plain text, no em dashes.
3. Run `/ship-content` with the upload copy path, cover, caption, account, date/time and platforms, marked as a reel, plus the funnel role and CTA keyword from `angle.md`. It holds Gate 3 and does the Meta Business Suite steps.

Finish with: the file, one line on the hook, the CTA used (and whether its offer is live), the OpenRouter spend from `budget.md`, when and where it is scheduled, and anything left waiting at a gate.

## Appendix A: Pexels fallback (budget spent, or a shot AI can't do)

The workspace can't reach Pexels, so search and download through Claude in Chrome. Read the chrome-browser skill first. Run `list_connected_browsers`: the zip lands in the Downloads folder of the computer running Chrome, which must be the computer linked to this session. If it isn't, stop and ask Gerrick to open this chat in the Claude desktop app on that computer.

Open one new tab at `https://www.pexels.com` and inject the helpers:

```js
window.__C = window.__C || {};
window.pxSearch = async function (kind, q, orient, n) {
  const url = (kind === 'video' ? '/search/videos/' : '/search/') + encodeURIComponent(q) + '/' + (orient ? '?orientation=' + orient : '');
  const t = await (await fetch(url)).text();
  const j = JSON.parse(t.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/)[1]);
  const d = j.props.pageProps.initialData; const arr = (d.data || d);
  return arr.slice(0, n || 8).map(it => { const a = it.attributes || it;
    if (kind === 'video') return { kind, id: a.id, title: a.title, w: a.width, h: a.height, dur: a.duration, user: a.user && a.user.username,
      thumb: a.video && a.video.thumbnail && (a.video.thumbnail.medium || a.video.thumbnail.small),
      files: (a.video && a.video.video_files || []).map(f => ({ w: f.width, h: f.height, fps: f.fps, link: f.link })) };
    return { kind, id: a.id, title: a.title || a.alt, user: a.user && a.user.username, thumb: a.image && (a.image.medium || a.image.small) }; });
};
window.showSheet = function (keys) {
  let o = document.getElementById('__sheet'); if (o) o.remove();
  o = document.createElement('div'); o.id = '__sheet';
  o.style.cssText = 'position:fixed;inset:0;z-index:2147483647;background:#111;color:#fff;font:12px monospace;overflow:hidden;padding:6px';
  keys.forEach(k => { const row = document.createElement('div'); row.style.cssText = 'display:flex;gap:6px;margin-bottom:6px';
    const lab = document.createElement('div'); lab.textContent = k; lab.style.cssText = 'width:110px;flex:none;color:#9CC5A8'; row.appendChild(lab);
    (window.__C[k] || []).forEach((it, i) => { const c = document.createElement('div'); c.style.cssText = 'width:108px;flex:none';
      c.innerHTML = `<img src="${it.thumb}" style="width:108px;height:192px;object-fit:cover;display:block"><div>${i}:${it.id}</div>`; row.appendChild(c); });
    o.appendChild(row); });
  document.body.appendChild(o); return 'ok';
};
```

1. Run each missing shot's queries into `window.__C[key]` (videos with `'portrait'`), show the contact sheet, screenshot it (wait 4s for thumbnails) and pick: portrait, at least 1080 wide, at least the shot length plus 0.6s, no labels or logos, matching mood.
2. Build `window.__DL = [{name, url, id, user, title}]`. Videos: the portrait file closest to 1080 wide (`files.filter(f => f.h > f.w).sort((a,b) => Math.abs(a.w-1080)-Math.abs(b.w-1080))[0]`). Photos: `https://images.pexels.com/photos/${id}/pexels-photo-${id}.jpeg?auto=compress&cs=tinysrgb&w=1400`. HEAD each URL for its size, and ask permission with filename, source and total size before downloading.
3. Download everything as one uncompressed zip (one Chrome download, no multi-download prompt):

```js
document.getElementById('__sheet')?.remove();
const T = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; T[n] = c >>> 0; }
const crc32 = u => { let c = 0xFFFFFFFF; for (let i = 0; i < u.length; i++) c = T[(c ^ u[i]) & 0xFF] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; };
const enc = new TextEncoder(), ZIP = 'SLUG-pexels', entries = [];
for (const d of window.__DL) { const r = await fetch(d.url); if (!r.ok) throw new Error(d.name); entries.push({ name: d.name, data: new Uint8Array(await r.arrayBuffer()) }); }
entries.push({ name: 'CREDITS.txt', data: enc.encode('Pexels licence: free to use and modify, no attribution required.\n' + window.__DL.map(d => `${d.name}\t${d.id}\t${d.user}\t${d.title}`).join('\n')) });
const parts = [], central = []; let off = 0;
for (const e of entries) { const nm = enc.encode(ZIP + '/' + e.name), crc = crc32(e.data), sz = e.data.length;
  const h = new DataView(new ArrayBuffer(30)); h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint16(12, 0x5521, true); h.setUint32(14, crc, true); h.setUint32(18, sz, true); h.setUint32(22, sz, true); h.setUint16(26, nm.length, true);
  parts.push(new Uint8Array(h.buffer), nm, e.data);
  const c = new DataView(new ArrayBuffer(46)); c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint16(14, 0x5521, true); c.setUint32(16, crc, true); c.setUint32(20, sz, true); c.setUint32(24, sz, true); c.setUint16(28, nm.length, true); c.setUint32(42, off, true);
  central.push(new Uint8Array(c.buffer), nm); off += 30 + nm.length + sz; }
const cd = central.reduce((a, b) => a + b.length, 0), end = new DataView(new ArrayBuffer(22));
end.setUint32(0, 0x06054b50, true); end.setUint16(8, entries.length, true); end.setUint16(10, entries.length, true); end.setUint32(12, cd, true); end.setUint32(16, off, true);
const blob = new Blob([...parts, ...central, new Uint8Array(end.buffer)], { type: 'application/zip' });
const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = ZIP + '.zip'; document.body.appendChild(a); a.click(); a.remove();
`${(blob.size / 1e6).toFixed(1)} MB`
```

4. If `~/Downloads` is not connected, call `device_request_folder_access` for it. Stage the zip with `device_stage_files`, unzip in the workspace with `python3 -I` and `zipfile` (reject names with `/` or `..`), copy the clips into `src/`, and close the tab. Pexels sources are often 1080 wide or more: in `prep.py` the scale-and-crop handles them, and `ybias` framing can be added by changing the crop's y offset.

## Appendix B: Kokoro voice fallback (free, local)

Use when OpenRouter speech is down. GitHub release downloads work through the proxy; Hugging Face does not.

```bash
mkdir -p /home/claude/kokoro && cd /home/claude/kokoro
curl -sSL -o kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sSL -o voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
pip install --break-system-packages -q kokoro-onnx soundfile
```

```python
"""Usage: python3 tts.py script.json out_dir [voice] [speed]  -> out_dir/vo.wav (48k stereo, -15 LUFS) + vo.json"""
import json, sys, subprocess, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
K = "/home/claude/kokoro"
lines = json.load(open(sys.argv[1])); out = sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "af_heart"; speed = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
k = Kokoro(f"{K}/kokoro-v1.0.onnx", f"{K}/voices-v1.0.bin"); SR = 24000
t = 0.35; chunks = [np.zeros(int(0.35 * SR), np.float32)]; meta = []
for ln in lines:
    s, _ = k.create(ln["say"], voice=voice, speed=speed, lang="en-us"); s = s.astype(np.float32)
    idx = np.where(np.abs(s) > 0.01 * np.abs(s).max())[0]; s = s[max(0, idx[0] - 240): idx[-1] + 1200]
    d = len(s) / SR; meta.append({"say": ln["say"], "start": round(t, 3), "end": round(t + d, 3)})
    chunks += [s, np.zeros(int(ln.get("pause", 0.4) * SR), np.float32)]; t += d + ln.get("pause", 0.4)
a = np.concatenate(chunks); sf.write(f"{out}/vo_raw.wav", a / np.abs(a).max() * 0.89, SR)
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{out}/vo_raw.wav", "-af",
    "highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=7",
    "-ar", "48000", "-ac", "2", f"{out}/vo.wav"], check=True)
json.dump({"duration": round(t, 3), "lines": meta}, open(f"{out}/vo.json", "w"), indent=1)
for m in meta: print(f'{m["start"]:6.2f}-{m["end"]:6.2f}  {m["say"]}')
```

Check pronunciation of brand words first with `Kokoro(...).tokenizer.phonemize("Atlas D S F", "en-us")`.