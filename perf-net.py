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
    [0.731278076, 0.381953093, 0.495231312, 0.90296503, 0.980590041, 0.972744157, 0.71906208, 0.623996865, 0.967851663,
     0.518662339])

nb = np.array(
    [2.064965142, 1.076715852, 1.548758893, 1.423805465, 0.931379088, 1.182785939, 0.643066805, 1.221570408,
     0.951503185, 0.59014303])

clique_l = np.array(
    [87.29360349, 49.47188921, 79.73407049, 7.518537974, 514.6033055, 194.3257835, 526.7571855, 111.0041817,
     208.3818177, 81.22137858])

normarl_l = np.array(
    [119.3712848, 129.5234678, 161.0036937, 8.326499612, 524.789447, 199.7707023, 732.5614855, 177.8922105, 215.303466,
     156.5977948])

nb_l = np.array(
    [246.4975421, 139.459971, 249.3559025, 11.85531565, 588.7779166, 236.2859777, 471.085974, 217.3078601, 204.8619337,
     92.4150971])

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
plt.ylim(0.0, 2.6)
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
plt.title("Network Bandwidth Utilization Improvement")
plt.savefig('/Users/snake0/taco-journal/newimgs/perf-net.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
