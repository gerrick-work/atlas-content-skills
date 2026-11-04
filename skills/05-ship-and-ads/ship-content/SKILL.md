---
name: ship-content
description: "Ship finished Atlas posts, carousels and reels to the right Facebook page and Instagram account in Meta Business Suite: schedule or publish after approval, verify, then update Odoo. YouTube later. Use for /ship-content, ship it, schedule these, post this to Meta, or when atlas-social-posts or explainer-reel hands off finished files."
---

# Ship content (Meta now, YouTube later)

Use for `/ship-content`, "ship it", "schedule these", "post this to Meta", or when atlas-social-posts or explainer-reel hands off finished files.

This command only publishes. It never edits the creative. Everything happens in Gerrick's Chrome through Claude in Chrome; read the chrome-browser skill first.

## Accounts (one Meta business portfolio, business_id 909381335581383)

| Account | Facebook page | Instagram | asset_id |
|---|---|---|---|
| Atlas DSF (B2B) | Atlas DSF | @atlasdsf.my | 1435715622951213 |
| Atlas Origins (B2C) | Atlas Origins | @atlasorigins.my | 909360398916810 |

Never post DSF content to Origins or the reverse. Always confirm the composer's "Post to" line reads "Atlas DSF and atlasdsf.my" or "Atlas Origins and atlasorigins.my".

## 1. Inputs and preflight

For each item collect:
- files in order
- the caption
- the account
- the type: post (1 image), carousel (2 to 10 images) or reel (1 video)
- the date and time (Asia/Kuala_Lumpur)
- placements (default: Facebook plus Instagram)

Preflight, fixing anything that fails before going further:
- **File location:** files are under `/home/claude/...`. Chrome `file_upload` rejects `/mnt/user-data/outputs`, so copy files into `/home/claude` first.
- **Images:** 4:5 to 1.91:1 (1080 x 1350 is best), at most 10 per post. 3:4 gets auto-cropped by Instagram: re-render at 4:5 rather than accept the crop.
- **Reels:** 1080 x 1920 MP4, upload copy under 10 MB. Each `file_upload` call must total under 10 MB.
- **Caption:** no em dashes, with the hashtags at the end.
- **Chrome:** `tabs_context_mcp` works. The Business Suite clock is the browser's; it should be on Malaysia time (the composer's default schedule time is about now plus 2h). If Chrome can't be reached, stop and ask Gerrick to open Chrome with the Claude extension on his computer.

## 2. Approval gate (required, every time)

1. Show the creative (contact sheet or video) and the exact caption.
2. Ask with AskUserQuestion:
   - approve all, approve with changes, or hold
   - timing: the calendar date at 8:30pm (default), now, or another time
   - placements: Facebook plus Instagram, or Instagram only
3. Approval covers only the items shown. Publishing now, deleting, replacing or boosting each needs its own explicit yes.

## 3. Posts and carousels (post composer)

1. **Open the composer.** New tab at `https://business.facebook.com/latest/composer/?asset_id=<asset_id>&business_id=909381335581383`. Confirm "Post to". If the wrong account shows, use the account switcher (top-left) and pick the right row.
2. **Upload the files.** The Add photo/video button opens a native file picker, which can't be used, so patch it first:
   ```js
   window.__caught=[];if(!window.__patched){window.__patched=1;const oc=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'){this.id='claude-file-input';this.setAttribute('aria-label','claude file input');if(!this.isConnected){this.style.cssText='position:fixed;left:0;top:0;width:10px;height:10px;opacity:0.01;z-index:99999';document.body.appendChild(this);}window.__caught.push(this);return;}return oc.call(this)};}
   const b=[...document.querySelectorAll('[role=button],button')].find(x=>/Add photo\/video/.test(x.textContent));b?(b.click(),'clicked'):'no button'
   ```
   - Then `find` "claude file input" and `file_upload` ALL images in slide order in ONE call.
   - Check that each row says 1080 x 1350 and that no "auto-cropped" warning shows.
   - If a wrong file went in, remove it with its "Remove Photo" button (in the draft only).
