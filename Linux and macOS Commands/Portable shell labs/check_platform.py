"""Run the eight practice scripts on the current platform using real shell processes."""

from pathlib import Path
from tempfile import TemporaryDirectory
import os
import shutil
import subprocess


def main():
    root = Path(__file__).resolve().parent
    cases = [
        [5, 4, 2],
        [3, 1, 2],
        [3, 10, 28],
        [500, 500],
        [600, 640, 644],
        [2, 1],
        [3, 6],
        [0, 1, 2],
    ]
    scripts = sorted(root.glob("*/example.sh"))
    assert len(scripts) == len(cases)
    for index, (script, expected) in enumerate(zip(scripts, cases)):
        for shell in ("sh", "bash", "zsh"):
            if not shutil.which(shell):
                continue
            with TemporaryDirectory() as where:
                out = subprocess.run(
                    [shell, str(script)],
                    cwd=where,
                    check=True,
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
            values = list(map(int, out.stdout.split()))
            good = (
                values[:2] == [0, 1] and len(values) == 3 and values[2] > 1
                if index == 7
                else values == expected
            )
            if not good:
                raise AssertionError((script.name, shell, values, expected))
            print(os.uname().sysname, shell, script.parent.name, values)


if __name__ == "__main__":
    main()
