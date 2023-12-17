#!/bin/sh
for page in {1..6}
do
    python /home/pi/tools/dupImgFinder.py
    sleep 10 
done

