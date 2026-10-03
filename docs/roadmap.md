# Roadmap

| Phase | Goal | Deliverable | Status |
|---|---|---|---|
| 1 | Project setup | Repo, folder structure | done |
| 2 | Villager textures: plains and farmer | `resourcepack/` PNGs, generator script | done |
| 3 | Remaining professions | shepherd, priest, blacksmith, librarian, etc. | todo |
| 4 | First Revival house | `structures/house_small.nbt` | todo |
| 5 | House variants, well, church, fence | 5+ structures | todo |
| 6 | Village data pack | `datapack/` generates a village | todo |
| 7 | Remove vanilla villages | Only Bulgarian villages spawn | todo |
| 8 | Fabric mod | `mod/` builds a working jar | todo |
| 9 | Biome types and villager variants | All biomes covered | todo |
| 10 | Polish and release | Version 1.0.0 on Modrinth, license chosen | todo |

## Open TODOs

- [ ] Find the right `pack_format` for 26.3 and add `pack.mcmeta` (copy from vanilla jar)
- [ ] Confirm the villager UV layout against vanilla textures from the 26.3 jar
- [ ] Confirm required Java version (generate the Fabric template at fabricmc.net/develop)
- [ ] Verify worldgen JSON formats for 26.3 before writing the village files
- [ ] Choose a license

## Known facts (checked)

- Minecraft 26.3 released 15 September 2026
- Fabric: Loader 0.19.5, Loom 1.17, Gradle 9.6.0 (per the Fabric 26.3 announcement)
- Fabric removed several APIs for 26.3, so old 1.20/1.21 tutorials may not compile
