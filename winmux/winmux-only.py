#!/usr/bin/python

"Ensure that the current window is the only version of a tmux window"

# Use the wonderful if slow (and probably slightly fragile) tmuxp package
import tmuxp

def main():
	server = tmuxp.Server()
	current_session = server.sessions[0]
	current_window, = [w for w in current_session.windows if w['window_active'] == '1']
	for s in server.sessions:
		has_same_window_open = [w for w in s.windows if w['window_name'] == current_window['window_name'] and w['window_active'] == '1']

		if not (s == current_session or s['session_name'] == 'world') and has_same_window_open:
			s.kill_session()

if __name__ == '__main__':
    main()
