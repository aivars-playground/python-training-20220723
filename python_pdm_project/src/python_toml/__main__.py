from argparse import ArgumentParser
from .a_module import main_function, call_b_module


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("name", help="name", default="UNKNOWN", nargs="?")
    return parser


def main():
    args = create_parser().parse_args()
    print(f"Hello, {args.name}")
    main_function()
    call_b_module()
