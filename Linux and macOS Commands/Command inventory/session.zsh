# Source this file in the active zsh session, then run visible_commands.
visible_commands() {
    emulate -L zsh
    rehash
    print -rl -- ${(k)commands} ${(k)builtins} ${(k)aliases} ${(k)functions} ${reswords[@]} | LC_ALL=C sort -u
}
