import pytest
from board import Board
from dice import Dice
from game import Game
from player import Player
from turn_handler import TurnHandler


class FixedDice:
    def __init__(self, value: int) -> None:
        self._value = value

    def roll(self) -> int:
        return self._value


def test_play_turn_moves_player_and_applies_tile_cash_effect():
    board = Board()
    player = Player("Ayesha", starting_cash=0, start_position=0)

    handler = TurnHandler()
    events = handler.play_turn(player, board, FixedDice(1))

    assert player.position == 1
    assert player.cash == -50
    assert any("rolled" in e for e in events)
    assert any("Cash changed" in e for e in events)


def test_play_turn_retires_player_on_retire_tile():
    board = Board()
    player = Player("Ayesha", starting_cash=0, start_position=18)

    handler = TurnHandler()
    handler.play_turn(player, board, FixedDice(6))

    assert player.position == board.final_position()
    assert player.is_retired is True


def test_game_setup_players_creates_players():
    game = Game(Board(), FixedDice(1), TurnHandler())
    game.setup_players(2, ["A", "B"], starting_cash=10)
    assert len(game.players) == 2
    assert game.players[0].cash == 10


def test_game_is_over_when_all_retired():
    game = Game(Board(), FixedDice(1), TurnHandler())
    game.setup_players(2, ["A", "B"])
    for p in game.players:
        p.retire()
    assert game.is_over() is True


def test_determine_winner_by_highest_cash():
    game = Game(Board(), FixedDice(1), TurnHandler())
    game.setup_players(2, ["A", "B"])
    game.players[0].apply_cash(50)
    game.players[1].apply_cash(10)
    assert game.determine_winner().name == "A"



import pytest

def test_setup_players_rejects_duplicate_names():
    game = Game(Board(), FixedDice(1), TurnHandler())
    with pytest.raises(ValueError):
        game.setup_players(2, ["A", "A"])
        
        
        
        
def test_summary_text_contains_player_names():
    game = Game(Board(), FixedDice(1), TurnHandler())
    game.setup_players(2, ["Sam", "Ayesha"], starting_cash=0)
    text = game.summary_text()
    assert "Sam" in text
    assert "Ayesha" in text
    assert "Position" in text
    assert "Cash" in text
    
    
def test_setup_players_invalid_player_count():
    game = Game(Board(), Dice(), TurnHandler())

    with pytest.raises(ValueError):
        game.setup_players(1, ["A"])

    with pytest.raises(ValueError):
        game.setup_players(5, ["A", "B", "C", "D", "E"])


def test_setup_players_duplicate_names_case_insensitive():
    game = Game(Board(), Dice(), TurnHandler())

    with pytest.raises(ValueError):
        game.setup_players(2, ["Sam", "sam"])


def test_is_over_only_when_all_retired():
    game = Game(Board(), Dice(), TurnHandler())
    game.setup_players(2, ["A", "B"])

    assert game.is_over() is False

    game.players[0].retire()
    assert game.is_over() is False

    game.players[1].retire()
    assert game.is_over() is True