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

x = ["w/o", "naïve", "LaS"]
lc_guest = [1, 708.0166667/810.7166667, 714.0166667/810.7166667]
# for i in range(len(lc_guest)):
#     lc_guest[i] = 1.0/lc_guest[i]
#
# mm = max(lc_guest)
# for i in range(len(lc_guest)):
#     lc_guest[i] = lc_guest[i]/mm

xrange = np.arange(len(x))

bar_width = 0.45
bar_interval = bar_width
bar_zoom = 0.85
linewidth = 4

plt.xticks(xrange, x)
ax.set_ylabel("Normalized (1 / Run Time)",)
ax.tick_params(axis='both', which='major',)

ax.set_axisbelow(True)

ax.set_ylim(.85, 1.01)
ax.set_xlim(min(xrange)-0.6, max(xrange)+0.6)


for i in xrange:
    ax.bar(i, lc_guest[i], width=bar_width*bar_zoom,
        bottom=0, color=colors_taco[-2], edgecolor="black")

plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.tight_layout()

plt.title("BE Co-runner Results")

plt.savefig('/Users/snake0/taco-journal/lc-guest.pdf', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
