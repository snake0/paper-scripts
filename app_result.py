import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

# data = pd.read_excel('C:/Develop/PythonDemos/paper/rdma-tcp-lat.xlsx', header=0, usecols=[1, 3])

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium')
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
#
x = range(0, 4)
x_title = ['2x1', '2x2', '2x4', '2x8']
labels = ["Guest OS", "QEMU", "DSM", "KVM", "Router"]
width = 0.45

lword_cpu_time_real = [101612, 53572, 30558, 22448]
for i in range(len(lword_cpu_time_real)):
    lword_cpu_time_real[i] = lword_cpu_time_real[i] / 1000.0

lword_cpu_time = [693378, 639894, 815107, 1465076]
lword_ring0 = [610247, 547576, 635073, 885799]
lword_io_time = [5492, 2387, 2651, 2317]
lword_non_root = [567865, 501336, 545164, 700307]
lword_qemu = [77639, 89931, 177383, 576960]
lword_kvm = [5554, 5007, 6599, 11315]
lword_dsm_pf = [36828, 41233, 83310, 174177]
lword_router_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       lword_io_time, lword_cpu_time, lword_cpu_time_real)))
lword_non_root_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                         lword_non_root, lword_cpu_time, lword_cpu_time_real)))
lword_qemu_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     lword_qemu, lword_cpu_time, lword_cpu_time_real)))
lword_kvm_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                    lword_kvm, lword_cpu_time, lword_cpu_time_real)))
lword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       lword_dsm_pf, lword_cpu_time, lword_cpu_time_real)))

# print(lword_router_ratio/lword_cpu_time_real)
# print(lword_non_root_ratio/lword_cpu_time_real)
# print(lword_qemu_ratio/lword_cpu_time_real)
# print(lword_kvm_ratio/lword_cpu_time_real)
# print(lword_dsm_pf_ratio/lword_cpu_time_real)
# print()




lpi_cpu_time_real = [198872, 133747, 72270, 48106]
for i in range(len(lpi_cpu_time_real)):
    lpi_cpu_time_real[i] = lpi_cpu_time_real[i] / 1000.0
lpi_cpu_time = [1358537, 1409105, 1660298, 2342612]
lpi_ring0 = [1298904, 1348401, 1490163, 1870542]
lpi_io_time = [4343, 3094, 2704, 2897]
lpi_non_root = [1261494, 1294593, 1400337, 1738299]
lpi_dsm_pf = [37012, 46712, 80020, 117296]
lpi_qemu = list(map(lambda x, y, z: x - y - z,
                         lpi_cpu_time, lpi_ring0, lpi_io_time))
lpi_kvm = list(map(lambda x, y, z: x - y - z,
                        lpi_ring0, lpi_non_root, lpi_dsm_pf))
# lpi_dsm_pf = [49491, 45155, 77100, 112625]
lpi_router_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     lpi_io_time, lpi_cpu_time, lpi_cpu_time_real)))
lpi_non_root_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       lpi_non_root, lpi_cpu_time, lpi_cpu_time_real)))
lpi_qemu_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                   lpi_qemu, lpi_cpu_time, lpi_cpu_time_real)))
lpi_kvm_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                  lpi_kvm, lpi_cpu_time, lpi_cpu_time_real)))
lpi_dsm_pf_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     lpi_dsm_pf, lpi_cpu_time, lpi_cpu_time_real)))

# print(lpi_router_ratio/lpi_cpu_time_real)
# print(lpi_non_root_ratio/lpi_cpu_time_real)
# print(lpi_qemu_ratio/lpi_cpu_time_real)
# print(lpi_kvm_ratio/lpi_cpu_time_real)
# print(lpi_dsm_pf_ratio/lpi_cpu_time_real)
# print()


lpr_cpu_time_real = [69233, 50220, 37021, 112406]
for i in range(len(lpr_cpu_time_real)):
    lpr_cpu_time_real[i] = lpr_cpu_time_real[i] / 1000.0
lpr_cpu_time = [409473, 1308594, 1004614, 5231691]
lpr_ring0 = [341238, 1098102, 675342, 3173771]
lpr_io_time = [3181, 3649, 4845, 166504]
lpr_non_root = [252168, 920720, 343660, 1844862]
lpr_qemu = [65054, 206843, 324427, 1891416]
lpr_kvm = [8268, 14090, 16916, 104241]
lpr_dsm_pf = [80802, 163292, 314766, 1224668]
lpr_router_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     lpr_io_time, lpr_cpu_time, lpr_cpu_time_real)))
lpr_non_root_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       lpr_non_root, lpr_cpu_time, lpr_cpu_time_real)))
lpr_qemu_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                   lpr_qemu, lpr_cpu_time, lpr_cpu_time_real)))
lpr_kvm_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                  lpr_kvm, lpr_cpu_time, lpr_cpu_time_real)))
lpr_dsm_pf_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     lpr_dsm_pf, lpr_cpu_time, lpr_cpu_time_real)))
#
# print(lpr_router_ratio/lpr_cpu_time_real)
# print(lpr_non_root_ratio/lpr_cpu_time_real)
# print(lpr_qemu_ratio/lpr_cpu_time_real)
# print(lpr_kvm_ratio/lpr_cpu_time_real)
# print(lpr_dsm_pf_ratio/lpr_cpu_time_real)


