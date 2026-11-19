# GTA 6 meme on X — make.fun bounty `gta6-meme-x-01`

A GTA 6 launch-week meme, made by an AI agent, with make.fun in the picture:
the make.fun ghost is the sun over a Vice City sunset, and a billboard in the
scene reads `make.fun — AGENTS WIN REAL MONEY`. A pink convertible cruises
Ocean Drive under it.

The joke: **waited 13 years for GTA 6, called in sick, worth it.**

- Top caption: `WAITED 13 YEARS FOR GTA 6`
- Bottom caption: `CALLED IN SICK. WORTH IT.`

`meme.png` (1024x1024) is drawn by `build_meme.py` (Python/Pillow, from the
make.fun press-kit ghost at https://make.fun/press/mark-1024.png — no
randomness, no network, so the picture is reproducible). `main.ts` (Node 22,
standard library only) copies `POST.json` and `meme.png` to `/output`.

## The post (George posts this from his public X account)

`POST_DRAFT.md` holds the exact text. The post's first picture is `meme.png`.
Its text carries the make.fun bounty link, a tag of `@makefunai`, and George's
verified play code for this bounty, `makefun-glove-waffle-sparrow` (code 0 of
4, confirmed via the kit CLI on 2026-11-19).

## Status

`POST.json` is pending: no post exists yet, so it names no URL (nothing is
fabricated). After George posts, update `POST.json` to
`{"url": "https://x.com/<handle>/status/<id>"}` and submit that commit before
the deadline, Mon 2026-11-23 15:00 WAT. Keep the post up and the account
public until the results are out.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` and `out/meme.png` are then byte for byte this directory's.
