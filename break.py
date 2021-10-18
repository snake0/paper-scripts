import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Arial', weight='medium', size=13)
# plt.rc('font', family='DejaVu Serif', weight='medium', size=13)

plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

# name = ["BT.A", "CG.B", "DC.W", "EP.C", "FT.B", "IS.C",
#         "LU.A", "MG.C", "SP.A", "UA.W"]

name = ["Apache", "MP3 Encoding", "OLTP RO", "OLTP RW", "PageRank", "Redis GET", "Redis GET/SET", "Restnet50 Inference",
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

vanilla0 = np.array([18.87, 19.51, 20.13, 20.18, 30.18, 26.75, 26.91, 19.71, 19.84, 20.84, 18.73, 28.41])
yanni0 = np.array(
    [18.87, 19.51, 20.13, 20.18, 30.18, 26.75, 26.91, 19.71, 19.84, 20.84, 18.73, 28.41])
vanilla1 = np.array([1.84, 2.33, 3.14, 5.43, 28.27, 26.66, 38.26, 3.76, 11.36, 9.76, 4.89, 24.36])
yanni1 = np.array([1.84, 2.33, 3.14, 5.43, 28.27, 26.66, 38.26, 3.76, 11.36, 9.76, 4.89, 24.36])
vanilla2 = np.array([1.73, 2.49, 3.66, 5.97, 27.46, 25.92, 20.87, 3, 9.45, 9.69, 1.51, 20.88])
yanni2 = np.array([1.73, 2.49, 3.66, 5.97, 27.46, 25.92, 20.87, 3, 9.45, 9.69, 1.51, 20.88])
vanilla3 = np.array([1.89, 2.55, 3.65, 5.96, 31.43, 25.3, 21.74, 2.76, 10.49, 13.14, 1.79, 20.73])
yanni3 = np.array([1.89, 2.55, 3.65, 5.96, 31.43, 25.3, 21.74, 2.76, 10.49, 13.14, 1.79, 20.73])

vanilla01 = np.array(
    [75.173, 78.603, 83.582, 82.632, 118.822, 106.378, 100.044, 89.211, 89.223, 91.121, 75.524, 76.843])
yanni01 = np.array([74.533, 81.187, 83.774, 83.582, 117.47, 104.824, 97.761, 88.432, 91.352, 91.119, 77.709, 77.229])
vanilla02 = np.array([4.432, 12.377, 17.32, 26.753, 105.003, 105.02, 104.623, 21.955, 46.289, 52.163, 29.832, 67.378])
yanni02 = np.array([2.296, 7.93, 13.389, 23.294, 102.568, 47.143, 93.886, 16.452, 40.812, 46.632, 27.803, 66.095])
vanilla03 = np.array([2.201, 8.504, 13.013, 24.946, 101.382, 48.58, 58.57, 11.832, 48.038, 47.843, 1.315, 40.198])
yanni03 = np.array([5.051, 11.821, 16.726, 28.215, 103.044, 103.496, 72.925, 16.621, 49.771, 50.732, 5.167, 44.414])
vanilla04 = np.array([5.474, 10.337, 16.275, 27.729, 111.591, 98.271, 72.964, 14.927, 49.07, 42.702, 7.145, 43.604])
yanni04 = np.array([2.874, 7.426, 12.666, 24.041, 108.784, 47.033, 60.031, 9.792, 42.176, 36.724, 2.898, 39.285])

vanilla11 = np.array([8.634, 12.745, 11.547, 11.915, 59.679, 11.651, 11.026, 17.293, 17.647, 19.098, 9.821, 10.324])
yanni11 = np.array([8.795, 11.556, 11.652, 12.199, 59.131, 11.512, 11.168, 16.247, 15.58, 19.194, 10.263, 10.307])
vanilla12 = np.array([4.534, 8.423, 7.759, 9.594, 46.105, 14.076, 14.215, 14.097, 19.227, 24.973, 9.259, 12.303])
yanni12 = np.array([1.72, 4.035, 5.605, 7.06, 43.618, 6.746, 11, 7.59, 12.685, 18.486, 7.55, 10.393])
vanilla13 = np.array([2.095, 5.567, 5.911, 8.626, 41.729, 7.525, 10.019, 7.508, 20.417, 28.175, 1.432, 8.8])
yanni13 = np.array([4.998, 7.602, 8.085, 11.198, 44.595, 14.668, 12.425, 14.667, 25.801, 36.264, 8.269, 13.476])
vanilla14 = np.array([4.792, 7.203, 8.007, 12.237, 41.052, 15.581, 13.126, 14.836, 23.943, 25.748, 8.742, 13.616])
yanni14 = np.array([2.034, 4.248, 6.204, 8.581, 40.119, 7.598, 9.776, 6.847, 19.21, 18.773, 2.235, 8.478])

data = [vanilla0, yanni0, vanilla1, yanni1, vanilla2, yanni2, vanilla3, yanni3]
x = np.arange(len(name))

# y = np.array([0] * len(x))
# for i in range(len(data)):
#     data[i] = data[i] + y
# for i in range(len(name)):
#     name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#d9e7d6", "#7eb6bd"]

width = 0.1

# sep = 0.01
zoom = 0.85

vstr = "Node 0"
ystr = "Node 1"

fig, ax1 = plt.subplots()

fig.set_size_inches(12.705, 3.503)


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
b01 = ax1.bar(x - 7 * width / 2, vanilla01, width * zoom, bottom=vanilla0,
              color=colors[0], edgecolor="black", linewidth=0.6)
b11 = ax1.bar(x - 7 * width / 2, vanilla11, width * zoom, bottom=vanilla01,
              color=colors[0], edgecolor="black", linewidth=0.6)

b2 = ax1.bar(x - 5 * width / 2, yanni0, width * zoom,
             color=colors[1], edgecolor="black", label=ystr, linewidth=0.6)
b02 = ax1.bar(x - 5 * width / 2, yanni01, width * zoom, bottom=yanni0,
              color=colors[1], edgecolor="black", linewidth=0.6)
b12 = ax1.bar(x - 5 * width / 2, yanni11, width * zoom, bottom=yanni01,
              color=colors[1], edgecolor="black", linewidth=0.6)

b3 = ax1.bar(x - 3 * width / 2, vanilla1, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)
b03 = ax1.bar(x - 3 * width / 2, vanilla02, width * zoom, bottom=vanilla1,
              color=colors[0], edgecolor="black", linewidth=0.6)
b13 = ax1.bar(x - 3 * width / 2, vanilla12, width * zoom, bottom=vanilla02,
              color=colors[0], edgecolor="black", linewidth=0.6)

b4 = ax1.bar(x - 1 * width / 2, yanni1, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)
b04 = ax1.bar(x - 1 * width / 2, yanni02, width * zoom, bottom=yanni1,
              color=colors[1], edgecolor="black", linewidth=0.6)
b14 = ax1.bar(x - 1 * width / 2, yanni12, width * zoom, bottom=yanni02,
              color=colors[1], edgecolor="black", linewidth=0.6)

b5 = ax1.bar(x + 1 * width / 2, vanilla2, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)
b05 = ax1.bar(x + 1 * width / 2, vanilla03, width * zoom, bottom=vanilla2,
              color=colors[0], edgecolor="black", linewidth=0.6)
b15 = ax1.bar(x + 1 * width / 2, vanilla13, width * zoom, bottom=vanilla03,
              color=colors[0], edgecolor="black", linewidth=0.6)

b6 = ax1.bar(x + 3 * width / 2, yanni2, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)
b06 = ax1.bar(x + 3 * width / 2, yanni03, width * zoom, bottom=yanni2,
              color=colors[1], edgecolor="black", linewidth=0.6)
b16 = ax1.bar(x + 3 * width / 2, yanni13, width * zoom, bottom=yanni03,
              color=colors[1], edgecolor="black", linewidth=0.6)

b7 = ax1.bar(x + 5 * width / 2, vanilla3, width * zoom,
             color=colors[0], edgecolor="black", linewidth=0.6)
b07 = ax1.bar(x + 5 * width / 2, vanilla04, width * zoom, bottom=vanilla3,
              color=colors[0], edgecolor="black", linewidth=0.6)
b17 = ax1.bar(x + 5 * width / 2, vanilla14, width * zoom, bottom=vanilla04,
              color=colors[0], edgecolor="black", linewidth=0.6)

b8 = ax1.bar(x + 7 * width / 2, yanni3, width * zoom,
             color=colors[1], edgecolor="black", linewidth=0.6)
b08 = ax1.bar(x + 7 * width / 2, yanni04, width * zoom, bottom=yanni3,
              color=colors[1], edgecolor="black", linewidth=0.6)
b18 = ax1.bar(x + 7 * width / 2, yanni14, width * zoom, bottom=yanni04,
              color=colors[1], edgecolor="black", linewidth=0.6)

plt.legend([b1, b2], [vstr, ystr], loc='best', ncol=2)
plt.legend([b1, b01, b11], ["Migration", "Sync", "Compression"], loc='best', ncol=3)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
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

# plt.yscale('log')

plt.grid(linewidth=0.4)

# ax1.legend(loc=2, frameon=False, prop={'size': 13})

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

ax1.set_ylim(0.0, 250)

# plt.text(s="Never Converge",
#          x=4 - 2 * width, y=0.05,
#
#          va='bottom', size=11, rotation=90, ha='center')
#
# plt.text(s="Never Converge",
#          x=11 - 2 * width, y=0.05,
#
#          va='bottom', size=11, rotation=90, ha='center')


plt.text(s="Migration 0 to 1",
         x=0 - 3 * width, y=vanilla0[0] + 100,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="Migration 1 to 0",
         x=0 - 1 * width, y=vanilla0[0] + 100,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="Migration 0 to 1",
         x=0 + 1 * width, y=vanilla0[0] + 100,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

plt.text(s="Migration 1 to 0",
         x=0 + 3 * width, y=vanilla0[0] + 100,
         va='bottom', size=10, rotation=90, ha='center', weight='bold')

# plt.text(-0.4, 2.2, "Unit = Mop/s/thread")
ax1.set_ylabel("Runtime Breakdown (s)")

ax1.tick_params(labelsize='medium', width=3, color="black")

plt.tight_layout()
# plt.title("Network Bandwidth Consumption")

plt.savefig('/Users/snake0/yanni-img/break.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
