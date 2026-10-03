# Small Revival house: build guide

Design by me, untested in game. Adjust freely. Coordinates are local to the
build: x goes left to right (0 to 10), z goes front to back (0 to 8), y goes up
(0 is the floor level). The front, with the bay window, is the z = 0 side.

Bounding box: 13 wide x 18 tall x 11 deep (with roof and chimney), well inside
the Structure Block limit.

## Palette (Java block names)

| Part | Block |
|---|---|
| Ground floor walls | cobblestone (60%), andesite (25%), stone bricks (15%), mixed randomly |
| Ground floor corners | stone bricks |
| Whitewashed upper walls | calcite (alternative: smooth quartz) |
| Ochre variant | yellow terracotta or smooth sandstone |
| Timber frame | dark oak log (corner posts), dark oak planks (beams) |
| Floors | spruce planks |
| Roof | brick stairs and brick slabs |
| Windows | glass panes, spruce trapdoors as shutters |
| Ground floor windows | iron bars |
| Door | dark oak door |
| Chimney | stone bricks, stone brick wall on top, a campfire for smoke |
| Brackets under overhang | upside-down spruce stairs |

## Layers

**y0: floor.** Fill x1..9, z1..7 with spruce planks (or cobblestone for a
rustic floor).

**y1 to y4: ground floor.** Wall ring at x1..9, z1..7, four blocks tall.
- Corners: stone bricks, all four heights.
- Door: x5, z1, two blocks tall (y1 to y2). A stone brick lintel at y3 above it.
- Windows: single iron-bar blocks at y2 on the front at x3 and x7, one on each
  side wall, one on the back.
- Fireplace: back wall, x8, z6 (inside). Stone bricks with the chimney column above.

**y5: upper floor and overhang.** Spruce planks over the whole x0..10, z0..8.
The ring one block outside the ground walls is the overhang. This is the
signature Revival detail.
- Under the overhang at y4, place upside-down spruce stairs with the tall side
  against the wall: front at x2, x4, x6, x8; back at the same x; each side at
  z2, z4, z6.

**y6 to y9: upper floor.** Wall ring x0..10, z0..8, four blocks tall, calcite.
- Timber frame: dark oak log posts at x0, x5, x10 on the front and back walls,
  and at z0, z4, z8 on the side walls. Dark oak plank beams along y6 and y9.
- Windows: two-by-two glass panes at y7 to y8. Front and back: x2 to x3 and
  x7 to x8. Sides: z2 and z6 (one wide, two tall). Spruce trapdoors on each
  side of every window as shutters.

**Bay window (cardak).** Projects one block out of the front wall at z = -1.
- Floor at y5, x3..7, z-1, with upside-down stair brackets underneath at y4.
- Posts: dark oak log at x3 and x7, y6 to y9.
- Sill: dark oak planks at y6, x4..6. Glass panes at y7 to y8 across x4..6 at
  z-1, and on the two sides at x3 and x7 between the posts.
- Cap: a small brick-stair eave at y10. Open the main wall at z0, x4..6, y7 to
  y8 to connect the room to the bay.

**y10 to y15: hipped roof.** Rings of brick stairs, low side facing outward,
each ring one block smaller on every side:

| Layer | Ring (x range, z range) |
|---|---|
| y10 | x-1..11, z-1..9 (overhangs the walls by one block) |
| y11 | x0..10, z0..8 |
| y12 | x1..9, z1..7 |
| y13 | x2..8, z2..6 |
| y14 | x3..7, z3..5 |
| y15 | x4..6, z4: fill with brick slabs (the ridge) |

Leave the attic hollow. Put a few lanterns or slabs on the y10 floor so mobs
cannot spawn inside.

**Chimney.** Stone bricks in the column x8, z6, from y1 up to y15. Top it with
a stone brick wall at y16 and a lit campfire at y17 for the smoke.

## Interior for villagers

Villagers need beds and a job site to claim, or the house stays empty.
- Two beds on the upper floor (a white or red bed, near the back wall).
- A job site block on the ground floor. A composter for the farmer, or a
  smithing table, depending on which villager you want.
- Light the interior (lanterns hung from the ceiling) so nothing spawns.
- Keep doorways two blocks tall and clear so pathfinding works.

## Exterior details

- Low stone wall (cobblestone wall, 1 block) around the yard at about two
  blocks from the house.
- A stone slab path from the door to the edge of the plot.
- A flower pot or two on the bay sill.
- Hay bale or a wood pile beside the chimney wall.

## Save it

1. Place a Structure Block at one bottom corner, a Corner block at the
   opposite top corner.
2. Set the name to `vazrazhdane:house_small`, mode Save, detect the size, and
   include entities off.
3. Press Save. The file appears in your world folder under `generated`
   (check the exact subfolder name for 26.3).
4. Copy it into `structures/house_small.nbt` in this repo.
