import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

plt.rc('font', family='Nimbus Sans L',size=12.5)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

colors = ["#26388f", "#6db8be", "#a7d5b9", "#d9ecb8", "#fffedd"]

fig, axs = plt.subplots(1, 2, figsize=(5.3, 2.5))

plt.tick_params(top=False, bottom=False, left=True, right=False)
# axs[0].set_axisbelow(False)
# axs[1].set_axisbelow(False)

normal = np.array([1, 1, 1, 1, 1, 1, 1, 1])

name = ["CG.D", "EP.D"]
name1 = ["FT.C", "BT.D"]
#
# das = np.array(
#     [0.250736034, 0.759410391, 0.741203563, 0.262148367, 0.092298162, 0.139807274, 0.205513571])
# 
# cfs = np.array(
#     [0.211841679, 0.716095968, 0.670350072, 0.221942211, 0.069449959, 0.135831214, 0.046144816])
# 
# nb = np.array(
#     [0.202537123, 0.510890045, 0.662745238, 0.172002994, 0.068187233, 0.118968264, 0.034669723])

# das_l = np.array(
#     [0.25, 0.75, 0.74, 0.26, 0.09, 0.14, 0.21])
#
# cfs_l = np.array(
#     [0.21, 0.72, 0.67, 0.22, 0.07, 0.14, 0.05])
#
# nb_l = np.array(
#     [0.20, 0.51, 0.66, 0.17, 0.07, 0.12, 0.03])


# colors = ["#366EAA", "#71A1E2", "#DDF2FF"]

width = 0.14

sep = 0.03


def autolabel(ax, rects, array, heights):
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
                x=rect.get_x() + rect.get_width() / 2 + 0.01, y=height - offset,

                va='bottom', rotation=90, size=10, ha='center')


cfs8non = np.array([0.392755271, 0.501995053])

das8loc = np.array([0.473380281, 0.508202741])

cfs16non = np.array([0.865876308, 0.957225522])

das16par = np.array([0.91825048, 1.058400673])

mpi = np.array([1.209162385, 1.427948711])

cfs8non1 = np.array([0.146843807, 0.266416139])

das8loc1 = np.array([0.596267751, 0.903784378])

cfs16non1 = np.array([0.311521995, 0.414458015])

das16par1 = np.array([0.367956063, 0.490552943])

mpi1 = np.array([1.403617605, 1.956451711])

x = np.arange(len(mpi))

# axs[0].set_ylabel("Normalized Results")

t1 = axs[0].bar(x - width * 2 - 2 * sep, cfs8non, width,
                color=colors[0], edgecolor="black", label='CFS-8-Non', linewidth=0.9)
autolabel(axs[0], t1, cfs8non, cfs8non + 0.03)

t2 = axs[0].bar(x - width * 1 - sep, das8loc, width,
                color=colors[1], edgecolor="black", label='DaS-8-Loc', linewidth=0.9)
autolabel(axs[0], t2, das8loc, das8loc + 0.03)

t3 = axs[0].bar(x, cfs16non, width,
                color=colors[2], edgecolor="black", label='CFS-16-Non', linewidth=0.9)
autolabel(axs[0], t3, cfs16non, cfs16non + 0.03)

t4 = axs[0].bar(x + width + sep, das16par, width,
                color=colors[3], edgecolor="black", label='DaS-16-Cli', linewidth=0.9)
autolabel(axs[0], t4, das16par, das16par + 0.03)

t5 = axs[0].bar(x + 2 * width + 2 * sep, mpi, width,
                color=colors[4], edgecolor="black", label='MPI', linewidth=0.9)
autolabel(axs[0], t5, mpi, mpi + 0.03)

axs[0].tick_params(top=False, bottom=False, left=True, right=False)

axs[0].set_xlim(-0.55, 1.55)
axs[0].set_ylim(0.0, 2.8)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([0, 1])
axs[0].set_xticks(x)
axs[0].set_xticklabels(name, rotation=00)
# axs[0].set_yticks([0, 0.3, 0.6, 0.9, 1.2, 1.5])

# plt.grid(axis='y', linewidth=0.9, linestyle=(0, (5, 3)))
axs[0].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[0].set_axisbelow(True)

axs[0].legend((t1, t2), ("CFS-8", "DaS-8"),
              loc='upper left', frameon=False, facecolor="white", ncol=1)

s1 = axs[1].bar(x - width * 2 - 2 * sep, cfs8non1, width,
                color=colors[0], edgecolor="black", label='CFS-8-Non', linewidth=0.9)
autolabel(axs[1], t1, cfs8non1, cfs8non1 + 0.03)

s2 = axs[1].bar(x - width * 1 - sep, das8loc1, width,
                color=colors[1], edgecolor="black", label='DaS-8-Loc', linewidth=0.9)
autolabel(axs[1], t2, das8loc1, das8loc1 + 0.03)

s3 = axs[1].bar(x, cfs16non1, width,
                color=colors[2], edgecolor="black", label='CFS-16-Non', linewidth=0.9)
autolabel(axs[1], t3, cfs16non1, cfs16non1 + 0.03)

s4 = axs[1].bar(x + width + sep, das16par1, width,
                color=colors[3], edgecolor="black", label='DaS-16-Cli', linewidth=0.9)
autolabel(axs[1], t4, das16par1, das16par1 + 0.03)

s5 = axs[1].bar(x + 2 * width + 2 * sep, mpi1, width,
                color=colors[4], edgecolor="black", label='MPI', linewidth=0.9)
autolabel(axs[1], t5, mpi1, mpi1 + 0.03)

plt.tick_params(top=False, bottom=False, left=True, right=False)

# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

axs[1].set_xlim(-1., 10)
axs[1].set_ylim(0.0, 3.8)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([0, 1])
axs[1].set_xticks(x)
axs[1].set_xticklabels(name1, rotation=00)
# axs[1].set_yticks([0, 0.3, 0.6, 0.9, 1.2, 1.5])

# plt.grid(axis='y', linewidth=0.9, linestyle=(0, (5, 3)))
axs[1].grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

axs[1].set_axisbelow(True)

# axs[1].legend(
#     loc='best', frameon=False, facecolor="white", ncol=1, bbox_to_anchor=(1.05, 1.0) )\
axs[1].legend((s3, s4, s5), ('CFS-16', 'DaS-16', "MPI"),
              loc='upper left', frameon=False, facecolor="white", ncol=1)

# ax.tick_params(length=0)

plt.xlim([-width * 1.8 - sep - 0.05 - 0.3, len(x) - 1 + width * 1.8 + sep + 0.05 + 0.3])

plt.tight_layout()
# plt.title("Single-thread Throughput Improvement")

plt.savefig('/Users/snake0/taco-journal/newimgs/single-com.pdf', dpi=300)
plt.show()

plt.close()
