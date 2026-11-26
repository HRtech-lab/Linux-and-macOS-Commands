"""Pipelines and grouped counts

Count repeated labels with a portable text-processing pipeline.

The Open Group, POSIX shell command language
https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html
GNU Bash reference manual
https://www.gnu.org/software/bash/manual/bash.html
Apple Terminal User Guide
https://support.apple.com/guide/terminal/welcome-trml2df0220c/mac"""

from pathlib import Path
import shutil, subprocess, tempfile
import matplotlib.pyplot as plt
import numpy as np

here = Path(__file__).resolve().parent


def main():
    expected = [3, 1, 2]
    shells = [name for name in ("sh", "bash", "zsh") if shutil.which(name)]
    runs = {}
    for shell in shells:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [shell, str(here / "example.sh")],
                cwd=directory,
                check=True,
                capture_output=True,
                text=True,
            )
        numbers = [int(v) for v in result.stdout.split()]
        runs[shell] = numbers
        print(shell, numbers)
        assert numbers == expected
    observed = runs[shells[0]]

    fig, ax = plt.subplots(figsize=(5.8, 2.9), constrained_layout=True)
    ax.bar(["apple", "pear", "plum"], observed, color="#357a80")
    ax.set(ylabel="Records")
    plt.show()


if __name__ == "__main__":
    main()
