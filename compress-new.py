import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from common import *

font["font.size"] = 13
plt.rcParams.update(font)

#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['ps.fonttype'] = 42

#plt.rc('font', family='Arial', weight='medium', size=13)
# plt.rc('font', family='DejaVu Serif', weight='medium', size=13)

plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

# name = ["BT.A", "CG.B", "DC.W", "EP.C", "FT.B", "IS.C",
#         "LU.A", "MG.C", "SP.A", "UA.W"]

name = ["Apache", "MP3 Encoding", "OLTP RO", "OLTP RW", "PageRank", "Redis GET", "Redis GET/SET", "Resnet50 Inference",
        "RNN Inference", "RNN Training", "Stress-ng I/O", "Stress-ng malloc"]

# clique = np.array(
#     [1.368111799, 1.124625749, 1.324786325, 1.003026373, 0.994180062, 1.194092827, 1.145605387, 1.538135853,
#      2.020523498, 1.318777293])
#
# nb = np.array(
#     [0.907575036, 0.954865269, 0.995641026, 0.94638997, 0.445799351, 0.926160338, 0.904172177, 0.378904093, 0.901150109,
#      0.887918486])
#
# clique_l = np.array(
#     [344.6, 150.25, 0.155, 23.2, 251.11, 5.66, 190.56, 250.67, 203.79, 0.0906])
#
# normarl_l = np.array(
#     [251.88, 133.6, 0.12, 23.13, 252.58, 4.74, 166.34, 162.97, 100.86, 0.0687])
#
# nb_l = np.array(
#     [228.6, 127.57, 0.12, 21.89, 112.6, 4.39, 150.4, 61.75, 90.89, 0.061])

