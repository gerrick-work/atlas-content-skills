---
name: atlas-content
description: Single entry point for all Atlas DSF and Atlas Origins content work (posts, carousels, static ads, reels, UGC, remixes of a reference or winner, captions, shipping, ads). Pulls the atlas-content-skills GitHub repo and follows the right skill in it.
---

# Atlas content (router)

All Atlas content skills live in one GitHub repo: **gerrick-work/atlas-content-skills** (private). This skill only fetches it and points to the right file; the instructions themselves are in the repo, so an update pushed there reaches every chat.

## 1. Pull the repo (every run)

1. If the session doesn't have the repo yet, add it with the `add_repo` tool (owner and repo from gerrick-work/atlas-content-skills, read access), then clone it:
   `git clone https://github.com/gerrick-work/atlas-content-skills.git /home/claude/atlas-content-skills`
   If it is already there: `git -C /home/claude/atlas-content-skills pull`.
2. If GitHub can't be reached, say so in one line and use the newest copy in the "ads week 1 NOV" Project (`atlas-content-skills/` docs) instead.

## 2. Route

1. Read `context/atlas-brand-context.md`. For any creative (post, carousel, reel, ad, LinkedIn image) also read `context/creative-tastebook.md` and build from one of its patterns.
2. If the request is "what's our next move", the morning run, weekly planning or any "what should we do" question, open `skills/00-director/growth-director/SKILL.md` and follow it.
3. Otherwise read `README.md`, find the job in "The sequence" or "Common jobs", and open that skill's `SKILL.md` with Read.
4. Follow it exactly, including the skills it hands off to (open each from the repo the same way).

## 3. Write back what was learned

When a run produces a new rule, template, shot plan or fix, edit the skill it belongs to in the repo and push with a short dated message (`git commit -m "4 Nov 2026: ..."`), after telling Gerrick in one line what changed. Never commit keys, customer data or supplier names.
