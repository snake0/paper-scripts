import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'size': 24, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig = plt.figure()
fig.set_size_inches(10, 7.85)
# fig.set_size_inches(11, 3.0)

x = [4, 8, 12, 16, 20, 24]
y1 = [2469135.80, 917431.19, 656598.82, 500000.00, 385356.45, 319386.78]
y2 = [1569858.71, 437062.94, 258866.17, 175438.60, 133815.07, 108073.06]
# y3 = [1379310.34, 422654.27, 252334.09, 149745.43, 126807.00, 117109.73]
y3 = [2941176.47, 1287001.29, 905797.10, 606060.61, 505561.17, 461680.52]
y4 = [1059322.03, 370782.35, 170735.87, 91549.94, 71715.43, 48292.85]
# y6 = [998003.99, 357653.79, 164636.15, 75740.36, 64850.84, 47986.95]
labels = ["{1,baseline}", "{1,GiantVM}", "{16,baseline}", "{16,GiantVM}"]
title = "Mutex"

dot_style = ['s', 'x', 'd', '^', '|', 'P', 'H', '.']
line_style = [':', '-.', '--', '-']
colors = ["#000000", "#D73F37", "#000000", "#D73F37"]
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
plt.ylabel("Ops/s", fontdict=font)
plt.tick_params(axis='both', which='major', labelsize=24)
plt.grid(False)
plt.legend(loc=0, prop={'size': 24}, frameon=False)
plt.xticks(x)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

# ax.set_xticklabels(labels, rotation=30)
plt.tight_layout()
plt.savefig('../imgs/new/evaluation/sysbench-mutex.pdf', dpi=300)
plt.show()
