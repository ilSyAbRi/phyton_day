```
Plant             → name, height, grow()
   ↓
FloweringPlant   → adds flower_color, blooming_state
   ↓
PrizeFlower      → adds prize_points
```
- Plant → parent

- FloweringPlant → child of Plant

- PrizeFlower → child of FloweringPlant (grandchild of Plant)

-> Because of this, PrizeFlower inherits everything from both its parent and grandparent.
