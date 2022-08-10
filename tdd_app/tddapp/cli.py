from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("source", help="source folder")
    parser.add_argument("--target", help="target file")
    return parser
