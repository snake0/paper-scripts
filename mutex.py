import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium')
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

x = [4, 8, 12, 16, 20, 24]
y1 = [2469135.80, 917431.19, 656598.82, 500000.00, 385356.45, 319386.78]
y2 = [1569858.71, 437062.94, 258866.17, 175438.60, 133815.07, 108073.06]
y3 = [2941176.47, 1287001.29, 905797.10, 606060.61, 505561.17, 461680.52]
y4 = [1059322.03, 370782.35, 170735.87, 91549.94, 71715.43, 48292.85]

x1 = [4,8,12,16]
y5 = [0.09, 0.12, 0.17, 0.13]
y6 = [3.17, 4.24, 4.58, 4.74]
y7 = [8.05, 2.83, 2.91, 2.77]
y8 = [94.26, 93.51, 91.88, 90.19]


fig = plt.figure(figsize=(6.25, 2.6))

colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]

titles= ["Mutex {1,*}","Mutex {16,*}","File I/O {1KiB,*}","File I/O {1MiB,*}"]

plt.subplot(121)
plt.plot(x, y2,linewidth=2, marker="x",markersize=8,label="* = GiantVM",color=colors[0],linestyle="dotted")
plt.plot(x, y1,linewidth=2, marker="x",markersize=8,label="* = baseline",color=colors[0])
plt.xlim(4, 24)
plt.ylim(0, 3000000)
plt.xlabel('# of vCPUs')
plt.ylabel('Locking Throughput (Ops/s)')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.yticks([0,1000000,2000000,3000000])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(loc=1)
plt.title(titles[0])

g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.1e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))





plt.subplot(122)
plt.plot(x, y4,linewidth=2, marker="x",markersize=8,label="* = GiantVM",color=colors[1],linestyle="dotted")
plt.plot(x, y3,linewidth=2, marker="x",markersize=8,label="* = baseline",color=colors[1])
plt.xlim(4, 24)
plt.ylim(0, 3000000)
plt.xlabel('# of vCPUs')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.yticks([0,1000000,2000000,3000000])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(loc=1)
plt.title(titles[1])

g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.1e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))




fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-mutex.pdf', dpi=300)
plt.show()

plt.close()