# utils/game.py

from .game_settings import GameSettings
from .code import Code
from .score import Score
from .players import Player
from .helper import binary_choice
from db import *

class Game:
    score = None

    def __init__(self, settings: GameSettings) -> None:
        db = connect_db()
        self.db = db
        self._reset(settings)
    
    def _reset(self, settings: GameSettings):
        self.players = self._get_player(settings.num_players)
        self.code = Code(settings.level)
        self.board = self.code.code
        self.b_len = len(self.board)
        if settings.score_mode:
            self.score = Score()
        self.var = 'digits'
        self.rounds = 10
        self.cur = 1
        self.guess = []
        self.fb = [0] * 2
        self.inst = \
            f"{self.b_len} {self.var} between {self.code.min} and {self.code.max}"
        self.keep_playing = False
        self._play(settings)

    def _get_player(self, num) -> list:
        players = []
        for i in range(num):
            temp = Player(self.db)
            players.append(temp.name)
        return players

    def _reset_guess(self):
        self.guess = []
        self.fb = [0] * 2

    def _print_inst(self):
        print(f"\nTry to figure out the secret code. {self.inst}")

    def _print_result(self):
        if self.fb[0] == 4:
            print("You won!")
        else:
            print("All out of guesses, sorry, you lost this one.")

    def _get_guess(self):
        while True:
            input_str = input(f"ROUND {self.cur}\nEnter guess: ").strip()
            if len(input_str) == self.b_len and input_str.isdigit():
                self.guess = [int(char) for char in input_str] 
                if all(self.code.min <= num <= self.code.max for num in self.guess):
                    break
            else:
                print(f"Invalid guess. Your guess must be {self.inst}.\n")
    
    def _create_hash(self, num_vars, src) -> list:
        hash = [0] * (num_vars)

        for num in range(len(src)):
            hash[src[num]] += 1
        return hash
    
    def _play_again(self, settings: GameSettings):
        self.db.close_db()
        question = "\Do you want to play again (yes/no)? "

        if binary_choice(question, 'yes', 'no'):
            question = "\nDo you need to change any settings (yes/no)? "

            if not binary_choice(question, 'yes', 'no'): 
                self._reset(settings)
            else: self.keep_playing = True

    
    def _evaluate(self, a_hash) -> bool:
        g_hash = self._create_hash(self.code.total_vars, self.guess)
        
        for num in range(self.code.total_vars):
            self.fb[1] += min(a_hash[num], g_hash[num])

        for num in range(self.b_len):
            if self.board[num] == self.guess[num]: self.fb[0] += 1

        self.fb[1] = self.fb[1] - self.fb[0]
        print(f"\tblack / white = {self.fb}\n")

        self.cur += 1
        if self.cur == self.rounds + 1 or self.fb[0] == 4:
            return True
        
        self._reset_guess()
        return False

    def _play(self, settings: GameSettings):
        # intro / local variables
        self._print_inst()
        game_over = False
        a_hash = self._create_hash(self.code.total_vars, self.board)

        # start timer
        if settings.score_mode:
            self.score.timer.start()

        # game loop
        while not game_over:
            self._get_guess()
            game_over = self._evaluate(a_hash)    
        
        # stop timer
        if settings.score_mode:
            self.score.timer.stop()
        
        # outro
        self._print_result()

        if not settings.tournament_mode:
            self._play_again(settings)
