import pytest


@pytest.fixture
def parser_to_test():
    from tddapp import cli

    return cli.create_parser()


def test_app_without_params(parser_to_test):
    """
    Without parameters app will exit
    """
    with pytest.raises(SystemExit):
        parser_to_test.parse_args()


def test_app_with_source_file_no_filename(parser_to_test):
    """
    With source and target file (without location)
    """
    with pytest.raises(SystemExit):
        parser_to_test.parse_args([".", "--target"])


def test_app_with_source_no_target(parser_to_test):
    """
    With source and default target
    """
    args = parser_to_test.parse_args(["."])
    assert args.source == "."
    assert args.target == None


def test_app_with_source_and_file_target(parser_to_test):
    """
    With source and default target
    """
    args = parser_to_test.parse_args([".", "--target", ".ignoreme/out.csv"])
    assert args.source == "."
    assert args.target == ".ignoreme/out.csv"
