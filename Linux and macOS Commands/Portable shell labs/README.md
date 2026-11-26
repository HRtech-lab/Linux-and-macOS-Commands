# Portable shell labs

Run each example in an empty temporary directory. The companion Python script creates one for each installed shell, captures the real exit status and output, and compares the results with known fixture values. The recorded examples ran with sh, Bash and zsh on Linux. A separate [hosted verification](https://github.com/HRtech-lab/HRtech-lab-Shell_Commands_for_Computational_biology_Bioinformatics/actions/runs/45726914354) ran all eight fixtures on Linux and macOS, including the BSD stat branch on macOS.

## Worked lectures

| Lecture | Question or experiment |
|---|---|
| [01. Quoting paths and expanding globs](01%20Quoting%20paths%20and%20expanding%20globs/README.md) | Count bytes in three files whose names contain spaces. |
| [02. Pipelines and grouped counts](02%20Pipelines%20and%20grouped%20counts/README.md) | Count repeated labels with a portable text-processing pipeline. |
| [03. Joining two tables](03%20Joining%20two%20tables/README.md) | Join a key-value table to a small lookup table and retain one row per matching key. |
| [04. Streams and gzip round trips](04%20Streams%20and%20gzip%20round%20trips/README.md) | Check that compression followed by decompression recovers the exact original bytes. |
| [05. Permissions and file modes](05%20Permissions%20and%20file%20modes/README.md) | Create three local files and inspect their permission bits through a platform-aware stat command. |
| [06. Finding files by type and suffix](06%20Finding%20files%20by%20type%20and%20suffix/README.md) | Compare matching file counts across two branches of a temporary directory tree. |
| [07. Archives and verified extraction](07%20Archives%20and%20verified%20extraction/README.md) | Archive two known files, restore into a new temporary destination and check the restored bytes. |
| [08. Exit status and conditional execution](08%20Exit%20status%20and%20conditional%20execution/README.md) | Observe matching, nonmatching and missing input through grep exit codes. |

[POSIX shell specification](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
