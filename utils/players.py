from db import *
from .helper import binary_choice

class Player:
    def __init__(self, db: MastermindDB) -> None:
        self.name = self._get_name(db)

        # testing
        print(db.find_player(self.name))

    # def make_code():
    #     # option to have a human code maker
    #     input("")

    # def get_scores(self):


    def _get_name(self, db: MastermindDB) -> str:
        while True:
            name = input("Choose Player Name (alphanumeric): ").strip()
            if not name.isalnum():
                print(f"Invalid name. Alphanumeric characters only.\n")
            if db.find_player(name):
                question = \
                    f"{name} already exists, continue as {name} (yes/no)?\n"
                use_name = binary_choice(question, 'yes', 'no')
                if use_name:
                    return name
            db.add_player(name)
            return name


class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
