---
name: ai-ugc-production
description: Production standard for realistic, conversion-oriented AI UGC videos (creator-style phone footage: recommendation, first impression, unboxing, demonstration, problem-solution, skits). Use for any AI UGC concept, script, prompt or review; works with video-direction for the shot syntax and shot.py.
---

# AI UGC Production Skill

## Mission

Create AI-generated UGC that feels like a real person independently filming on a phone for a believable reason, while communicating a clear product benefit and motivating the intended audience to act.

This skill is a production standard, not a prompt collection. Apply it consistently whenever generating, reviewing, or revising AI UGC concepts, scripts, shot descriptions, or video-generation prompts.

## Governing principle

**Describe how the video was filmed, not just what the video is about.**

A concept such as "a woman talks about skincare in a nice bathroom and smiles" describes a subject and topic. It does not define the recording behaviour. The model fills those gaps with generic commercial conventions: flattering lighting, perfect framing, polished delivery, staged gestures, and an advertisement-like finish.

Instead, specify:
- Who is filming and why.
- Where the phone is and how it is being held.
- What the creator is doing with the product.
- What happens in the first one to three seconds.
- What the creator says and how naturally they say it.
- What imperfections make the recording credible.
- Which visual and performance conventions must be avoided.

The target is **believable creator-shot footage**, not deliberately poor-quality footage. Imperfection should feel incidental, not manufactured.

## 0. Atlas adaptation (overrides the general sections below)

Read `context/atlas-brand-context.md` first. This standard decides **what** the creator does and why; `../video-direction` decides **how it is written** for the model (slot order, timestamps, the fixed camera vocabulary) and `shot.py` checks both. Use them together:

