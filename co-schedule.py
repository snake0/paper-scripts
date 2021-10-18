import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', size=13)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(6.5, 2.8)

top = 7

normal = np.array([1, 1, 1, 1, 1, 1])

name = ["CG.B", "EP.C", "FT.B", "BT.A", "MG.C", "SP.A"]

timee=[51.33,48.67,]

clique = np.array(
    [1.205280528, 1.012366035, 4.060557702, 3.392378482, 4.382665696, 4.91410344])

nb = np.array(
    [2.204620462, 1.906842539, 2.121451369, 1.555679081, 2.37392571, 2.298017772])

clique_l = np.array(
    [73.04, 12.28, 483.45, 549.26, 300.87, 215.68])

normal_l = np.array(
    [60.6, 12.13, 119.06, 161.91, 68.65, 43.89])

nb_l = np.array(
    [133.6, 23.13, 252.58, 251.88, 162.97, 100.86])

x = np.array([1, 2, 4, 5, 7, 8])

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

                va='bottom', size=11, rotation=90, ha='center')


b1 = plt.bar(x - width * 1.2 - sep, clique, width,
             color=colors[0], edgecolor="black", label='DaS', linewidth=0.6)
# b10 = plt.bar(x - width * 1.3 - sep, 100 - clique, width, bottom=clique,
#             color=colors[0], edgecolor="black", label='Application Time', linewidth=0.6)
autolabel(b1, clique_l, clique + 0.12)
# autolabel(b10, clique_e, clique + 83 - clique)

b2 = plt.bar(x, normal, width,
             color=colors[1], edgecolor="black", label='CFS', linewidth=0.6)
# b20 = plt.bar(x, 100 - normal, width, bottom=normal,
#               color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b2, normal_l, normal + 0.12)
# autolabel(b20, normal_e, normal + 83 - normal)

b3 = plt.bar(x + width * 1.2 + sep, nb, width,
             color=colors[2], edgecolor="black", label='Singleton', linewidth=0.6)
# b30 = plt.bar(x + width * 1.3 + sep, 100 - nb, width, bottom=nb,
#              color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b3, nb_l, nb + 0.12)
# autolabel(b30, nb_e, nb + 83 - nb)
# autolabel(b1)
# autolabel(b2)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp) + 'X'


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 7.2)
plt.ylim(0.0, top)
# plt.ylim(min(nb) - 50, max(clique) + 1)

plt.yticks([0, 1, 2, 4,top])
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

plt.plot([3, 3], [0, top], linewidth=1.5, color='black', linestyle='dotted')

plt.plot([6, 6], [0, top], linewidth=1.5, color='black', linestyle='dotted')

plt.text(0,6,"Unit = Mop/s/thread")

plt.tight_layout()
plt.title("Task Co-location Throughput Comparison")
plt.savefig('/Users/snake0/taco-journal/newimgs/colocate.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
