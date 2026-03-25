from board import Board
from dice import Dice
from game import Game
from turn_handler import TurnHandler


def prompt_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < min_value or value > max_value:
            print(f"Please enter a number between {min_value} and {max_value}.")
            continue

        return value


def prompt_nonempty_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty.")


def main() -> None:
    print("Welcome to Game of Life (CLI)\n")

    num_players = prompt_int_in_range("How many players (2-4)? ", 2, 4)

    names: list[str] = []
    for i in range(num_players):
        while True:
            name = prompt_nonempty_name(f"Enter name for Player {i + 1}: ")
            if name.lower() in {n.lower() for n in names}:
                print("That name is already taken. Please choose a unique name.")
                continue
            names.append(name)
            break

        board = Board()
    dice = Dice()
    handler = TurnHandler()
    game = Game(board, dice, handler)
    game.setup_players(num_players=num_players, names=names, starting_cash=0)

    try:
        game.run_cli()
    except (KeyboardInterrupt, EOFError):
        print("\nExited game.")
        

if __name__ == "__main__":
    main()
    




# --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.