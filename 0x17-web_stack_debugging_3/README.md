# Web stack debugging #3

This project, a broken/bugged webstacks was given a in isolated containers,
and tasked with fixing the web stack to a working state. For task, a script automating the commands necessary to fix the
web stack.

## Task :page_with_curl:

* **0. Strace is your friend**
  * [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp): Puppet manifest
  that fixes a typo error causing a WordPress application being served by an Apache
  web server to fail.
  * Usage: `puppet apply 0-strace_is_your_friend.pp`
