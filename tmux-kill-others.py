#!/usr/bin/python

import tmuxp
import argparse
import multiprocessing.pool

PARSER = argparse.ArgumentParser(description="Kill all the windows with a given name in all sessions")
PARSER.add_argument('--exclude-session', '-x', type=str, action='append', help='Do not kill windows in these sessions')
PARSER.add_argument('--dry-run', '-n',  action='store_true', default=False)
PARSER.add_argument('window_name', type=str)
args = PARSER.parse_args()

pool = multiprocessing.pool.ThreadPool(10)

server = tmuxp.Server()
sessions = server.list_sessions()
pairs = pool.map(lambda session: (session, session.attached_window()), sessions)

for session, window in pairs:
    if args.exclude_session and session['session_name'] in args.exclude_session:
        continue

    if window['window_name'] == args.window_name:
        if args.dry_run:
            print "Would have killed session", session
        else:
            session.kill_session()
