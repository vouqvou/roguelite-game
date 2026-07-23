"""Spawns and resolves enemy waves."""
import json
import math
import os


class WaveManager:
    def __init__(self, hp_mult: float, dmg_mult: float):
        self.hp_mult = hp_mult
        self.dmg_mult = dmg_mult
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "waves.json")
        with open(data_path, encoding="utf-8") as fh:
            self.config = json.load(fh)

    def enemy_count(self, wave: int, base: int = 8) -> int:
        return base + math.floor(wave * self.config["scaling"]["spawn_growth"])

    def play_wave(self, wave: int) -> bool:
        count = self.enemy_count(wave)
        hp_scale = 1 + self.config["scaling"]["hp_per_wave"] * wave
        print(f"Wave {wave}: {count} enemies (hp x{hp_scale:.2f} x{self.hp_mult})")
        # Combat simulation is handled by the engine layer; returns survival flag.
        return True
