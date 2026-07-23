# Game Design Document - Roguelite Game

## Vision
Fast-paced top-down survival roguelite. Each run lasts ~15-25 min. Player fights escalating waves, chooses one skill per wave cleared, and uses persistent meta-currency to unlock permanent upgrades between runs.

## Pillars
1. Readable combat - clear telegraphs, fair deaths.
2. Build variety - synergistic skills create emergent builds.
3. Meaningful meta - each run advances permanent progression.

## Core Loop
Spawn -> Fight wave -> Clear wave -> Choose 1 of 3 skills -> Repeat (harder) -> Die/Win -> Spend meta-currency -> New run.

## Systems
- Combat: real-time, WASD move + auto/aim attack.
- Skills: active + passive; stackable rarities (Common/Rare/Epic).
- Enemies: melee, ranged, swarm, elite, boss (every 5 waves).
- Progression: run XP -> skill picks; meta shards -> permanent unlocks.
- Difficulty: linear stat scaling + composition changes + modifiers.

See sibling docs for detail: gameplay-loop.md, progression.md, difficulty.md.
