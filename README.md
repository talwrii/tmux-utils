tmux-utils
==========

Various scripts and added tmux beahviors.

*tmux-pane* - returns the unique id of the current pane

*tmux-zoom* - takes the current pane and extracts it full size into its own
window

*tmux-unzoom* - replaces the zoom window into its original position


Pane Zoom
---------

1. Add these scripts to your $PATH.

2. Put the following into your .tmux.conf:

    unbind Up
    bind Up run-shell tmux-zoom

    unbind Down
    bind Down run-shell tmux-unzoom

    
