import numpy as np
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'size': 24, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig = plt.figure()
fig.set_size_inches(10, 7.85)

x = [4, 8, 12, 16, 20, 24]
y1 = [8683.06, 6484.08, 6208.55, 6126.54, 6436.79, 6278.47]
y2 = [3022.08, 4809.57, 6008.72, 6461.55, 7645.22, 7311.65]
y3 = [4113.1, 5921.72, 7533.25, 7427.28, 7343.97, 7135.68]
y4 = [256.36, 496.97, 598.65, 897.33, 1146.98, 1050.94]
labels = ["{4KiB,global,write,GiantVM}", "{4KiB,global,write,baseline}",\
        "{4KiB,global,write,GiantVM-IPoIB}", "{4MiB,global,write,GiantVM}"]
title = "Memory-2"

dot_style = ['s', 'x', 'd', '^', '*', '|', 'H', '.']
line_style = [':', '-.', '--', '-']
colors = ["#D73F37", "#000000", "#D73F37", "#D73F37"]
marker_size = 12
labelx = -0.15
downtime_draw = []
total_draw = []
linewidth = 4

plt.title(title, fontdict=font)
plt.plot(x, y1, fillstyle='none', linestyle='--', marker=dot_style[0],\
        markersize=marker_size, linewidth=linewidth, label=labels[0], color=colors[0])
plt.plot(x, y2, fillstyle='none', linestyle='--', marker=dot_style[1],\
        markersize=marker_size, linewidth=linewidth, label=labels[1], color=colors[1])
plt.plot(x, y3, fillstyle='none', linestyle='--', marker=dot_style[2],\
        markersize=marker_size, linewidth=linewidth, label=labels[2], color=colors[2])
plt.plot(x, y4, fillstyle='none', linestyle='-', marker=dot_style[3],\
        markersize=marker_size, linewidth=linewidth, label=labels[3], color=colors[3])

plt.xlabel("#vCPUs", fontdict=font)
plt.ylabel("MiB/s", fontdict=font)
plt.ylim([0, 12000])
plt.tick_params(axis='both', which='major', labelsize=24)
plt.grid(False)
plt.legend(loc=0, prop={'size': 24}, frameon=False)

plt.xticks(x)
# ax.set_xticklabels(labels, rotation=30)
plt.tight_layout()
plt.savefig('../imgs/new/evaluation/sysbench-memory-special.pdf', dpi=300)
plt.show()
