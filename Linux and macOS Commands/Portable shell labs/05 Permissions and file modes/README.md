# Permissions and file modes

Create three local files and inspect their permission bits through a platform-aware stat command.

A mode comprises owner, group and other permissions. The first digit in this exercise describes owner access. GNU stat and the BSD stat shipped with macOS use different format options, so the example selects the documented form.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[example.sh](example.sh)

## Run the shell script

The Python driver gives each installed shell its own empty working directory. Each run must agree with the independently specified fixture.

## Inspect the outcome

Mode labels are encoded as octal digits and should not be interpreted as a linear access scale. The figure shows the effective read, write and execute bits.

## Recorded output

```text
sh [600, 640, 644]
bash [600, 640, 644]
zsh [600, 640, 644]
```

## Interpreting the result

Mode labels are encoded as octal digits and should not be interpreted as a linear access scale. The figure shows the effective read, write and execute bits.

![Permissions and file modes, worked result](figure.svg)

## Exercise

Set 660 on one file. Identify which class has gained write access.

## References

[The Open Group, POSIX shell command language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)

[GNU Bash reference manual](https://www.gnu.org/software/bash/manual/bash.html)

[Apple Terminal User Guide](https://support.apple.com/guide/terminal/welcome-trml2df0220c/mac)
