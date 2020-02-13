from source.board import Board


board = Board(["xxtestxx", "xxsomexx", "xxwordsxx"])


def test_positive():
    assert board.contains_word("test")
    assert board.contains_word("some")
    assert board.contains_word("words")


def test_reversed():
    assert board.contains_word("tset")
    assert board.contains_word("emos")
    assert board.contains_word("sdrow")


def test_bt_cols():
    assert board.contains_word("tsw")
    assert board.contains_word("xxx")
    assert board.contains_word("ooe")


def test_negative():
    assert not board.contains_word("vevrvrb")
    assert not board.contains_word(" ")
    assert not board.contains_word("TEST")
