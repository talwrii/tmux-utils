winmux -- multiple window tmux bother with a few utilities

usage winmux (alter your terminal manage to start this by default)


= Requirements =

Python
tmuxp (pip install -r requirements.txt)

= Caveats =

tmuxp is slow to fetch window information, perhaps only when you have a lot of windows. I think this might be an easy fix..., but have not attempted to fix this.

Does not support multiple shared sessions, for laziness. This probably isn't too hard to add


= Installing =

1. Ensure the requirements are matched
1. Ensure winmux is on your path
1. Source winmux.tmux in your tmux configuration. Use tmux list-keys to get a list of bindings.
1. Alter you x terminal so that it runs winmux on startup

