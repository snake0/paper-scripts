#!/bin/sh

python3 stress-ng-scale.py &
python3 stress-ng.py &
python3 sysbench-cdf.py &
python3 sysbench-io.py &
python3 sysbench-memory-all.py &
python3 line-chart-web.py &

sleep 6
killall Python