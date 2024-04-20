from db import *
from utils import *

def main():
    setup_db()
    keep_playing = True

    while keep_playing:
        settings = GameSettings()
        db = connect_db(settings.tournament_mode)
        game = Game(settings)
        keep_playing = game.play
        db.close_db()

if __name__ == "__main__":
    main()

