import random
from string import ascii_lowercase

from source.board import Board


class BoardGenerator:

    def __init__(self, width: int, height: int):
        self.cols = width
        self.rows = height

    def generate_board(self) -> Board:
        """Generates the board of random letters for columns and rows.
        One row is a string of random letters. Each letter is a column.
        """
        board = []
        for row in range(self.rows):
            board.append(self._get_random_letters())
        return Board(board)

    def _get_random_letters(self) -> str:
        """Returns a string of random letters.
        Size of the string is columns of the board.
        """
        return "".join(random.choices(ascii_lowercase, k=self.cols))
