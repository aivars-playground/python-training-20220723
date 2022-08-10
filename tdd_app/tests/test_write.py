import tempfile
from tddapp import writer


def test_write_to_file():
    """
    Writes content of one file (everything is a file) to another
    """
    infile_for_test = tempfile.TemporaryFile()
    infile_for_test.write(b"Test")  # write bytes object
    infile_for_test.seek(0)

    outfile_to_test = tempfile.NamedTemporaryFile(delete=False)
    writer.local(infile_for_test, outfile_to_test)
    with open(outfile_to_test.name, "rb") as outfile:
        assert outfile.read() == b"Test"