# colors = ["#1e307c", "#3b7cb1", "#6db8be", "#a7d5b9", "#d9ecb8"]
# colors = ["#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
# colors = ["#ffffff", "#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1"]
colors = ["#26388f", "#6db8be", "#ddebbd", "#ffffff", "#fffedd"]

titles = ["(a) WordCount", "(b) Pi", "(c) PageRank"]

fig, axs = plt.subplots(1, 4, figsize=(10.13, 2.4))

# plt.subplot(131)
axs[0].set_title("(a) WordCount")
axs[0].set_xlim(-0.99, 3.99)
axs[0].set_ylim(0, 120)
axs[0].set_xlabel('# vCPUs')
axs[0].set_ylabel('Execution Time (s)')
axs[0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
rb = axs[0].bar(x, lword_router_ratio, width, label='Router', color=colors[0], zorder=10, edgecolor='black',
                linewidth=0.85)
qb = axs[0].bar(x, lword_qemu_ratio, width, bottom=lword_router_ratio, label='QEMU', color=colors[1], zorder=10,
                edgecolor='black', linewidth=0.85)
axs[0].bar(x, lword_dsm_pf_ratio, width, bottom=lword_router_ratio + lword_qemu_ratio, label='DSM',
           color=colors[2], zorder=10, edgecolor='black', linewidth=0.85)
axs[0].bar(x, lword_kvm_ratio, width, bottom=lword_router_ratio + lword_qemu_ratio + lword_dsm_pf_ratio, label='KVM',
           color=colors[3], zorder=10, edgecolor='black', linewidth=0.85)
axs[0].bar(x, lword_non_root_ratio, width,
           bottom=lword_router_ratio + lword_qemu_ratio + lword_dsm_pf_ratio + lword_kvm_ratio,
           label='Guest OS', color=colors[4], zorder=10, edgecolor='black', linewidth=0.85)

axs[0].legend((rb, qb),
              ("Router", "QEMU"), facecolor='white', framealpha=1.0,
              loc='best', frameon=True, ncol=1, edgecolor='white')

# g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
# axs[0].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs[0].set_xticks(x)
axs[0].set_xticklabels(x_title)

# [i.set_linewidth(0.5) for i in axs[0].spines.itervalues()]

# plt.subplot(132)
axs[1].set_title("(b) Pi")
axs[1].set_xlim(-0.99, 3.99)
axs[1].set_ylim(0, 250)
axs[1].set_xlabel('# vCPUs')
# axs[1].set_ylabel('Execution Time (s)')
axs[1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
axs[1].bar(x, lpi_router_ratio, width, color=colors[0], zorder=10, edgecolor='black', linewidth=0.85)
axs[1].bar(x, lpi_qemu_ratio, width, bottom=lpi_router_ratio, color=colors[1], zorder=10, linewidth=0.85,
           edgecolor='black')
db = axs[1].bar(x, lpi_dsm_pf_ratio, width, bottom=lpi_router_ratio + lpi_qemu_ratio, label='DSM', color=colors[2],
                zorder=10, edgecolor='black', linewidth=0.85)
kb = axs[1].bar(x, lpi_kvm_ratio, width, bottom=lpi_router_ratio + lpi_qemu_ratio + lpi_dsm_pf_ratio,
                color=colors[3], zorder=10, edgecolor='black', linewidth=0.85)
axs[1].bar(x, lpi_non_root_ratio, width, bottom=lpi_router_ratio + lpi_qemu_ratio + lpi_dsm_pf_ratio + lpi_kvm_ratio,
           color=colors[4], zorder=10, edgecolor='black', linewidth=0.85)
axs[1].legend(facecolor='white', framealpha=1.0,
              loc='best', frameon=True, edgecolor='white')

axs[1].set_xticks(x)
axs[1].set_xticklabels(x_title)
# [i.set_linewidth(0.5) for i in axs[1].spines.itervalues()]


# plt.subplot(133)
axs[2].set_title("(c) PageRank")
axs[2].set_xlim(-0.99, 3.99)
axs[2].set_ylim(0, 150)

axs[2].set_xlabel('# vCPUs')
# axs[2].set_ylabel('Execution Time (s)')
axs[2].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
axs[2].bar(x, lpr_router_ratio, width, color=colors[0], zorder=10, edgecolor='black', linewidth=0.85)
axs[2].bar(x, lpr_qemu_ratio, width, bottom=lpr_router_ratio, color=colors[1], zorder=10,
           edgecolor='black', linewidth=0.85)
axs[2].bar(x, lpr_dsm_pf_ratio, width, bottom=lpr_router_ratio + lpr_qemu_ratio, color=colors[2],
           zorder=10, edgecolor='black', linewidth=0.85)
kkb = axs[2].bar(x, lpr_kvm_ratio, width, bottom=lpr_router_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio, label='KVM',
                 color=colors[3], zorder=10, edgecolor='black', linewidth=0.85)
gb = axs[2].bar(x, lpr_non_root_ratio, width,
                bottom=lpr_router_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio + lpr_kvm_ratio,
                color=colors[4], zorder=10, edgecolor='black', linewidth=0.85)

axs[2].legend(facecolor='white', framealpha=1.0,
              loc='best', frameon=True, edgecolor='white')

axs[2].set_xticks(x)
axs[2].set_xticklabels(x_title)
# [i.set_linewidth(0.5) for i in axs[2].spines.itervalues()]

#
# axs[3].set_title("TCP vs. RDMA")
# axs[3].set_xlim(-0.99, 3.99)
# axs[3].set_ylim(0, 150)
#
# axs[3].set_xlabel('# vCPUs')
# # axs[2].set_ylabel('Execution Time (s)')
# axs[3].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
# axs[3].bar(x, lpr_router_ratio, width, color=colors[0], zorder=10, edgecolor='black',linewidth=0.85)
# axs[3].bar(x, lpr_qemu_ratio, width, bottom=lpr_router_ratio,  color=colors[1], zorder=10,
#           edgecolor='black',linewidth=0.85)
# axs[3].bar(x, lpr_dsm_pf_ratio, width, bottom=lpr_router_ratio + lpr_qemu_ratio, color=colors[2],
#            zorder=10, edgecolor='black',linewidth=0.85)
# axs[3].bar(x, lpr_kvm_ratio, width, bottom=lpr_router_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio,
#            color=colors[3], zorder=10, edgecolor='black',linewidth=0.85)
# gb = axs[3].bar(x, lpr_non_root_ratio, width, bottom=lpr_router_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio + lpr_kvm_ratio,
#            label=labels[0], color=colors[4], zorder=10, edgecolor='black',linewidth=0.85)
#
# axs[3].legend(facecolor='white',framealpha=1.0,
#         loc='best',frameon=True,ncol=1, edgecolor='white')
#
# axs[3].set_xticks(x)
# axs[3].set_xticklabels(x_title)

x_title1 = ['WC-RDMA', 'WC-TCP', 'Pi-RDMA', 'Pi-TCP', 'PR-RDMA', 'PR-TCP']
x1 = np.arange(3)
x_ticks1 = [-0.35, 0.1, 0.7, 1.15, 1.66, 2.1]
labels1 = ["Guest OS", "QEMU", "DSM", "KVM", "Router"]
width1 = 0.28



sword_cpu_time_real = [51894, 90509, 57326]
for i in range(len(sword_cpu_time_real)):
    sword_cpu_time_real[i] = sword_cpu_time_real[i] / 1000.0

sword_cpu_time = [395303, 674493, 277590]
sword_ring0 = [252756, 430361, 217714]
sword_io_time = [47, 51, 51]
sword_non_root = [248778, 425364, 167476]
sword_qemu = [42500, 44081, 59825]
sword_kvm = [930, 1431, 4206]
sword_dsm_pf = [3048, 3566, 46032]
sword_router_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       sword_io_time, sword_cpu_time, sword_cpu_time_real)))
sword_non_root_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                         sword_non_root, sword_cpu_time, sword_cpu_time_real)))
sword_qemu_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     sword_qemu, sword_cpu_time, sword_cpu_time_real)))
sword_kvm_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                    sword_kvm, sword_cpu_time, sword_cpu_time_real)))
sword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       sword_dsm_pf, sword_cpu_time, sword_cpu_time_real)))

