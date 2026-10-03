# Villager texture layout (64 x 64)

Classic layout, from memory of the vanilla villager. VERIFY against the 26.3
vanilla textures before trusting it.

Box format: origin (u,v), size (w x h x d). Front face starts at (u+d, v+d).

| Part | Origin | Size | Front face | Bulgarian costume |
|---|---|---|---|---|
| Head | 0,0 | 8x10x8 | 8,8 | skin, brows, mustache |
| Hat layer | 32,0 | 8x10x8 | 40,8 | kalpak or headscarf |
| Nose | 24,0 | 2x4x2 | 26,6 | darker skin |
| Body | 16,20 | 8x12x6 | 22,26 | white shirt |
| Jacket layer | 0,38 | 8x20x6 | 6,44 | sukman, apron, red sash |
| Arm | 44,22 | 4x8x4 | 48,26 | white sleeve, gold cuff |
| Crossed arms | 40,38 | 8x4x4 | 44,42 | sleeve trim, hands |
| Leg | 0,22 | 4x12x4 | 4,26 | potur, white socks |
| Hat brim | 30,47 | 16x16x1 | 31,48 | straw brim (unused so far) |

Layers: `type/<biome>.png` (face, base body) then `profession/<job>.png`
(clothing overlay) then `profession_level/` (badge, untouched).

## Palette

| Name | Hex | Use |
|---|---|---|
| Red | `#B3202A` | apron, sash, scarf |
| Black | `#1C1C22` | sukman, kalpak |
| White | `#F4EFE2` | shirt, socks |
| Gold | `#E0A526` | trim, embroidery |
| Green | `#2D6B3A` | accents, eyes |
| Navy | `#22304A` | potur |
| Dark red | `#7A1F1F` | vest, cap band |

Embroidery motifs: rows of diamonds, zigzags, small cross-stitch dots.
