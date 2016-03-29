#!/usr/bin/python


import argparse

import tmuxp

PARSER = argparse.ArgumentParser(description='Open a window in a given session')
PARSER.add_argument('session', type=str)
PARSER.add_argument('window', type=str)
args = PARSER.parse_args()


server = tmuxp.Server()
session, = [s for s in server.list_sessions() if s['session_name'] == args.session]
session.new_window(args.window)
