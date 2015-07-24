#!/bin/bash
tmux list-windows | awk '{ print $2 }' | tr -d '!' | sed -E 's/(-|\*)$//'
