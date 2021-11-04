import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

plt.rc('font', family='Nimbus Sans L', weight='medium', size=12)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

fig = plt.figure(figsize=(3.125, 2.8))

x = np.arange(0, 100)

y_read = np.array([123491, 59329, 45551, 37612, 29861, 24477, 23978, 23653, 17370, 16467,
        15995, 15786, 15498, 15296, 14459, 13638, 12013, 11876, 11805, 10707,
        10167, 10130, 9814, 9671, 9394, 9049, 9006, 8878, 8627, 8484, 8098,
        7985, 7975, 7912, 7845, 7775, 7774, 7772, 7710, 7635, 7500, 7489,
        7462, 7450, 7368, 7174, 6988, 6935, 6933, 6383, 6368, 6337, 6241, 6090,
        6056, 5842, 5789, 5502, 5497, 5441, 5430, 5317, 5198, 5067, 4936, 4906,
        4904, 4895, 4872, 4846, 4738, 4730, 4692, 4653, 4391, 4336, 4089, 4035,
        4003, 3975, 3881, 3766, 3745, 3744, 3710, 3624, 3610, 3474, 3393, 3323,
        3109, 3051, 3048, 2991, 2884, 2675, 2674, 2645, 2614, 2402])
y_write = np.array([184221, 145878, 106927, 36787, 29018, 27282, 21723, 21234, 19114, 18761,
        18567, 18021, 17729, 16552, 16293, 13823, 13568, 11857, 11373, 11136,
        10919, 10880, 10826, 10815, 10788, 10375, 10242, 10240, 10233, 9936,
        9929, 9902, 9281, 9076, 9035, 9020, 8972, 8825, 8622, 8504, 8323, 8144,
        8130, 8119, 8076, 7951, 7906, 7900, 7889, 7809, 7801, 7798, 7788, 7786,
        7740, 7729, 7623, 7619, 7533, 7472, 7412, 7251, 6906, 6665, 6567, 6412,
        6385, 6324, 5941, 5811, 5807, 5782, 5669, 5338, 5262, 5205, 5098,
        5082, 5023, 4956, 4927, 4900, 4875, 4843, 4581, 4330, 4169, 4135, 4120,
        4066, 3881, 3878, 3672, 3650, 3514, 3245, 3192, 3154, 3017, 2780])


colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]

# plt.subplot(144)
# y_read_sort1=np.sort(y_read[:10])
# y_write_sort1=np.sort(y_write[:10])
#
# y_read_cdf1 = 1. * np.arange(len(y_read_sort1)) / (len(y_read_sort1) - 1)
# y_write_cdf1 = 1. * np.arange(len(y_write_sort1)) / (len(y_write_sort1) - 1)
#
#
# plt.plot(y_read_sort1, y_read_cdf1,linewidth=1.4,label="Read Faults",color=colors[3],linestyle="dotted")
# plt.plot(y_write_sort1, y_write_cdf1,linewidth=2.2, label="Write Faults",color=colors[0])
#
# plt.xlabel("Number of Page Faults")
# plt.xscale("log")
# plt.ylim([0,1])
# plt.xlim([2400,184500])
# plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
# plt.title("Top 10 Pages")
#
# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
#
# g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))
#
# plt.legend(facecolor='white',framealpha=1.0,
#         loc='best',frameon=True,ncol=1, edgecolor='white')




# plt.subplot(143)
# y_read_sort1=np.sort(y_read[:20])
# y_write_sort1=np.sort(y_write[:20])
#
# y_read_cdf1 = 1. * np.arange(len(y_read_sort1)) / (len(y_read_sort1) - 1)
# y_write_cdf1 = 1. * np.arange(len(y_write_sort1)) / (len(y_write_sort1) - 1)
#
#
# plt.plot(y_read_sort1, y_read_cdf1,linewidth=1.4,label="Read Faults",color=colors[3],linestyle="dotted")
# plt.plot(y_write_sort1, y_write_cdf1,linewidth=2.2, label="Write Faults",color=colors[0])
#
# plt.xlabel("Number of Page Faults")
# plt.xscale("log")
# plt.ylim([0,1])
# plt.xlim([2400,184500])
# plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
# plt.title("Top 20 Pages")
#
# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
#
# g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))
#
# plt.legend(facecolor='white',framealpha=1.0,
#         loc='best',frameon=True,ncol=1, edgecolor='white')





# plt.subplot(142)
#
# y_read_sort2=np.sort(y_read[:50])
# y_write_sort2=np.sort(y_write[:50])
#
# y_read_cdf2 = 1. * np.arange(len(y_read_sort2)) / (len(y_read_sort2) - 1)
# y_write_cdf2 = 1. * np.arange(len(y_write_sort2)) / (len(y_write_sort2) - 1)
#
#
# plt.plot(y_read_sort2, y_read_cdf2,linewidth=1.4,label="Read Faults",color=colors[3],linestyle="dotted")
# plt.plot(y_write_sort2, y_write_cdf2,linewidth=2.2, label="Write Faults",color=colors[0])
#
# plt.xlabel("Number of Page Faults")
# plt.xscale("log")
# plt.ylim([0,1])
# plt.xlim([2400,184500])
# plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
# plt.title("Top 50 Pages")
#
# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
#
# g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))
#
# plt.legend(facecolor='white',framealpha=1.0,
#         loc='best',frameon=True,ncol=1, edgecolor='white')








plt.subplot(111)


y_read_sort3 = np.sort(y_read)
y_write_sort3 = np.sort(y_write)

y_read_cdf3 = 1. * np.arange(len(y_read_sort3)) / (len(y_read_sort3) - 1)
y_write_cdf3 = 1. * np.arange(len(y_write_sort3)) / (len(y_write_sort3) - 1)


plt.plot(y_read_sort3, y_read_cdf3,linewidth=1.4,label="Read Faults",color=colors[3],linestyle="dotted")
plt.plot(y_write_sort3, y_write_cdf3,linewidth=2.2, label="Write Faults",color=colors[0])

plt.xlabel("Number of Page Faults")
plt.xscale("log")
plt.ylim([0,1])
plt.ylabel("CDF")
plt.xlim([2400,184500])
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.title("(h) Top 100 Pages")
plt.yticks([0,0.2,0.4,0.6,0.8,1])
#
# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
#
# g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))

plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
# plt.subplots_adjust(left=0.35,bottom=-0.05)


fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-cdf.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()