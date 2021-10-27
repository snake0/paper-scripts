import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
import pandas as pd
import seaborn as sns

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

# data = pd.read_excel('C:/Develop/PythonDemos/paper/rdma-tcp-lat.xlsx', header=0, usecols=[1, 3])

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium')
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
#

x_title = ['WC-RDMA', 'WC-TCP', 'Pi-RDMA', 'Pi-TCP', 'PR-RDMA', 'PR-TCP']
x = np.arange(3)
x_ticks = [-0.35, 0.1, 0.7, 1.15, 1.66, 2.1]
labels = ["Guest OS", "QEMU", "DSM PF", "KVM", "Router"]
width = 0.32

# RDMA

sword_cpu_time_real = [51894, 90509, 57326]
for i in range(len(sword_cpu_time_real)):
    sword_cpu_time_real[i] = sword_cpu_time_real[i] / 1000.0

sword_cpu_time = [395303, 674493, 277590]
sword_ring0 = [252756, 430361, 217714]
sword_io_time = [47, 51, 51]
sword_non_root = [248778, 425364, 167476]
sword_qemu = [142500, 244081, 59825]
sword_kvm = [930, 1431, 4206]
sword_dsm_pf = [3048, 3566, 46032]
sword_router_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       sword_io_time, sword_cpu_time, sword_cpu_time_real)))
sword_non_root_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                         sword_non_root, sword_cpu_time, sword_cpu_time_real)))
sword_qemu_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     sword_qemu, sword_cpu_time, sword_cpu_time_real)))
sword_kvm_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                    sword_kvm, sword_cpu_time, sword_cpu_time_real)))
sword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       sword_dsm_pf, sword_cpu_time, sword_cpu_time_real)))

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
tword_router_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       tword_io_time, tword_cpu_time, tword_cpu_time_real)))
tword_non_root_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                         tword_non_root, tword_cpu_time, tword_cpu_time_real)))
tword_qemu_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                     tword_qemu, tword_cpu_time, tword_cpu_time_real)))
tword_kvm_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                    tword_kvm, tword_cpu_time, tword_cpu_time_real)))
tword_dsm_pf_ratio = np.array(list(map(lambda x, y, z: (x / y) * z,
                                       tword_dsm_pf, tword_cpu_time, tword_cpu_time_real)))

# colors = ["#1e307c", "#3b7cb1", "#6db8be", "#a7d5b9", "#d9ecb8"]
# colors = ["#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
# colors = ["#ffffff", "#d9ecb8", "#a7d5b9", "#6db8be", "#3b7cb1"]
colors = ["#26388f", "#6db8be", "#a7d5b9", "#d9ecb8", "#fffedd"]

titles = ["Wordcount", "Pi", "Pagerank"]

fig, axs = plt.subplots(1, 1, figsize=(6.13, 4.4))

# plt.subplot(131)
axs.set_title("RDMA V.S TCP")
axs.set_xlim(-0.99, 2.99)
axs.set_ylim(0, 300)
axs.set_xlabel('Tasks')
axs.set_ylabel('Execution Time (s)')
axs.grid(axis='y', linewidth=0.6, linestyle="--")
axs.tick_params(bottom=False, top=False, left=True, right=False)
# RDMA
ro = axs.bar(x - width * 0.6, sword_router_ratio, width, label='Router', color=colors[0], zorder=10, edgecolor='black',
        linewidth=0.95)
qe = axs.bar(x - width * 0.6, sword_qemu_ratio, width, bottom=sword_router_ratio, label='QEMU', color=colors[1], zorder=10,
        edgecolor='black', linewidth=0.95)
dp = axs.bar(x - width * 0.6, sword_dsm_pf_ratio, width, bottom=sword_router_ratio + sword_qemu_ratio, label='DSM PF',
        color=colors[2], zorder=10, edgecolor='black', linewidth=0.95)
kv = axs.bar(x - width * 0.6, sword_kvm_ratio, width, bottom=sword_router_ratio + sword_qemu_ratio + sword_dsm_pf_ratio,
        label='KVM',
        color=colors[3], zorder=10, edgecolor='black', linewidth=0.95)
nr = axs.bar(x - width * 0.6, sword_non_root_ratio, width,
        bottom=sword_router_ratio + sword_qemu_ratio + sword_dsm_pf_ratio + sword_kvm_ratio,
        label='Guest OS', color=colors[4], zorder=10, edgecolor='black', linewidth=0.95)
# TCP
axs.bar(x + width * 0.6, tword_router_ratio, width, label='Router', color=colors[0], zorder=10, edgecolor='black',
        linewidth=0.95, linestyle='dotted')
axs.bar(x + width * 0.6, tword_qemu_ratio, width, bottom=tword_router_ratio, label='QEMU', color=colors[1], zorder=10,
        edgecolor='black', linewidth=0.95, linestyle='dotted')
axs.bar(x + width * 0.6, tword_dsm_pf_ratio, width, bottom=tword_router_ratio + tword_qemu_ratio, label='DSM PF',
        color=colors[2], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')
axs.bar(x + width * 0.6, tword_kvm_ratio, width, bottom=tword_router_ratio + tword_qemu_ratio + tword_dsm_pf_ratio,
        label='KVM',
        color=colors[3], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')
axs.bar(x + width * 0.6, tword_non_root_ratio, width,
        bottom=tword_router_ratio + tword_qemu_ratio + tword_dsm_pf_ratio + tword_kvm_ratio,
        label='Guest OS', color=colors[4], zorder=10, edgecolor='black', linewidth=0.95, linestyle='dotted')

axs.legend((ro, qe, dp, kv, nr),
        ("Router", "QEMU", "DSM PF", "KVM", "Non-Root"),facecolor='white',framealpha=1.0,
        loc='best', frameon=True,ncol=1, edgecolor='white')

# g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
# axs[0].yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xticks(x_ticks)
axs.set_xticklabels(x_title, rotation=30)

#
fig.tight_layout()
# fig.savefig('/Users/snake0/taco-journal/newimgs/breakdown.pdf', dpi=100)
fig.savefig('./newimgs/non-write-latency-2.pdf', dpi=100)
plt.show()

plt.close()
