import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium',size=28)

fig = plt.figure(figsize=(7, 6.5))

R1 = np.loadtxt("/Users/snake0/taco-journal/newdata/ft.B.csv", delimiter=",", skiprows=1)

sns_plot1 = sns.heatmap(R1, xticklabels=2, yticklabels=2, vmax=800, cmap="YlGnBu", square=True)
for xitem in sns_plot1.get_xticklabels():
    xitem.set_rotation(90)
for yitem in sns_plot1.get_yticklabels():
    yitem.set_rotation(0)
# plt.xlabel('thread ID', fontproperties=sub_font)
# plt.ylabel('thread ID', fontproperties=sub_font)
plt.title('FT.B.y')

plt.tight_layout()
plt.subplots_adjust(left=0.05,right=0.96,bottom=0.05,top=0.95)

plt.savefig('/Users/snake0/taco-journal/newimgs/ft.B.pdf', dpi=300)
plt.show()


plt.close()
