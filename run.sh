#!/bin/bash

python3 $1 &
#open $2
sleep 3
killall Python

