# mastermind_LI
Welcome to my Python/OOP version  of the 70's game Mastermind, where the goal is to guess the secret code within a set number of attempts.

My implementation is structured with multiple classes that manage game mechanics, player data, and game settings, enhanced with database support for tracking statistics.

## Features

- **Game Modes**:
  - **Standard Mode**: Play a single game of Mastermind.
  - **Series Mode**: Engage in a series of 5 games with a summary of results at the end.

- **Difficulty Settings**: Adjust the number of variable options in the secret code to increase the game's challenge.

- **Scoring System**: Opt in or out of scoring to customize how competitive the game feels.

- **Archives**: Utilizes an SQLite database to track each game's details, including scores, wins, losses, and player stats, all linked to a unique player ID.

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
2. **Select Game Mode**: Choose from solo or series mode.
3. **Set Difficulty**: Select the difficulty level – each level adds an additonal variable option for the secret code.
4. **Choose to Keep Score**: Opt into scoring to add a level of competition to your game.
5. **Enter Player Name**: Start with a new name or reuse a past name to keep track of game statistics.
4. **Guess the Code**: Enter your guesses based on feedback from previous attempts. The game will indicate how many of your guess variables and positions are correct. Black indicates that both the variable and postion are correct, White means you have a correct variable in the wrong position.
5. **End of Game**: The game concludes either when you guess the code correctly or exhaust your attempts. 

## Class Overview

**GameSettings Class:** 
Handles the configuration of the game.
- **Attributes**:
  - `series_mode`: Boolean indicating whether playing individual games or a series.
  - `multi_mode`: Boolean indicating whether playing with multiple players. *Not yet implemented*
  - `score_mode`: Boolean indicating if scoring should be tracked.
  - `num_players`: Int tracking the number of players. *Only used with multi-player*
  - `level`: Int indicating the difficulty level. *Current level options are 1 to 3*

**Game Class:** 
Serves as the central engine managing all gameplay. 
- The `Game` class takes 1 parameter, the `GameSettings` object. 
- All other class objects are initiated within the `Game` class. This structure mnimizes the risk of circular dependencies and simplifies argument passing. 
- All `Game` methods are private, and called from within the class.
<!-- - **Key Methods**:
  - `_play()`: Manages a single round of guessing in the game.
  - `evaluate()`: Concludes the game session and stores results. -->

**Player Class:** This class represents the player and manages their identification and game history.

- **Attributes**:
  - `id`: Unique identifier for each player.
  - `name`: Player's name.
- **Methods**:
  - `_get_name()`: Fetches user input for name selection.
  - `check_win_loss()`: Retrieves win and loss stats for player.

**Code Class:**
`Code` is responsible for generating the secret code.

- **Key Attributes**:
  - `code`: The current secret code the player needs to guess.
- **Methods**:
  - `generate_code()`: Generates a new secret code based on the current setting.

**GameTimer Class:**
Manages the timing of each game, providing data on how long the player takes to complete a game.

- **Methods**:
  - `start_timer()`: Starts the timer at the beginning of the game.
  - `stop_timer()`: Stops the timer when the game ends and calculates the total time taken.
  - `get_duration()`: Fetches the duration of playing time for the last completed game, return a string representation of seconds (precision level 2).

## Additional Design Elements

- **Docker** 
   - The docker container includes all the necessary dependencies and configurations simplifying the setup and installation process.
   - Docker allows programs to run in isolated environments, reducing conflicts between running applications and between their dependencies.
   - The Docker container can be run on any system that supports Docker without modification.
   - I decided to use a regular dockerfile instead of docker compose to limit the prerequisites for installing the program.

- **Pytest** 

---

## Features Attempted but Not Included

During the development of this Mastermind program, I envisioned several features that aimed to enhance user interaction and provide a dynamic gaming experience. 

### Web-Based Application Interface

**Concept:**
A web-based interface would have made the game accessible from browsers, enhancing accessibility and ease of use. This interface was intended to support multiple simultaneous users with minimal latency, providing a platform for broader interaction.

**Implementation:**
I experimented with creating an API with both FastAPI and Django. I choose these options for their ability to handle asynchronous operations and real-time web communication.

**Reason for Exclusion:**
Transforming the CLI-based game into a web application required a shift in the underlying architecture, including the adoption of web technologies (FastAPI or Django) with which I was less familiar. Additionally, I did not want to divert my focus to any frontend implementation. Given my timeline, prioritizing this transformation was deemed impractical.

### Multiplayer Tournament Mode with Real-time Updates

**Concept:**
I planned a tournament mode where multiple players could compete simultaneously in real time. The interface would have supported displaying up to three games concurrently, allowing spectators to watch and players to compete against each other.

**Implementation:**
To support real-time interactions and manage multiple games efficiently, I began implementing multithreading for database interactions.


---