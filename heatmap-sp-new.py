import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Nimbus Sans L', weight='medium', size=28)

fig = plt.figure(figsize=(7, 6.5))

R1 = np.loadtxt("/Users/snake0/taco-journal/newdata/sp.A.csv", delimiter=",", skiprows=1)
# R1=R1+1
#
# R1 = np.log2(R1)
sns_plot1 = sns.heatmap(R1, xticklabels=2, yticklabels=2, vmax=400, cmap="YlGnBu", square=True)
for xitem in sns_plot1.get_xticklabels():
    xitem.set_rotation(90)
for yitem in sns_plot1.get_yticklabels():
    yitem.set_rotation(0)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('SP.A.y')


def add_rect(arr, sns_plot):
    for i in arr:
        for j in arr:
            if i != j:
                sns_plot1.add_patch(Rectangle((i, j), 1, 1, fill=False, edgecolor='black', lw=3.5))

add_rect([0,1,2,11],sns_plot1)
add_rect([4,5,6,7],sns_plot1)
add_rect([8,9,10,11],sns_plot1)
add_rect([4,13,14,15],sns_plot1)

plt.tight_layout()
plt.subplots_adjust(left=0.08, right=0.98, bottom=0.04, top=0.97)
plt.savefig('/Users/snake0/taco-journal/newimgs/sp.A-annotate.pdf', dpi=300)
plt.show()

plt.close()
