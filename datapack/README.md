# datapack

Village generation for Minecraft Java 26.3 (data pack format 121.0).

## What is in here

| File | Purpose |
|---|---|
| `pack.mcmeta` | Pack metadata, format 121 |
| `data/vazrazhdane/worldgen/structure/village.json` | The village (a jigsaw structure) |
| `data/vazrazhdane/worldgen/structure_set/villages.json` | Where and how often villages generate |
| `data/vazrazhdane/tags/worldgen/biome/has_structure/village.json` | Biomes allowed to have our villages |
| `data/vazrazhdane/worldgen/template_pool/village/*.json` | Piece pools: town centers, streets, terminators, houses |
| `data/minecraft/worldgen/structure_set/villages.json` | Overrides vanilla, so vanilla villages stop generating |
| `data/minecraft/tags/worldgen/structure/village.json` | Lets `/locate structure #minecraft:village` find ours |

Structure `.nbt` files are NOT stored here. They live in `../structures/` and
`tools/build.py` copies them into the pack.

## Current state: one-house test

`town_centers.json` only lists `house_small`. As soon as `structures/house_small.nbt`
exists, a "village" of one house generates. That is the quickest way to test.
`streets.json`, `terminators.json` and `houses.json` are ready but unused until the
street and house pieces exist and have jigsaw blocks (see `docs/village-jigsaw.md`).

## Build and test

    python3 tools/build.py

1. Copy `dist/vazrazhdane-datapack.zip` into a new world's `datapacks` folder
   (or drag it onto the Create World screen).
2. Run `/locate structure vazrazhdane:village`, or in a creative world
   `/place structure vazrazhdane:village`.
3. Check the game log for lines about missing templates or pools.

## Open items

- Confirm the vanilla file is really named `villages.json` in the 26.3 jar
  (`data/minecraft/worldgen/structure_set/`). If vanilla villages still appear, check this.
- `pack.mcmeta` has both `pack_format` and `min_format`/`max_format`. A report says 26.3
  logged "Missing metadata in pack" without `pack_format`, while the wiki says it is
  optional. Having both is the safe choice.
- The vanilla `#minecraft:has_structure/village_*` biome tags may have changed in 26.3
  (26.3 added biome tags), so this pack uses its own biome tag instead.
