import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Nimbus Sans L', size=13)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(6.5, 3.2)

normal = np.array([10.22150428, 10.22892095, 14.456258, 1.003155954, 21.30449186, 29.37214144, 29.92757, 8.341463218,
                   15.33439944, 17.77646099])

name = ["BT.A", "CG.B", "DC.W", "EP.C", "FT.B", "IS.C",
        "LU.A", "MG.C", "SP.A", "UA.W"]

clique = np.array(
    [7.998315602, 4.150075209, 5.980609183, 0.671152778, 21.10172233, 29.15483553, 22.15520013, 7.949557251,
     14.81370637, 9.312773328])

nb = np.array([19.90348932, 11.08862739, 22.08420194, 1.571802338, 22.623722914409533, 30.03261374407583, 30.49634336,
               9.465316823,
               14.70520242, 9.890117065])

clique_l = np.array(
    [2.884992438, 0.944972125, 2.155291938, 0.154029563, 4.880828375, 4.320746625, 8.669329813, 3.086018125, 3.86193325,
     4.635898563])
clique_e = np.array(
    [33.18500756, 21.82502788, 33.88270806, 22.79597044, 18.24917163, 10.49925338, 30.46067019, 35.73398188,
     22.20806675, 45.14410144])

normarl_l = np.array(
    [4.268500188, 2.599168813, 6.887395, 0.232932813, 4.774336625, 4.802345125, 13.41353688, 4.980687688, 8.078161625,
     11.70579956])
normal_e = np.array(
    [37.49149981, 22.81083119, 40.755605, 22.98706719, 17.63566338, 11.54765488, 31.40646313, 54.72931231, 44.60183838,
     54.14420044])

nb_l = np.array(
    [9.157595438, 2.786572063, 8.126986313, 0.379904625, 8.3526785, 6.3368815, 14.57725213, 14.91544625, 8.595190813,
     7.276159125])
nb_e = np.array(
    [36.85240456, 22.34342794, 28.67301369, 23.79009538, 28.5673215, 14.7631185, 33.22274788, 142.6645538, 49.85480919,
     66.29384088])

x = np.arange(len(clique))

# for i in range(len(name)):
#     name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#c3ddbd", "#7eb6bd"]

width = 0.25

# sep = 0.01
sep = 0.00


def autolabel(rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.1f}".format(array[i])
        l = len(s)
        if l == 5:
            offset = 4
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
             color=colors[1], edgecolor="black", label='Page Transfer Time', linewidth=0.6)
b10 = plt.bar(x - width * 1.2 - sep, 100 - clique, width, bottom=clique,
              color=colors[0], edgecolor="black", label='Application Time', linewidth=0.6)
autolabel(b1, clique_l, clique + 4)
autolabel(b10, clique_e, clique + 77 - clique)

b2 = plt.bar(x, normal, width,
             color=colors[1], edgecolor="black", linewidth=0.6)
b20 = plt.bar(x, 100 - normal, width, bottom=normal,
              color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b2, normarl_l, normal + 4)
autolabel(b20, normal_e, normal + 77 - normal)

b3 = plt.bar(x + width * 1.2 + sep, nb, width,
             color=colors[1], edgecolor="black", linewidth=0.6)
b30 = plt.bar(x + width * 1.2 + sep, 100 - nb, width, bottom=nb,
              color=colors[0], edgecolor="black", linewidth=0.6)
autolabel(b3, nb_l, nb + 4)
autolabel(b30, nb_e, nb + 77 - nb)
# autolabel(b1)
# autolabel(b2)

ax.text(s="DaS", x=9 - 1.2 * width - sep - 0.02, y=105,
        va='bottom', size=12, rotation=90, ha='center', weight='bold')
ax.text(s="CFS", x=9, y=105,
        va='bottom', size=12, rotation=90, ha='center', weight='bold')
ax.text(s="NB", x=9 + 1.2 * width + sep + 0.02, y=105,
        va='bottom', size=12, rotation=90, ha='center', weight='bold')

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 9.5)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
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
# plt.plot([9.5,9.5],[min(nb)-77, max(clique)+1], linewidth=1.5, color='black')
plt.xlim([-width * 1.8 - sep - 0.05, 9 + width * 1.8 + sep + 0.05])
plt.ylim(0, 105)
plt.text(-0.4, 105, "Unit = second")

plt.tight_layout()
plt.title("Execution Time Distribution")
plt.savefig('/Users/snake0/taco-journal/newimgs/latency-occupy.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
