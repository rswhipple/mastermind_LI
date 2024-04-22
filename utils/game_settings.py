from .helper import binary_choice

class GameSettings:
    def __init__(self) -> None:
        self.tournament_mode = False
        self.score_mode = False
        self.num_players = 1
        self.level = 0
        self._run()
    
    def _set_mode(self):
        question = "Do you want to play a solo game or in championship mode (solo/champ)? "

        if binary_choice(question, 'champ', 'solo'):
            self.tournament_mode = True
    
    def _set_score(self):
        question = "Do you want to keep score (yes/no)? "

        if binary_choice(question, 'yes', 'no'):
            self.score_mode = True     

    def _set_players(self):
        question = "How many players (1/2)? "
        
        if binary_choice(question, "2", "1"):
            self.num_players = 2

    def _set_level(self):
        question = "\nChoose your challenge level! Level 1, 2 or 3: "

        while True:
            answer = int(input(f"{question}").strip())
            if answer <= 3 and answer > 0:
                self.level = answer
                break

    def _print_settings(self):
        print(
            "\nGame Settings:"
            f"\ntournament_mode = {self.tournament_mode}"
            f"\nscore_mode = {self.score_mode}"
            f"\nnum_players = {self.num_players}"
            f"\nlevel = {self.level}\n"
            )

    def _run(self):
        #self._set_mode()
        self._set_level() 
        self._set_score()
        # self._set_players()

        # test by printing settings
        self._print_settings()
        