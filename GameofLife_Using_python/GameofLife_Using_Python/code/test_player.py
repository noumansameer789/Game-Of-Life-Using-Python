import pytest
from player import Player


def test_player_requires_nonempty_name():
    with pytest.raises(ValueError):
        Player("   ")


def test_player_initial_values():
    p = Player("Ayesha", starting_cash=100)
    assert p.name == "Ayesha"
    assert p.cash == 100
    assert p.position == 0
    assert p.is_retired is False


def test_move_to_updates_position():
    p = Player("Sam")
    p.move_to(5)
    assert p.position == 5


def test_move_to_rejects_negative_position():
    p = Player("Sam")
    with pytest.raises(ValueError):
        p.move_to(-1)


def test_move_by_moves_forward():
    p = Player("Sam", start_position=2)
    p.move_by(3, final_position=10)
    assert p.position == 5


def test_move_by_clamps_to_final_position():
    p = Player("Sam", start_position=8)
    p.move_by(5, final_position=10)
    assert p.position == 10


def test_apply_cash_changes_balance():
    p = Player("Sam", starting_cash=10)
    p.apply_cash(5)
    assert p.cash == 15
    p.apply_cash(-20)
    assert p.cash == -5


def test_retire_sets_flag():
    p = Player("Sam")
    p.retire()
    assert p.is_retired is True


def test_summary_format():
    p = Player("Sam", starting_cash=50)
    p.move_to(3)
    text = p.summary()
    assert "Sam" in text
    assert "pos=3" in text
    assert "cash=50" in text
    assert "ACTIVE" in text
