import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 28,}
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium')
# font = {'size': 28, 'family': 'Helvetica Neue', 'weight': 'medium'}
# plt.rc('font', family='Helvetica Neue', weight='medium')

fig, ax = plt.subplots()
fig.set_size_inches(8, 7.2)
plt.subplots_adjust(top=0.90, right=0.95, bottom=0.2)



x = ["ackermann", "clongdouble", "decimal128", "fft", "hamming",
     "jenkin", "matrixprod", "nqsrt", "rand48"]
xrange = np.arange(len(x))
giantVM = [0.939948116, 0.7652072415, 0.7751622627, 0.8960600598, 0.7435865961,
        0.4053164141, 0.9621792433, 0.9820859601, 0.8520079264]

title = "Stress-ng Overhead on GiantVM"
colors = ['#f4f8c2']
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['//////', '\\\\\\\\\\\\', '----', '//////',
           '++++', 'xxx', '\\\\\\\\\\\\', '----']

marker_size = 8
bar_width = 0.35
labelx = -0.15
zoom = 2
linewidth = 2

ax.set_title(title, fontdict=font)

plt.xticks(xrange, x, rotation=-30,ha='left')
ax.set_ylabel("Normalized Results", fontdict=font)
ax.tick_params(axis='x', which='major', labelsize=22)
ax.tick_params(axis='y', which='major', labelsize=24)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height < 0:
            offset = -16
        else:
            offset = 6
        ax.annotate("{:.2f}".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, offset),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',size=22,rotation=90, fontweight='black')

for i in xrange:
    giantVM_bar = ax.bar(i, giantVM[i], width=bar_width * zoom,
                         bottom=0, color=colors[0], edgecolor="black",
                         label="GiantVM", linewidth=1)
    autolabel(giantVM_bar)

ax.legend(["GiantVM"], loc=2, prop={'size': 28}, frameon=False)

# plt.hlines(1.0,-1,len(x),colors="#4a7cac",linestyles="dotted",linewidth=3)
plt.xlim(-1,len(x))
plt.grid(True,linewidth=0.8,linestyle=(0,(5,3)),axis="y")
plt.yticks([0,1.0])
plt.ylim(0,1.47)
#plt.tight_layout()
plt.savefig('/Users/snake0/taco-journal/newimgs/stress-ng.pdf', dpi=300)
plt.show()
