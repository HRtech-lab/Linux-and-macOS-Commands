"""Permissions and file modes

Create three local files and inspect their permission bits through a platform-aware stat command.

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
    expected = [600, 640, 644]
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

    labels = ["owner only", "group read", "others read"]
    bits = np.array(
        [
            [int(int(str(mode), 8) & (1 << bit) != 0) for bit in reversed(range(9))]
            for mode in observed
        ]
    )
    fig, ax = plt.subplots(figsize=(6.4, 2.9), constrained_layout=True)
    ax.imshow(bits, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set(
        xticks=range(9),
        xticklabels=list("rwxrwxrwx"),
        yticks=range(3),
        yticklabels=labels,
        xlabel="Owner, group and other permission bits",
    )
    plt.show()


if __name__ == "__main__":
    main()
