from source.board_generator import BoardGenerator


def test():
    gen = BoardGenerator(5, 3)
    board = gen.generate_board()
    assert board.table.shape == (3, 5)
