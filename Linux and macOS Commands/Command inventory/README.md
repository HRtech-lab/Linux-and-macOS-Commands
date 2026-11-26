# Inventory the installed commands

A manual describes a particular system release. Your session also sees installed applications, package-manager tools, shell builtins, functions and aliases. Search an inventory from the same host and shell in which you intend to use the command.

```sh
python3 inventory.py
python3 inventory.py --paths > commands.csv
```

The Python script lists executable files in the current PATH. Where several directories supply the same name it retains the first. The CSV variant includes the resolved search location. It does not run the commands.

For shell-specific names, source the appropriate file in the interactive session whose definitions you want to inspect. Use `type name` in Bash or `whence -v name` in zsh to see how a particular name resolves. Running a new non-interactive shell can omit aliases and functions from the current one.

```bash
source session.bash
visible_commands
```

```zsh
source session.zsh
visible_commands
```

[GNU Bash builtins](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html) · [zsh parameters](https://zsh.sourceforge.io/Doc/Release/Parameters.html)
