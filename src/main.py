"""Roguelite game - entry point."""
from game_loop import GameLoop


def main() -> None:
    game = GameLoop(difficulty="normal")
    game.run()


if __name__ == "__main__":
    main()
