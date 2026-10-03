# Village jigsaw plan

Pieces and jigsaw blocks, using names we control. A connection is valid when the
parent jigsaw's **Target Name** equals the child jigsaw's **Name**.

| Piece (`structures/*.nbt`) | Used in pool | Jigsaw blocks inside |
|---|---|---|
| `house_small`, `house_small_ochre`, `house_large`, `workshop`, `church` | `village/houses` | 1 at the door: Name `vazrazhdane:entrance`, Target `vazrazhdane:entrance`, Pool `minecraft:empty` |
| `street_straight`, `street_corner`, `street_cross` | `village/streets` | At each open end: Name `vazrazhdane:street`, Target `vazrazhdane:street`, Pool `vazrazhdane:village/streets`. At each side where a house can attach: Name `vazrazhdane:entrance`, Target `vazrazhdane:entrance`, Pool `vazrazhdane:village/houses` |
| `street_end` | `village/terminators` | 1 matching jigsaw: Name `vazrazhdane:street`, Target `vazrazhdane:street`, Pool `minecraft:empty` |
| `town_center` (well or square) | `village/town_centers` | One street jigsaw on each side: Name `vazrazhdane:street`, Target `vazrazhdane:street`, Pool `vazrazhdane:village/streets` |

Rules of thumb:
- Jigsaw blocks must sit on the edge of the piece, facing outward.
- Street pieces use `terrain_matching` projection so they follow the ground. Houses use `rigid`.
- Houses attach to streets, never directly to houses.
- Keep the depth (`size` in `structure/village.json`) at 6 or more so streets can branch.

## Testing a piece alone

    /place jigsaw vazrazhdane:village/streets vazrazhdane:street 3

(pool, target name, max depth). Use `/place structure vazrazhdane:village` for a full village.

## Villagers

Villagers come from entities saved in the structure. Place villagers in the house
before saving it, and keep "include entities" ON in the Structure Block. They will
spawn with the type and profession you saved them with. Each house should have 1 or
2 beds and one job site block, or the villagers will wander off.

## Next, in order

1. `house_small.nbt` (one-house test)
2. `street_straight`, `street_end`, `town_center`
3. Switch `town_centers.json` to use `town_center`
4. Remaining houses, church, workshop
