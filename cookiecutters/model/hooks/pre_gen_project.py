import os
import sys


def check_if_manage_py_exists():
    if not os.path.exists("../manage.py"):
        print("Current directory:", os.getcwd())
        print("ERROR: The command should be executed at project root dir.")
        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == '__main__':
    check_if_manage_py_exists()
