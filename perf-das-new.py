import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally


plt.rc('font', family='Nimbus Sans L',size=12.5)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(5.9,2.5)

plt.tick_params(top=False,bottom=False,left=True,right=False)
ax.set_axisbelow(True)

normal = np.array([1, 1, 1, 1, 1, 1, 1, 1])

name = ["BT.D", "CG.D", "EP.D", "FT.C", "IS.C",
        "LU.D", "MG.D", "SP.D"]

das = np.array(
    [0.250736034, 0.759410391, 0.741203563, 0.262148367, 0.092298162, 0.139807274, 0.205513571, 0.261173644])

cfs = np.array(
    [0.211841679, 0.716095968, 0.670350072, 0.221942211, 0.069449959, 0.135831214, 0.046144816, 0.207297069])

nb = np.array(
    [0.202537123, 0.510890045, 0.662745238, 0.172002994, 0.068187233, 0.118968264, 0.034669723, 0.166057199])

das_l = np.array(
    [0.25, 0.75, 0.74, 0.26, 0.09, 0.14, 0.21, 0.26])

cfs_l = np.array(
    [0.21, 0.72, 0.67, 0.22, 0.07, 0.14, 0.05, 0.21])

nb_l = np.array(
    [0.20, 0.51, 0.66, 0.17, 0.07, 0.12, 0.03, 0.17])

x = np.arange(len(das))

# colors = ["#366EAA", "#71A1E2", "#DDF2FF"]
colors = ["#fffedd", "#c3ddbd", "#26388f"]

width = 0.2

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

                va='bottom', rotation=90,size=10, ha='center')


b1 = plt.bar(x + width * 1.25 + sep, das, width,
             color=colors[0], edgecolor="black", label='DaS (N = 2)',  linewidth=0.7)
autolabel(b1, das_l, das +0.03)

b2 = plt.bar(x, cfs, width,
             color=colors[1], edgecolor="black", label='CFS',  linewidth=0.7)
autolabel(b2, cfs_l, cfs +0.03 )

b3 = plt.bar(x - width * 1.25 - sep, nb, width,
             color=colors[2], edgecolor="black", label='NUMA Balancing',  linewidth=0.7)
autolabel(b3, nb_l, nb  +0.03)

# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp)

plt.text(s="MPI = 1.0X",x=2.7,y=0.93)


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-1., 10)
plt.ylim(0.0, 1.1)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([0, 1])
plt.xticks(x, name, rotation=00)
# plt.yticks([0,0.2,0.4,0.6,0.8,1])

# plt.grid(axis='y', linewidth=0.7, linestyle=(0, (5, 3)))
plt.grid(axis='y',linewidth=0.4,linestyle=(0,(2,4)),color = "#000000")

ax.legend(loc='upper right',facecolor='white',framealpha=1.0,
        frameon=True,ncol=1, edgecolor='white')
plt.ylabel("Normalized Results")

# ax.tick_params(length=0)

plt.xlim([-width * 1.8 - sep - 0.05-0.3, 7 + width * 1.8 + sep + 0.05+0.3])

plt.tight_layout()
# plt.title("Single-thread Throughput Improvement")

plt.savefig('/Users/snake0/taco-journal/newimgs/das-new.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
