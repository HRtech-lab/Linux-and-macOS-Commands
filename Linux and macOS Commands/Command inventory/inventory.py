"""List executable files visible on the current PATH. The first directory wins."""

import argparse
import csv
import os
from pathlib import Path
import sys


def executables(path_value):
    found = {}
    for entry in path_value.split(os.pathsep):
        directory = Path(entry or ".")
        try:
            for candidate in directory.iterdir():
                if (
                    candidate.name not in found
                    and candidate.is_file()
                    and os.access(candidate, os.X_OK)
                ):
                    found[candidate.name] = str(candidate.absolute())
        except (FileNotFoundError, NotADirectoryError, PermissionError):
            continue
    return sorted(found.items())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--paths",
        action="store_true",
        help="Include the first matching executable path as CSV",
    )
    args = parser.parse_args()
    rows = executables(os.environ.get("PATH", os.defpath))
    if args.paths:
        writer = csv.writer(sys.stdout)
        writer.writerow(("command", "path"))
        writer.writerows(rows)
    else:
        for name, _ in rows:
            print(name)
