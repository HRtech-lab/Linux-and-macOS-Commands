# macOS system and metadata

Examples name small local fixture files. Use the installed manual for flags, available utilities and version-specific behaviour.

| Command | Example | Purpose |
|---|---|---|
| `sw_vers` | `sw_vers` | Show the macOS product version and build. |
| `system_profiler` | `system_profiler SPSoftwareDataType` | Read the local software overview. |
| `sysctl` | `sysctl -n hw.memsize` | Read physical memory in bytes on macOS. |
| `diskutil` | `diskutil info /` | Inspect the volume containing the root filesystem. |
| `mdls` | `mdls -name kMDItemFSSize notes.txt` | Read a selected Spotlight metadata attribute. |
| `mdfind` | `mdfind -onlyin . 'kMDItemFSName == "*.txt"'` | Search the indexed local scope for matching filenames. |
| `plutil` | `plutil -lint settings.plist` | Validate the syntax of a property list. |
| `defaults` | `defaults read -g AppleLocale` | Read the global locale preference if present. |
| `scutil` | `scutil --get ComputerName` | Read the configured display name. |
| `networksetup` | `networksetup -listallhardwareports` | List local hardware port names. |
| `pmset` | `pmset -g batt` | Read the battery and power-source summary. |
| `ioreg` | `ioreg -l -c AppleSmartBattery` | Inspect available local battery registry properties. |
| `vm_stat` | `vm_stat` | Show virtual-memory page statistics. |
| `csrutil` | `csrutil status` | Read the local System Integrity Protection status. |
| `tmutil` | `tmutil status` | Show the current Time Machine activity. |
| `launchctl` | `launchctl print-disabled system` | Read disabled launch-service overrides. |
| `softwareupdate` | `softwareupdate --history` | Review the history of installed software updates. |
| `pkgutil` | `pkgutil --pkgs` | List installed package receipts. |
| `xcode-select` | `xcode-select -p` | Show the active developer directory. |
| `xcrun` | `xcrun --find clang` | Find a tool in the selected Apple developer toolchain. |

[Apple Terminal User Guide](https://support.apple.com/guide/terminal/welcome-trml2df0220c/mac) · [Apple shell scripting primer](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/Introduction/Introduction.html) · [macOS manual page index](https://keith.github.io/xcode-man-pages/)
