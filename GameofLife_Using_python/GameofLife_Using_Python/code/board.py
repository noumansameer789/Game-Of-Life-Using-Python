from tile import Tile


class Board:
    
    """
Represents the game board as an ordered list of Tile objects.

This implementation uses a fixed 20-tile board to:
- keep the game duration short
- simplify automated testing
- guarantee termination in a small number of turns

The Board provides tile lookup and end-of-board detection.
    """


    def __init__(self) -> None:
        self._tiles = self._create_default_board()

    def _create_default_board(self) -> list[Tile]:
        """
        Creates a simplified 20-tile board.
        """
        tiles = []

        # Start tile
        tiles.append(Tile("Start", "START"))

        # Middle tiles
        for i in range(1, 19):
            if i % 5 == 0:
                tiles.append(Tile("Payday", "PAYDAY", cash_effect=100))
            else:
                tiles.append(Tile("Event", "EVENT", cash_effect=-50))

        # End tile
        tiles.append(Tile("Retirement", "RETIRE"))

        return tiles

    def get_tile(self, position: int) -> Tile:
        return self._tiles[position]

    def is_end(self, position: int) -> bool:
        return position >= len(self._tiles) - 1

    def final_position(self) -> int:
        return len(self._tiles) - 1

    def size(self) -> int:
        return len(self._tiles)    






# --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.