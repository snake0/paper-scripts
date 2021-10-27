import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium', size=11)
# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#1d2f7b", "#000000"]
colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]


matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

x_title = ['64', '128', '256', '512', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', '1M']
y1 = [15.55, 29.67, 58.98, 116.70, 212.41, 361.01, 501.49, 831.06, 1333.94, 1694.48, 2209.63, 2562.68, 2465.64, 2804.25,
      2824.67]
y2 = [1.37, 2.63, 4.97, 8.58, 15.09, 23.38, 38.12, 145.90, 245.67, 238.15, 231.03, 227.66, 226.05, 225.19, 224.78]
x = range(len(x_title))

xdwcolor = ["#5b22c4","#b02318","#0022e3","#ffffff"]
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

y3 = [3.92, 4.11, 4.14, 4.18, 4.60, 5.41, 7.79, 9.40, 11.71, 18.44, 28.29, 48.78, 101.39, 178.30, 354.02]
y4 = [44.40, 46.45, 49.12, 56.89, 64.73, 83.53, 102.47, 53.55, 63.60, 131.22, 270.53, 549.07, 1105.96, 2220.37, 4448.78]
ylatency = [10.90569025, 11.3494405, 11.25516425, 11.3727005, 11.67127925, 15.71775825, 16.680504, 18.89748175,
            24.5918275, 80.874023, 81.1689375, 269.1671623,
            598.466558,
            1210.440283,
            6025.49152]
# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

# titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig, axs = plt.subplots(1,2,figsize=(6.33125, 2.6))

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

l1,=axs[0].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted",)
l2,=axs[0].plot(x, y4, linewidth=1.5, marker="^", markersize=5, color='black', markerfacecolor='none')
l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[0].set_yscale('log')
axs[0].set_ylabel('Request Latency (us)')
axs[0].set_xlabel('Request Size (Byte)')
axs[0].set_xlim([-2,16])
axs[0].set_ylim([1,50000])

axs[0].legend((l1, l2,l3),
        ("RDMA", "TCP-Ethernet", "TCP-IPoIB"),facecolor='white',framealpha=1.0,
        loc='best', frameon=True,ncol=1, edgecolor='white')
axs[0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0].set_xticks(x[::2])
axs[0].set_xticklabels(x_title[::2], rotation=26)

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



l4,=axs[1].plot(x, y1, linewidth=2., color=colors[3], linestyle="dotted",)
l5,=axs[1].plot(x, y2, linewidth=1.5, marker="^", markersize=5, color='black', markerfacecolor='none')
l6,=axs[1].plot(x, ybandwidth, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[1].set_yscale('log')
axs[1].set_ylabel('Bandwidth (us)')
axs[1].set_xlabel('Request Size (Byte)')

axs[1].set_xlim([-2,16])
axs[1].set_ylim([0.1,8000])

axs[1].legend((l4, l5,l6),
        ("RDMA", "TCP-Ethernet", "TCP-IPoIB"),facecolor='white',framealpha=1.0,
        loc='best', frameon=True,ncol=1, edgecolor='white')
axs[1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1].set_xticks(x[::2])
axs[1].set_xticklabels(x_title[::2], rotation=26)

fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/latency-bandwidth.pdf', dpi=100)
# fig.savefig('./newimgs/sysbench-latency-all.pdf', dpi=100)
plt.show()

plt.close()
