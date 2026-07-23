# Difficulty Scaling

## Per-wave scaling
- Enemy HP: base * (1 + 0.12 * wave)
- Enemy damage: base * (1 + 0.08 * wave)
- Spawn count: base + floor(wave * 1.5)

## Composition shifts
- Waves 1-4: melee + swarm.
- Waves 5-9: add ranged.
- Waves 10-14: add elites.
- Waves 15-19: mixed + heavy elites.
- Boss waves (5/10/15/20): single boss + adds.

## Difficulty modes
| Mode    | HP mult | Dmg mult | Shard mult |
|---------|---------|----------|------------|
| Easy    | 0.85    | 0.85     | 0.8        |
| Normal  | 1.00    | 1.00     | 1.0        |
| Hard    | 1.25    | 1.20     | 1.3        |
| Nightmare | 1.60  | 1.45     | 1.7        |

## Dynamic (optional)
- Ascension modifiers unlocked after first win (elite density, less rerolls, boss enrage).
