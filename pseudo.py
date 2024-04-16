""" 
MASTERMIND PSUEDO

class Game:
    init Mode
    init Board
    init

    method play()
        while not max_attempts and not won:
            guess = codeBreaker.make_guess()
            feedback = board.check_guess(guess)
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

    method make_guess()
        input guess from user
        return guess

class CodeBreaker:
    init CodeBreaker

    method make_guess()

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


main
    call set parameters
        choose mode
            tournament mode or individual game
                if tournament mode choose number of players
            create game instance
        choose code_maker (default ComputerPlayer, optional HumanPlayer)
        choose code_breaker (default HumanPlayer, optional ComputerPlayer)
        choose difficulty
            generate secret code (based on difficulty/players)
            init board(s) (based on difficulty/players)
    start game
        play again?
    return
    
"""


