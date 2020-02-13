from source.board_generator import BoardGenerator


def test():
    gen = BoardGenerator(5, 3)
    board = gen.generate_board()
    print(board)
    assert len(board) == 3
    assert len(board[0]) == 5
