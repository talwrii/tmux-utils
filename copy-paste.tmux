# Copyright Tal Wrii

bind-key P copy-mode \; \
     if-shell 'bash -c "source ~/.bashrc; tmux-await-copy"' paste-buffer
