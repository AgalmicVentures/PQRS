#!/bin/bash

CWD=`pwd`
PROCESSES=`ps xa | grep $CWD/PQRS/__init__.py | grep -v grep`
if [[ $? -eq 0 ]]; then
	echo "Already running"
	exit
fi

echo "Starting..."
nohup $CWD/PQRS/__init__.py &
sleep 1
echo "Started."
