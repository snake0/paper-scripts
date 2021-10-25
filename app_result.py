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
x = range(0, 4)
x_title = ['2x1', '2x2', '2x4', '2x8']
labels = ["Non-Root", "QEMU", "DSM PF", "KVM", "Router"]
width = 0.54

lword_cpu_time_real = [101612, 53572, 30558, 22448]
lword_cpu_time = [693378, 639894, 815107, 1465076]
lword_ring0 = [610247, 547576, 635073, 885799]
lword_io_time = [5492, 2387, 2651, 2317]
lword_non_root = [567865, 501336, 545164, 700307]
lword_qemu = [77639, 89931, 177383, 576960]
lword_kvm = [5554, 5007, 6599, 11315]
lword_dsm_pf = [36828, 41233, 83310, 174177]
lword_router_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       lword_io_time, lword_cpu_time, lword_cpu_time_real)))
lword_non_root_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                         lword_non_root, lword_cpu_time, lword_cpu_time_real)))
lword_qemu_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     lword_qemu, lword_cpu_time, lword_cpu_time_real)))
lword_kvm_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                    lword_kvm, lword_cpu_time, lword_cpu_time_real)))
lword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       lword_dsm_pf, lword_cpu_time, lword_cpu_time_real)))

lpi_cpu_time_real = [198872, 133747, 72270, 48106]
lpi_cpu_time = [1184668, 1826393, 1916052, 2455227]
lpi_ring0 = [1040361, 1354302, 1480707, 1843596]
lpi_io_time = [3682, 3392, 2070, 2190]
lpi_non_root = [984475, 1301681, 1394309, 1717229]
lpi_qemu = [140625, 468699, 433275, 609441]
lpi_kvm = [6395, 7466, 9298, 13742]
lpi_dsm_pf = [49491, 45155, 77100, 112625]
lpi_router_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     lpi_io_time, lpi_cpu_time, lpi_cpu_time_real)))
lpi_non_root_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       lpi_non_root, lpi_cpu_time, lpi_cpu_time_real)))
lpi_qemu_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                   lpi_qemu, lpi_cpu_time, lpi_cpu_time_real)))
lpi_kvm_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                  lpi_kvm, lpi_cpu_time, lpi_cpu_time_real)))
lpi_dsm_pf_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     lpi_dsm_pf, lpi_cpu_time, lpi_cpu_time_real)))

lpr_cpu_time_real = [69233, 50220, 37021, 112406]
lpr_cpu_time = [409473, 1308594, 1004614, 5231691]
lpr_ring0 = [341238, 1098102, 675342, 3173771]
lpr_io_time = [3181, 3649, 4845, 166504]
lpr_non_root = [252168, 920720, 343660, 1844862]
lpr_qemu = [65054, 206843, 324427, 1891416]
lpr_kvm = [8268, 14090, 16916, 104241]
lpr_dsm_pf = [80802, 163292, 314766, 1224668]
lpr_router_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     lpr_io_time, lpr_cpu_time, lpr_cpu_time_real)))
lpr_non_root_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       lpr_non_root, lpr_cpu_time, lpr_cpu_time_real)))
lpr_qemu_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                   lpr_qemu, lpr_cpu_time, lpr_cpu_time_real)))
lpr_kvm_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                  lpr_kvm, lpr_cpu_time, lpr_cpu_time_real)))
lpr_dsm_pf_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     lpr_dsm_pf, lpr_cpu_time, lpr_cpu_time_real)))

colors = ["#1e307c", "#3b7cb1", "#6db8be", "#a7d5b9", "#d9ecb8"]

titles = ["Wordcount", "Pi", "Pagerank"]

fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.6))

# plt.subplot(131)
axs[0].set_title("Wordcount", fontdict={'size': 18})
axs[0].set_xlim(-0.5, 3.5)
axs[0].set_xlabel('vCPUs', fontdict={'size': 16})
axs[0].set_ylabel('time (ms)', fontdict={'size': 16})
axs[0].grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)), zorder=0)
axs[0].bar(x, lword_non_root_ratio, width, label='Non-Root', color=colors[0], zorder=10, edgecolor='black')
axs[0].bar(x, lword_qemu_ratio, width, bottom=lword_non_root_ratio, label='QEMU', color=colors[1], zorder=10, edgecolor='black')
axs[0].bar(x, lword_dsm_pf_ratio, width, bottom=lword_non_root_ratio + lword_qemu_ratio, label='DSM PF',
           color=colors[2], zorder=10, edgecolor='black')
