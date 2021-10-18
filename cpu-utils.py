import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

from common import *

font["font.size"] = 24
plt.rcParams.update(font)

fig, ax = plt.subplots()
fig.set_size_inches(6, 5)
plt.subplots_adjust(top=0.8, right=0.95, left=0.25, bottom=0.1)
labels = ["Apache", "OLTP (RO)", "OLTP (RW)", "Redis (GET)", "Redis (GET/SET)"]

# vanilla_avg = [1.732, 0.78, 17.48, 27.81, 23.76]
# vanilla_tail = [3, 0.93, 22.87, 5, 5]
node0 = [85.34505343,
         72.83476764]
node1 = [8.9407101,
         32.81663837]
node2 = [72.17338849,
         78.10546204]
node3 = [74.49431231,
         75.40425532]

data = [node0, node1, node2, node3]

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j] / 100.0

xrange = np.arange(len(node0))

# for i in range(len(labels)):
#     vm_live_avg[i], vm_live_tail[i], yanni_avg[i], yanni_tail[i] = \
#         vm_live_avg[i] / vanilla_avg[i], \
#         vm_live_tail[i] / vanilla_tail[i], \
#         yanni_avg[i] / vanilla_avg[i], \
#         yanni_tail[i] / vanilla_tail[i]


title = "Text-Processing\nComparison with Spark"
colors = ["#f5f7c8", "#c3ddbd"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.21
bar_interval = 0.01
bar_zoom = 0.9
linewidth = 4

# ax.set_title(title,fontdict=font)

# plt.xticks(xrange, labels, rotation=15)
plt.xticks([0, 1], ["Vanilla", "Yanni"])
ax.set_ylabel("Average CPU Utilization")
ax.tick_params(axis='both', which='major')


# y_major_locator = MultipleLocator(0.25)
# ax.yaxis.set_major_locator(y_major_locator)


def to_percent(temp, position):
    return '%1.0f' % (100 * temp) + '%'


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

ax.set_ylim([0, 1.5])
# ax.set_xlabel("Program", fontdict=font)

# ax.axhline(y=1, color='grey', linestyle='--')
bars = [0, 1]
for i in xrange:
    bars[i] = ax.bar(i - 3 * bar_width / 2, node0[i], width=bar_width * bar_zoom,
                     bottom=0, color=colors[i],
                     label="vm live avg", edgecolor="black")
    vmlive_tail_bar = ax.bar(i - 1 * bar_width / 2, node1[i], width=bar_width * bar_zoom,
                             bottom=0, color=colors[i],
                             label="vm live tail", hatch="//", edgecolor="black")
    yanni_avg_bar = ax.bar(i + bar_width / 2, node2[i], width=bar_width * bar_zoom,
                           bottom=0, color=colors[i],
                           label="yanni avg", edgecolor="black")
    yanni_tail_bar = ax.bar(i + 3 * bar_width / 2, node3[i], width=bar_width * bar_zoom,
                            bottom=0, color=colors[i],
                            label="yanni tail", hatch="//", edgecolor="black")
plt.text(s="Node 0",
         x=0 - 3 * bar_width / 2, y=1.1,
         va='bottom', size=16, rotation=90, ha='center')
plt.text(s="Node 1",
         x=0 - 1 * bar_width / 2, y=1.1,
         va='bottom', size=16, rotation=90, ha='center')
plt.text(s="Node 2",
         x=0 + 1 * bar_width / 2, y=1.1,
         va='bottom', size=16, rotation=90, ha='center')
plt.text(s="Node 3",
         x=0 + 3 * bar_width / 2, y=1.1,
         va='bottom', size=16, rotation=90, ha='center')

plt.text(s="%1.1f%%" % 60.2,
         x=0 , y=0.9,
         va='bottom', size=18, rotation=00, ha='center', weight = 'bold')
plt.text(s="%1.1f%%" % 64.8,
         x=1 , y=0.9,
         va='bottom', size=18, rotation=00, ha='center', weight = 'bold')
# ax.legend((bars[0], bars[1]),
#           ("Vanilla", "Yanni"),
#           loc=0, frameon=True, ncol=2)

plt.xlim([0 - 4 * bar_width / 2 - 0.2, max(xrange) + 4 * bar_width / 2 + 0.2])

plt.subplots_adjust(top=0.86)

plt.grid(True)
plt.savefig('/Users/snake0/yanni-img/cpu.pdf', dpi=300)
plt.show()
