from board import Board
from dice import Dice
from player import Player
from turn_handler import TurnHandler


class Game:
    """
    Coordinates the overall flow of the Game of Life (board game).

    Responsibilities:
    - Validate and create players during setup
    - Maintain turn order
    - Delegate single-turn mechanics to TurnHandler
    - Provide summary output for the CLI ('p' command)
    - Detect termination when all players have retired
    - Determine the winner based on cash balance

    This class acts as the orchestration layer, keeping movement rules and
    tile effects in dedicated components.
    """

    def __init__(self, board: Board, dice: Dice, turn_handler: TurnHandler) -> None:
        self._board = board
        self._dice = dice
        self._turn_handler = turn_handler
        self._players: list[Player] = []
        self._current_index = 0

    @property
    def players(self) -> list[Player]:
        return self._players

    def setup_players(self, num_players: int, names: list[str], starting_cash: int = 0) -> None:
        """Create and validate players for the game."""
        if num_players < 2 or num_players > 4:
            raise ValueError("Number of players must be between 2 and 4.")
        if len(names) != num_players:
            raise ValueError("Names list must match number of players.")

        cleaned = [n.strip() for n in names]
        if any(not n for n in cleaned):
            raise ValueError("Player names cannot be empty.")
        if len({n.lower() for n in cleaned}) != len(cleaned):
            raise ValueError("Player names must be unique.")

        self._players = [Player(name, starting_cash=starting_cash, start_position=0) for name in cleaned]
        self._current_index = 0

    def is_over(self) -> bool:
        """Return True when all players are retired."""
        return bool(self._players) and all(p.is_retired for p in self._players)

    def current_player(self) -> Player:
        return self._players[self._current_index]

    def advance_turn(self) -> None:
        self._current_index = (self._current_index + 1) % len(self._players)

    def summary_text(self) -> str:
        """Return a formatted summary table of all players."""
        header = "Name       Position   Cash   Status"
        line = "-" * len(header)
        rows = [header, line]

        for p in self._players:
            status = "RETIRED" if p.is_retired else "ACTIVE"
            rows.append(f"{p.name:<10} {p.position:<10} {p.cash:<6} {status}")

        return "\n".join(rows)

    def determine_winner(self) -> Player:
        """Winner is highest cash (tie-break: first encountered)."""
        return max(self._players, key=lambda p: p.cash)

    def run_cli(self) -> None:
        """
        Run the command-line loop.

        Controls:
        - Press ENTER on an empty line to roll.
        - Type 'p' to print summary (does not end the turn).
        """
        if not self._players:
            raise RuntimeError("Game cannot start without players. Call setup_players first.")

        print("Game of Life (Board Game) - CLI")
        print("Press ENTER to roll. Type 'p' to show summary.")
        print("Tip: press Enter on a blank line to roll (do not type the word ENTER).\n")

        while not self.is_over():
            player = self.current_player()

            if player.is_retired:
                self.advance_turn()
                continue

            user = input(f"{player.name}'s turn (ENTER=roll, p=summary): ").strip().lower()

            if user == "p":
                print(self.summary_text())
                continue

            if user != "":
                print("Invalid input. Press ENTER to roll, or type 'p' for summary.")
                continue

            events = self._turn_handler.play_turn(player, self._board, self._dice)
            for e in events:
                print(e)

            self.advance_turn()

        winner = self.determine_winner()
        print("\nGame over!")
        print(self.summary_text())
        print(f"Winner: {winner.name} with cash={winner.cash}")