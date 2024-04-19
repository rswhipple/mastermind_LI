# utils/game.py

from .game_settings import GameSettings
from .code import Code
# from db import MastermindDB

class Game:
    def __init__(self, settings: GameSettings) -> None:

        self.board = Code(settings.level).code
        self.print_board()
        # Players(settings.num_players)
        
    def print_board(self):
        print(f"The secret board code is: {self.board}")

    def run(self):
        

# class MultiPlayer(Game):
#     def 