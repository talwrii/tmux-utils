#!/bin/bash

# Continually append a list of tmux windows to a file to be restored
while true; do
    pgrep -f '^tmux.*world$' && tmux-windows-dump.sh world > ~/var/tmux-windows.new ;
    cat ~/var/tmux-windows > ~/var/tmux-windows.new
    sort ~/var/tmux-windows.new | uniq > ~/var/tmux-windows;
    sleep 60;
done;
