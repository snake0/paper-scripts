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

# y3 = [3.92, 4.11, 4.14, 4.18, 4.60, 5.41, 7.79, 9.40, 11.71, 18.44, 28.29, 48.78, 101.39, 178.30, 354.02]
# y3 = [54.3504715, 54.65364456, 54.66747284, 54.97131348, 56.65893555, 56.29882813, 58.78601074, 62.94555664,
#       79.39453125, 154.0710449, 306.6711426, 610.7666016, 1216.845703, 2445.068359, 5023.632813]
# y4 = [44.40, 46.45, 49.12, 56.89, 54.73, 50.53, 51.47, 59.55, 63.60, 131.22, 270.53, 549.07, 1105.96, 2220.37, 4448.78]
# ylatency = [10.90569025, 11.3494405, 11.25516425, 11.3727005, 11.67127925, 15.71775825, 16.680504, 18.89748175,
#             24.5918275, 80.874023, 81.1689375, 269.1671623,
#             598.466558,
#             1210.440283,
#             6025.49152]
y3 = [642, 642, 642, 642, 642, 642, 642, 642, 284, 292, 300, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299,
      299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 299, 300, 307, 312, 317, 322,
      328, 332, 336, 344, 351, 351, 351, 352, 352, 352, 354, 361, 369, 383, 389, 392, 392, 392, 392, 392, 393, 399, 406,
      414, 421, 424, 425, 425, 425, 425, 428, 436, 456, 462, 468, 474, 474, 474, 474, 474, 474, 475, 481, 489, 496, 500,
      500, 500, 500, 500, 503, 510, 518, 526, 535, 535, 535, 535, 535, 535, 539, 546, 554, 561, 571, 571, 573, 575, 577,
      588, 602, 609, 615, 621, 625, 625, 625, 625, 625, 625, 625, 628, 635, 643, 651, 652, 652, 652, 652, 653, 657, 665,
      672, 680, 686, 686, 686, 686, 686, 686, 693, 701, 708, 715, 719, 719, 719, 719, 720, 723, 731, 738, 746, 753, 753,
      753, 753, 753, 754, 762, 771, 779, 787, 788, 788, 788, 788, 788, 792, 796, 797, 798, 798, 799, 799, 799, 799, 799,
      799, 799, 799, 799, 799, 799, 799, 799, 799, 799, 799, 799, 799, 799, 799]
x = range(len(y3))
x = [0.5 * i for i in x]
x_title = [str(i) for i in x]

y4 = [773, 773, 773, 773, 773, 773, 773, 773, 35, 37, 37, 38, 38, 37, 37, 37, 45, 48, 58, 64, 69, 75, 80, 85, 89, 94,
      100, 105, 108, 108, 108, 108, 108, 109, 112, 116, 121, 125, 132, 138, 142, 147, 148, 148, 148, 149, 149, 153, 165,
      177, 189, 201, 213, 225, 237, 248, 260, 272, 284, 288, 288, 288, 289, 294, 298, 304, 312, 319, 324, 328, 332, 336,
      338, 340, 340, 340, 340, 340, 340, 344, 352, 359, 365, 365, 365, 365, 365, 366, 370, 378, 385, 392, 399, 399, 399,
      399, 399, 399, 403, 411, 419, 426, 435, 436, 437, 439, 441, 459, 468, 474, 480, 486, 492, 492, 492, 492, 492, 492,
      492, 492, 498, 506, 513, 517, 517, 517, 517, 517, 522, 530, 538, 546, 548, 550, 550, 550, 550, 550, 550, 550, 550,
      550, 550, 551, 551, 551, 551, 551, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552,
      552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552,
      552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552, 552]
# colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

# titles = ["{4KiB,local,write,*}", "{4KiB,global,read,*}", "{4KiB,global,write,*}", "{4MiB,global,write,*}"]

fig, axs = plt.subplots(1, 1, figsize=(9, 2.7))

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

