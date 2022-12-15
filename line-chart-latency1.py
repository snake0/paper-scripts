import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium', size=11)
# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


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

y3 = [5, 5, 8, 13]
y4 = [5, 17, 32, 94]

x_title = ["2G", "1G", "512M", "256M"]
x = range(len(x_title))

# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

# titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig, axs = plt.subplots(2, 3, figsize=(8.1, 5))

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

l1, = axs[0][0].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l2, = axs[0][0].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[0][0].set_yscale('log')
axs[0][0].set_ylabel('Latency (ms)')
axs[0][0].set_xlim([-0.5, 3.5])
axs[0][0].set_ylim([3, 800])

axs[0][0].legend((l1, l2),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[0][0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0][0].set_xticks(x)
axs[0][0].set_xticklabels(x_title)

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

y3 = [1.96, 2.81, 4.89, 82.96]
y4 = [2.12, 9.06, 101.13, 161.51]

l4, = axs[0][1].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l5, = axs[0][1].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[0][1].set_yscale('log')
# axs[1].set_ylabel('Latency (ms)')
axs[0][1].set_xlim([-0.5, 3.5])
axs[0][1].set_ylim([0.5, 2900])
# axs[0][1].set_ylabel('Latency (ms)')


axs[0][1].legend((l4, l5),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[0][1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0][1].set_xticks(x)
axs[0][1].set_xticklabels(x_title)

y3 = [203.33, 369.67, 407.82, 1469.6]
y4 = [240.02, 511.33, 861.95, 1561.52]

l6, = axs[0][2].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l7, = axs[0][2].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[0][2].set_yscale('log')
# axs[2].set_ylabel('Latency (ms)')
axs[0][2].set_xlim([-0.5, 3.5])
axs[0][2].set_ylim([150, 17000])
# axs[0][2].set_ylabel('Latency (ms)')


axs[0][2].legend((l6, l7),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[0][2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0][2].set_xticks(x)
axs[0][2].set_xticklabels(x_title)

y3 = [2, 2, 6, 16]
y4 = [2, 5, 16, 20]

l6, = axs[1][0].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l7, = axs[1][0].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[1][0].set_yscale('log')
axs[1][0].set_xlabel('Anemoi$ Size (MiB)')
# axs[3].set_ylabel('Latency (ms)')
axs[1][0].set_xlim([-0.5, 3.5])
axs[1][0].set_ylim([0.5, 600])

axs[1][0].legend((l6, l7),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[1][0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1][0].set_xticks(x)
axs[1][0].set_xticklabels(x_title)
axs[1][0].set_ylabel('Latency (ms)')


y3 = [2, 4, 7, 14]
y4 = [2, 16, 51, 86]

l6, = axs[1][1].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l7, = axs[1][1].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
axs[1][1].set_yscale('log')
axs[1][1].set_xlabel('Anemoi$ Size (MiB)')
# axs[4].set_ylabel('Latency (ms)')
axs[1][1].set_xlim([-0.5, 3.5])
axs[1][1].set_ylim([0.3, 2500])

axs[1][1].legend((l6, l7),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[1][1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1][1].set_xticks(x)
axs[1][1].set_xticklabels(x_title)


# axs[1][1].set_ylabel('Latency (ms)')


y3 = [14.1, 14.7, 15.1, 16.9]
y4 = [14.2, 14.5, 17.3, 19.2]

l6, = axs[1][2].plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l7, = axs[1][2].plot(x, y4, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=6.5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
# axs[1][2].set_yscale('log')
axs[1][2].set_xlabel('Anemoi$ Size (MiB)')
# axs[4].set_ylabel('Latency (ms)')
axs[1][2].set_xlim([-0.5, 3.5])
axs[1][2].set_ylim([13, 25])

axs[1][2].legend((l6, l7),
              ("Anemoi$", "Linux Swap"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')
axs[1][2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1][2].set_xticks(x)
axs[1][2].set_xticklabels(x_title)
axs[1][2].set_ylabel('Execution Time (s)')




axs[0][0].set_title("(a) Apache (Max)")
axs[0][1].set_title("(b) OLTP RO (P95)")
axs[0][2].set_title("(c) OLTP RW (P95)")
axs[1][0].set_title("(d) Redis GET (P99.99)")
axs[1][1].set_title("(e) Redis GET/SET (P99.99)")
axs[1][2].set_title("(f) MP3 Encoding")

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

fig.tight_layout()
plt.subplots_adjust(hspace=0.7)
fig.savefig('/Users/snake0/MasterThesis/figures/_latency-comp.pdf', dpi=100)
# fig.savefig('./newimgs/sysbench-latency-all.pdf', dpi=100)
plt.show()

plt.close()
