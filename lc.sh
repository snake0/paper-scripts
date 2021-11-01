#!/bin/sh

python3 lc-latency.py &
python3 lc-guest.py &
python3 lc-util.py &
python3 lc-qps.py &


sleep 6
killall Python