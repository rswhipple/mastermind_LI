class GameSettings:
    tournament_mode = False
    score_mode = False
    num_players = 1
    difficulty = 0

    def __init__(self) -> None:
        self._run()
    
    def _binary_choice(option_flag, question, a, b) -> bool:
        while True:
            answer = input(f"{question}").strip().lower()

            if answer == a:
                option_flag = True
                return True
            elif answer == b:
                return False
            else:
                print(f"Please enter either '{a}' or '{b}'.")

    def _set_mode(self):
        option_flag = False
        question = "Which game mode do you want to play? (individual/tournament)"

        if self._binary_choice(option_flag, question, "tournament", "individual"):
            self.tournament_mode = True
    
    def _set_score(self):
        option_flag = False
        question = "Do you want to keep score? (yes/no)"

        if self._binary_choice(option_flag, question, "yes", "no"):
            self.score_mode = True     

    def _set_players(self):
        option_flag = False
        question = "How many players? (1/2)"
        
        if self._binary_choice(option_flag, question, "2", "1"):
            self.num_players = 2

    def _set_difficulty(self):
        question = "Choose your challenge level! Level 1, 2 or 3"

        while True:
            answer = int(input(f"{question}").strip())
            if answer <= 3 and answer > 0:
                self.difficulty = answer
                break

    def _print_settings(self):
        print(f"tournament_mode = {self.tournament_mode}")
        print(f"score_mode = {self.score_mode}")
        print(f"num_players = {self.num_players}")
        print(f"difficulty = {self.difficulty}")

    def _run(self):
        self._set_mode()
        self._set_score()
        self._set_players()
        self._set_difficulty() 

        # test by printing settings
        self._print_settings()
        