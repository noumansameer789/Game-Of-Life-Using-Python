# Game of Life (CLI)

Author: Nouman Sameer  
Module: COMM109J  

Command-line, object-oriented implementation of a simplified Game of Life board game developed for COMM109J.
“This is the board game version, not Conway’s automaton.”

---

## Project Overview

This project implements a modular, object-oriented command-line version of the Game of Life board game.  

The system demonstrates:

- Clean separation of concerns
- Multiple interacting classes
- Full game loop implementation
- Deterministic logic (no AI players)
- Robust input validation
- Unit testing with pytest
- Documentation with Sphinx

The game supports 2–4 human players and ends when all players retire. The winner is determined by highest cash balance.

---

## Project Structure

All implementation and tests are contained inside the `code/` directory.


---

## Requirements

- Python 3.13 (tested)
- pip

---

## Installation

From the repository root:

```bash
cd code
python -m pip install -r requirements.txt

Running the Game
cd code
python main.py
Controls

Press ENTER to roll the dice
Type p to print the current game summary (does not end the turn)
The game ends when all players reach retirement.
The winner is the player with the highest cash balance.

Running Tests (pytest)
cd code
python -m pytest

All tests must pass before submission.

The project includes unit tests for:
Board
Dice
Player
TurnHandler
Game logic
Documentation (Sphinx)


Sphinx is used for automatic documentation generation.

To build the documentation:
cd code
sphinx-build -b html doc doc/build/html

Open the generated file:
code/doc/build/html/index.html




Game Simplifications:

To ensure clarity and testability:
The board consists of 20 tiles.
Tile effects are deterministic.
No AI players are implemented.
No randomness beyond dice rolls.
The game ends when all players reach retirement.
The winner is the player with the highest cash balance.


Coursework Links:
GitHub Repository: <ADD YOUR GITHUB LINK HERE>
Video Demonstration: <ADD YOUR VIDEO LINK HERE>
