"""Core run/loop controller."""
from wave_manager import WaveManager
from skill_system import SkillSystem

DIFFICULTY = {
    "easy": (0.85, 0.85, 0.8),
    "normal": (1.0, 1.0, 1.0),
    "hard": (1.25, 1.20, 1.3),
    "nightmare": (1.60, 1.45, 1.7),
}


class GameLoop:
    def __init__(self, difficulty: str = "normal", total_waves: int = 20):
        self.hp_mult, self.dmg_mult, self.shard_mult = DIFFICULTY[difficulty]
        self.total_waves = total_waves
        self.waves = WaveManager(self.hp_mult, self.dmg_mult)
        self.skills = SkillSystem()
        self.shards = 0
        self.player_alive = True

    def run(self) -> None:
        for wave in range(1, self.total_waves + 1):
            survived = self.waves.play_wave(wave)
            if not survived:
                self.player_alive = False
                break
            self.shards += int((2 + (10 if wave % 5 == 0 else 0)) * self.shard_mult)
            self.skills.offer_choices(wave)
        self.end_run()

    def end_run(self) -> None:
        status = "WIN" if self.player_alive else "DEFEAT"
        print(f"Run over: {status}. Shards earned: {self.shards}")
