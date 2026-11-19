// gta6-meme-x-01 entry (Node 22, standard library only, no network).
//
// The entry is the X post named in POST.json: a GTA 6 meme whose picture shows
// make.fun's ghost mascot (drawn as the sun over Vice City, plus a make.fun
// billboard), posted from a public X account with make.fun and the entrant's
// play code in its text. The house reads the post from X itself; nothing this
// program writes about the post is judged.
//
// What this program does, every run, byte for byte:
//   1. copies POST.json from the repository root to /output/POST.json,
//      which is the file the gate reads;
//   2. copies meme.png (the meme picture, drawn by build_meme.py from the
//      make.fun press-kit ghost) to /output/meme.png, so the run's output
//      carries the exact picture the post shows.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

for (const name of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, name), join(OUTPUT_DIR, name));
  } catch (err) {
    console.error(`${name} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}
