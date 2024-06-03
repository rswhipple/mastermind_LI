# mastermind_LI
Welcome to my Python, object oriented version of the 70's game Mastermind, where the goal is to guess the secret code within a set number of attempts.

# Game Setup and Play
## Prerequisites

**Docker**:

- Docker Engine: For installation instructions, refer to the Docker documentation: https://docs.docker.com/engine/install/


## Installation

The following instructions were tested on a Mac 6-Core Intel Core i7 running macOS Sonoma 14.4.1.

1. **Clone this repository**:
   ```bash
   git clone https://github.com/rswhipple/mastermind_LI.git
   ```
   ```
   cd mastermind_LI
    ```
2. **Build the Docker Image**:
   ```bash
   docker build -t python-mastermind-cli:1.0 .
    ```
3. **Run the game**:
   ```bash
   docker run -it python-mastermind-cli:1.0
   ```


## How to Play

1. **Start the Game**: Launch the game within the  terminal by running `docker run -it python-mastermind-cli:1.0`.
2. **Set Difficulty**: Select the difficulty level – each level adds an additional variable option for the secret code.
3. **Choose Timer**: Choose whether or not you want to keep track of how long it takes to complete each game.
3. **Choose How Many Players**: Play with 1 or 2 players. 2 player version of the game will alternate turns between players to guess the secret code.
4. **Enter Player Name(s)**: Start with a new name or reuse a past name to keep track of game statistics.
5. **Guess the Code**: Enter your guesses based on feedback from previous attempts. The game will indicate how many of your guess variables and positions are correct. Black indicates that both the variable and position are correct, White means you have a correct variable in the wrong position.
6. **End of Game**: The game concludes either when you guess the code correctly or exhaust your attempts. 
7. **See your Stats**: Choose to see your player's history of wins and losses.

# Development Notes

## Extension Features

Additions implemented beyond the minimal viable product:

1. **Error Handling**: Robust error handling for player input edge cases.
2. **Parameter Customization**: Adjust the difficulty setting to change the number of variables from which the secret code is selected and increase the game's challenge.
4. **Database and Game Tracking**: Utilizes an SQLite database to track each game's details, including wins, losses, and players.
5. **Game Timer**: Monitor how long it takes to solve each code with an integrated timer.
6. **Unit Tests**  
    - Pytest was setup, but only a few tests written
    - Goal is to reduce risk of regressions.
7. **Docker Container**
    - Includes all the necessary dependencies and configurations simplifying the setup and installation process.
    - Use of a simple dockerfile in lieu of docker compose to limit the number of prerequisites needed to run the program.

## Incomplete Extension Features
1. **Scoring System**: Calculate player's score based on how many rounds they needed to guess the correct answer, game difficulty and overall time.
2. **Game Modes**:
    - **Standard Mode**: Play a single game of Mastermind.
    - **Series Mode**: Engage in a series of 5 games with a summary of results at the end.
3. **Variable Options**:
    - **Numeric Mode**: Play with a random selection of numbers in the specified range.
    - **Alpha Mode**: Play with a random selection of characters in a specified range

## Design Elements
### File Structure + Naming Conventions
  - The root directory contains the README, Dockerfile, requirements and main.py file, in addition to directories for the python class files ('utils'), database ('db'), pytest environment ('pytest-env'), and pytest tests ('tests').
  - Class files are named after the classes.

### Class Overview
**GameSettings Class:** 
Handles the configuration of the game.
- **Attributes**:
  - `score_mode`: Boolean indicating if scoring should be tracked.
  - `num_players`: Int tracking the number of players. 
  - `level`: Int indicating the difficulty level. *Current level options are 1 to 3*
  - `series_mode`: Boolean indicating whether playing individual games or a series. *Not yet implemented*
  - `multi_mode`: Boolean indicating whether playing with multiple players. *Not yet implemented*

**Game Class:** 
Serves as the central engine managing all gameplay. 
- The `Game` class takes 1 parameter, the `GameSettings` object. 
- All other class objects (except for `GameSettings`) are initiated within the `Game` class. This structure minimizes the risk of circular dependencies and simplifies argument passing. 
- All `Game` methods are private, and called from within the class.

**Player Class:** This class represents the player and manages their identification and game history.

- **Attributes**:
  - `id`: Unique identifier for each player.
  - `name`: Player's name.
- **Methods**:
  - `_get_name()`: Allows user input for name selection.
  - `check_win_loss()`: Retrieves win and loss stats for player.

**Code Class:**
`Code` is responsible for generating the secret code.

- **Key Attributes**:
  - `code`: The current secret code the player needs to guess.
- **Methods**:
  - `generate_code()`: Generates a new secret code based on the current settings.

**GameTimer Class:**
Manages the timing of each game, providing data on how long the player takes to complete a game.

- **Methods**:
  - `start_timer()`: Starts the timer at the beginning of the game.
  - `stop_timer()`: Stops the timer when the game ends and calculates the total time taken.
  - `get_duration()`: Fetches the duration of playing time for the last completed game, returns a string representation in seconds (precision level 2).

**MastermindDB Class:**
Includes most sqlite database functionality.

- **Methods**:
  - `add_player()`: Inserts a new player into the `players` table, checking that the name is a unique entry.
  - `find_player()`: Retrieves the player id from the `players` table for a given player name.
  - `add_game()`: Inserts a completed game into the `games` table.
  - `add_win()`: Records a win in the `wins` table, with foreign key references to the player and game ids.
  - `add_loss()`: Records a loss in the `losses` table, with foreign key references to the player and game ids.
  - `get_win()`: Retrieves the number of total wins from the `wins` table, for a given player id.
  - `get_loss()`: Retrieves the number of total losses from the `losses` table, for a given player id.

---

## Features Attempted but Not Included

During the development of this Mastermind program, I envisioned a web-based application interface, designed to provide a more dynamic gaming experience and showcase my ability to manage concepts such as multi-threading and concurrency. Ultimately, I decided that I did not have time to complete this feature; however, I did explore several technologies and concepts in the process:

### Web-Based Application Interface

**Concept:**
A web-based interface was intended to support displaying up to three games concurrently, allowing spectators to watch and players to compete against each other in real-time.

**Implementation:**
I experimented in creating APIs with both FastAPI and Django - these options were chosen for their ability to handle asynchronous operations, real-time web communication, and their broad, industry-wide adoption. Additionally, I initiated the implementation of multithreaded database interactions.

**Reason for Exclusion:**
Transforming the CLI-based game into a web application required a shift in the underlying architecture, including the adoption of web technologies (FastAPI or Django) with which I was less familiar. Additionally, I did not want to divert my focus to include frontend implementation. Given my timeline, prioritizing this transformation was impractical.

## Future Updates
- **Complete Outstanding Features:**
  - Finish adding series mode
  - Finish adding alpha variable option
  - Add additional scoring logic:
    - include bonus time related bonus
    - add logging
- **Next Step Features:**
  - Add multiplayer
    - multiple players can solve a code together
    - take turns as code maker and code breaker
  - Add a hint/suggestion function

---