import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium', size=14.5)


# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

def autolabel(ax, rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.0f}".format(array[i])
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
                x=rect.get_x() + rect.get_width() / 2 + 0.01, y=height - offset,

                va='bottom', rotation=90, size=10.5, ha='center')


# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#1d2f7b", "#000000"]
# colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]
colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

x_title = ['64', '128', '256', '512', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', '1M']
# y1 = [15.55, 29.67, 58.98, 116.70, 212.41, 361.01, 501.49, 831.06, 1333.94, 1694.48, 2209.63, 2562.68, 2465.64, 2804.25,
#       2824.67]
y1 = [1.122992213, 2.233525568, 4.465921183, 8.882473769, 17.23580739, 34.69210755, 66.44863209, 124.1151944,
      206.801968, 202.8285069, 203.8013733, 204.6608306, 205.4492195, 204.4932601, 199.0591346]
y2 = [1.37, 2.63, 4.97, 8.58, 15.09, 23.38, 38.12, 145.90, 245.67, 238.15, 231.03, 227.66, 226.05, 225.19, 224.78]
x = range(len(x_title))

xdwcolor = ["#5b22c4", "#b02318", "#0022e3", "#ffffff"]
ybandwidth = [5.596633945,
              10.75562381,
              21.69143156,
              42.93450355,
              83.67227611,
              124.2623133,
              234.1805739,
              413.4148721,
              635.3736826,
              386.4034314,
              769.9989913,
              464.3954298,
              417.7342855,
              413.0728357,
              165.9615646]

ylatency = [10.90569025, 11.3494405, 11.25516425, 11.3727005, 11.67127925, 15.71775825, 16.680504, 18.89748175,
            24.5918275, 80.874023, 81.1689375, 269.1671623,
            598.466558,
            1210.440283,
            6025.49152]

y3 = [369.67, 407.82, 1469.6]
y4 = [382.25, 571.96, 2828.87]

x_title = ["1G", "512M", "256M"]
x = range(len(x_title))

# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

# titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig, axs = plt.subplots(1, 4, figsize=(12, 2.9))

# plt.xlim([-1, 16])
# plt.ylim([0, 100000])
# plt.xlabel('Request Size (Bytes)')
# plt.xticks(x, x_title, rotation=60)
# plt.grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)))
# p1, = plt.plot([], [], marker="^", markersize=9, color=colors[3])
# p2, = plt.plot([], [], marker="^", markersize=9, color=colors[0])
# p3, = plt.plot([], [], marker="x", markersize=9, linestyle="dotted", color=colors[3])
# p4, = plt.plot([], [], marker="x", markersize=9, linestyle="dotted", color=colors[0])
# plt.legend([p1, p3, p2, p4], ["", "", "RDMA", "TCP"], ncol=2, columnspacing=0)

l1, = axs[0].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l2, = axs[0].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
# axs[0].set_yscale('log')
axs[0].set_xlabel('Anemoi$ Size (MiB)')
axs[0].set_ylabel('OLTP RO Latency (P95,ms)')
axs[0].set_xlim([-0.5, 2.5])
axs[0].set_ylim([0, 5000])

axs[0].ticklabel_format(style='sci', scilimits=(-1,2), axis='y')


axs[0].legend((l1, l2),
              ("LRU-K", "FIFO"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0].set_xticks(x)
axs[0].set_xticklabels(x_title)

# ax1.yaxis.label.set_color(colors[2])
# ax1.yaxis.label.set_fontsize(16)
# ax1.tick_params(axis='y', colors=colors[2])

# g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

# ax2 = ax1.twinx()
# ax2.plot(x, y1, linewidth=1, marker="^", markersize=9, label="RDMA", color=colors[0])
# ax2.plot(x, y2, linewidth=1, marker="x", markersize=9, label="TCP", color=colors[0], linestyle="dotted")
# # ax2.set_ylim(1, 10000)
# ax2.set_yscale('log')
# ax2.set_ylabel('Bandwidth (MiB/s)')
# # ax2.yaxis.label.set_color(colors[0])
# ax2.yaxis.label.set_fontsize(16)
# ax2.tick_params(axis='y', colors=colors[0])

# plt.title(titles[0])
# plt.ylim([0, 100000])

cfs8non = np.array([43.62, 43.75])
das8loc = np.array([116.58, 141.49])
cfs16non = np.array([407.82, 469.77])
das16par = np.array([1260.84, 1700.44])
mpi = np.array([15.114, 13.3885])

width = 0.14

sep = 0.03

x = np.arange(len(mpi))
name = ["PML", "w/o PML"]

# axs[0].set_ylabel("Normalized Results")

colors1 = ["#26388f", "#6db8be", "#a7d5b9", "#d9ecb8", "#fffedd"]

t1 = axs[1].bar(x - width * 1.5 - 1.5 * sep, cfs8non, width,
                color=colors1[0], edgecolor="black", label='CFS-8-Non', linewidth=0.9)
autolabel(axs[1], t1, cfs8non, cfs8non + 60)

t2 = axs[1].bar(x - width * 0.5 - 0.5 * sep, das8loc, width,
                color=colors1[1], edgecolor="black", label='DaS-8-Loc', linewidth=0.9)
autolabel(axs[1], t2, das8loc, das8loc + 60)

t3 = axs[1].bar(x + width * 0.5 + sep * 0.5, cfs16non, width,
                color=colors1[2], edgecolor="black", label='CFS-16-Non', linewidth=0.9)
autolabel(axs[1], t3, cfs16non, cfs16non + 60)

t4 = axs[1].bar(x + width * 1.5 + 1.5 * sep, das16par, width,
                color=colors1[3], edgecolor="black", label='DaS-16-Cli', linewidth=0.9)
autolabel(axs[1], t4, das16par, das16par + 60)

# t5 = axs[1].bar(x + 2 * width + 2 * sep, mpi, width,
#                 color=colors1[4], edgecolor="black", label='MPI', linewidth=0.9)
axs[1].tick_params(top=False, bottom=False, left=True, right=False)

axs[1].set_xlim(-0.55, 1.55)
axs[1].set_ylim(0.0, 3250)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([0, 1])
axs[1].set_ylabel('OLTP RW Latency(ms)')
axs[1].set_xticks(x)
axs[1].set_xticklabels(name, rotation=00)
axs[1].ticklabel_format(style='sci', scilimits=(-1,2), axis='y')


# axs[0].set_yticks([0, 0.3, 0.6, 0.9, 1.2, 1.5])

# plt.grid(axis='y', linewidth=0.9, linestyle=(0, (5, 3)))
# axs[1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1].set_axisbelow(True)

axs[1].legend((t1, t2, t3, t4), ("MIN", "AVG", "P95", "MAX"),
              loc='upper left', frameon=False, facecolor="white", ncol=2,fontsize=10.5)

y1 = [217.83, 193.29, 156.89, 137.29, 116.58, 119.39, 121.22]
y2 = [1473.41, 968.26, 754.68, 593.82, 660.84, 714.85, 703.71]
y3 = [893.56, 719.92, 569.67, 484.44, 407.82, 414.08, 417.38]
x = range(len(y1))
x_title = [r"$2^4$", r"$2^6$", r"$2^8$", r"$2^{10}$", r"$2^{12}$", r"$2^{14}$", r"$2^{16}$"]

l1, = axs[2].plot(x, y1, linewidth=2.0, color=colors[3], linestyle="dotted", )
l2, = axs[2].plot(x, y2, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
l3, = axs[2].plot(x, y3, linewidth=1.4, color="black")
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
# axs[2].set_yscale('log')
axs[2].set_xlabel('Associativity')
# axs[2].set_ylabel('Latency (ms)')
axs[2].set_xlim([-0.5, len(x) - 0.5])
axs[2].set_ylim([-150, 1800])
axs[2].set_ylabel('OLTP RW Latency(ms)')

axs[2].legend((l2, l3, l1),
              ("MAX", "P95", "AVG"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[2].set_xticks(x)
axs[2].set_xticklabels(x_title)
axs[2].ticklabel_format(style='sci', scilimits=(-1,2), axis='y')


y1 = [1.29, 1.30, 1.27, 1.30, 1.29, 1.30, 1.29, 1.30, 1.31, 1.30, 1.31, 1.30, 1.32, 1.28, 1.30, 1.31, 1.30, 1.30, 1.30,
      1.30, 1.30, 1.31, 1.30, 1.28, 1.30, 1.29, 1.32, 1.30, 1.31, 1.30, 1.28, 1.30]
y2 = [1.37, 1.31, 1.32, 1.36, 1.28, 1.30, 1.39, 1.30, 1.31, 1.31, 1.38, 1.28, 1.29, 1.30, 1.33, 1.39, 1.30, 1.38, 1.36,
      1.36, 1.29, 1.39, 1.30, 1.30, 1.35, 1.28, 1.40, 1.39, 1.27, 1.31, 1.33, 1.36]

x = range(len(y1))

l1 = axs[3].scatter(x, y1, marker='o', edgecolor="red", s=6,  c='none')
l2 = axs[3].scatter(x, y2, marker='s', c='black', s=4)

axs[3].legend((l1, l2),
              ("LRU-K", "FIFO"), facecolor='white', framealpha=1.0,
              loc='lower right', frameon=True, ncol=1, edgecolor='white')

axs[3].set_xlabel('Cache Set Number')
axs[3].set_ylabel('AVG # of Cache Misses')
axs[3].set_ylim([0.5, 1.7])



# data = pd.read_excel('~/MasterThesis/tcp-latency.xlsx', header=0, usecols=[0,1,2])
#
# y_rdma = np.array(data['write'].values.tolist())
# y_tcp = np.array(data['read'].values.tolist())
# y_ipoib = np.array(data['xbzrle'].values.tolist())
#
# y_rdma = y_rdma / 1000
# y_tcp = y_tcp / 1000
# y_ipoib = y_ipoib / 1000
#
# colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]
#
# y_rdma_sort3 = np.sort(y_rdma)
# y_tcp_sort3 = np.sort(y_tcp)
# y_iboip_sort3 = np.sort(y_ipoib)
#
# rdma_90 = np.percentile(y_rdma_sort3,90)
# tcp_90 = np.percentile(y_tcp_sort3,90)
# iboip_90 = np.percentile(y_iboip_sort3,90)
#
#
# rdma_50 = np.percentile(y_rdma_sort3,50)
# tcp_50 = np.percentile(y_tcp_sort3,50)
# iboip_50 = np.percentile(y_iboip_sort3,50)
#
# # print(rdma_50,tcp_50,iboip_50)
# # print(rdma_90,tcp_90,iboip_90)
#
# y_rdma_cdf3 = 1. * np.arange(len(y_rdma_sort3)) / (len(y_rdma_sort3) - 1)
# y_tcp_cdf3 = 1. * np.arange(len(y_tcp_sort3)) / (len(y_tcp_sort3) - 1)
# y_iboip_cdf3 = 1. * np.arange(len(y_iboip_sort3)) / (len(y_iboip_sort3) - 1)
#
#
# axs[4].plot(y_rdma_sort3, y_rdma_cdf3,label="WRITE",linewidth=1.4,color=colors[3],linestyle="dotted")
# axs[4].plot(y_tcp_sort3, y_tcp_cdf3,label="READ",linewidth=1.8, color="black")
# axs[4].plot(y_iboip_sort3, y_iboip_cdf3,label="W-XBZRLE",linewidth=2.2, color=colors[0])
#
#
# axs[4].set_xlabel("Network Latencies (ns)")
# axs[4].set_xscale("log")
# axs[4].set_ylim([0,1])
# axs[4].set_ylabel("CDF")
# axs[4].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
# axs[4].set_yticks([0,0.2,0.4,0.6,0.8,1])
#
# axs[4].legend(facecolor='white',framealpha=0.0,
#         loc='lower right',frameon=True,ncol=1, edgecolor='white')


axs[0].set_title("(a) $ Eviction")
axs[1].set_title("(b) PML")
axs[2].set_title("(c) Assoc.")
axs[3].set_title("(d) Cache Misses")
# axs[4].set_title("Functions")

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

fig.tight_layout()
fig.savefig('/Users/snake0/MasterThesis/figures/_other-comp.pdf', dpi=100)
# fig.savefig('./newimgs/sysbench-latency-all.pdf', dpi=100)
plt.show()

plt.close()
