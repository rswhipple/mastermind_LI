from utils import GameSettings, Game

def main():
    new_settings = GameSettings()
    new_game = Game(new_settings)
    new_game._run

if __name__ == "__main__":
    main()