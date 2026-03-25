import pytest
from dice import Dice


class FakeRng:
    def __init__(self, values):
        self._values = values
        self._index = 0

    def randint(self, a, b):
        value = self._values[self._index]
        self._index += 1
        return value


def test_roll_returns_injected_values():
    dice = Dice(rng=FakeRng([2, 5, 6]))
    assert dice.roll() == 2
    assert dice.roll() == 5
    assert dice.roll() == 6


def test_invalid_sides_raises_error():
    with pytest.raises(ValueError):
        Dice(sides=1)