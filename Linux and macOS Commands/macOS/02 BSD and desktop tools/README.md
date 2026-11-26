# BSD and desktop tools on macOS

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `stat` | `stat -f '%Lp %z' notes.txt` | Print numeric permissions and file size with BSD stat. |
| `date` | `date -u -j -f '%Y-%m-%d' '2026-11-01' '+%A'` | Parse and format a date without changing the clock. |
| `du` | `du -hd 1 .` | Show a one-level directory summary with BSD du. |
| `shasum` | `shasum -a 256 notes.txt` | Calculate a SHA-256 digest with the Perl shasum frontend. |
| `ditto` | `ditto fixture-copy destination-copy` | Copy a known teaching directory to a new destination. |
| `open` | `open .` | Open the current directory in Finder. |
| `pbcopy` | `printf %s sample \| pbcopy` | Replace clipboard contents with a short fixture string. |
| `pbpaste` | `pbpaste` | Write the current clipboard to standard output. |
| `sips` | `sips -g pixelWidth -g pixelHeight image.png` | Read image dimensions. |
| `textutil` | `textutil -info notes.rtf` | Inspect local text document metadata. |
| `qlmanage` | `qlmanage -h` | Show options for the Quick Look tool. |
| `osascript` | `osascript -e 'return 2 + 3'` | Evaluate a local AppleScript expression. |
| `afinfo` | `afinfo sample.wav` | Display audio file information. |
| `afplay` | `afplay sample.wav` | Play a local audio fixture. |
| `caffeinate` | `caffeinate -t 3` | Hold a short assertion against idle sleep. |
| `hdiutil` | `hdiutil imageinfo example.dmg` | Inspect a local disk image. |
| `xattr` | `xattr notes.txt` | List extended attribute names on a file. |
| `codesign` | `codesign --display --verbose=2 /bin/ls` | Display signing metadata for a local binary. |
| `lipo` | `lipo -archs /bin/ls` | List architecture slices when Apple tools are installed. |
| `otool` | `otool -L /bin/ls` | List dynamic library dependencies when installed. |

[Apple Terminal User Guide](https://support.apple.com/guide/terminal/welcome-trml2df0220c/mac) · [Apple shell scripting primer](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/Introduction/Introduction.html) · [macOS manual page index](https://keith.github.io/xcode-man-pages/)
