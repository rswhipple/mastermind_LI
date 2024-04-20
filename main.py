from utils import GameSettings, Game

def main():
    keep_playing = True

    while keep_playing:
        new_settings = GameSettings()
        game = Game(new_settings)
        keep_playing = game.play

if __name__ == "__main__":
    main()