- **Plan format:** write the plan as a `shot.py` JSON with a `ugc` block (see `../video-direction/templates/ugc-first-impression.json`). `shot.py` then outputs the twelve required sections in this skill's order and warns if motivation, opening, product handling, CTA or continuity is missing, or if more than three imperfections are stacked.
- **Model limits (Veo 3.1 Lite, our default):** 6 seconds with audio per generation (the connector's US$0.50 cap). So the "short test" in section 7 is one 6 s clip, and a longer video is several 6 s clips with the same creator block, cut together in the edit. Each clip still gets one dominant beat.
- **Selfie caution:** front-camera selfie footage is the most believable UGC look, but a handheld selfie plus any two-handed product action gives a third arm. Rule: selfie only when one hand holds the phone and the other does one simple thing. Anything two-handed (opening a bottle, dropping oil) goes on a propped phone ("phone leaning against the mirror at chest height").
- **Our products are perfume oils, not sprays:** amber or clear dropper bottles, small vials, roll-ons, beakers. Realistic actions: unscrewing a dropper, letting one or two drops fall onto the inner wrist or into a small bottle, rubbing wrists together lightly, smelling the wrist from a short distance, swirling a vial. No spraying unless the product is actually a spray.
- **Packaging fidelity:** text-only prompts cannot reproduce our real bottle or label. Either (a) show unbranded generic dropper bottles in the video and put the real product and price in the end card, or (b) if the video tool accepts a reference image, give it the real product photo from origins.atlasdsf.com and instruct it to keep shape, colour, label and proportions. Never invent a label.
- **Truthfulness:** an AI creator is a fictional illustrative scenario, never "a real customer". No invented reviews, results, longevity, sales counts or notes the product doesn't have. Tick the TikTok and Meta AI-content labels.
- **Atlas audience and motivations that fit:** someone who already buys perfume oils showing a base that saved them time; a beginner's first try at making their own scent; "people keep asking what I'm wearing"; showing a small haul; comparing what they expected an accord to smell like vs what it does. Prices and offers come from the live shop.
- **Language and setting:** Malaysian creators, everyday Malaysian homes (condo bedroom, kitchen, parked car), English with natural Malaysian phrasing where it fits; never mock accents.
- **Edit and end card:** per `../ugc-video/README.md` (captions, grain, 2.2 s end card with the lockup, real price, origins.atlasdsf.com).
- **Output contract:** keep section 9's deliverables, but send Gerrick only the short brief, the three hooks and the cost for one-click approval; the full prompt goes in the run folder.

---

## 1. Required production inputs

Before writing the final generation prompt, establish the following. If information is missing, make conservative assumptions or ask only for details that materially affect the result.

### A. Creator

Define a plausible person for the target audience and product.

Specify:
- Approximate age range, not an unnecessarily exact age.
- Relevant appearance and clothing, described neutrally and consistently.
- Personality and energy: reserved, matter-of-fact, enthusiastic, curious, dry-humoured, etc.
- Relationship to the product: recent buyer, existing user, gift recipient, hobbyist, friend making a recommendation, or demonstrator.
- Level of camera confidence.

Avoid:
- Casting every creator as a flawless influencer.
- Overly polished makeup, wardrobe, hair, or presentation unless the concept requires it.
- Generic labels such as "beautiful woman" without useful production detail.
- Treating demographic appearance as a substitute for a credible point of view.

### B. Reason for filming

Give the creator a believable reason to record this video now.

Good motivations:
- Showing something they recently bought.
- Sharing a discovery with a friend.
- Explaining why they replaced an older product.
- Demonstrating how they use something.
- Answering a question they keep receiving.
- Showing an unexpected detail or result.
- Sharing a small problem and what they tried.
- Recording a quick recommendation before going out.

Weak motivations:
- "Promoting the product."
- "Making an advertisement."
- "Reading a testimonial."
- "Explaining why everyone needs this."

The reason should shape the delivery, actions, and structure. Do not merely state the motivation and then produce a conventional scripted commercial.

### C. Setting

Choose a plausible, lived-in environment that supports the filming motivation.

Specify:
- Room or location.
- Relevant background objects.
- Time-of-day feel where useful.
- Natural or practical light source.
- Background activity or ambient conditions, if relevant.
- Whether the environment is tidy, lived-in, or slightly cluttered.

Prefer believable everyday locations: bedroom, bathroom, kitchen, desk, living room, car while parked, or a simple shop/workspace.

Avoid making every location look like a designed set. Do not add decorative detail that does not contribute to believability.

### D. Camera and recording behaviour

Always define the camera. This is a core requirement, not optional decoration.

Specify:
- Device style: ordinary modern smartphone footage.
- Position: front-facing selfie, rear camera, phone propped on a shelf, handheld close-up, etc.
- Distance and framing: arm's length, chest-up, head-and-shoulders, product close-up.
- Angle: eye-level, slightly above, slightly low, or naturally off-centre.
- Stability: handheld micro-movements, a phone resting on a surface, or a small adjustment.
- Focus behaviour: mostly stable, with a brief focus adjustment when the product moves close.
- Exposure and lighting: natural window light, ordinary room lighting, or mixed practical light.
- Orientation and aspect ratio when the destination requires it.

Use restrained imperfections:
- Slightly imperfect framing.
- A small hand movement.
- A brief glance at the screen.
- A natural pause before speaking.
- A minor correction to the phone position.
- A moment where the creator looks away to handle the product.

Do not stack every imperfection into one clip. Choose two or three that fit the situation.

### E. Product handling

Product handling must be physically specific.

Describe:
- Which hand holds the product.
- Where the product begins in the frame.
- When it is picked up, opened, turned, applied, sprayed, smelled, or put down.
- Whether the creator looks at the product, camera, or screen.
- How close it comes to the lens.
- What the packaging looks like, based on supplied product references.
- How the creator's hands interact with caps, lids, pumps, labels, or other components.

Avoid:
- A product floating in the creator's hand.
- Unmotivated, repetitive product posing.
- Perfectly timed movements that feel choreographed.
- Invented packaging, logos, labels, or product details.
- Product interactions that are physically implausible.

If exact packaging accuracy matters, use a reference image and explicitly instruct the generation system to preserve its shape, colour, label, typography, and proportions. Do not rely on a text description alone to reproduce a branded pack accurately.

### F. Message and conversion objective

Define one primary audience, one main problem or desire, and one intended action.

Specify:
- Target viewer.
- Viewer problem, desire, objection, or curiosity.
- One central product benefit.
- Evidence or demonstration that supports the benefit.
- Call to action (CTA).
- Destination or next step, if known.

Do not cram multiple unrelated selling points into a short video. One video should have one dominant message.

---

## 2. First-seconds and hook standard

The opening must earn attention before the viewer has a reason to scroll.

Design the first one to three seconds deliberately. Do not begin with a generic greeting, a slow introduction, or a product held motionlessly at the centre of the frame.

Useful opening patterns:
- **Immediate opinion:** "I didn't think I'd like this, but..."
- **Specific discovery:** "I finally found one that..."
- **Problem recognition:** "If yours keeps doing this, try..."
- **Unexpected detail:** "I bought this for one reason, but..."
- **Demonstration first:** Show the action or result before explaining it.
- **Confession or contrast:** "I used to think this was a waste of money."
- **Question from experience:** "People keep asking me what this is."

These are structural patterns, not lines to reuse mechanically. Write hooks that are truthful, product-relevant, and natural for the creator.

### Opening sequence requirements

For every concept, define:
1. What the viewer sees in the first frame.
2. What the creator does immediately.
3. The first spoken line or on-screen text.
4. The information gap, tension, or curiosity that makes the viewer continue.

The first frame and first line should reinforce each other. Do not make the opening visually busy without a clear message.

### Hook testing

Generate at least three materially different hook options when the task is performance-oriented. Keep the body of the video constant during the first test so the hook can be evaluated independently.

Test different angles, not merely synonyms:
- Problem-led.
- Discovery-led.
- Opinion-led.
- Demonstration-led.
- Objection-led.

Do not assume that more visual realism automatically improves conversion. Once the footage is sufficiently believable, test the message, hook, pacing, and offer.

---

## 3. Natural speech and creator performance

The creator should sound like a person explaining something, not an actor reciting ad copy.

Use:
- Short, conversational sentences.
- Contractions and ordinary vocabulary.
- Specific observations rather than empty superlatives.
- Small pauses where a person would think or handle the product.
- Occasional self-correction only where it sounds natural.
- A delivery speed appropriate to the creator's personality.

Avoid:
- Perfectly structured marketing paragraphs.
- Repeated brand and product names.
- Excessive excitement.
- Every sentence ending with a sales claim.
- Artificial filler words inserted just to simulate authenticity.
- Overacting, exaggerated surprise, and constant smiling.
- Claims that the creator could not reasonably know.

A script should sound speakable aloud. Read it as if sending a voice note to a friend. Rewrite any sentence that feels like website copy.

### Script structure

A useful short-form structure is:

1. **Hook:** Stop the scroll with a specific observation, problem, opinion, or action.
2. **Context:** Why the creator is talking about this.
3. **Demonstration or proof:** Show the product being used or explain a concrete detail.
4. **Payoff:** Explain what changed, what was discovered, or why it matters.
5. **CTA:** Give one clear next step.

Not every video needs all five parts in a rigid order. A demonstration-led video may show the product before the context. Preserve natural flow.

---

## 4. Visual realism: required avoid list

Every final video-generation prompt must include a tailored negative direction. Use the following as a baseline and remove anything irrelevant to the chosen format.

Avoid:
- Glossy commercial or studio-ad aesthetics.
- Cinematic lighting, dramatic rim lights, or elaborate colour grading.
- Perfectly symmetrical, static influencer framing.
- Unnaturally smooth camera movement.
- Excessive shallow depth of field or artificial background blur.
- Overly clean, staged, showroom-like environments.
- Perfectly timed gestures and rehearsed reactions.
- Constant direct eye contact.
- A continuous exaggerated smile.
- Robotic facial expressions or unnaturally precise lip movement.
- Unmotivated slow motion, dramatic transitions, or montage editing.
- Floating, morphing, duplicated, or distorted products.
- Changing packaging, labels, logos, text, or product proportions.
- Unrequested captions, graphics, watermarks, or UI elements.
- Music-video or television-commercial production conventions.

Important: Do not use "low quality" as a substitute for realism. The footage should remain clear, watchable, and product-legible.

---

## 5. Product-category adaptation

Keep the same production principles while adapting handling and proof to the product.

### Fragrance and perfume

For fragrance videos:
- Show believable actions: picking up the bottle, handling the cap, spraying onto a wrist or clothing where appropriate, and smelling from a sensible distance.
- Do not imply that a viewer can smell the fragrance through the screen.
- Use reactions that communicate a personal impression without pretending the video transmits scent.
- Translate scent descriptions into accessible associations and situations.
- Avoid unsupported claims about longevity, projection, ingredients, concentration, safety, or performance.
- Do not invent notes, accords, formulation details, or comparisons.
- Keep the bottle and label consistent with the supplied product reference.
- Avoid spraying directly into the face or eyes.
- A creator can describe what they personally perceive, but do not fabricate a real customer's testimonial or imply a synthetic creator is an actual verified purchaser.

Possible creative angles:
- "What I wear when..."
- "I wanted something that smells like..."
- "I didn't expect this combination to work."
- "The difference between what I thought this would smell like and what it actually smells like."
- "A quick first impression."

### Other product categories

For skincare, food, household, fashion, electronics, and other products, adapt the demonstration to safe, plausible real-world use. Do not invent performance evidence or encourage unsafe use.

---

## 6. Prompt construction standard

The final prompt must be usable by a video-generation system without requiring it to infer the important production decisions.

Write in concrete, observable language. Prefer "the phone is propped at eye level on a shelf, framing the creator from mid-chest upward" over "casual authentic selfie vibe."

### Required prompt sections

Every final generation prompt must contain:

1. **Format and intent**: platform, orientation, approximate duration, and purpose.
2. **Creator**: appearance, personality, relationship to the product, and delivery style.
3. **Filming motivation**: why the creator is recording this.
4. **Setting**: location, background, and light.
5. **Camera direction**: device perspective, position, distance, framing, movement, and focus.
6. **Opening action**: first frame, first movement, and first spoken line.
7. **Product interaction**: exact handling sequence and packaging constraints.
8. **Dialogue**: natural spoken script, if dialogue is required.
9. **Performance direction**: expressions, pauses, eye contact, and delivery.
10. **Ending and CTA**: natural close and one next step.
11. **Avoid list**: unwanted commercial conventions and generation errors.
12. **Continuity constraints**: details that must remain consistent across frames and shots.

If a system has separate fields for visual prompt, dialogue, negative prompt, reference images, or shot instructions, distribute the content accordingly. Do not omit required information merely because the tool has a different interface.

### Reusable prompt template

```text
FORMAT
[Platform, aspect ratio, approximate duration, one-take or edit style.]

CREATOR
[A plausible creator description, personality, clothing, camera confidence,
and relationship to the product.]

WHY THEY ARE FILMING
[A believable reason to record this now. The video is a personal share,
demonstration, discovery, or recommendation, not a scripted commercial.]

SETTING
[Specific everyday location, background details, and practical light source.]

CAMERA
[Smartphone perspective, front/rear camera, placement, distance, angle,
framing, handheld or propped behaviour, small movements, focus behaviour.]

OPENING: FIRST 1–3 SECONDS
[Exact first frame, immediate action, first spoken line or text,
and the curiosity/problem/opinion being introduced.]

PRODUCT HANDLING
[Hand, grip, starting position, sequence of actions, interaction with
packaging, and any reference-image fidelity requirements.]

DIALOGUE
[Speakable, conversational lines. Include natural pauses only where useful.]

PERFORMANCE
[Delivery speed, expressions, eye contact, gestures, and natural imperfections.]

ENDING / CTA
[One natural closing thought and one clear next action.]

AVOID
[No glossy ad look, studio lighting, perfect framing, choreographed gestures,
robotic delivery, exaggerated reactions, product distortion, invented claims,
or unrequested graphics.]

CONTINUITY
[Creator appearance, wardrobe, room layout, product design, hand use,
and other details that must not change.]
```

### Prompt writing rules

- Do not leave important camera behaviour to interpretation.
- Do not overload a short clip with too many actions.
- Do not specify contradictory camera instructions.
- Do not describe a "one-take" video and then request multiple cinematic angles.
- Do not ask for a natural performance while writing dialogue that sounds like a commercial.
- Do not invent visual details that conflict with product references.
- Use time-coded beats only when they improve action sequencing.
- Keep the final prompt concise enough for the target video model to follow. Completeness is more important than verbosity.

---

## 7. Generation and iteration protocol

Use a controlled, credit-conscious workflow.

### Stage 1: Concept

Write:
- Audience.
- Objective.
- Creator motivation.
- Hook.
- Core message.
- Demonstration.
- CTA.

Do not generate video until the concept is coherent.

### Stage 2: Short test

Generate a short proof-of-concept first, usually around 5–8 seconds where the tool permits. Test:
- Creator believability.
- Face and hand stability.
- Product fidelity.
- Camera realism.
- Opening action.
- Speech quality, if dialogue is included.

Do not spend credits on a full 30-second version before the core visual behaviour works.

### Stage 3: Diagnose

Identify the single most consequential failure. Examples:
- Looks like a commercial.
- Product changes shape.
- Hand interaction is implausible.
- Creator looks directly into the lens unnaturally.
- Framing is too perfect.
- Hook is weak.
- Speech is robotic.
- The opening takes too long.

### Stage 4: Change one variable

Change one major variable per iteration wherever practical:
- Camera placement.
- Creator performance.
- Lighting.
- Product handling.
- Opening action.
- Dialogue.
- Setting.

Keep the other variables stable. This makes it easier to identify what improved or damaged the result.

If multiple failures are inseparable (for example, a product interaction requires a different camera angle), document the coupled changes.

### Stage 5: Expand

Only after the short test passes should the concept be extended to the intended duration. Preserve the same creator, setting, product design, camera logic, and performance style.

### Stage 6: Test conversion

Once visual credibility is acceptable, test:
- Hook variants.
- First-frame variants.
- Message angles.
- CTA variants.
- Different creator motivations where relevant.

Do not keep polishing visual realism while neglecting the message.

---

## 8. Quality-control rubric

Score each dimension from 1 to 5. A score of 1 is a serious failure; 3 is usable but needs work; 5 is strong.

| Dimension | What to evaluate |
|---|---|
| Creator credibility | Does this feel like a plausible person with a reason to film? |
| Camera credibility | Does the camera behave like a phone being used by a person? |
| Setting credibility | Does the environment feel ordinary and coherent? |
| Product interaction | Are grip, handling, scale, and movement plausible? |
| Performance | Does speech and expression feel conversational? |
| Opening strength | Is there a compelling first frame and first line? |
| Message clarity | Is one useful product idea communicated clearly? |
| Conversion logic | Is there a reason to care and a sensible next step? |
| Product fidelity | Does the product remain accurate and consistent? |
| Technical quality | Is the footage clear, stable enough, and usable? |

### Acceptance thresholds

- **Reject:** Any critical product distortion, materially false claim, unsafe demonstration, or unusable face/hand/product generation.
- **Revise:** Any score below 3 in creator credibility, camera credibility, product interaction, opening strength, or product fidelity.
- **Test:** Overall average of at least 3.5, with no critical failure.
- **Production candidate:** Overall average of at least 4, with product fidelity and message clarity both at least 4.

These thresholds are internal review standards, not a guarantee of ad performance.

### Final review questions

Before delivering a prompt or approving a video, ask:

1. Can I explain why this person is filming?
2. Does the prompt specify exactly how the phone is positioned and behaving?
3. Is the first one to three seconds intentionally designed?
4. Is the product handled in a physically plausible way?
5. Does the dialogue sound like something a person would actually say?
6. Does the footage avoid obvious commercial conventions?
7. Are product details and claims supported by supplied information?
8. Is there one clear message and one CTA?
9. Has a short test been used before a costly full generation?
10. Is the next iteration based on an identifiable problem?

If any of questions 1–8 cannot be answered, the prompt is not ready.

---

## 9. Output contract

When asked to create an AI UGC concept or prompt, return the following unless the user requests a different format:

### A. Creative brief
- Audience:
- Objective:
- Creator:
- Filming motivation:
- Setting:
- Core message:
- CTA:

### B. Hook options
Provide three distinct options when performance testing is relevant. Explain the angle of each in a short phrase.

### C. Recommended script
Provide natural, speakable dialogue. Do not make it sound like polished brand copy.

### D. Generation prompt
Provide one complete prompt using the required prompt sections. It must be copy-ready.

### E. Negative prompt / avoid list
Provide a separate negative prompt if the target tool supports one. Otherwise include it in the main prompt.

### F. Test plan
State:
- What to generate first.
- What success looks like.
- The one variable to change if it fails.
- What should remain constant.

### G. QC result
Evaluate the prompt against the quality-control rubric. Identify unresolved assumptions rather than pretending they are settled.

Do not output a long explanation of the methodology every time. Apply the methodology internally and return the production-ready deliverables.

---

## 10. Truthfulness, rights, and platform considerations

- Do not invent customer experiences, verified reviews, measurable results, endorsements, credentials, or product performance.
- Do not present a synthetic creator as a real customer or identifiable real person.
- Use likenesses, voices, logos, and reference material only when the user has the rights or permission to use them.
- Follow applicable advertising, consumer-protection, and platform rules, including disclosure requirements for synthetic or materially altered content where applicable.
- Do not create unsupported health, safety, efficacy, or comparative claims.
- Keep testimonials clearly distinguished from fictional illustrative scenarios.
- Do not imply that a viewer can directly experience a sensory property through the screen (for example, smell or taste).

---

## 11. Common failure patterns and corrections

| Failure | Likely cause | Correction |
|---|---|---|
| Looks like a glossy ad | Prompt describes the topic but not the filming method | Specify phone position, practical light, framing, motivation, and incidental movement |
| Looks like an influencer campaign | Creator is too polished and delivery too rehearsed | Give a believable reason to film and use simpler, more personal language |
| Product looks fake | Handling and packaging are underspecified | Define the grip and action sequence; use product reference images |
| Opening feels slow | No designed first frame or immediate action | Start with an opinion, problem, discovery, or demonstration |
| Speech sounds robotic | Dialogue is too formal or too dense | Shorten sentences and write for spoken delivery |
| Video feels artificially messy | Too many imperfections were explicitly staged | Keep only two or three incidental imperfections |
| Good-looking video does not sell | Hook, message, offer, or CTA is weak | Test creative angles and opening lines independently |
| Long generation wastes credits | Full duration generated before visual validation | Run a short proof-of-concept first |
| Iterations do not teach anything | Too many prompt variables changed together | Change one major variable per test |
| Product changes between shots | No continuity or reference constraints | Reinforce product identity and avoid unnecessary cuts |

---

## 12. Operating rules for the AI system

When this skill is active:

1. Treat this document as the default production standard for AI UGC tasks.
2. Do not return a generic scene description as a finished video prompt.
3. Do not omit creator motivation, camera behaviour, opening sequence, product handling, or avoid directions.
4. Separate creative strategy from the generation prompt so the user can inspect both.
5. Prefer a small number of concrete, observable instructions over piles of vague adjectives such as "authentic", "viral", "relatable", or "cinematic".
6. Distinguish what is known from what is assumed. Never invent product facts.
7. Prioritise product fidelity and truthful communication over visual novelty.
8. Use short tests and controlled iterations before recommending full-length generation.
9. Evaluate realism and conversion as separate dimensions.
10. If the requested video tool has known limitations, adapt the prompt to those limitations instead of pretending the tool can guarantee perfect output.

**Definition of done:** The output gives a video-generation system enough information to reproduce a believable creator-shot recording, gives the creator a credible reason to speak, gives the viewer a compelling opening and clear message, and gives the production team a repeatable way to evaluate and improve the result.
