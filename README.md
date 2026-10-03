# Vazrazhdane Villages

A Minecraft Java Edition project that replaces vanilla villages with villages
in the style of the Bulgarian National Revival (1800s): stone ground floors,
overhanging whitewashed upper floors with timber framing, a cardak bay window,
clay-tile roofs, and villagers in authentic folk costume (sukman, prestilka,
potur, red pas, kalpak).

Inspiration: Koprivshtitsa, Tryavna, Bozhentsi, Zheravna.

Target version: Minecraft 26.3 ("Wilderness Bound"), Fabric.

## Repo layout

| Folder | What lives there |
|---|---|
| `resourcepack/` | Villager textures and anything visual |
| `datapack/` | Village generation: structure sets, template pools, jigsaw |
| `structures/` | Source `.nbt` houses saved from Structure Blocks |
| `mod/` | Fabric mod that bundles the packs into one jar |
| `tools/` | Scripts, for example the texture generator |
| `docs/` | Roadmap, texture layout and palette |

## Build the textures

    python3 tools/gen_textures.py

Needs Python 3 and Pillow (`pip install pillow`).

## Status

See `docs/roadmap.md`.

## Legal

Do not commit files extracted from the Minecraft jar. This project is not
affiliated with Mojang or Microsoft. Pick a license before publishing.
