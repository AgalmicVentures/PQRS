#!/usr/bin/env python3

import cherrypy
import sys

import Application

def main():
	print('Starting up PQRS...')

	pqrs = Application.PqrsApplication()
	cherrypy.quickstart(pqrs, config='server.conf')

	print('Shutting down PQRS...')
	return 0

if __name__ == '__main__':
	sys.exit(main())
