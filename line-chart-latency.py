import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Helvetica Neue', weight='medium', size=11)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

x = range(16)
x_title = ['64B', '128B', '256B', '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', '1M',
           '2M']
y1 = [15.55, 29.67, 58.98, 116.70, 212.41, 361.01, 501.49, 831.06, 1333.94, 1694.48, 2209.63, 2562.68, 2465.64, 2804.25,
      2824.67, 2840.28]
y2 = [1.37, 2.63, 4.97, 8.58, 15.09, 23.38, 38.12, 145.90, 245.67, 238.15, 231.03, 227.66, 226.05, 225.19, 224.78,
      224.68]
y3 = [3.92, 4.11, 4.14, 4.18, 4.60, 5.41, 7.79, 9.40, 11.71, 18.44, 28.29, 48.78, 101.39, 178.30, 354.02, 704.15]
y4 = [44.40, 46.45, 49.12, 56.89, 64.73, 83.53, 102.47, 53.55, 63.60, 131.22, 270.53, 549.07, 1105.96, 2220.37, 4448.78,
      8901.61]

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig, ax1 = plt.subplots()

plt.xlim(1, 15)
plt.xlabel('Request Size (Bytes)', fontdict={'size': 16})
plt.xticks(x, x_title, rotation=36)
plt.grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)))
p1, = plt.plot([], [], marker="^", markersize=9, color=colors[2])
p2, = plt.plot([], [], marker="^", markersize=9, color=colors[0])
p3, = plt.plot([], [], marker="x", markersize=9, linestyle="dotted", color=colors[2])
p4, = plt.plot([], [], marker="x", markersize=9, linestyle="dotted", color=colors[0])
plt.legend([p1, p3, p2, p4], ["", "", "RDMA", "TCP"], ncol=2, columnspacing=0)

ax1.plot(x, y3, linewidth=2, marker="^", markersize=9, label="RDMA", color=colors[2])
ax1.plot(x, y4, linewidth=2, marker="x", markersize=9, label="TCP", color=colors[2], linestyle="dotted")
ax1.set_ylim(1, 10000)
ax1.set_yscale('log')
ax1.set_ylabel('Latency (us)')
ax1.yaxis.label.set_color(colors[2])
ax1.yaxis.label.set_fontsize(16)
ax1.tick_params(axis='y', colors=colors[2])

g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

ax2 = ax1.twinx()
ax2.plot(x, y1, linewidth=2, marker="^", markersize=9, label="RDMA", color=colors[0])
ax2.plot(x, y2, linewidth=2, marker="x", markersize=9, label="TCP", color=colors[0], linestyle="dotted")
ax2.set_ylim(1, 10000)
ax2.set_yscale('log')
ax2.set_ylabel('Bandwidth (MiB/s)')
ax2.yaxis.label.set_color(colors[0])
ax2.yaxis.label.set_fontsize(16)
ax2.tick_params(axis='y', colors=colors[0])

# plt.title(titles[0])

fig.tight_layout()
# fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-memory-all.pdf', dpi=100)
fig.savefig('./newimgs/sysbench-latency-all.pdf', dpi=100)
plt.show()

plt.close()