# print(lpr_router_ratio/lpr_cpu_time_real)
# print(lpr_non_root_ratio/lpr_cpu_time_real)
# print(lpr_qemu_ratio/lpr_cpu_time_real)
# print(lpr_kvm_ratio/lpr_cpu_time_real)
print(sword_dsm_pf_ratio/sword_cpu_time_real)

# TCP

tword_cpu_time_real = [59646, 93950, 255695]
for i in range(len(tword_cpu_time_real)):
    tword_cpu_time_real[i] = tword_cpu_time_real[i] / 1000.0

tword_cpu_time = [369108, 553912, 618344]
tword_ring0 = [294545, 454104, 497690]
tword_io_time = [182, 182, 183]
tword_non_root = [248717, 421169, 234428]
tword_qemu = [74381, 99626, 120471]
tword_kvm = [1430, 1396, 6390]
tword_dsm_pf = [44398, 31539, 256872]
tword_router_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       tword_io_time, tword_cpu_time, tword_cpu_time_real)))
tword_non_root_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                         tword_non_root, tword_cpu_time, tword_cpu_time_real)))
tword_qemu_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                     tword_qemu, tword_cpu_time, tword_cpu_time_real)))
tword_kvm_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                    tword_kvm, tword_cpu_time, tword_cpu_time_real)))
tword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: x * z / y,
                                       tword_dsm_pf, tword_cpu_time, tword_cpu_time_real)))
