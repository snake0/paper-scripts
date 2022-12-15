import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium', size=14.5)

fig, ax = plt.subplots()
fig.set_size_inches(3, 3)
plt.subplots_adjust(top=1.8, right=0.95, left=0.08, bottom=0.2)
labels = ["Apache", "OLTP (RO)"]

xrange = np.arange(len(labels))

# vanilla_avg = [2.1,0.92]
# vanilla_tail =[8.7,1.1]
vanilla_avg = [1.732, 0.78, 17.48, 27.81, 23.76]
vanilla_tail = [3, 0.93, 22.87, 5, 5]
vm_live_avg = [2.1, 0.92]
vm_live_tail = [8.7, 1.1]
yanni_avg = [1.74, 0.83]
yanni_tail = [3.1, 0.96]

for i in range(len(labels)):
    vm_live_avg[i], vm_live_tail[i], yanni_avg[i], yanni_tail[i] = \
        vm_live_avg[i] / vanilla_avg[i], \
        vm_live_tail[i] / vanilla_tail[i], \
        yanni_avg[i] / vanilla_avg[i], \
        yanni_tail[i] / vanilla_tail[i]

title = "Text-Processing\nComparison with Spark"
colors = ["#f5f7c8", "#c3ddbd", "#dce8fa"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.6
bar_interval = 0.3
bar_zoom = 0.2
linewidth = 4

# ax.set_title(title,fontdict=font)

plt.xticks(xrange, labels, rotation=15)
plt.yticks([0,1,2,4])
# ax.set_ylabel("Relative Latency")
ax.tick_params(axis='both', which='major')
ax.set_ylim([0, 4.3])
# ax.set_xlabel("Program", fontdict=font)

# ax.axhline(y=1, color='grey', linestyle='--')
for i in xrange:
    vmlive_avg_bar = ax.bar(i - bar_interval*0.8, vm_live_avg[i], width=bar_width * bar_zoom,
                            bottom=0, color=colors[2],
                            label="vm live avg", edgecolor="black")
    vmlive_tail_bar = ax.bar(i - bar_interval *0.3, vm_live_tail[i], width=bar_width * bar_zoom,
                             bottom=0, color=colors[2],
                             label="vm live tail", edgecolor="black", linestyle='--', linewidth=0.5)
    yanni_avg_bar = ax.bar(i + bar_interval *0.3, yanni_avg[i], width=bar_width * bar_zoom,
                           bottom=0, color=colors[1],
                           label="yanni avg", edgecolor="black")
    yanni_tail_bar = ax.bar(i + bar_interval*0.8, yanni_tail[i], width=bar_width * bar_zoom,
                            bottom=0, color=colors[1],
                            label="yanni tail", edgecolor="black", linestyle='--', linewidth=0.5)

ax.legend((vmlive_avg_bar, vmlive_tail_bar),
          ("w/o Mig AVG", "w/o Mig Tail"),
          facecolor='white', framealpha=1.0,
          loc='upper right', frameon=True, ncol=1, edgecolor='white')
plt.subplots_adjust(top=0.86)

plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.savefig('/Users/snake0/MasterThesis/figures/_application_perf1.pdf', dpi=300)
plt.show()
