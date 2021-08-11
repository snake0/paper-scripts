#!/bin/bash

python3 heatmap-ep.py &
python3 heatmap-ft.py &
python3 heatmap-mg.py &
python3 heatmap-sp.py &
python3 heatmap-bt.py &
python3 heatmap-cg.py &

sleep 5

killall Python