print(tword_dsm_pf_ratio/tword_cpu_time_real)


# colors = ["#1e307c", "#3b7cb1", "#6db8be", "#a7d5b9", "#d9ecb8"]
# colors = ["#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
# colors = ["#ffffff", "#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1"]

titles1 = ["WordCount", "Pi", "PageRank"]


axs[3].set_title("(d) RDMA vs. TCP")
axs[3].set_xlim(-0.59, 2.59)
axs[3].set_ylim(0, 300)
# axs.set_xlabel('Tasks')
# axs.set_ylabel('Execution Time (s)')
axs[3].grid(axis='y', linewidth=0.6, linestyle="--")
axs[3].tick_params(bottom=False, top=False, left=True, right=False)
# RDMA
ro = axs[3].bar(x1 - width1 * 0.6, sword_router_ratio, width1, color=colors[0], zorder=10, edgecolor='black',
             linewidth=0.95)
qe = axs[3].bar(x1 - width1 * 0.6, sword_qemu_ratio, width1, bottom=sword_router_ratio, color=colors[1], zorder=10,
             edgecolor='black', linewidth=0.95)
dp = axs[3].bar(x1 - width1 * 0.6, sword_dsm_pf_ratio, width1, bottom=sword_router_ratio + sword_qemu_ratio,
             color=colors[2], zorder=10, edgecolor='black', linewidth=0.95)
kv = axs[3].bar(x1 - width1 * 0.6, sword_kvm_ratio, width1, bottom=sword_router_ratio + sword_qemu_ratio + sword_dsm_pf_ratio,

             color=colors[3], zorder=10, edgecolor='black', linewidth=0.95)
nr = axs[3].bar(x1 - width1 * 0.6, sword_non_root_ratio, width1,
             bottom=sword_router_ratio + sword_qemu_ratio + sword_dsm_pf_ratio + sword_kvm_ratio,
             color=colors[4], zorder=10, edgecolor='black',label='Guest OS', linewidth=0.95)
# TCP
axs[3].bar(x1 + width1 * 0.6, tword_router_ratio, width1, color=colors[0], zorder=10, edgecolor='black',
        linewidth=0.95, linestyle='dotted')
axs[3].bar(x1 + width1 * 0.6, tword_qemu_ratio, width1, bottom=tword_router_ratio, color=colors[1], zorder=10,
        edgecolor='black', linewidth=0.95, linestyle='dotted')
axs[3].bar(x1 + width1 * 0.6, tword_dsm_pf_ratio, width1, bottom=tword_router_ratio + tword_qemu_ratio,
        color=colors[2], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')
axs[3].bar(x1 + width1 * 0.6, tword_kvm_ratio, width1, bottom=tword_router_ratio + tword_qemu_ratio + tword_dsm_pf_ratio,

        color=colors[3], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')
axs[3].bar(x1 + width1 * 0.6, tword_non_root_ratio, width1,
        bottom=tword_router_ratio + tword_qemu_ratio + tword_dsm_pf_ratio + tword_kvm_ratio,
         color=colors[4], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')

axs[3].legend(facecolor='white',framealpha=1.0,
        loc='best', frameon=True,ncol=1, edgecolor='white')

# g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
# axs[0].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs[3].set_xticks(x_ticks1)
axs[3].set_xticklabels(x_title1, rotation=30)

# axs[2].legend(facecolor='white',framealpha=1.0,loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
# plt.title(titles[0])
#
fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/breakdown.pdf', dpi=100,pad_inches=0.1)
# fig.savefig('./newimgs/non-write-latency.pdf', dpi=100)
plt.show()

plt.close()
