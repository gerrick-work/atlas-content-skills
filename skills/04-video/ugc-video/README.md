# AI UGC video ads (Atlas Origins)

The production standard is `../ai-ugc-production/SKILL.md`; prompt syntax is `../video-direction/SKILL.md` (use `shot.py` for every generation). This file keeps the test log and the edit spec.

First test: 4 Nov 2026, "Sorry I'm late, traffic was crazy!" / "the traffic:" meme, remade with an AI persona and Atlas Origins as the punchline.

## Stack
- Model: `google/veo-3.1-lite` on OpenRouter, 6 s, 9:16, 720p, `generate_audio: true`. Actual cost US$0.30 per take (the connector estimates higher, so 8 s trips the US$0.50 per-call cap).
- Both scenes in ONE generation, with a hard cut written into the prompt, keeps the same face across the cut. No reference-image support needed.
- Edit (free, local): TikTok Sans 600 white captions with a soft shadow, light film grain, 2.2 s end card (mark + ATLAS ORIGINS lockup, "Make your own, from RM9.90", origins.atlasdsf.com).
- Finished file: `ORIGINS_UGC_LATE_FINAL.mp4` (Mac: Atlas/OpenRouter Outputs/videos). Total spend for the test: US$0.90 over 3 takes.

## Prompt rules learned
- Never "handheld selfie" plus a two-handed gesture: the model adds a third arm. Use "phone on a tripod, camera never visible, exactly two arms and two hands".
- Describe the same face and hair in a shared character block used by both shots (age, hair length and parting, freckles, brows), and say "hair worn down in both shots".
- Force speed: "says fast, all within two seconds", otherwise the line eats the punchline time.
- Say "no phones in frame" (take 2 put an iPhone on the desk) and "no labels" (still partly ignored, labels are tiny).
- Say "no bag and no sunglasses" in shot 2; continuity carry-over still happens sometimes.

## QC checklist before sending
Hand and arm count every frame, same face across the cut, lip sync, text and labels, objects appearing from nowhere, warping background.

## Disclosure
Tick TikTok's AI-generated content label (and Meta's AI disclosure) when posting. Keep these as skits, never as fake customer testimonials.
