import random
from typing import Protocol


class RandomSource(Protocol):
    def randint(self, a: int, b: int) -> int:
        ...


class Dice:
    """
Represents a dice used to determine movement.

Randomness is isolated inside this class and can be injected via an RNG
object to support deterministic unit testing.
"""


    def __init__(self, sides: int = 6, rng: RandomSource | None = None) -> None:
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")

        self._sides = sides
        self._rng = rng if rng is not None else random.Random()

    @property
    def sides(self) -> int:
        return self._sides

    def roll(self) -> int:
        return self._rng.randint(1, self._sides)
    
    
    
    
    
    
    # --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.