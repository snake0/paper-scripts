import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Nimbus Sans L', weight='medium', size=11)

fig, ax = plt.subplots()
fig.set_size_inches(5.5, 3.3)

normal = [251.88, 133.6, 0.117, 23.13, 252.58, 4.74, 166.34, 162.97, 100.86, 0.0687]

name = ["BT.A.*", "CG.B.*", "DC.W.*", "EP.C.*", "FT.B.*", "IS.C.*",
        "LU.A.*", "MG.C.*", "SP.A.*", "UA.W.*"]

clique = [36.81117993, 12.46257485, 32.47863248, 0.302637268, -0.581993824,
          19.4092827, 14.56053866, 53.81358532, 102.0523498, 31.87772926]

nb = [-9.242496427, -4.513473054, 28.20512821, -5.361003026, -55.42006493,
      -7.383966245, -9.582782253, -62.10959072, -9.884989094, -11.20815138]

x = np.arange(len(clique))

for i in range(len(name)):
    name[i] = name[i] + '\n' + str(normal[i])

# colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]
colors = ["#f5f7c8", "#c3ddbd"]

width = 0.33

sep = 0.02


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        s = "{:.1f}%".format(height)
        l = len(s)
        if height < 0:
            offset = height - 40 - len(s)*1.1
        else:
            offset = 0 - 40 - len(s)*1.1
        ax.text(s=s,
                    x=rect.get_x() + rect.get_width() / 2, y=offset,

                    va='bottom', size=10, rotation=90,ha='center', fontweight='black')


b1 = plt.bar(x - width / 2 - sep, clique, width,
             label='x (DSM-aware Scheduler)', color=colors[0], edgecolor="black", linewidth=0.75)
b2 = plt.bar(x + width / 2 + 2*sep, nb, width,
             label='y (NUMA Balancing Enabled)', color=colors[1], edgecolor="black", linewidth=0.75)
autolabel(b1)
autolabel(b2)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-0.5, 9.5)
plt.ylim(min(nb)-50, max(clique)+1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([])
# plt.ylabel('Percentage of Improvement')
plt.xticks(x, name, rotation=90,fontsize=12)

plt.grid(axis='x', linewidth=1, linestyle='dotted')
plt.plot([-0.5, 9.5], [0, 0], linewidth=0.8, color='black')

plt.legend(loc=2)

ax.tick_params(length=0)

# plt.subplots_adjust(top=1.2)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# plt.plot([9.5,9.5],[min(nb)-80, max(clique)+1], linewidth=1.5, color='black')

plt.tight_layout()
plt.title("NAS Parallel Benchmarks Throughput Improvement")
plt.savefig('/Users/snake0/taco-journal/newimgs/performance.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
