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
fig.set_size_inches(3., 2.6)
plt.subplots_adjust()

x = ["w/o", "naïve", "LaS"]
lc_qps = [1,  517.775/532.525,523.09375/532.525]

xrange = np.arange(len(x))

bar_width = 0.45
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("Normalized QPS",)
ax.tick_params(axis='both', which='major')
ax.set_axisbelow(True)

ax.set_ylim(.96, 1.02)
ax.set_xlim(min(xrange)-0.6, max(xrange)+0.6)

for i in xrange:
    qps_bar = ax.bar(i, lc_qps[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[-1], edgecolor="black")

plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.title("LC Tasks QPS")

plt.tight_layout()
plt.savefig('/Users/snake0/taco-journal/lc-qps.pdf', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
