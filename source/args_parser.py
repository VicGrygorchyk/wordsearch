import argparse


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-", "--version", help="show program version", action="store_true")
    return parser.parse_args()
