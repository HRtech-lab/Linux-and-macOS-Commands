# Linux and macOS Commands

Start with the [portable shell labs](Portable%20shell%20labs/README.md) for hands-on exercises or open the command catalogue for a particular platform. The tables contain 180 command entries, including platform variants. Local inventories extend the catalogue to whatever programs and shell definitions are installed on your own machine.

| Collection | Topics |
|---|---|
| [Shared Unix](Shared%20Unix/README.md) | Paths, files, streams, tables, archives, shell state, processes and manuals |
| [Linux](Linux/README.md) | GNU utilities, storage, systemd, package managers and system information |
| [macOS](macOS/README.md) | BSD variants, Spotlight, property lists, desktop tools, power and developer utilities |
| [Portable shell labs](Portable%20shell%20labs/README.md) | Eight worked examples with shell source, Python checks, notebooks and figures |
| [Command inventory](Command%20inventory/README.md) | List local executables, builtins, functions and aliases |

## Why a command behaves differently on two machines

A shell parses quotes, expands names and starts programs. The executable chosen from PATH supplies its own options. On macOS the default stat has BSD-style format options. GNU stat on Linux accepts a different option for the same information. The permissions lab selects the appropriate implementation explicitly. When checking an unfamiliar command, use the local manual, the command inventory and the platform-specific catalogue together.

![Permissions and file modes](Portable%20shell%20labs/05%20Permissions%20and%20file%20modes/figure.svg)

## Running the examples

Use Python 3 with Matplotlib, NumPy and Jupyter. In any lab, run `python lesson.py` or open the notebook. To run a shell listing directly, copy it into an empty temporary directory and run `sh example.sh` there. Several examples create, change or remove their own named fixture files. The notebook outputs were recorded on Linux. All eight scripts also passed the [Linux and macOS checks](https://github.com/HRtech-lab/Linux-and-macOS-Commands/actions/runs/45726914354). The macOS catalogue links the platform manuals for its native utilities.

[POSIX utility index](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [Apple Terminal guide](https://support.apple.com/guide/terminal/welcome-trml2df0220c/mac) · [MIT licence](../LICENSE)
