# Roguelite Game

A wave-based roguelite: survive escalating enemy waves, pick skills between rounds, die, and grow stronger across runs.

## Repository Structure

```
/docs        Game design documentation
/src         Game source code (starter structure)
/data        Balance data (waves, enemies, skills) in JSON
```

## Docs
- `docs/GDD.md` - full Game Design Document
- `docs/gameplay-loop.md` - core loop
- `docs/progression.md` - meta & run progression
- `docs/difficulty.md` - difficulty scaling

## Data
- `data/waves.json` - enemy wave definitions
- `data/enemies.json` - enemy stats
- `data/skills.json` - skill catalog

## Source
- `src/main.py` - entry point
- `src/game_loop.py` - run/loop controller
- `src/wave_manager.py` - wave spawning
- `src/skill_system.py` - skill selection/apply

## License
MIT