axs[0].bar(x, lword_kvm_ratio, width, bottom=lword_non_root_ratio + lword_qemu_ratio + lword_dsm_pf_ratio, label='KVM',
           color=colors[3], zorder=10, edgecolor='black')
axs[0].bar(x, lword_router_ratio, width,
           bottom=lword_non_root_ratio + lword_qemu_ratio + lword_dsm_pf_ratio + lword_kvm_ratio,
           label='Router', color=colors[4], zorder=10, edgecolor='black')

g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
axs[0].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs[0].xaxis.set_major_formatter(mticker.IndexFormatter(x_title))

# plt.subplot(132)
axs[1].set_title("Pi", fontdict={'size': 18})
axs[1].set_xlim(-0.5, 3.5)
axs[1].set_xlabel('vCPUs', fontdict={'size': 16})
# axs[1].set_ylabel('time (ms)', fontdict={'size': 16})
axs[1].grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)), zorder=0)
axs[1].bar(x, lpi_non_root_ratio, width, label='Non-Root', color=colors[0], zorder=10, edgecolor='black')
axs[1].bar(x, lpi_qemu_ratio, width, bottom=lpi_non_root_ratio, label='QEMU', color=colors[1], zorder=10,
           edgecolor='black')
axs[1].bar(x, lpi_dsm_pf_ratio, width, bottom=lpi_non_root_ratio + lpi_qemu_ratio, label='DSM PF', color=colors[2],
           zorder=10, edgecolor='black')
axs[1].bar(x, lpi_kvm_ratio, width, bottom=lpi_non_root_ratio + lpi_qemu_ratio + lpi_dsm_pf_ratio, label='KVM',
           color=colors[3], zorder=10, edgecolor='black')
axs[1].bar(x, lpi_router_ratio, width, bottom=lpi_non_root_ratio + lpi_qemu_ratio + lpi_dsm_pf_ratio + lpi_kvm_ratio,
           label='Router', color=colors[4], zorder=10, edgecolor='black')

g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
axs[1].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs[1].xaxis.set_major_formatter(mticker.IndexFormatter(x_title))

# plt.subplot(133)
axs[2].set_title("Pagerank", fontdict={'size': 18})
axs[2].set_xlim(-0.5, 3.5)
axs[2].set_xlabel('vCPUs', fontdict={'size': 16})
# axs[2].set_ylabel('time (ms)', fontdict={'size': 16})
axs[2].grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)), zorder=0)
axs[2].bar(x, lpr_non_root_ratio, width, label=labels[0], color=colors[0], zorder=10, edgecolor='black')
axs[2].bar(x, lpr_qemu_ratio, width, bottom=lpr_non_root_ratio, label=labels[1], color=colors[1], zorder=10,
           edgecolor='black')
axs[2].bar(x, lpr_dsm_pf_ratio, width, bottom=lpr_non_root_ratio + lpr_qemu_ratio, label=labels[2], color=colors[2],
           zorder=10, edgecolor='black')
axs[2].bar(x, lpr_kvm_ratio, width, bottom=lpr_non_root_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio, label=labels[3],
           color=colors[3], zorder=10, edgecolor='black')
axs[2].bar(x, lpr_router_ratio, width, bottom=lpr_non_root_ratio + lpr_qemu_ratio + lpr_dsm_pf_ratio + lpr_kvm_ratio,
           label=labels[4], color=colors[4], zorder=10, edgecolor='black')

g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
axs[2].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs[2].xaxis.set_major_formatter(mticker.IndexFormatter(x_title))

axs[2].legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)

# plt.title(titles[0])
#
fig.tight_layout()
# fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-memory-all.pdf', dpi=100)
fig.savefig('./newimgs/non-write-latency.pdf', dpi=100)
plt.show()

plt.close()
