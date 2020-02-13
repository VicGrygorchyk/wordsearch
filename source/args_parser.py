import argparse


def parse_args() -> (int, int):
    """Parse provided args for the board's width and height.
    Width and height should be int and both are required.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", "--width", help="Provide the board's width.", type=int, required=True)
    parser.add_argument("-H", "--height", help="Provide the board's height.", type=int, required=True)
    results = parser.parse_args()
    return results.width, results.height
