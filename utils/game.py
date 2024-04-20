# utils/game.py

from .game_settings import GameSettings
from .code import Code
from .score import Score
# from db import MastermindDB

class Game:
    score = None

    def __init__(self, settings: GameSettings) -> None:
        self._reset(settings)
    
    def _reset(self, settings: GameSettings):
        self.code = Code(settings.level)
        self.board = self.code.code
        self.len = len(self.board)
        if settings.score_mode:
            self.score = Score()
        self.var = 'digits'
        self.rounds = 10
        self.cur = 1
        self.guess = []
        self.fb = [0] * 2
        self.play = False
        self._play(settings)

    def _reset_guess(self):
        self.guess = []
        self.fb = [0] * 2

    def _print_inst(self, inst):
        print(f"\nTry to figure out the secret code. {inst}")
        
    def _print_secret_code(self): # testing only
        print(f"\nThe secret code is: {self.board}")

    def _get_guess(self, inst):
        while True:
            input_str = input(f"ROUND {self.cur}\nEnter guess: ").strip()
            if len(input_str) == self.len and input_str.isdigit():
                self.guess = [int(char) for char in input_str] 
                if all(self.code.min <= num <= self.code.max for num in self.guess):
                    break
            else:
                print(f"Invalid guess. Your guess must be {inst}.\n")

    def _play(self, settings: GameSettings):
        inst = f"{self.len} {self.var} between {self.code.min} and {self.code.max}"
        self._print_inst(inst)

        game_over = False
        a_hash = [0] * (self.code.total_vars)

        for num in range(self.len):
            a_hash[self.board[num]] += 1

        if settings.score_mode:
            self.score.timer.start()

        while not game_over:
            self._get_guess(inst)
            # print(f"Guess = {self.guess}")    # testing only
            game_over = self._evaluate(a_hash)    
        
        if settings.score_mode:
            self.score.timer.stop()
        
        if self.fb[0] == 4:
            print("You won!")
        else:
            print("All out of guesses, sorry, you lost.")
        
        question = "\nWould you like to play again (yes/no)? "
        if settings.binary_choice(question, 'yes', 'no'):
            question = "\nWould you like to change settings (yes/no)? "
            if not settings.binary_choice(question, 'yes', 'no'): self._reset(settings)
            else: self.play = True
 
    def _evaluate(self, a_hash) -> bool:
        g_hash = [0] * (self.code.total_vars)
        for index in range(self.len):
            g_hash[self.guess[index]] += 1
        
        for num in range(self.code.total_vars):
            self.fb[1] += min(a_hash[num], g_hash[num])

        for num in range(self.len):
            if self.board[num] == self.guess[num]: self.fb[0] += 1

        self.fb[1] = self.fb[1] - self.fb[0]
        print(f"\tblack / white = {self.fb}\n")
        self.cur += 1
        if self.cur == self.rounds + 1 or self.fb[0] == 4:
            return True
        self._reset_guess()
        return False

