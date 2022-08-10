from tddapp import tree
import subprocess
import pytest

source = "."


def test_calls_tree(mocker):
    """
    calling tree utility
    """
    mocker.patch("subprocess.Popen")
    assert tree.read(source)
    subprocess.Popen.assert_called_with(["tree", "."], stdout=subprocess.PIPE)


def test_calls_tree_missing(mocker):
    """
    calling with missing tree utility
    """
    mocker.patch("subprocess.Popen", side_effect=OSError("No such file or directory"))
    with pytest.raises(SystemExit):
        tree.read(source)
    subprocess.Popen.assert_called_with(["tree", "."], stdout=subprocess.PIPE)
