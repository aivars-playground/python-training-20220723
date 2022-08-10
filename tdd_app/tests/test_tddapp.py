import pytest
from tddapp import cli


def test_app_without_params():
    """
    Without parameters app will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args()


def test_app_with_source_file_no_filename():
    """
    With source and target file (without location)
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([".", "--target"])


def test_app_with_source_no_target():
    """
    With source and default target
    """
    parser = cli.create_parser()
    args = parser.parse_args(["."])
    assert args.source == "."
    assert args.target == None


def test_app_with_source_and_file_target():
    """
    With source and default target
    """
    parser = cli.create_parser()
    args = parser.parse_args([".", "--target", ".ignoreme/out.csv"])
    assert args.source == "."
    assert args.target == ".ignoreme/out.csv"
