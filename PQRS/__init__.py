#!/usr/bin/env python3

import cherrypy
import sys

import Application

def main():
	print('Starting up PQRS...')

	cherrypy.config.update({
		'server.socket_host': '0.0.0.0',
		'server.socket_port': 27181,
	})

	pqrs = Application.PqrsApplication()
	cherrypy.quickstart(pqrs)

	print('Shutting down PQRS...')
	return 0

if __name__ == '__main__':
	sys.exit(main())
