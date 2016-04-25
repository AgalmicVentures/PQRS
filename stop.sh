#!/bin/bash

CWD=`pwd`
PROCESSES=`ps xa | grep $CWD/PQRS/__init__.py | grep -v grep`
if [[ $? -eq 1 ]]; then
	echo "Not running"
	exit
fi

PID=`echo $PROCESSES | awk '{print $1}'`
kill $@ $PID
