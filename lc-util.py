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

plt.rc('font', family='Nimbus Sans L', weight='medium',size=13)

fig, ax = plt.subplots()
fig.set_size_inches(3., 2.47)
plt.subplots_adjust()

x = ["w/o", "naïve", "LaS"]
lc_util = [30.6147614, 36.10551394, 41.28190491]
lc_gini = [0.568788477, 0.48619563, 0.425715139]

xrange = np.arange(len(x))

bar_width = 0.4
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("CPU Utilization (%)")

ax.set_axisbelow(True)
ax.tick_params(top=False, bottom=False, left=True, right=False)

# ax2 = ax.twinx()
# ax2.set_ylabel("Gini Coefficient")

ax.set_ylim(25, 45)
# ax2.set_ylim(.3, .75)
# ax2.tick_params(top=True, bottom=False, left=True, right=False)

# ax2.set_axisbelow(True)

for i in xrange:
    util_bar = ax.bar(i, lc_util[i], width=bar_width * bar_zoom,
                      bottom=0, color=colors_taco[2], edgecolor="black")
    # gini_bar = ax2.bar(i + bar_interval / 2, lc_gini[i], width=bar_width * bar_zoom,
    #                    bottom=0, color=colors_taco[4], edgecolor="black")

# ax2.legend((util_bar), ("CPU Util"), facecolor='white', framealpha=1.0,
#            loc='best', frameon=True, edgecolor='white')

plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.tight_layout()
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

ax.set_xlim(min(xrange) - 0.6, max(xrange) + 0.6)
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

plt.title("CPU Results")



plt.savefig('/Users/snake0/taco-journal/lc-util.pdf', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
