import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from brokenaxes import brokenaxes
import numpy as np
import matplotlib.dates as mdates

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally


plt.rc('font', family='Nimbus Sans L')
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1


fig,ax = plt.subplots()
bax = brokenaxes(xlims=None, ylims=((0, 7.5), (20.5, 23)), hspace=.1, despine=False)
fig.set_size_inches(6.5, 6.5)

plt.tick_params(top=True,bottom=False,left=True,right=False)
ax.set_axisbelow(True)


normal = np.array([1, 1, 1, 1, 1, 1])

name = ["CG.D", "EP.D", "FT.C",
        "BT.D", "MG.D", "SP.D"]

das = np.array(
    [1.060486898, 1.105696253, 1.181155967, 1.183601054, 4.453665386, 1.018700578])

singleton = np.array(
    [2.204620462, 1.906842539, 2.121451369, 1.555679081, 2.37392571, 2.298017772])

mpi = np.array(
    [1.396460873, 1.491757876, 4.505677372, 4.720506402, 21.67090648, 4.823994885])

das_l = np.array(
    [1.06, 1.11, 1.18, 1.18, 4.45, 1.02])

singleton_l = np.array(
    [2.20, 1.91, 2.12, 1.56, 2.37, 2.30])

mpi_l = np.array(
    [1.40, 1.49, 4.51, 4.72, 21.67, 4.82])

x = np.arange(len(das))

# colors = ["#366EAA", "#71A1E2", "#DDF2FF"]
colors = ["#f5f7c8", "#c3ddbd", "#7eb6bd"]

width = 0.23

sep = 0.00


def autolabel(rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects[0])):
        rect = rects[0][i]
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
        bax.text(s=s,
                x=rect.get_x() + rect.get_width() / 2 + 0.02, y=height - offset,
                va='bottom', size=11, rotation=90, ha='center')


b1 = bax.bar(x - width * 1.2 - sep, das, width,
             color=colors[0], edgecolor="black", label='DaS', linewidth=0.6)
autolabel(b1, das_l, das + 0.07)

b2 = bax.bar(x, singleton, width,
             color=colors[1], edgecolor="black", label='Singleton', linewidth=0.6)
autolabel(b2, singleton_l, singleton + 0.07)

b3 = bax.bar(x + width * 1.2 + sep, mpi, width,
             color=colors[2], edgecolor="black", label='MPI', linewidth=0.6)
autolabel(b3, mpi_l, mpi + 0.07)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp)


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

# plt.xlim(-0.5, 9.5)
# plt.ylim(0.0, 6)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')

for ax in bax.axs:
    ax.xaxis.set_major_formatter(mticker.IndexFormatter(name))

bax.grid(axis='y', linewidth=0.8, linestyle=(0, (5, 3)))
bax.legend(loc=2)
bax.tick_params(length=0)

plt.xlim([-width * 1.8 - sep - 0.05, 5 + width * 1.8 + sep + 0.05])

# plt.tight_layout()
# plt.title("Single-thread Throughput Improvement")

plt.savefig('/Users/snake0/taco-journal/newimgs/singleton-comp.pdf', dpi=300, bbox_inches='tight')

plt.show()

plt.close()
