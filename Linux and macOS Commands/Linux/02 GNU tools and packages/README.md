# GNU tools and package inventories

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `sha256sum` | `sha256sum notes.txt` | Calculate a SHA-256 file digest with GNU Coreutils. |
| `readlink` | `readlink -f .` | Resolve symbolic links and canonicalise the path. |
| `stat` | `stat -c '%a %s' notes.txt` | Print the numeric mode and size with GNU stat. |
| `date` | `date -u -d '2026-11-01 + 1 day' '+%F'` | Perform calendar arithmetic with GNU date. |
| `du` | `du -h --max-depth=1 .` | Summarise immediate directory sizes. |
| `sort` | `sort -V versions.txt` | Use GNU version sorting for labels. |
| `timeout` | `timeout 3s sleep 1` | Limit the duration of a child process. |
| `numfmt` | `numfmt --to=iec 1048576` | Display a byte count in IEC-style units. |
| `seq` | `seq 1 5` | Print integer values across a range. |
| `tac` | `tac notes.txt` | Print lines in reverse order. |
| `shuf` | `shuf -n 2 notes.txt` | Sample two lines without replacement. |
| `factor` | `factor 84` | Print the prime factors of an integer. |
| `rev` | `rev notes.txt` | Reverse the characters on each input line. |
| `dpkg-query` | `dpkg-query -W bash` | Inspect an installed Debian-family package. |
| `apt-cache` | `apt-cache policy bash` | Inspect Debian-family package version candidates. |
| `rpm` | `rpm -q bash` | Query a local RPM package database. |
| `dnf` | `dnf list --installed bash` | List an installed package on a DNF system. |
| `pacman` | `pacman -Q bash` | Query an Arch package database. |
| `zypper` | `zypper search -i bash` | Search installed packages on openSUSE. |
| `snap` | `snap list` | List locally installed snaps where the service exists. |
| `flatpak` | `flatpak list --app` | List installed Flatpak applications. |

[Linux man-pages](https://man7.org/linux/man-pages/) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [systemd manuals](https://www.freedesktop.org/software/systemd/man/latest/)
