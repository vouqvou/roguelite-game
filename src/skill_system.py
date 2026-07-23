"""Handles skill offers, selection and stacking."""
import json
import os
import random


class SkillSystem:
    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "skills.json")
        with open(data_path, encoding="utf-8") as fh:
            data = json.load(fh)
        self.catalog = data["skills"]
        self.weights = data["rarity_weights"]
        self.owned = []

    def _pool(self, wave: int):
        return self.weights["late"] if wave >= 10 else self.weights["early"]

    def offer_choices(self, wave: int, n: int = 3):
        weights = self._pool(wave)
        pick = random.choices(
            self.catalog,
            weights=[weights[s["rarity"]] for s in self.catalog],
            k=n,
        )
        print(f"Skill choices (wave {wave}): {[s['name'] for s in pick]}")
        return pick

    def choose(self, skill):
        self.owned.append(skill)
