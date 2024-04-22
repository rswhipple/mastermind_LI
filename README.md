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

You need the Docker Engine:

- Docker: You need Docker installed on your system to run the containers. For installation instructions, refer to the Docker documentation: https://docs.docker.com/engine/install/

- Docker Compose: For managing multi-container Docker applications. Docker Compose installation instructions can be found on the Docker website: https://docs.docker.com/compose/install/


## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/rswhipple/mastermind_LI.git
   cd mastermind
2. **Build and run Docker containers**:
   ```bash
   docker compose up -d
3. **Run the game**:
   ```bash
   python3 main.py