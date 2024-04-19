# test_game.py

# from utils import GameSettings
# from utils import Code
# from utils import Game
from utils import *

def test_game():
    new_settings = GameSettings()
    code = Code(0)
    new_game = Game(new_settings)
    assert new_game.board


