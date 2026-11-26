# Archives, identity and manuals

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `tar` | `tar -tf example.tar` | List archive members. |
| `gzip` | `gzip -c < notes.txt > notes.gz` | Compress to a separate destination. |
| `gunzip` | `gunzip -c notes.gz` | Write decompressed bytes to standard output. |
| `bzip2` | `bzip2 -c < notes.txt > notes.bz2` | Produce a bzip2 stream when installed. |
| `unzip` | `unzip -l example.zip` | List a ZIP archive. |
| `zip` | `zip example.zip notes.txt` | Create or update a ZIP archive from the named file. |
| `chmod` | `chmod 640 example.txt` | Set permissions on a file you own. |
| `id` | `id -u` | Print the effective numeric user ID. |
| `groups` | `groups` | List group memberships for the current account. |
| `whoami` | `whoami` | Print the effective account name. |
| `who` | `who` | List current login records where available. |
| `uname` | `uname -s` | Print the operating-system kernel name. |
| `hostname` | `hostname` | Read the local hostname. |
| `date` | `date -u '+%Y-%m-%d'` | Print the date in UTC. |
| `cal` | `cal 11 2026` | Show a calendar if the utility is installed. |
| `locale` | `locale charmap` | Report the current character encoding. |
| `iconv` | `iconv -f UTF-8 -t UTF-8 notes.txt` | Validate a text encoding during conversion. |
| `getconf` | `getconf LONG_BIT` | Read the supported long-integer width. |
| `man` | `man sort` | Open the locally installed manual for a command. |
| `apropos` | `apropos calendar` | Search manual descriptions. |
| `whatis` | `whatis awk` | Show a short manual description. |
| `tput` | `tput cols` | Report the terminal width via its capability database. |
| `stty` | `stty size` | Ask the current terminal for its rows and columns. |
| `which` | `which awk` | Show executable lookup information. Shell resolution is available with command -v. |

[POSIX utility index](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
