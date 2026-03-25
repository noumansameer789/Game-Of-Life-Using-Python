class Player:
    """
    Represents a player in the Game of Life.

    Attributes:
    - name: player display name
    - position: current tile index on the board
    - cash: accumulated money
    - is_retired: indicates whether the player has reached retirement

    The Player class is responsible only for managing its own state.
    It does not contain board logic or turn sequencing behaviour.
    """

    def __init__(self, name: str, starting_cash: int = 0, start_position: int = 0) -> None:
        cleaned = name.strip()
        if not cleaned:
            raise ValueError("Player name cannot be empty.")
        if starting_cash < 0:
            raise ValueError("Starting cash cannot be negative.")
        if start_position < 0:
            raise ValueError("Start position cannot be negative.")

        self._name = cleaned
        self._cash = starting_cash
        self._position = start_position
        self._is_retired = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def cash(self) -> int:
        return self._cash

    @property
    def position(self) -> int:
        return self._position

    @property
    def is_retired(self) -> bool:
        return self._is_retired

    def move_to(self, new_position: int) -> None:
        if new_position < 0:
            raise ValueError("Position cannot be negative.")
        self._position = new_position

    def move_by(self, steps: int, final_position: int) -> None:
        """
        Move forward by a number of steps.
        If movement would go past final_position, clamp to final_position.
        """
        if steps < 0:
            raise ValueError("Steps cannot be negative.")
        if final_position < 0:
            raise ValueError("Final position cannot be negative.")

        target = self._position + steps
        self._position = final_position if target > final_position else target

    def apply_cash(self, amount: int) -> None:
        self._cash += amount

    def retire(self) -> None:
        self._is_retired = True

    def summary(self) -> str:
        status = "RETIRED" if self._is_retired else "ACTIVE"
        return f"{self._name}: pos={self._position}, cash={self._cash}, status={status}"






# --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.