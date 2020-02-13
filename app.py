"""This app generates a board of random letters.
Identifies all valid words (contained in the attached word list) in the board.
Displays results to the user.

"""
from source import args_parser


def run_main():
    width, height = args_parser.parse_args()


if __name__ == "__main__":
    run_main()
