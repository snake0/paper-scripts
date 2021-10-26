#!/bin/sh

python3 stress-ng-scale.py &
python3 stress-ng.py &
python3 line-chart-2.py &
python3 line-chart-1.py &
python3 line-chart.py &

sleep 6
killall Python