import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

plt.rc('font', family='Nimbus Sans L')
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

colors = ["#26388f", "#6db8be", "#a7d5b9", "#d9ecb8", "#fffedd"]

fig, ax = plt.subplots()
fig.set_size_inches(4.6, 2.8)

plt.tick_params(top=True, bottom=False, left=True, right=False)
ax.set_axisbelow(True)

normal = np.array([1, 1, 1, 1, 1, 1, 1, 1])

name = ["CG.D", "EP.D"]
# 
# das = np.array(
#     [0.250736034, 0.759410391, 0.741203563, 0.262148367, 0.092298162, 0.139807274, 0.205513571])
# 
# cfs = np.array(
#     [0.211841679, 0.716095968, 0.670350072, 0.221942211, 0.069449959, 0.135831214, 0.046144816])
# 
# nb = np.array(
#     [0.202537123, 0.510890045, 0.662745238, 0.172002994, 0.068187233, 0.118968264, 0.034669723])

# das_l = np.array(
#     [0.25, 0.75, 0.74, 0.26, 0.09, 0.14, 0.21])
#
# cfs_l = np.array(
#     [0.21, 0.72, 0.67, 0.22, 0.07, 0.14, 0.05])
#
# nb_l = np.array(
#     [0.20, 0.51, 0.66, 0.17, 0.07, 0.12, 0.03])


# colors = ["#366EAA", "#71A1E2", "#DDF2FF"]

width = 0.12

sep = 0.03


def autolabel(rects, array, heights):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i in range(len(rects)):
        rect = rects[i]
        height = heights[i]
        s = "{:.2f}X".format(array[i])
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
                x=rect.get_x() + rect.get_width() / 2 + 0.05, y=height - offset,

                va='bottom', rotation=90, size=10, ha='center')
        
cfs8non = np.array([0.392755271,0.501995053])

das8loc = np.array([0.473380281,0.508202741])

cfs16non = np.array([0.865876308,0.957225522])

das16par = np.array([0.91825048,1.058400673])

mpi = np.array([1.209162385,1.427948711])

x = np.arange(len(mpi))

t1 = plt.bar(x - width * 2 - 2*sep, cfs8non, width,
             color=colors[0], edgecolor="black", label='DaS', linewidth=0.9)
autolabel(t1, cfs8non, cfs8non + 0.03)

t2 = plt.bar(x - width * 1 - sep, das8loc, width,
             color=colors[1], edgecolor="black", label='DaS', linewidth=0.9)
autolabel(t2, das8loc, das8loc + 0.03)

t3 = plt.bar(x, cfs16non, width,
             color=colors[2], edgecolor="black", label='DaS', linewidth=0.9)
autolabel(t3, cfs16non, cfs16non + 0.03)

t4 = plt.bar(x + width  + sep, das16par, width,
             color=colors[3], edgecolor="black", label='DaS', linewidth=0.9)
autolabel(t4, das16par, das16par + 0.03)

t5 = plt.bar(x + 2*width + 2*sep, mpi, width,
             color=colors[4], edgecolor="black", label='DaS', linewidth=0.9)
autolabel(t5, mpi, mpi + 0.03)




# f = mticker.ScalarFormatter(useOffset=False, useMathText=True)


def to_percent(temp, position):
    return '%1.1f' % (temp)


plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(to_percent))

plt.xlim(-1., 10)
plt.ylim(0.0, 1.8)
# plt.ylim(min(nb) - 50, max(clique) + 1)

# plt.yticks([-90, -60, -30, 0, 30, 60, 90, 120])
# plt.xlabel('# vCPUs')
# plt.yticks([0, 1])
plt.xticks(x, name, rotation=00)
plt.yticks([0, 0.3, 0.6, 0.9, 1.2, 1.5])

# plt.grid(axis='y', linewidth=0.9, linestyle=(0, (5, 3)))
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

ax.legend(loc='upper right', facecolor='white', framealpha=1.0,
          frameon=True, ncol=3, edgecolor='white')

ax.legend(title='# vCPUs',
            loc='center left', bbox_to_anchor=(1, 0.5) ,frameon=False,facecolor="white",ncol=1)

plt.ylabel("Normalized Results")

# ax.tick_params(length=0)

plt.xlim([-width * 1.8 - sep - 0.05 - 0.2, len(x) - 1 + width * 1.8 + sep + 0.05 + 0.2])

plt.tight_layout()
# plt.title("Single-thread Throughput Improvement")

plt.savefig('/Users/snake0/taco-journal/newimgs/single-com.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()
