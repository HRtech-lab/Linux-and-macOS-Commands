# Navigation and files

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `pwd` | `pwd -P` | Print the physical working directory. |
| `cd` | `cd ..` | Move to the parent directory in the current shell. |
| `ls` | `ls -la .` | List entries, including hidden files, with metadata. |
| `mkdir` | `mkdir -p work/tables` | Create required directories and parents. |
| `rmdir` | `rmdir empty-dir` | Remove a named empty directory. |
| `touch` | `touch example.txt` | Create an empty file or update timestamps. |
| `cp` | `cp input.txt copy.txt` | Copy bytes to a new destination. |
| `mv` | `mv draft.txt final.txt` | Move or rename a known file. |
| `rm` | `rm -i draft-copy.txt` | Request confirmation before removing the named fixture. |
| `ln` | `ln -s report.txt latest.txt` | Create a symbolic link to a named target. |
| `readlink` | `readlink latest.txt` | Read the target stored in a symbolic link. |
| `basename` | `basename /tmp/notes.txt .txt` | Extract the last component and trim the given suffix. |
| `dirname` | `dirname /tmp/notes.txt` | Remove the final path component. |
| `find` | `find . -type f -name '*.csv'` | Select regular files matching a filename pattern. |
| `file` | `file example.txt` | Classify a file from its content or filesystem type. |
| `du` | `du -sk .` | Summarise disk usage in KiB. |
| `df` | `df -k .` | Report filesystem capacity for the current directory. |
| `mktemp` | `mktemp -d` | Create a fresh temporary directory. |
| `realpath` | `realpath .` | Resolve a pathname where this utility is installed. |
| `stat` | `stat example.txt` | Display file status. Formatted output options differ by platform. |

[POSIX utility index](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
