""" 
MASTERMIND PSUEDO

class Game:
    init Mode
    init Board
    init

    method play()
        while not max_attempts and not won:
            guess = CodeBreaker.make_guess()
            feedback = Board.check_guess(guess)
            display feedback
            if feedback is full match:
                won = True
                break
        display win or lose message

class CodeMaker:
    init CodeMaker

    method make_code()

class HumanCodeMaker inherits CodeMaker:
    init HumanCodeMaker

    method make_code()
        input code from user
        return guess

class CodeBreaker:
    init CodeBreaker

    method make_guess()
        input guess from user
        return guess

class Difficulty:
    init level
        board size
        board total_variables
        max_attempts

    method adjust_difficulty_settings()
    # method call init_board ??

class Easy(Difficulty):

class Medium(Difficulty):

class Hard(Difficulty):

class Board:
    init Board

    method check_guess(guess)
        compare guess with secret code
        return feedback

class Score:

main
    call set parameters
        choose mode
            tournament mode or individual game
                choose number of players
            create game instance
        choose CodeMaker (default ComputerPlayer, optional HumanPlayer)
        # choose CodeBreaker (default HumanPlayer, optional ComputerPlayer) this is a possible extention 
        choose Difficulty
            generate secret code (based on difficulty/players)
            init board(s) (based on difficulty/players)
    start game
        play again?
    return
    
"""


