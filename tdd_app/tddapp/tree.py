import subprocess
import sys


def read(source):
    try:
        return subprocess.Popen(["tree", source], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Err:{err}")
        sys.exit(1)
