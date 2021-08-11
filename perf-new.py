import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium', size=13)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(6.5, 3.7)

normal = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

name = ["BT.A", "CG.B", "DC.W", "EP.C", "FT.B", "IS.C",
        "LU.A", "MG.C", "SP.A", "UA.W"]

clique = np.array(
    [1.368111799, 1.124625749, 1.324786325, 1.003026373, 0.994180062, 1.194092827, 1.145605387, 1.538135853,
     2.020523498, 1.318777293])

nb = np.array(
    [0.907575036, 0.954865269, 1.025641026, 0.94638997, 0.445799351, 0.926160338, 0.904172177, 0.378904093, 0.901150109,
     0.887918486])

clique_l = np.array(
    [344.6, 150.25, 0.155, 23.2, 251.11, 5.66, 190.56, 250.67, 203.79, 0.0906])

normarl_l = np.array(
    [251.88, 133.6, 0.117, 23.13, 252.58, 4.74, 166.34, 162.97, 100.86, 0.0687])

nb_l = np.array(
    [228.6, 127.57, 0.12, 21.89, 112.6, 4.39, 150.4, 61.75, 90.89, 0.061])

x = np.arange(len(clique))

# for i in range(len(name)):
#     name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#c3ddbd", "#7eb6bd"]

width = 0.23

# sep = 0.01
sep = 0.00


def autolabel(rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.2f}".format(array[i])
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

                va='bottom', size=11, rotation=90, ha='center', weight='bold')


b1 = plt.bar(x - width * 1.2 - sep, clique, width,
             color=colors[0], edgecolor="black", label='DSM-aware', linewidth=0.6)
# b10 = plt.bar(x - width * 1.3 - sep, 100 - clique, width, bottom=clique,
#             color=colors[0], edgecolor="black", label='Application Time', linewidth=0.6)
autolabel(b1, clique_l, clique + 0.04)
# autolabel(b10, clique_e, clique + 83 - clique)

b2 = plt.bar(x, normal, width,
             color=colors[1], edgecolor="black", label='CFS', linewidth=0.6)
# b20 = plt.bar(x, 100 - normal, width, bottom=normal,
#               color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b2, normarl_l, normal + 0.04)
# autolabel(b20, normal_e, normal + 83 - normal)

b3 = plt.bar(x + width * 1.2 + sep, nb, width,
             color=colors[2], edgecolor="black", label='NUMA Balancing', linewidth=0.6)
# b30 = plt.bar(x + width * 1.3 + sep, 100 - nb, width, bottom=nb,
#              color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b3, nb_l, nb + 0.04)
# autolabel(b30, nb_e, nb + 83 - nb)
# autolabel(b1)
# autolabel(b2)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp) + 'X'


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 9.5)
plt.ylim(0.0,2.6)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# of vCPUs')
# plt.yticks([])
# plt.ylabel('Percentage of Improvement')
plt.xticks(x, name, rotation=00, size=11)

plt.grid(axis='y', linewidth=0.4)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=False, shadow=False, ncol=3, frameon=False, prop={'size': 14})

# plt.legend(
#     mode="expand", loc="upper center",
#     ncol=3, frameon=False)

ax.tick_params(length=0)

# plt.subplots_adjust(top=1.2)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# plt.plot([9.5,9.5],[min(nb)-80, max(clique)+1], linewidth=1.5, color='black')
plt.xlim([-width * 1.8 - sep - 0.05, 9 + width * 1.8 + sep + 0.05])

plt.tight_layout()
plt.title("Single-thread Throughput Improvement")
plt.savefig('/Users/snake0/taco-journal/newimgs/perf-new.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
