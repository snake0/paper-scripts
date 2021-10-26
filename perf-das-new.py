import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', size=13)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(6.5, 2.8)

normal = np.array([1, 1, 1, 1, 1, 1, 1, 1])

name = ["BT.D", "CG.D", "EP.D", "FT.C", "IS.C",
        "LU.D", "MG.D", "SP.D"]

das = np.array(
    [0.250736034, 0.759410391, 0.741203563, 0.262148367, 0.092298162, 0.139807274, 0.205513571, 0.211173644])

cfs = np.array(
    [0.211841679, 0.716095968, 0.670350072, 0.221942211, 0.069449959, 0.135831214, 0.046144816, 0.207297069])

nb = np.array(
    [0.202537123, 0.510890045, 0.662745238, 0.172002994, 0.068187233, 0.118968264, 0.034669723, 0.166057199])

das_l = np.array(
    [0.25, 0.75, 0.74, 0.26, 0.09, 0.14, 0.21, 0.21])

cfs_l = np.array(
    [0.21, 0.72, 0.67, 0.22, 0.07, 0.14, 0.05, 0.21])

nb_l = np.array(
    [0.20, 0.51, 0.66, 0.17, 0.07, 0.12, 0.03, 0.17])

x = np.arange(len(das))

# colors = ["#366EAA", "#71A1E2", "#DDF2FF"]
colors = ["#f5f7c8", "#c3ddbd", "#7eb6bd"]

width = 0.23

sep = 0.00


def autolabel(rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.2f}X".format(array[i])
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
                x=rect.get_x() + rect.get_width() / 2 + 0.02, y=height - offset,

                va='bottom', size=11, rotation=90, ha='center')


b1 = plt.bar(x - width * 1.2 - sep, das, width,
             color=colors[0], edgecolor="black", label='DaS', linewidth=0.6)
autolabel(b1, das_l, das + 0.07)

b2 = plt.bar(x, cfs, width,
             color=colors[1], edgecolor="black", label='CFS', linewidth=0.6)
autolabel(b2, cfs_l, cfs + 0.07)

b3 = plt.bar(x + width * 1.2 + sep, nb, width,
             color=colors[2], edgecolor="black", label='NUMA Balancing', linewidth=0.6)
autolabel(b3, nb_l, nb + 0.07)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp)


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 9.5)
plt.ylim(0.0, 1.2)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
plt.yticks([0, 1])
plt.xticks(x, name, rotation=00, size=11)

plt.grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)))

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=False, shadow=False, ncol=3, frameon=False, prop={'size': 14})

ax.tick_params(length=0)

plt.xlim([-width * 1.8 - sep - 0.05, 7 + width * 1.8 + sep + 0.05])

plt.tight_layout()
# plt.title("Single-thread Throughput Improvement")
plt.savefig('./newimgs/perf-das-new.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
