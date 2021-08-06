import numpy as np
import matplotlib.pyplot as plt

font = {'size': 26, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(10, 7.85)
plt.subplots_adjust(top=0.95, right=0.95)

x = ["1", "4", "16"]

xrange = np.arange(len(x));
local = [8595, 5701, 2597]
shmrpc = [5264, 5006, 6382]
baseline = [8608, 6631, 6010]

title = "MongoDB"
colors = ["#555555", "#BBBBBB", "#EEEEEE"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['//////', '\\\\\\\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

marker_size = 8
bar_width = 0.2
labelx = -0.15
bar_zoom = 0.98
linewidth = 2

ax.set_title(title, fontdict=font)

plt.xticks(xrange, x)
ax.set_ylabel("TPS", fontdict=font)
ax.set_xlabel("Size (KiB)", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=20)

for i in xrange:
    base_bar = ax.bar(i - bar_width, baseline[i], width=bar_width * bar_zoom,
                          bottom=0, color=colors[0], edgecolor="black",
                           label="Baseline")
    local_bar = ax.bar(i, local[i], width=bar_width * bar_zoom,
                       bottom=0, color=colors[1], edgecolor="black",
                        label="Local")
    shmrpc_bar = ax.bar(i + bar_width, shmrpc[i], width=bar_width * bar_zoom,
                        bottom=0, color=colors[2], edgecolor="black",
                        label="Shmrpc")

ax.legend((base_bar, local_bar, shmrpc_bar),
          ("Baseline", "Local", "Shmrpc"),
          loc=0, prop={'size': 20}, frameon=False)


plt.grid(False)
#plt.tight_layout()
plt.savefig('../imgs/new/evaluation/mongodb.pdf', dpi=300)
plt.show()
