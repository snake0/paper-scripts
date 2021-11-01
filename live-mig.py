import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from color import *

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

# data = pd.read_excel('C:/Develop/PythonDemos/paper/rdma-tcp-lat.xlsx', header=0, usecols=[1, 3])

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium')

marker_size = 10
linewidth = 2.5
bar_width = 0.23  # the width of the bars: can also be len(x) sequence
bar_interval = bar_width * 1.16 / 1.8

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)
fig.set_size_inches(5.5, 2.2)
plt.subplots_adjust(top=0.97, bottom=0.18, right=0.98, left=0.09)

labels = ["Apache2", "Apache-build", "OpenSSL", "Blowfish",
          "MD5", "POV-Ray", "7-Zip", "Redis", "PHPBench"]
N = 9
# working_set = [482, 683, 469, 510, 520, 510, 3791, 507, 702]
PLLM = np.array([162, 693.6, 74.2, 78.4, 54.7, 60.1, 9943.1, 99.6, 62.2])
# w_o_diff = [267.9, 1207.9, 125.7, 145.6, 130.3, 118.4, 10022.0, 133.0, 89.4]
vm_live_migration = np.array([995.8, 2329, 838.1, 910.9, 921.4, 863.5, 5120.9, 1129, 862.9])

PLLM_ratio = PLLM / vm_live_migration
vm_ratio = vm_live_migration / vm_live_migration

PLLM = PLLM / 1024.0
vm_live_migration = vm_live_migration / 1024.0

ind = np.arange(N)  # the x locations for the groups


def autolabel(ax, rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.2f}".format(array[i])
        s = s + "X"
        l = len(s)
        if l == 5:
            offset = -0.01
        else:
            offset = 0
        # if height < 0:
        #     offset = height - 40 - len(s) * 1.1
        # else:
        #     offset = 0 - 40 - len(s) * 1.1
        ax.text(s=s,
                x=rect.get_x() + rect.get_width() / 2 + 0.02, y=height - offset + 0.08,

                va='bottom', rotation=90, ha='center', weight='bold')


for i in ind:
    # working_set_bar = ax.bar(i - bar_interval, working_set[i], bar_width, color=colors[0],
    # edgecolor="black", hatch='++')
    vm_bar = ax.bar(i + bar_interval, vm_live_migration[i], bar_width, color=colors_taco[2],
                    edgecolor="black", linewidth=0.88)
    # diff_bar = ax.bar(i - bar_interval, w_o_diff[i], bar_width, color=colors_taco[3], edgecolor="black",linewidth=0.88)
    PLLM_bar = ax.bar(i - bar_interval, PLLM[i], bar_width, color=colors_taco[4], edgecolor="black", linewidth=0.88)
    # ax2.bar(i - bar_interval, working_set[i], bar_width, color=colors[0],
    # edgecolor="black", hatch='++')
    vm_bar1 = ax2.bar(i + bar_interval, vm_live_migration[i], bar_width, color=colors_taco[2],
                      edgecolor="black", linewidth=0.88)
    # ax2.bar(i - bar_interval, w_o_diff[i], bar_width, color=colors_taco[3], edgecolor="black",linewidth=0.88)
    PLLM_bar1 = ax2.bar(i - bar_interval, PLLM[i], bar_width, color=colors_taco[4], edgecolor="black", linewidth=0.88)

    # autolabel(ax2,vm_bar1,[vm_ratio[i]], [vm_live_migration[i]])
    if i == 6:
        autolabel(ax, PLLM_bar1, [PLLM_ratio[i]], [PLLM[i] + 1])
    else:
        autolabel(ax2, PLLM_bar1, [PLLM_ratio[i]], [PLLM[i]])

ax.set_ylim(1.953125, 20)  # outliers only
ax2.set_ylim(0, 1.26953125)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = .010  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# No common y-label for two subplots, hence such hack.
ax.set_ylabel('Network Bandwidth (GiB/s)' + 25 * ' ')
# ax.set_title('Network Bandwidth Consumption')


ax2.set_title('...')
plt.xticks(ind, labels, rotation=15)
ax.legend((PLLM_bar, vm_bar),
          ("Migration with GiantVM", "VM Live Migration (1.0X)"), facecolor='white', framealpha=1,
          loc='upper left', frameon=True, ncol=1, edgecolor='white')

ax.set_axisbelow(True)

ax2.set_axisbelow(True)

ax.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
ax2.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

plt.tick_params(top=False, bottom=False, left=True, right=False)

plt.savefig('/Users/snake0/taco-journal/vm_live_migration.pdf', dpi=300)
plt.show()
