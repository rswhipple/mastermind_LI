# utils/game.py

from .game_settings import GameSettings
from .code import Code
from .timer import GameTimer
from .players import Player
from .helper import binary_choice
from db import connect_db

class Game:
    score = None

    def __init__(self, settings: GameSettings) -> None:
        db = connect_db()   # open db
        self.db = db
        self.t = GameTimer()
        self.p = self._get_player(settings.num_players)
        self.var = 'digits'
        self.rounds = 10
        self.score = 0
        self._reset(settings)
        # add game info to db here
        db.add_game(self.p[0].id, self.t.start_t, self.t.end_t, \
                    self.t.dur, self.score)
    
    def _reset(self, settings: GameSettings):
        self.c = Code(settings.level)
        self.board = self.c.code
        self.b_len = len(self.board)
        self.cur = 1
        self.guess = []
        self.fb = [0] * 2
        self.inst = \
            f"{self.b_len} {self.var} between {self.c.min} and {self.c.max}"
        self.keep_playing = False
        self._play(settings)

    def _get_player(self, num) -> list:
        players = []
        for i in range(num):
            temp = Player(self.db)
            players.append(temp)
        # testing
        # for player in players:
        #     print(player.name, player.id)
        return players
    
    def _print_inst(self):
        inst = (
            "\nTry to decipher the secret code!"
            f"\nPick {self.inst}."
            "\nDuplicates are allowed."
            )
        print(f"{inst}")

    def _reset_guess(self):
        self.guess = []
        self.fb = [0] * 2

    def _get_guess(self):
        while True:
            input_str = input(f"ROUND {self.cur}\nEnter guess: ").strip()
            if len(input_str) == self.b_len and input_str.isdigit():
                self.guess = [int(char) for char in input_str] 
                if all(self.c.min <= num <= self.c.max for num in self.guess):
                    break
            else:
                print(f"Invalid guess. Your guess must be {self.inst}.\n")
    
    def _create_hash(self, num_vars, src) -> list:
        hash = [0] * (num_vars)
        for num in range(len(src)):
            hash[src[num]] += 1
        return hash
    
    def _play_again(self, settings: GameSettings):
        question = "\nDo you want to play again (yes/no)? "

        if binary_choice(question, 'yes', 'no'):
            question = "\nDo you need to change any settings (yes/no)? "

            if binary_choice(question, 'yes', 'no'): 
                self.db.close_db()  # close db
                self.keep_playing = True # return to main
            else: 
                self._reset(settings) # restarts _play() 
        else:
            self.db.close_db()  # close db
            print("Thanks for playing!")

    def _print_result(self):
        if self.fb[0] == 4:
            print("You won!")
        else:
            print("All out of guesses, sorry, you lost this one.")
        self.score = self._calc_score()
    
    def _calc_score(self):
        return (self.rounds - self.cur) * (100 / self.rounds)
    
    def _evaluate(self, a_hash) -> bool:
        g_hash = self._create_hash(self.c.total_vars, self.guess)
        
        for num in range(self.c.total_vars):
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
        self._print_inst()
        game_over = False
        a_hash = self._create_hash(self.c.total_vars, self.board)

        if settings.score_mode: 
            self.t.start() # start timer

        while not game_over:
            self._get_guess()
            game_over = self._evaluate(a_hash)    
        
        if settings.score_mode:
            self.t.stop() # stop timer
        
        self._print_result()

        if not settings.tournament_mode:
            self._play_again(settings)
