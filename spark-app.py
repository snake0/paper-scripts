import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font_size=36
font = {'size': font_size,}
plt.rc('font', family='Helvetica Neue', weight='medium')

# font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
# plt.rc('font', family='Helvetica Neue', weight='medium')
fig, ax = plt.subplots()
fig.set_size_inches(10, 7.85)
plt.subplots_adjust(top=0.90, right=0.94,left=0.2)
x = ["Word Count", "Inverted Index"]

xrange = np.arange(len(x))
giantvm = [24.313, 26.083]
inverted_index = [60 + 25.134, 60 + 16.020]

title = "Text-Processing\nComparison with Spark"
colors = ["#f5f7c8", "#c3ddbd"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.5
bar_interval = 0.19
bar_zoom = 0.6
linewidth = 4

ax.set_title(title,fontdict=font)

plt.xticks(xrange, x)
plt.xlim(-0.5,1.5)
ax.set_ylabel("Execution Time (s)", fontdict=font)
ax.tick_params(axis='both', which='major', labelsize=font_size)
ax.set_ylim([0, 120])
#ax.set_xlabel("Program", fontdict=font)

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
                    ha='center', va='bottom',size=32,rotation=0, fontweight='black')

for i in xrange:
    giantvm_bar = ax.bar(i - bar_interval, giantvm[i], width=bar_width * bar_zoom,
                          bottom=0, color=colors[0], edgecolor="black",
                          label="GiantVM")
    autolabel(giantvm_bar)
    spark_bar = ax.bar(i + bar_interval, inverted_index[i], width=bar_width * bar_zoom,
                       bottom=0, color=colors[1], edgecolor="black",
                       label="Spark")
    autolabel(spark_bar)

ax.legend((giantvm_bar, spark_bar),
          ("GiantVM", "Spark"),
          loc=0, prop={'size': font_size}, frameon=False)
plt.subplots_adjust(top=0.87)

plt.grid(False)
plt.savefig('/Users/snake0/taco-journal/newimgs/spark.pdf', dpi=300)
plt.show()
