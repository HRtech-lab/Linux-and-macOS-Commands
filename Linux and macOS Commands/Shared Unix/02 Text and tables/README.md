# Text and tables

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `cat` | `cat report.txt` | Copy file contents to standard output. |
| `head` | `head -n 5 report.txt` | Read the first five lines. |
| `tail` | `tail -n 5 report.txt` | Read the final five lines. |
| `wc` | `wc -l report.txt` | Count newline characters. |
| `cut` | `cut -f 2 table.tsv` | Select the second tab-separated field. |
| `paste` | `paste names.txt values.txt` | Place corresponding lines side by side. |
| `sort` | `LC_ALL=C sort names.txt` | Sort records in a specified collation. |
| `uniq` | `uniq -c sorted.txt` | Count adjacent runs of equal lines. |
| `tr` | `tr '[:lower:]' '[:upper:]' < names.txt` | Map lowercase letters to uppercase in the selected locale. |
| `grep` | `grep -n 'sample' notes.txt` | Print matching lines with line numbers. |
| `sed` | `sed -n '2,4p' notes.txt` | Print a range without editing the original. |
| `awk` | `awk 'NR > 1 {print $1}' table.txt` | Print a field from each data row. |
| `join` | `join sorted-a.txt sorted-b.txt` | Match records by a common sorted key. |
| `comm` | `comm -12 sorted-a.txt sorted-b.txt` | Show common lines of two sorted inputs. |
| `diff` | `diff -u old.txt new.txt` | Compare text revisions. |
| `cmp` | `cmp copy-a copy-b` | Compare files byte for byte. |
| `nl` | `nl -b a notes.txt` | Number all lines, including blank lines. |
| `fold` | `fold -w 72 notes.txt` | Wrap lines to a fixed width. |
| `expand` | `expand -t 4 notes.txt` | Expand tabs into spaces. |
| `unexpand` | `unexpand -a notes.txt` | Convert suitable blanks into tab stops. |
| `od` | `od -An -tx1 example.txt` | Display hexadecimal byte values. |
| `tee` | `printf 'sample\n' \| tee copy.txt` | Write a stream to a file and standard output. |
| `xargs` | `printf 'one\ntwo\n' \| xargs -n 1 echo` | Build one invocation per simple input token. |
| `fmt` | `fmt -w 72 notes.txt` | Reflow prose to a target width. |
| `strings` | `strings fixture.bin` | Display printable sequences from a local file. |
| `cksum` | `cksum example.txt` | Report the POSIX checksum and byte count. |

[POSIX utility index](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