vanilla0 = np.array([9.1, 11.3, 9.1, 9.5, 8.8, 8.6, 8.3, 10.7, 10.3, 9, 9.9, 9.1])
yanni0 = np.array(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

vanilla1 = np.array([302.5, 72.1, 48.5, 70.3, 125.1, 53.9, 57.2, 64.9, 62.5, 63, 99.5, 197.4])
yanni1 = np.array([0.7, 2.6, 26.2, 15.8, 23.1, 23, 9, 7.3, 14.3, 3.8, 11.4, 10.1])

vanilla2 = np.array([1619.2, 1675.8, 1128, 638.3, 634.9, 279.8, 293.3, 1339.8, 694.9, 1201.5, 1613.4, 507.1])
yanni2 = np.array([4.2, 5.2, 5.4, 5.2, 6.5, 2.6, 3.4, 6.5, 5, 5.7, 4.7, 5])

vanilla3 = np.array([75, 72.8, 74, 70.9, 66.1, 49.9, 46, 82.3, 88.8, 87.8, 65.6, 46.1])
yanni3 = np.array([26.9, 25, 27.8, 27.7, 25.9, 19, 18.2, 29.2, 28.5, 28.7, 25.3, 25])

data = [vanilla0, yanni0, vanilla1, yanni1, vanilla2, yanni2, vanilla3, yanni3]
x = np.arange(len(name))

print(mean(yanni3) / mean(yanni1))
print(mean(yanni3) / mean(yanni2))

y = np.array([0] * len(x))
for i in range(len(data)):
    data[i] = data[i] + y
# for i in range(len(name)):
#     name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#d9e7d6", "#7eb6bd", "#bcdfba"]

width = 0.1

# sep = 0.01
zoom = 0.85

vstr = "Compression"
ystr = "Decompression"

fig, ax1 = plt.subplots()

fig.set_size_inches(12.705, 2.9)


def autolabel(ax, rects, array, heights):
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


b1 = ax1.bar(x - 7 * width / 2, vanilla0, width * zoom,
             color=colors[0], edgecolor="black", label=vstr, linewidth=0.6)

b2 = ax1.bar(x - 5 * width / 2, yanni0, width * zoom,
             color=colors[1], edgecolor="black", label=ystr, linewidth=0.6)

b3 = ax1.bar(x - 3 * width / 2, vanilla1, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)

b4 = ax1.bar(x - 1 * width / 2, yanni1, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)

b5 = ax1.bar(x + 1 * width / 2, vanilla2, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)

b6 = ax1.bar(x + 3 * width / 2, yanni2, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)

b7 = ax1.bar(x + 5 * width / 2, vanilla3, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)

b8 = ax1.bar(x + 7 * width / 2, yanni3, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)

# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
#
#
# def to_percent(temp, position):
#     return '%1.1f' % (temp) + 'X'
#
#
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

# plt.xlim(-0.5, 9.5)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# of vCPUs')
# plt.yticks([])
# plt.ylabel('Percentage of Improvement')
plt.xticks(x, name, rotation=12, size=11)

# g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.1e' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

plt.yscale('log')

plt.grid(linewidth=0.4)

ax1.legend(loc=2, frameon=True, prop={'size': 13}, ncol=2)

# plt.legend(
#     mode="expand", loc="upper center",
#     ncol=3, frameon=False)


# plt.subplots_adjust(top=1.2)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# plt.plot([9.5,9.5],[min(nb)-80, max(clique)+1], linewidth=1.5, color='black')
plt.xlim([0 - 8 * width / 2 - 0.05, max(x) + 8 * width / 2 + 0.05])

ax1.set_ylim(0.1, 100000000)

# plt.text(s="Never Converge",
#          x=4 - 2 * width, y=0.05,
#
#          va='bottom', size=11, rotation=90, ha='center')
#
# plt.text(s="Never Converge",
#          x=11 - 2 * width, y=0.05,
#
#          va='bottom', size=11, rotation=90, ha='center')


plt.text(s="Zero",
         x=8 - 3 * width, y=vanilla0[0] + 15000,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="SaPM",
         x=8 - 1 * width, y=vanilla0[0] + 15000,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="SiPM",
         x=8 + 1 * width, y=vanilla0[0] + 15000,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="General",
         x=8 + 3 * width, y=vanilla0[0] + 15000,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

# plt.text(s="VM Live Migration\nNever Converges",
#          x=4, y=yanni0[4] + 2000,
#          va='bottom', size=12, rotation=90, ha='center', weight='bold')
#
# plt.text(s="VM Live Migration\nNever Converges",
#          x=11, y=yanni0[4] + 1000,
#          va='bottom', size=12, rotation=90, ha='center', weight='bold')

ax2 = ax1.twinx()

xs = []
for i in range(12):
    xs.append([i - 6 * width / 2, i - 2 * width / 2, i + 2 * width / 2, i + 6 * width / 2])

ys = [[451104, 5842, 41080, 42243],
      [398083, 27321, 51122, 80979],
      [359563, 56915, 75133, 89099],
      [334398, 41858, 152599, 137341],
      [49985, 50017, 439311, 462316],
      [112021, 224424, 1110970, 110774],
      [162620, 181166, 936636, 146292],
      [329515, 43184, 78177, 142710],
      [141274, 125173, 227901, 236387],
      [266028, 105453, 119123, 239556],
      [427737, 42137, 51052, 113754],
      [442699, 42227, 137661, 286047],
      ]

for i in range(1):
    ax2.plot(xs[1 * i], ys[1 * i], marker="s", markersize=3.5, label="#Pages", color=colors[1],
             markerfacecolor='black',
             markeredgecolor="black", linestyle="None")

for i in range(1, 12):
    ax2.plot(xs[i], ys[i], marker="s", markersize=3.5, color=colors[1],
             markerfacecolor='black', markeredgecolor="black", linestyle="None")

# plt.text(-0.4, 2.2, "Unit = Mop/s/thread")
ax1.set_ylabel("(De)compression Latency/μs")
# ax2.set_ylabel("# of Pages")

# ax2.set_ylim(-3, 110)

rate = [93.1640625, 85.83984375, 81.73828125, 77.734375, 22.21679688, 50.43945313, 58.93554688, 75.24414063, 64.0625,
        94.140625, 86.57226563, 77.34375]
rates = []
for i in rate:
    rates.append("%1.1f%%" % i)

for i in range(len(rates)):
    plt.text(s=rates[i],
             x=i, y=520000,
             va='bottom', size=11, rotation=00, ha='center', weight='bold')

ax2.legend(loc=0, frameon=True, prop={'size': 13})
ticks = range(0, 1200000, 200000)
tt = []
for i in ticks:
    temp = i/1000000
    tt.append(str(temp) + "x10e6")
ax2.set_yticks(ticks)
ax2.set_yticklabels(tt)

# ax1.tick_params(labelsize='medium', width=3, color="black")
# ax2.tick_params(labelsize='medium', width=3, color="black")

plt.tight_layout()
#plt.title("Yanni (De)compression Results")

plt.savefig('imgs/compress.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()