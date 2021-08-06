import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'size': 26,}
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium')
# font = {'size': 28, 'family': 'Helvetica Neue', 'weight': 'medium'}
# plt.rc('font', family='Helvetica Neue', weight='medium')

fig, ax = plt.subplots()
fig.set_size_inches(6, 6.2)
plt.subplots_adjust(top=0.90, right=0.97, bottom=0.2)


x= ["QEMU", "Router", "Others", "GuestOS", "DSM"]

xrange = np.arange(len(x))
giantVM = [1.06, 0.97, 35.44, 43.75, 18.89]
giantVM.sort()


title = "Bottleneck Analysis with Perf"
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

plt.xticks(xrange, x, rotation=-20)
ax.set_ylabel("CPU Time Occupancy", fontdict=font)
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
        ax.annotate("{:.2f}%".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, offset),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',size=22,rotation=00, fontweight='black')

for i in xrange:
    giantVM_bar = ax.bar(i, giantVM[i], width=bar_width * zoom,
                         bottom=0, color=colors[0], edgecolor="black",
                         label="GiantVM", linewidth=1)
    autolabel(giantVM_bar)

ax.legend(["CPU Time %"], loc=2, prop={'size': 28}, frameon=False)

# plt.hlines(1.0,-1,len(x),colors="#4a7cac",linestyles="dotted",linewidth=3)
plt.xlim(-0.7,len(x)-0.3)
# plt.grid(True,linewidth=0.8,linestyle=(0,(5,3)),axis="y")
plt.ylim(0,60)
plt.yticks([])
#plt.tight_layout()
plt.savefig('/Users/snake0/taco-journal/newimgs/percent.pdf', dpi=300)
plt.show()
