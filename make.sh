#!/bin/sh

python3 line-chart.py &
python3 line-chart-1.py &
python3 line-chart-2.py &
python3 line-chart-web.py &
python3 mutex.py &
python3 stress-ng.py &

sleep 5
killall Python