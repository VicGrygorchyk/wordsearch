"""This app generates a board of random letters.
Identifies all valid words (contained in the attached word list) in the board.
Displays results to the user.

"""
import numpy as np

from global_const import DATA_PATH
from source import args_parser
from source.board_generator import BoardGenerator


def get_doc_file_to_np():
    """Open the file with words from data/
    And store each words to numpy arr.
    """
    arr = []
    with open(DATA_PATH, "r+") as doc:
        lines = doc.readlines()
        for line in lines:
            arr.append(line)

    np_arr = np.array(arr, dtype=np.str)
    return np_arr


def run_main():
    # get width and height of the board
    width, height = args_parser.parse_args()
    # generate a board
    generator = BoardGenerator(width=width, height=height)
    board = generator.generate_board()
    # open the doc file
    words_arr = get_doc_file_to_np()

    # find all possible words from the doc
    for word in words_arr:
        word_ = board.contains_word(word)
        if word_:
            print(word_)


if __name__ == "__main__":
    run_main()
