# mastermind_LI
Welcome to my Python, object oriented version of the 70's game Mastermind, where the goal is to guess the secret code within a set number of attempts.

## Features

- **Difficulty Settings**: Adjust the number of variables to increase the game's challenge.

- **Scoring System**: Opt in or out of scoring to customize how competitive the game feels.

- **Archives**: Utilizes an SQLite database to track each game's details, including scores, wins, losses, and players.

- **Game Timer**: Monitor how long it takes to solve each code with an integrated timer.

## Prerequisites

**Docker**:

- Docker Engine: For installation instructions, refer to the Docker documentation: https://docs.docker.com/engine/install/


## Installation

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

1. **Start the Game**: Launch the game within the  terminal by running `docker run -it python-mastermind-cli:1.0` or `python3 main.py`.
2. **Set Difficulty**: Select the difficulty level – each level adds an additional variable option for the secret code.
3. **Choose to Keep Score**: Opt into scoring to add a level of competition to your game.
5. **Enter Player Name**: Start with a new name or reuse a past name to keep track of game statistics.
4. **Guess the Code**: Enter your guesses based on feedback from previous attempts. The game will indicate how many of your guess variables and positions are correct. Black indicates that both the variable and position are correct, White means you have a correct variable in the wrong position.
5. **End of Game**: The game concludes either when you guess the code correctly or exhaust your attempts. 
6. **See your Stats**: Choose to see your player's history of wins and losses.

## Class Overview

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
- All other class objects are initiated within the `Game` class. This structure minimizes the risk of circular dependencies and simplifies argument passing. 
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

## Additional Design Elements

- **File Structure + Naming Conventions** 
  - The root directory contains the README, Dockerfile, requirements and main.py file, in addition to directories for the python class files ('utils'), database ('db'), pytest environment ('pytest-env'), and pytest tests ('tests').
  - Class files are named after the classes.
- **Docker Container** 
  - Includes all the necessary dependencies and configurations simplifying the setup and installation process.
  - Use of a simple dockerfile in lieu of docker compose to limit the number of prerequisites needed to run the program.

- **Pytest** 
  - Simplify unit and integration testing.
  - Reduce risk of regressions.

---

## Features Partially Implemented
- **Game Modes**:
  - **Standard Mode**: Play a single game of Mastermind.
  - **Series Mode**: Engage in a series of 5 games with a summary of results at the end.
- **Variable Options**:
  - **Numeric Mode**: Play with a random selection of numbers in the specified range.
  - **Alpha Mode**: Play with a random selection of characters in a specified range

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