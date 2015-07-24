#!/usr/bin/python

import argparse
import sys
import time

import tmuxp

PARSER = argparse.ArgumentParser(description='Restore tmux windows')
PARSER.add_argument('session', type=str, help='Which session to use')
args = PARSER.parse_args()

session, = [s for s in tmuxp.Server().list_sessions() if s['session_name'] == args.session]

window_names =  set([w['window_name'] for w in session.list_windows()])
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    name = line.strip()
    if name in window_names:
        print 'Not spawning {}'.format(name)
    else:
        print 'Spawned {}'.format(name)
        # Hack - we need some sort of delay so that tmux
        #   we need some sort of delay to give bashrc
        #   enough time to run
        time.sleep(0.3)
        session.new_window(name)
