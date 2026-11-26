# Source this file in the active Bash session, then run visible_commands.
visible_commands() {
    compgen -c | LC_ALL=C sort -u
}
