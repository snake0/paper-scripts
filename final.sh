#!/bin/bash

./run.sh perf-new.py &
./run.sh latency-occupy.py &
./run.sh perf-net.py &
./run.sh co-schedule.py &
