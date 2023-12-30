#!/bin/sh

DIRECTORY=pi
if [ -d "$DIRECTORY" ]; then
    echo "$DIRECTORY existing......"
else
    echo "creating directory $DIRECTORY......"
    mkdir $DIRECTORY
fi

nohup python3 ImageServer.py &

echo "init done......"