import numpy as np
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font_size = 24

font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig = plt.figure()
fig.set_size_inches(10, 7.85)
# fig.set_size_inches(11, 3.0)

x = [4, 8, 12, 16]
y1 = [0.09, 0.12, 0.17, 0.13]
y2 = [3.17, 4.24, 4.58, 4.74]
y3 = [8.05, 2.83, 2.91, 2.77]
y4 = [94.26, 93.51, 91.88, 90.19]
labels = ["{1KiB,GiantVM}", "{1KiB,baseline}",\
        "{1MiB,GiantVM}", "{1MiB,baseline}"]
title = "File I/O"

dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
colors = ["#D73F37", "#000000", "#D73F37", "#000000"]
marker_size = 12
labelx = -0.15
downtime_draw = []
total_draw = []
linewidth = 4

plt.title(title, fontdict=font)
plt.plot(x, y1, fillstyle='none', linestyle='--', marker=dot_style[0],\
        markersize=marker_size, linewidth=linewidth, label=labels[0],\
         color=colors[0])
plt.plot(x, y2, fillstyle='none', linestyle='--', marker=dot_style[1],\
        markersize=marker_size, linewidth=linewidth, label=labels[1],\
         color=colors[1])
plt.plot(x, y3, fillstyle='none', linestyle='-', marker=dot_style[2],\
        markersize=marker_size, linewidth=linewidth, label=labels[2],\
         color=colors[2])
plt.plot(x, y4, fillstyle='none', linestyle='-', marker=dot_style[3],\
        markersize=marker_size, linewidth=linewidth, label=labels[3],\
         color=colors[3])
plt.xlabel("#vCPUs", fontdict=font)
plt.ylabel("MiB/s", fontdict=font)
plt.yscale('log')
plt.ylim([0, 3000])
plt.tick_params(axis='both', which='major', labelsize=font_size)
plt.grid(False)
plt.legend(loc=0, prop={'size': font_size}, frameon=False)

plt.xticks(x)
# ax.set_xticklabels(labels, rotation = 30)
plt.tight_layout()
plt.savefig('../imgs/new/evaluation/sysbench-fileio.pdf', dpi=300)
plt.show()
