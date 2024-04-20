from .timer import GameTimer

class Score:
    def __init__(self) -> None:
        self.timer = GameTimer()
        self.rounds = 0
        self.result = 0
