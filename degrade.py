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

plt.rc('font', family='Nimbus Sans L', weight='medium')

fig, ax = plt.subplots()
fig.set_size_inches(3., 2.2)
fig.subplots_adjust(top=.95,bottom=.18,right=.95,left=.15)

apache = [630, 657, 632, 624, 639, 582, 452, 321, 617, 639, 644, 637, 635]
iperf = [342, 334, 344, 344, 321, 322, 297, 302, 344, 345, 332, 332, 345]
redis = [6896.55, 6993.01, 6060.61, 6578.95, 6134.97, 5952.38, 6097.56, \
        3952.57, 4310.34, 5882.35, 6060.61, 6493.51, 6329.11]
x = range(len(apache))

apache_max = max(apache)
iperf_max = max(iperf)
redis_max = max(redis)
for i in x:
    apache[i] = apache[i] * 1.0 / apache_max
    iperf[i] = iperf[i] * 1.0 / iperf_max
    redis[i] = redis[i] * 1.0 / redis_max

dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]
marker_size = 12
labelx = -0.15
downtime_draw = []
total_draw = []
linewidth = 4

#ax.set_title("Performance degradation during migration")
ax.plot(x, apache, linewidth=1.4,label="Apache2",color=colors[3],linestyle="dotted")
ax.plot(x, iperf,linewidth=1.5, label="iPerf",color="black")
ax.plot(x, redis,linewidth=2.2, label="Redis",color=colors[0])


ax.set_xlabel("Time/s")
ax.set_ylabel("Normalized QPS")
plt.tick_params(top=False, bottom=False, left=True, right=False)

ax.legend(facecolor='white', framealpha=1,
          loc='best', frameon=True, ncol=1, edgecolor='white')

plt.xticks(x)
# ax.set_xticklabels(labels, rotation = 30)
#plt.tight_layout()

plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.savefig('/Users/snake0/taco-journal/performance_degradation.pdf', dpi=300)
plt.show()
