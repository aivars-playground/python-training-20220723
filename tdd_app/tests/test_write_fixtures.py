import tempfile
import pytest
from tddapp import writer


@pytest.fixture
def infile_for_test():
    f = tempfile.TemporaryFile()
    f.write(b"Test")  # write bytes object
    f.seek(0)
    return f


def test_write_to_file(infile_for_test):
    """
    Writes content of one file-like (everything is a file) to another
    """

    outfile_to_test = tempfile.NamedTemporaryFile(delete=False)
    writer.local(infile_for_test, outfile_to_test)

    with open(outfile_to_test.name, "rb") as outfile:
        assert outfile.read() == b"Test"


def test_write_to_s3(mocker, infile_for_test):
    """
    Writes content of one file-like to s3 bucket
    """

    client = mocker.Mock()

    writer.s3(client, infile_for_test, "bucket-name", "file-name")

    client.upload_fileobj.assert_called_with(
        infile_for_test, "bucket-name", "file-name"
    )
