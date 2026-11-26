# Shell and processes

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `sh` | `sh example.sh` | Interpret a POSIX shell script. |
| `bash` | `bash --version` | Identify the available Bash release. |
| `zsh` | `zsh --version` | Identify the available Z shell release. |
| `command` | `command -v awk` | Ask the current shell how it resolves a name. |
| `type` | `type cd` | Describe a name in the current shell. |
| `alias` | `alias` | Display aliases from the current shell session. |
| `unalias` | `unalias demo` | Remove a session alias named demo. |
| `set` | `set -- one two` | Replace the current positional parameters. |
| `shift` | `shift` | Discard the first positional argument. |
| `export` | `export LC_ALL=C` | Set and export a locale for child processes. |
| `unset` | `unset OPTION_DEMO` | Remove a named shell variable. |
| `read` | `IFS= read -r line < notes.txt` | Read one line while preserving backslashes. |
| `printf` | `printf '%s\n' sample` | Print using an explicit format. |
| `test` | `test -f notes.txt` | Check whether a path names a regular file. |
| `true` | `true` | Return a successful exit status. |
| `false` | `false` | Return a nonzero exit status. |
| `trap` | `trap -p` | Show traps in Bash or zsh. The POSIX display form is trap with no options. |
| `eval` | `eval 'value=3'` | Evaluate a fixed literal as shell syntax. |
| `umask` | `umask` | Show the default file-creation mask. |
| `env` | `env LC_ALL=C date` | Run a command with a specified environment value. |
| `printenv` | `printenv LANG` | Read one named environment variable. |
| `ps` | `ps -p $$ -o pid=,comm=` | Show the current shell process. |
| `jobs` | `jobs` | List jobs known to the interactive shell. |
| `wait` | `wait` | Wait for the shell's active child jobs. |
| `sleep` | `sleep 1` | Wait for one second. |
| `time` | `time sh -c 'true'` | Measure a local command's elapsed and CPU time. |
| `nice` | `nice -n 5 sh -c 'true'` | Run a child at an adjusted scheduling priority. |
| `nohup` | `nohup sh -c 'printf done' > status.txt` | Let a short fixture process ignore hangups. |
| `getopts` | `getopts 'ab:' option` | Parse a shell option from positional arguments. |
| `ulimit` | `ulimit -n` | Show the process limit for open file descriptors. |

[POSIX utility index](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
