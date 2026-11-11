# Icon library: 3D icons for every Atlas creative

Set 11 Nov 2026. Gerrick: no Claude-drawn icons. Every icon, pictogram or small object in a post, carousel, ad or reel comes from this library.

## The library

**Microsoft Fluent Emoji 3D**, github.com/microsoft/fluentui-emoji, MIT licence (free for commercial use, attribution not required in the creative). About 1,600 glossy 3D objects as transparent 256px PNGs: noses, trees, test tubes, alembics, microbes, droplets, flowers, wood, coffee, clocks, money, shops, parcels, gifts, charts.

Why this one: it is the largest fully free 3D set, it lives on GitHub (the workspace can always reach it), the style is consistent across every object, and Microsoft maintains it.

Backup for business and UI concepts it lacks: **3dicons** (3dicons.co, CC0, about 120 icons in clay, colour and gradient styles, 2400px). Download single icons from the site; there is no API.

## How to use it

```
python3 fetch_icon.py search tree          # list names
python3 fetch_icon.py get "Deciduous tree" "Nose"   # PNGs into /home/claude/assets/icons3d/
```

Names and paths are in `fluent3d_index.txt`. Skin-tone icons resolve to the Default tone.

## Rules

- Use icons at 180px or smaller on a 1080px slide (the source is 256px); never upscale past 256px.
- Skip orange-dominant icons (orange is out of the brand): e.g. megaphone, sun. Pick another object or another library icon.
- No emoji faces or people. Objects only.
- Place them like cut-outs: a soft shadow is fine, no box or circle behind them unless the layout needs a shape with character.
- Still 1 to 2 diagrams per carousel: arrows and lines stay drawn in SVG; the objects in them are library icons.
