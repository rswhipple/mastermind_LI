from db import *
from .helper import binary_choice

class Player:
    def __init__(self, db: MastermindDB, i) -> None:
        self.num = i + 1
        self.name = None
        self.id = None
        self._get_name(db)

    # def input_code():
    #     # option to have a human code maker

    def check_scores(self):
        # check total wins and losses
        pass

    def _get_name(self, db: MastermindDB):
        while True:
            name = input(f"Choose Player {self.num} Name (alphanumeric): ").strip()
            if not name.isalnum():
                print(f"Invalid name. Alphanumeric characters only.\n")

            id = db.add_player(name)
            if id:
                self.name = name
                self.id = id
                break
            else:
                q = f"{name} already exists, continue as {name} (yes/no)?\n"
                if binary_choice(q, 'yes', 'no'):
                    player_data = db.find_player(name)
                    for player in player_data:
                        self.id, self.name = player
                    break
                
        player_str = f"Player {self.num}'s name is {self.name}, id is {self.id}.\n"
        print(player_str)


class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
