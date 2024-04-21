from db import *
from utils import *

def main():
    setup_db()
    keep_playing = True

    while keep_playing:
        settings = GameSettings()
        game = Game(settings)
        keep_playing = game.keep_playing

if __name__ == "__main__":
    main()

