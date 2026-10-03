# Roadmap

| Phase | Goal | Deliverable | Status |
|---|---|---|---|
| 1 | Project setup | Repo, folder structure | done |
| 2 | Villager textures: plains and farmer | `resourcepack/` PNGs, generator script | done |
| 3 | Remaining professions | all 15 profession textures (cleric = priest, three smith types) | done |
| 4 | First Revival house | `docs/house-small.md` guide, then `structures/house_small.nbt` | in progress |
| 5 | House variants, well, church, fence | 5+ structures | todo |
| 6 | Village data pack | `datapack/` generates a village | in progress |
| 7 | Remove vanilla villages | Only Bulgarian villages spawn | override written, untested |
| 8 | Fabric mod | `mod/` builds a working jar | todo |
| 9 | Biome types and villager variants | All biomes covered | todo |
| 10 | Polish and release | Version 1.0.0 on Modrinth, license chosen | todo |

## Open TODOs

- [x] Data pack format for 26.3 is 121.0 (done, `datapack/pack.mcmeta`)
- [ ] Resource pack format for 26.3: find it with `/version` or F3+V in game, then add `resourcepack/pack.mcmeta`
- [ ] Confirm the villager UV layout against vanilla textures from the 26.3 jar
- [ ] Confirm required Java version (generate the Fabric template at fabricmc.net/develop)
- [x] Worldgen JSON formats checked against the wiki (structure, structure set, template pool)
- [ ] Test in game: `/locate structure vazrazhdane:village`
- [ ] Choose a license

## Known facts (checked)

- Minecraft 26.3 released 15 September 2026
- Fabric: Loader 0.19.5, Loom 1.17, Gradle 9.6.0 (per the Fabric 26.3 announcement)
- Fabric removed several APIs for 26.3, so old 1.20/1.21 tutorials may not compile