l1, = axs.plot(x, y3, linewidth=2.0, color=colors[3], linestyle="dotted", )
l2, = axs.plot(x, y4, linewidth=1.5, color=colors[0])
# l3,=axs[0].plot(x, ylatency, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# ax1.set_ylim(1, 10000)
# axs.set_yscale('log')
axs.set_xlabel('VM Execution Time (s)')
axs.set_ylabel('Local Cache Size (MiB)')
axs.set_xlim([-2.7, 102])
# axs.set_ylim([0, 10000])

axs.legend((l1, l2),
           ("Enable XBZRLE", "Disable XBZRLE"), facecolor='white', framealpha=1.0,
           loc='best', frameon=True, ncol=1, edgecolor='white')
axs.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
axs.spines['bottom'].set_visible(False)
# axs.axvline(3.9,linewidth=1.7,color="#a52416", linestyle="dotted")

axs.text(0.4, 270, "Min1\n284MiB", size=9, weight="bold",horizontalalignment='center')
axs.text(0.5, 38, "Min2\n35MiB", size=9, weight="bold",horizontalalignment='center')

axs.text(178/2, 799-120, "Max1\n799MiB", size=9, weight="bold",horizontalalignment='center')
axs.text(135/2, 552-120, "Max2\n552MiB", size=9, weight="bold",horizontalalignment='center')


# axs.set_xticks(x[::2])
# axs.set_xticklabels(x_title[::2], rotation=26)

# axs.set_xticks(x)
# axs.set_xticklabels(x_title)

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

#
# l4, = axs[1].plot(x, y1, linewidth=2., color=colors[3], linestyle="dotted", )
# l5, = axs[1].plot(x, y2, linewidth=1.5, color=colors[0])
# # l6, = axs[1].plot(x, ybandwidth, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# # ax1.set_ylim(1, 10000)
# axs[1].set_yscale('log')
# axs[1].set_ylabel('Bandwidth (MiB/s)')
# axs[1].set_xlabel('Request Size (Byte)')
#
# axs[1].set_xlim([-2, 16])
# axs[1].set_ylim([0.5, 1000])
#
# axs[1].legend((l4, l5),
#               ("HDD", "TCP-Ethernet"), facecolor='white', framealpha=1.0,
#               loc='best', frameon=True, ncol=1, edgecolor='white')
# axs[1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
#
# axs[1].set_xticks(x[::2])
# axs[1].set_xticklabels(x_title[::2], rotation=26)
#
# x1=[1,2,4,8]
# x1_title=["1","2","4","8"]
#
# y9 = [12772.46, 13265.31, 14036.43, 14785.03]
#
# y10 = [11950.41, 11832.44, 11076.81, 10419.28]
#
# l6, = axs[2].plot(x1, y9, linewidth=2., color=colors[3], linestyle="dotted")
# l7, = axs[2].plot(x1, y10, linewidth=1.5, color=colors[0])
# # l6, = axs[1].plot(x, ybandwidth, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# # ax1.set_ylim(1, 10000)
# # axs[2].set_yscale('log')
# axs[2].set_ylabel('Mem. Through. (MiB/s)')
# axs[2].set_xlabel('# of Threads')
#
# axs[2].set_xlim([-1,10])
# axs[2].set_ylim([9500, 16000])
#
# axs[2].legend((l6, l7),
#               ("Local", "Anemoi$"), facecolor='white', framealpha=1.0,
#               loc='best', frameon=True, ncol=1, edgecolor='white')
# axs[2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
#
# axs[2].set_xticks(x1)
# axs[2].set_xticklabels(x1_title)
#
#
#
# y9 = [12464.22,12982.25,13537.26,13485.36]
#
# y10 = [11774.18,11802.1,11011.82,10767.52]
#
#
# l8, = axs[3].plot(x1, y9, linewidth=2., color=colors[3], linestyle="dotted")
# l9, = axs[3].plot(x1, y10, linewidth=1.5, color=colors[0])
# # l6, = axs[1].plot(x, ybandwidth, linewidth=1.9, marker="s", markersize=5, color=colors[0], markerfacecolor='none')
# # ax1.set_ylim(1, 10000)
# # axs[2].set_yscale('log')
# axs[3].set_ylabel('Mem. Through. (MiB/s)')
# axs[3].set_xlabel('# of Threads')
#
# axs[3].set_xlim([-1,10])
# axs[3].set_ylim([9500, 16000])
#
# axs[3].legend((l8, l9),
#               ("Local", "Anemoi$"), facecolor='white', framealpha=1.0,
#               loc='best', frameon=True, ncol=1, edgecolor='white')
# axs[3].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
#
# axs[3].set_xticks(x1)
# axs[3].set_xticklabels(x1_title)


