#!/bin/bash

python3 $1 &
#open $2
sleep 5
killall Python

