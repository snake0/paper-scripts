import numpy as np
import matplotlib.pyplot as plt
from color import *


import matplotlib
matplotlib.rcParams['axes.linewidth'] = 0.5 #set the value globally

# data = pd.read_excel('C:/Develop/PythonDemos/paper/rdma-tcp-lat.xlsx', header=0, usecols=[1, 3])

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium',size=13)
plt.tick_params(top=True, bottom=False, left=True, right=False)


fig, ax = plt.subplots()
fig.set_size_inches(3., 2.4)
plt.subplots_adjust()

x = ["naïve", "LaS"]
lc_latency = [2031455.692/1976033.625, 1975565.927/1976033.625]
lc_95latency = [3195470.417/2332104.538, 2344859.067/2332104.538]
lc_99latency = [4752269.695/2514224.813, 3464523.773/2514224.813]
lc_999latency = [5658748.351/2633488.885, 4364897.765/2633488.885]

xrange = np.arange(len(x))

bar_width = 0.22
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("Normalized Latency")

ax.set_ylim(.8, 3.4)

for i in xrange:
    latency_bar = ax.bar(i-3*bar_interval/2, lc_latency[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[1], edgecolor="black")
    latency95_bar = ax.bar(i-bar_interval/2, lc_latency[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[2], edgecolor="black")
    latency99_bar = ax.bar(i+bar_interval/2, lc_99latency[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[3], edgecolor="black")
    latency999_bar = ax.bar(i+3*bar_interval/2, lc_999latency[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[4], edgecolor="black")

ax.legend((latency_bar, latency95_bar, latency99_bar, latency999_bar),
        ("AVG", "P95", "P99", "P99.9"),
          facecolor='white', framealpha=0.5,
          loc='best', frameon=True, ncol=1, edgecolor='white')
plt.tick_params(top=False, bottom=False, left=True, right=False)

ax.set_axisbelow(True)

ax.set_xlim(min(xrange)-0.6, max(xrange)+0.6)


plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.tight_layout()

plt.title("Latency of LC tasks")

plt.savefig('/Users/snake0/taco-journal/lc-latency.pdf', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
