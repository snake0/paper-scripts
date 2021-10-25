import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
import pandas as pd
import seaborn as sns

data = pd.read_excel('C:/Develop/PythonDemos/paper/rdma-tcp-lat.xlsx', header=0, usecols=[1, 3])

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Helvetica Neue', weight='medium', size=11)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
#
x = range(1000)
# x_title = ['64B', '128B', '256B', '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', '1M',
#            '2M']
y1 = data['Non-owner Write TCP(us)'].values.tolist()
y2 = data['Non-owner Write RDMA(us)'].values.tolist()

y1_min = np.min(y1)
y1_max = np.max(y1)
y2_min = np.min(y2)
y2_max = np.max(y2)
y1_mean = np.mean(y1)
y2_mean = np.mean(y2)

y2.sort()
print(y2[:10])

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b", "#c5c9c7"]

titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig = plt.figure()

plt.xlim(1, 1500)
plt.xscale('log')
plt.xlabel('Latency (us)', fontdict={'size': 16})
plt.grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)))

plt.ylim(0, 1)
plt.ylabel('Cumulative Probability', fontdict={'size': 16})

sns.kdeplot(y1, cumulative=True, label='TCP', color=colors[2])
sns.kdeplot(y2, cumulative=True, label='RDMA', color=colors[0])
plt.legend()

plt.axvline(y1_mean, color=colors[4], label='y1_mean')
plt.text(x=y1_mean+50, y=0.72, s='mean: {:.1f}'.format(y1_mean))
plt.scatter(y1_min-10, 0, color=colors[2], label='y1_min')
plt.text(x=y1_min-100, y=0.02, s='min: {:.1f}'.format(y1_min))
plt.scatter(y1_max, 1, color=colors[2], label='y1_max')
plt.text(x=y1_max, y=0.95, s='max: {:.1f}'.format(y1_max))

plt.axvline(y2_mean, color=colors[4], label='y2_mean')
plt.text(x=y2_mean+2, y=0.62, s='mean: {:.1f}'.format(y2_mean))
plt.scatter(y2_min, 0, color=colors[0], marker='^', label='y2_min')
plt.text(x=y2_min-2, y=0.02, s='min: {:.1f}'.format(y2_min))
plt.scatter(y2_max, 1, color=colors[0], marker='^', label='y2_max')
plt.text(x=y2_max, y=0.95, s='max: {:.1f}'.format(y2_max))

g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))

# plt.title(titles[0])
#
fig.tight_layout()
# fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-memory-all.pdf', dpi=100)
fig.savefig('./newimgs/non-write-latency.pdf', dpi=100)
plt.show()

plt.close()
