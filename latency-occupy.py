import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium', size=9)

fig, ax = plt.subplots()
fig.set_size_inches(7, 2)

normal = [10.22150428, 10.22892095, 14.456258, 1.003155954, 21.30449186, 29.37214144, 29.92757, 8.341463218,
          15.33439944, 17.77646099]

name = ["BT.A.*", "CG.B.*", "DC.W.*", "EP.C.*", "FT.B.*", "IS.C.*",
        "LU.A.*", "MG.C.*", "SP.A.*", "UA.W.*"]

clique = [7.998315602, 4.150075209, 5.980609183, 0.671152778, 21.10172233, 29.15483553, 22.15520013, 7.949557251,
          14.81370637, 9.312773328]

nb = [19.90348932, 11.08862739, 22.08420194, 1.571802338, 19.91516387, 27.94178796, 30.49634336, 9.465316823,
      14.70520242, 9.890117065]



x = np.arange(len(clique))

# for i in range(len(name)):
#     name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#c3ddbd", "#7eb6bd"]

width = 0.19

# sep = 0.01
sep = 0


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        s = "{:.1f}%".format(height)
        l = len(s)
        if height < 0:
            offset = height - 40 - len(s) * 1.1
        else:
            offset = 0 - 40 - len(s) * 1.1
        ax.text(s=s,
                x=rect.get_x() + rect.get_width() / 2, y=offset,

                va='bottom', size=10, rotation=90, ha='center', fontweight='black')


b1 = plt.bar(x - width * 1.3 - sep, clique, width,
             label='x (DSM-aware Scheduler)', color=colors[0], edgecolor="black", linewidth=0.75)

b2 = plt.bar(x, normal, width,
             label='x (Default CFS Scheduler)', color=colors[1], edgecolor="black", linewidth=0.75)

b3 = plt.bar(x + width * 1.3 + sep, nb, width,
             label='y (NUMA Balancing Enabled)', color=colors[2], edgecolor="black", linewidth=0.75)
# autolabel(b1)
# autolabel(b2)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 9.5)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# of vCPUs')
# plt.yticks([])
# plt.ylabel('Percentage of Improvement')
plt.xticks(x, name, rotation=00, fontsize=12)

plt.grid(axis='y', linewidth=0.8)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),
           mode="expand", loc="lower center", prop={'size': 9},
           ncol=3,frameon=False)

ax.tick_params(length=2)

# plt.subplots_adjust(top=1.2)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# plt.plot([9.5,9.5],[min(nb)-80, max(clique)+1], linewidth=1.5, color='black')

plt.tight_layout()
plt.title("Execution Time Distribution")
plt.savefig('/Users/snake0/taco-journal/newimgs/latency-occupy.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
