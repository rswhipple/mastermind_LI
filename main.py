from db import *
from utils import GameSettings, Game

def main():
    db = setup_db()
    keep_playing = True

    while keep_playing:
        new_settings = GameSettings()
        game = Game(new_settings)
        keep_playing = game.play
    
    db.close_db()

if __name__ == "__main__":
    main()

