# Copyright Tal Wrii
# Select and immediately copy to x clipboard
bind-key X copy-mode \; if-shell 'bash -c "source ~/.bashrc; tmux-await-copy"' "run-shell 'tmux paste-buffer | xclip -i'"
