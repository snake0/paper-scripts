import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

plt.rc('font', family='Nimbus Sans L', weight='medium',size=11)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

x = [4, 8, 12, 16, 20, 24]
y1 = [2469135.80, 917431.19, 656598.82, 500000.00, 385356.45, 319386.78]
y2 = [1569858.71, 437062.94, 258866.17, 175438.60, 133815.07, 108073.06]
y3 = [2941176.47, 1287001.29, 905797.10, 606060.61, 505561.17, 461680.52]
y4 = [1059322.03, 370782.35, 170735.87, 91549.94, 71715.43, 48292.85]

x1 = [4,8,12,16,20,24]
y5 = [0.09, 0.12, 0.17, 0.13, 0.12, 0.11]
y6 = [3.17, 4.24, 4.58, 4.74, 4.88, 4.97]
y7 = [8.05, 2.83, 2.91, 2.77, 2.55, 2.12]
y8 = [94.26, 93.51, 91.88, 90.19, 89.07, 88.78]

# a=1.0
# for i in range(4):
#     a=a*y6[i]/y5[i]
#
# a=a**(0.25)
# print(a)
#
# b = 1.0
# for i in range(4):
#     b *= y8[i] / y7[i]
#
# b=b**(0.25)
# print(b)
#
# print((a*b)**0.5)



fig = plt.figure(figsize=(6.25, 2.6))

colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]

titles= ["Mutex {1,*}","Mutex {16,*}","File I/O {1KiB,*}","File I/O {1MiB,*}"]


plt.subplot(121)
plt.plot(x1, y5,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[0],linestyle="dotted")
plt.plot(x1, y6,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[0])
plt.xlim(4, 20)
plt.ylim(0.07,1000)
plt.xlabel('# vCPUs')
plt.ylabel('File I/O Speed (MiB/s)')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.yscale('log')
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[2])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))




plt.subplot(122)
plt.plot(x1, y7,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[1],linestyle="dotted")
plt.plot(x1, y8,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[1])
plt.xlim(4, 20)
plt.ylim(0.07,1000)
plt.yscale('log')
plt.xlabel('# vCPUs')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[3])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))








fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-io.pdf', dpi=300)
plt.show()

plt.close()