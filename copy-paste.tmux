# Copyright Tal Wrii

bind-key P copy-mode \; \
     if-shell tmux-await-copy paste-buffer
