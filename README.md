# Atlas content skills

One repository for every skill that makes Atlas DSF and Atlas Origins content: research, copy, statics, carousels, ads, video, UGC, iteration and shipping. Modelled on coreyhaines31/marketingskills: plain Markdown skill files, sequenced in the order work actually happens, each pointing to the next.

Claude pulls this repo at the start of any content task (via the `atlas-content` router skill), so an update pushed here reaches every chat.

## Start here

1. Read `context/atlas-brand-context.md` (the rules every skill assumes).
2. Asked "what's our next move?" or anything about what to do next: open `skills/00-director/growth-director` first. It decides what to build and hands the work to the skills below.
3. For a specific job, find it in the table below and open that skill.
4. Follow it to the end; it hands off to the next skill.

## The sequence

| Step | Skill | Use it for |
|---|---|---|
| **00 Director** | `skills/00-director/growth-director` | Decides what to build next and why; keeps the 7/30/90-day plan and state files; routes work to every skill below |
| **01 Research** | `skills/01-research/atlas-growth-loop` | Weekly loop: hunt cross-industry winners, shortlist, produce, measure, promote to ads |
| | `skills/01-research/stash` | Save a reel, video, link or idea; turn it into a brief |
| **02 Copy** | `skills/02-copy/atlas-script-lab` | Hook, angle, body and CTA for any piece (load before writing anything) |
| | `skills/02-copy/atlas-content-engine` | Batches of educational posts from the atom x format x hook library in Odoo |
| | `skills/02-copy/tiktok-caption-and-sound` | TikTok captions, hooks and sounds |
| **03 Static** | `skills/03-static/ad-library` | Origins static ads by family (search, problems, meme, presenter), with variant fan-out |
| | `skills/03-static/atlas-origins-post-designs` | Origins B2C carousels (Fact Sheet, Recipe Card, Compare; intro series) |
| | `skills/03-static/atlas-social-posts` | Atlas DSF posts and carousels (white-first, green gradients) |
| | `skills/03-static/icon-library` | Free 3D icons (Fluent Emoji 3D, MIT) for every icon or small object; no hand-drawn icons |
| | `skills/03-static/atlas-glass-grid` | 9-post DSF Instagram grid, frosted-glass style |
| **04 Video** | `skills/04-video/video-direction` | Shot, camera and lens rules plus `shot.py`: load before ANY AI video generation |
| | `skills/04-video/ai-ugc-production` | Standard for AI UGC: creator, reason to film, phone behaviour, first 3 seconds, product handling, script, QC rubric |
| | `skills/04-video/explainer-reel` | Polished vertical explainer reel (US$1 cap per reel) |
| | `skills/04-video/ugc-video` | AI UGC skit log, edit spec and disclosure rules |
| **05 Ship and ads** | `skills/05-ship-and-ads/ship-content` | Publish or schedule to Meta after approval |
| | `skills/05-ship-and-ads/atlas-ads-manager` | Paid Meta and TikTok: offers, campaigns, spend, KPIs |
| | `skills/05-ship-and-ads/shopee-ads-advisor` | MoleculeLabs Shopee ads and sales reports |
| **06 Iterate** | `skills/06-iterate/atlas-remix` | One reference or winner in, a batch of on-brand variants (hooks, colours, formats) out |

## Common jobs

| "I want to..." | Path |
|---|---|
| What's our next move? / morning run / weekly plan | growth-director |
| Copy the structure of an ad I saw | atlas-remix, which runs atlas-script-lab, then ad-library or a carousel skill, then video-direction for video |
| Make more of a winning ad | atlas-remix (variant plan: hooks first, then format, then colour) |
| Make this week's posts | atlas-content-engine or atlas-growth-loop, then the static or video skill, then ship-content |
| Make an AI UGC video | ai-ugc-production (brief, 3 hooks, script) + video-direction (`shot.py`, `ugc-first-impression` template), then the edit spec in ugc-video |
| Launch a test ad set | atlas-remix or ad-library, then atlas-ads-manager |

## Rules for changing this repo

- One skill per folder, `SKILL.md` first, supporting files beside it.
- Brand rules live only in `context/atlas-brand-context.md`; skills point to it rather than repeating it.
- When a run teaches something (a prompt failure, a design rule Gerrick sets), write it into the skill it belongs to and commit with a short dated message.
- Never commit API keys, customer data or supplier names.
