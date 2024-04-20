from .game import Game
from .timer import GameTimer

class Score:
    def __init__(self, game: Game) -> None:
        self.timer = GameTimer()
        self.rounds = game.rounds
        self.result = 0

    def run_timer(self):
        self.timer.start()