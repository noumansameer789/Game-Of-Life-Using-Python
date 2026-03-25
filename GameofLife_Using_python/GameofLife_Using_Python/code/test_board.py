from board import Board


def test_board_size_is_20():
    board = Board()
    assert board.size() == 20


def test_start_tile():
    board = Board()
    tile = board.get_tile(0)
    assert tile.name == "Start"
    assert tile.tile_type == "START"


def test_end_tile_is_retirement():
    board = Board()
    tile = board.get_tile(board.final_position())
    assert tile.tile_type == "RETIRE"


def test_is_end_detection():
    board = Board()
    assert board.is_end(board.final_position()) is True
    assert board.is_end(board.final_position() - 1) is False
