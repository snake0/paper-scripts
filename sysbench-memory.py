import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font = {'size': 24, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Nimbus Sans L', weight='medium')
fig = plt.figure()
fig.set_size_inches(10, 7.85)
# fig.set_size_inches(11, 3.0)

x = [4, 8, 12, 16, 20, 24]
y1 = [42061.26, 92469.49, 131072.9, 183858.78, 223154.86, 229467.97]
y2 = [75527.9, 143261.82, 211938.7, 277095.76, 336383.4, 365684.81]
# y3 = [8683.06, 6484.08, 6208.55, 6126.54, 6436.79, 6278.47]
# y4 = [3022.08, 4809.57, 6008.72, 6461.55, 7645.22, 7311.65]
# y5 = [256.36, 496.97, 598.65, 897.33, 1146.98, 1050.94]
y6 = [27193.03, 47503.08, 58012.17, 63876.5, 68984.96, 76913.48]
y7 = [74320.72, 152924.43, 224953.49, 300204.18, 422482.79, 414039.46]
y8 = [138041.83, 258236.07, 384571.71, 499286.39, 615887.18, 656600.11]
labels = ["{4KiB,local,write,GiantVM}", "{4KiB,local,write,baseline}",
          "{4KiB,global,write,GiantVM}", "{4KiB,global,write,baseline}",
          "{4MiB,global,write,GiantVM}", "{4MiB,global,write,baseline}",
          "{4KiB,global,read,GiantVM}", "{4KiB,global,read,baseline}"]
title = "Memory-1"

dot_style = ['s', 'x', 'H', '|', '^', 'd', 'P', 'o']
line_style = [':', '-.', '--', '-']
#colors = ["#FF6C91", "#BC9D00", "#00BB57", "#00B8E5", "#CD79FF", "#FC8D62"]
colors = ["#D73F37", "#000000", "#000000", "#000000", "#D73F37", "#000000"]
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
# plt.plot(x, y3, fillstyle='none', linestyle='-', marker=dot_style[2],\
#        markersize=marker_size, linewidth=linewidth, label=labels[2])
# plt.plot(x, y4, fillstyle='none', linestyle='-', marker=dot_style[3],\
#         markersize=marker_size, linewidth=linewidth, label=labels[3])
# plt.plot(x, y5, fillstyle='none', linestyle='-', marker=dot_style[4],\
#         markersize=marker_size, linewidth=linewidth, label=labels[4],\
#          color=colors[2])
plt.plot(x, y6, fillstyle='none', linestyle='-', marker=dot_style[5],\
        markersize=marker_size, linewidth=linewidth, label=labels[5],\
        color=colors[3])
plt.plot(x, y7, fillstyle='none', linestyle='--', marker=dot_style[6],\
        markersize=marker_size, linewidth=linewidth, label=labels[6],\
         color=colors[4])
plt.plot(x, y8, fillstyle='none', linestyle='--', marker=dot_style[7],\
        markersize=marker_size, linewidth=linewidth, label=labels[7],\
         color=colors[5])

plt.xlabel("#vCPUs", fontdict=font)
plt.ylabel("MiB/s", fontdict=font)
plt.ylim([0, 900000])
plt.tick_params(axis='both', which='major', labelsize=24)
plt.grid(False)
plt.legend(loc=0, prop={'size': 22}, frameon=False)
plt.xticks(x)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

# ax.set_xticklabels(labels, rotation=30)
plt.tight_layout()
plt.savefig('../imgs/new/evaluation/sysbench-memory.pdf', dpi=300)
plt.show()
