from utils import *
from db import MastermindDB

class Game:
    def __init__(self, settings: GameSettings) -> None:

        self.board = Code(settings.level).generate_code()
        # Players(settings.num_players)
        

# class MultiPlayer(Game):
#     def 