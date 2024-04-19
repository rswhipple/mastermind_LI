# utils/game.py

from .game_settings import GameSettings
from .code import Code
# from db import MastermindDB

class Game:
    def __init__(self, settings: GameSettings) -> None:
        self.board = Code(settings.level).code
        self.guess = []
        self.feedback = [0] * 2
        self._print_board()
        self._run(settings)
        # Players(settings.num_players)
    
    def _reset_guess(self):
        self.guess = []
        self.feedback = [0] * 2
        
    def _print_board(self):
        print(f"The secret board code is: {self.board}")

    def _run(self, settings: GameSettings):
        game_over = False

        while not game_over:
            input_string = input("Enter your guess")
            self.guess = [int(char) for char in input_string] 

            # add error checking for input
            # testing ln 32/33
            print(f"\tGuess = {self.guess}")

            answer_hash = [0] * (settings.num_vars)
            for num in range(len(self.board)):
                answer_hash[self.board[num]] += 1

            guess_hash = [0] * (settings.num_vars)
            for index in range(len(self.guess)):
                guess_hash[self.guess[index]] += 1
            
            for num in range(settings.num_vars):
                self.feedback[1] += min(answer_hash[num], guess_hash[num])
                # print(f"feedback[1] = {self.feedback[1]}")

            for num in range(len(self.board)):
                if self.board[num] == self.guess[num]: 
                    self.feedback[0] += 1
                # print(f"feedback[0] = {self.feedback[0]}")

            self.feedback[1] = self.feedback[1] - self.feedback[0]
            print(f"black / white = {self.feedback}")
            self._reset_guess()


# class MultiPlayer(Game):
#     def 