# test_game_settings.py

from utils import *
# import pytest


def test_game_settings():
    new_settings = GameSettings()
    assert new_settings.level == 0
