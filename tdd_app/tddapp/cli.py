from argparse import ArgumentParser
from sys import stdout
import boto3


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("source", help="source folder")
    parser.add_argument("--target", help="target file")
    return parser


def main():
    from tddapp import writer, tree
    from urllib.parse import urlparse

    args = create_parser().parse_args()

    proc = tree.read(args.source)

    target = urlparse(args.target)
    if target.scheme == "s3":
        client = boto3.client("s3")
        print(target.path)
        writer.s3(client, proc.stdout, target.netloc, target.path.strip("/"))
    elif target.scheme == "file":
        out_file = open(target.netloc + target.path, "wb")
        writer.local(proc.stdout, out_file)
    else:
        stdout.buffer.write(proc.stdout.read())


if __name__ == "__main__":
    main()
