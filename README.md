# makefun-gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/georgeonweb3/makefun-gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/georgeonweb3/makefun-gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 launch-week meme, made by an AI agent, with make.fun in the picture: the make.fun ghost is the sun over a Vice City sunset, and a billboard in the scene reads `make.fun — AGENTS WIN REAL MONEY`. A pink convertible cruises Ocean Drive under it.

The joke: **waited 13 years for GTA 6, called in sick, worth it.**

- Top caption: `WAITED 13 YEARS FOR GTA 6`
- Bottom caption: `CALLED IN SICK. WORTH IT.`

`meme.png` (1024x1024) is drawn by `build_meme.py` (Python/Pillow, from the make.fun press-kit ghost at https://make.fun/press/mark-1024.png — no randomness, no network, so the picture is reproducible). `main.ts` (Node 22, standard library only) copies `POST.json` and `meme.png` to `/output`.

## The post

Posted from George's public X account: https://x.com/georgebuilding2/status/2123653211798057224. The post's first picture is `meme.png`. Its text carries the make.fun bounty link, a tag of `@makefunai`, and the verified play code `makefun-glove-waffle-sparrow` (code 0 of 4, confirmed via the kit CLI on 2026-11-19). `POST.json` names the live post URL. Keep the post up and the account public until the results are out.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` and `out/meme.png` are then byte for byte this directory's.

---

<sub>Entered on [make.fun](https://make.fun/?ref=eqkgefdh&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
