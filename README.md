tmux-utils
==========

Various scripts and added tmux behaviours.

**tmux-get VAR** - gets variable VAR from within the tmux environment

**tmux-set VAR VALUE** - sets variable VAR to VALUE within the tmux environment

**tmux-pane** - returns the unique id of the current pane

**tmux-zoom** - takes the current pane and extracts it full size into its own
window

**tmux-unzoom** - replaces the zoom window into its original position

**tmux-await-copy** - block until something has been copied using the copy-mode command

**tmux-split-in-cwd** - open a new shell with same cwd as calling pane

**tmux-xcopy** - select some text and immediately copy it to the X selection clipboard

**tmux-copy** - select some text and immediately paste it into the current terminal

**tmux-super-select** - Select a window using a pop up window (tmenu or rofi)

**tmx** - Allow mutiple distinct views into the same tmux session.

Alternatives
-----------

You might want to look the `tmux-plugins` library https://github.com/tmux-plugins.
This seems to be a plugin framework very much influenced by zsh.

The `tmuxp` library can be very useful for your own ad-hoc tools.

Pane Zoom
---------

1. Add these scripts to your *$PATH*.

2. Put the following into your *.tmux.conf*:

```
unbind Up
bind Up run-shell tmux-zoom

unbind Down
bind Down run-shell tmux-unzoom
```

Configuration files (*.tmux)
----------------------------

These are sample bindings. To use them source them from your .tmux.conf. You must ensure that a directory containing the binaries is on your path when you start tmux.