3. **Caption.** Click the Text combobox ("Write in the dialogue box..."), `type` the caption, then press Escape to close any hashtag or mention popup.
4. **Schedule.**
   1. Turn on the "Set date and time" switch.
   2. For each of the Facebook and Instagram rows: triple-click the dd/mm/yyyy box, type `DD/MM/YYYY`, press Enter. Click the hours spinbutton and type `20`; click the minutes spinbutton and type `30` (24-hour).
   3. Verify with: `[...document.querySelectorAll('input[placeholder="dd/mm/yyyy"], [role=spinbutton]')].map(e=>e.value||e.getAttribute('aria-valuenow')).join(' | ')`.
   4. Click Schedule.
   - To publish now (needs its own yes), skip the switch and click Publish.
5. **After scheduling.** "Save time by scheduling another post": choose "Maybe later", or "Schedule another post" to stay on the same account. On the Boost pop-up, choose "Maybe later" (see Paid boosts).
6. **Next item.** Go back to step 1 for the next one.

## 4. Reels (reels composer)

1. Open `https://business.facebook.com/latest/reels_composer/?asset_id=<asset_id>&business_id=909381335581383` and confirm "Post to".
2. Patch the input as in step 3.2, click Add video, and `file_upload` the upload copy (under 10 MB).
3. Type the caption into the Text editor. The Title field is locked when posting to both platforms.
4. Click Next, then Next again (keep the original audio).
5. Choose Schedule. Set each time by clicking its hours and minutes spinbuttons and pressing ArrowUp or ArrowDown; typing digits does not stick in this composer. Check both the Facebook and Instagram rows, then click Schedule.

## 5. Verify (always, before reporting)

- **Scheduled posts:** open `https://business.facebook.com/latest/posts/scheduled_posts?business_id=909381335581383&asset_id=<asset_id>` for each account. Every item should have one Facebook row and one Instagram row at the right date and time.
- **Something showing "Failed to publish":** check the Published tab (`/latest/posts/published_posts?...`) before reporting a failure. A leftover duplicate can show as failed while the real post is live.
- Close the tabs you opened.
- Report a table of date and time, account and post. Name anything that did not schedule.

## 6. Odoo (after verifying)

Offer to move the matching tasks in project "Atlas Content Calendar" (id 5) to "Ready to post" (scheduled) or "Posted" (published). This is a write, so it needs a yes. On a yes, in an atlas-dsf.odoo.com tab:

```js
const rpc=async(model,method,args,kwargs={})=>(await (await fetch('/web/dataset/call_kw',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jsonrpc:'2.0',method:'call',params:{model,method,args,kwargs}})})).json());
const st=(await rpc('project.task.type','search_read',[[['project_ids','in',[5]],['name','=','Ready to post']]],{fields:['id']})).result[0].id;
await rpc('project.task','write',[[TASK_IDS],{stage_id:st}]);
```

## 7. Replacing or deleting

- Replacing a scheduled post: schedule the new one first, confirm it in Scheduled, then delete the old one. Get a yes for the delete.
- Never delete published posts unless Gerrick asks for that specific post.

## 8. Paid boosts and ads (only when explicitly asked)

- Organic is the default. Boosting spends money from the payment method on file, so each boost needs an explicit yes naming:
  - the exact amount in RM
  - the duration
  - the audience
  - the post
- Keep within the marketing budget Gerrick has set (RM500 to 2,000 a month), and never enter card or payment details.
- For full campaigns, use Ads Manager only on his instruction, and summarise the setup before he confirms.

## 9. YouTube (not set up yet)

If asked to ship to YouTube, say it isn't configured yet. Offer to set it up:
- confirm the channel and that Gerrick is signed in to YouTube Studio in Chrome
- vertical reels under 3 min go up as Shorts
- then add the tested steps to this file

Do not attempt an upload before that.
