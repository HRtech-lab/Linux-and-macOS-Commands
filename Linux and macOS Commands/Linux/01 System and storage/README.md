# Linux system and storage

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `lsblk` | `lsblk -o NAME,SIZE,TYPE` | List block devices and types. |
| `findmnt` | `findmnt -T .` | Identify the mount covering the current directory. |
| `mountpoint` | `mountpoint /` | Test whether a path is a mount point. |
| `lsmem` | `lsmem` | Summarise memory block ranges. |
| `lscpu` | `lscpu` | Inspect CPU architecture and topology. |
| `free` | `free -h` | Display used and available memory. |
| `uptime` | `uptime -p` | Report time since boot in a readable form. |
| `nproc` | `nproc` | Count processing units available to the current process. |
| `lsns` | `lsns` | List namespaces visible to the current user. |
| `lsipc` | `lsipc` | Display system IPC facilities visible locally. |
| `lslocks` | `lslocks` | List current local file locks. |
| `namei` | `namei -l /tmp` | Examine the components of a pathname. |
| `getent` | `getent group users` | Query a named entry in the configured account databases. |
| `systemctl` | `systemctl list-timers` | Inspect scheduled timers on a systemd host. |
| `journalctl` | `journalctl -b -n 10` | Read the ten newest visible records from this boot. |
| `hostnamectl` | `hostnamectl status` | Show local host metadata where systemd provides it. |
| `timedatectl` | `timedatectl status` | Show local time and synchronisation settings. |
| `loginctl` | `loginctl list-sessions` | List visible local login sessions. |
| `lsmod` | `lsmod` | List loaded kernel modules when the kmod utility is installed. |

[Linux man-pages](https://man7.org/linux/man-pages/) · [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [systemd manuals](https://www.freedesktop.org/software/systemd/man/latest/)
