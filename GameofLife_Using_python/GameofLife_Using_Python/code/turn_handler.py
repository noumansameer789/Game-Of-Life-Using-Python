from board import Board
from dice import Dice
from player import Player


class TurnHandler:
    """
    Executes the rules for a single player's turn.

    A turn consists of:
    - Rolling the dice
    - Moving the player (clamped to board end)
    - Applying the landed tile effect
    - Retiring the player if the retirement tile is reached

    The TurnHandler returns event messages rather than printing directly,
    so behaviour remains unit-testable and the CLI remains separate.
    """

    def play_turn(self, player: Player, board: Board, dice: Dice) -> list[str]:
        if player.is_retired:
            return [f"{player.name} is retired and skips their turn."]

        roll = dice.roll()
        player.move_by(roll, final_position=board.final_position())

        tile = board.get_tile(player.position)
        events: list[str] = [f"{player.name} rolled {roll} and landed on {tile.name} ({tile.tile_type})."]

        if tile.cash_effect != 0:
            player.apply_cash(tile.cash_effect)
            events.append(f"Cash changed by {tile.cash_effect}. New balance: {player.cash}.")

        if tile.tile_type == "RETIRE":
            player.retire()
            events.append(f"{player.name} has retired.")

        return events






# --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.