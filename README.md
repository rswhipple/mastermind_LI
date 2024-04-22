# mastermind_LI
Welcome to my Python/OOP version  of the 70's game Mastermind, where the goal is to guess the secret code within a set number of attempts.

My implementation is structured with multiple classes to manage game mechanics, player data, and game settings, enhanced with database support for tracking statistics.

## Features

- **Game Modes**:
  - **Standard Mode**: Play a single game of Mastermind.
  - **Tournament Mode**: Engage in a series of 5 games with a summary of results at the end.

- **Difficulty Settings**: Adjust the number of slots in the secret code to increase the game's challenge.

- **Scoring System**: Opt in or out of scoring to customize how competitive the game feels.

- **Persistent Storage**: Utilizes an SQLite database to track each game's details, including scores, wins, losses, and player stats, all linked to a unique player ID.

- **Game Timer**: Monitor how long it takes to solve each code with an integrated timer.

## Prerequisites

Docker:

- Docker Engine: For installation instructions, refer to the Docker documentation: https://docs.docker.com/engine/install/

<!-- - Docker Compose: For managing multi-container Docker applications. Docker Compose installation instructions can be found on the Docker website: https://docs.docker.com/compose/install/ -->


## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/rswhipple/mastermind_LI.git
   cd mastermind
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

1. **Start the Game**: Launch the game from your terminal by running `python3 main.py`.
2. **Select Game Mode**: Choose from standard or tournament mode.
3. **Set Difficulty**: Select the difficulty level, each level adds an additonal slot in the secret code.
4. **Choose to Keep Score**: Opt into scoring to add a level of competition to your game.
5. **Enter Player Name**: Start with a new name or reuse a past name to keep track of game statistics.
4. **Guess the Code**: Enter your guesses based on feedback from previous attempts. The game will indicate how many of your guessed numbers and positions are correct. Black means the number and postion is correct, White means just the number is correct.
5. **End of Game**: The game concludes either when you guess the code correctly or exhaust your attempts. In tournament mode, proceed through multiple games.

## Class Overview

**Game Class:** 
Serves as the central engine for managing the entire gameplay process. It coordinates the interaction between the player, game settings, and game components, such as the secret code and timer. 
- All `Game` methods are private. The game loop begins automatically when you initiate a `Game` object.
- The `Game` class takes one parameter: the `GameSettings` object.
- **Methods**:
  - `_play()`: Manages a single round of guessing in the game.
  - `end_game()`: Concludes the game session and stores results.

**GameSettings CLass:** 
Handles the configuration of the game, including difficulty levels and scoring options.
- **Attributes**:
  - `difficulty`: Number of slots in the secret code, which affects the game's challenge.
  - `scoring_enabled`: Boolean indicating if scoring should be tracked.

**Player Class:** This class represents the player and manages their identification and game history.

- **Attributes**:
  - `id`: Unique identifier for each player.
  - `name`: Player's name.
- **Methods**:
  - `update_stats(win: bool)`: Updates the player's win/loss record after each game.

**Code Class:**
`Code` is responsible for generating the secret code.

- **Attributes**:
  - `secret_code`: The current secret code the player needs to guess.
- **Methods**:
  - `generate_code()`: Generates a new secret code based on the current difficulty setting.


**GameTimer Class:**
Manages the timing of each game, providing statistics on how long the player takes to complete a game.

- **Methods**:
  - `start_timer()`: Starts the timer at the beginning of the game.
  - `stop_timer()`: Stops the timer when the game ends and calculates the total time taken.

Each of these classes works together to create a comprehensive and interactive Mastermind game experience, ensuring that each component is modular and handles its specific tasks efficiently.