# data1 = pd.read_excel('/Users/snake0/taco-journal/newdata/rdma-tcp-lat.xlsx', header=0, usecols=[0,1,2])
#
# x = np.arange(0, 100)
#
# y_rdma = np.array(data1['Non-owner Write RDMA'].values.tolist())
# y_tcp = np.array(data1['Non-owner Write TCP'].values.tolist())
# y_ipoib = np.array(data1['Non-owner Write IPoIB'].values.tolist())
#
# y_rdma = y_rdma / 1000
# y_tcp = y_tcp / 1000
# y_ipoib = y_ipoib / 1000
#
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
# print(rdma_50,tcp_50,iboip_50)
# print(rdma_90,tcp_90,iboip_90)
#
# y_rdma_cdf3 = 1. * np.arange(len(y_rdma_sort3)) / (len(y_rdma_sort3) - 1)
# y_tcp_cdf3 = 1. * np.arange(len(y_tcp_sort3)) / (len(y_tcp_sort3) - 1)
# y_iboip_cdf3 = 1. * np.arange(len(y_iboip_sort3)) / (len(y_iboip_sort3) - 1)
#
#
#
# axs[2].plot(y_rdma_sort3, y_rdma_cdf3,label="RDMA",linewidth=1.4,color=colors[3],linestyle="dotted")
# axs[2].plot(y_tcp_sort3, y_tcp_cdf3,label="TCP-Ethernet",linewidth=1.8, color="black")
# axs[2].plot(y_iboip_sort3, y_iboip_cdf3,label="TCP-IPoIB",linewidth=2.2, color=colors[0])
#
# # plt.scatter(rdma_90, 0.9,color = 'black', s=15,marker='s')
# # plt.scatter(tcp_90, 0.9,color = 'black', s=15,marker='s')
# # plt.scatter(iboip_90, 0.9,color = 'black', s=15,marker='s')
# #
# # plt.text(30000, 0.87, "P90",size=11,weight='bold')
#
# axs[2].set_xlabel("Non-owner Write Latency (us)")
# axs[2].set_xscale("log")
# axs[2].set_ylim([0,1])
# axs[2].set_ylabel("CDF")
# # plt.xlim([2400,184500])
# axs[2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
# # plt.title("Non-owner Write Latency")
# axs[2].set_yticks([0,0.2,0.4,0.6,0.8,1])
# # plt.scatter(0.1,0.95, s=4, c='red', marker='s')
# #
# # plt.text(0.1,0.9,"Main Memory")
# # #
# # g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# # plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
# #
# # g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# # plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))
#
# axs[2].legend(facecolor='white',framealpha=0.0,
#         loc='lower right',frameon=True,ncol=1, edgecolor='white')

# axs[0].set_title("(a) Latency")
# axs[1].set_title("(b) Bandwidth")
# axs[2].set_title("(c) Throughput (seq)")
# axs[3].set_title("(d) Throughput (rnd)")

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

fig.tight_layout()
fig.savefig('/Users/snake0/MasterThesis/figures/_memory-occupy.pdf', dpi=100)
# fig.savefig('./newimgs/sysbench-latency-all.pdf', dpi=100)
plt.show()

plt.close()
