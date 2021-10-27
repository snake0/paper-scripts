import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
import pandas as pd
import seaborn as sns

matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally



matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

plt.rc('font', family='Nimbus Sans L', weight='medium', size=12)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

fig = plt.figure(figsize=(3.125, 2.7))
data = pd.read_excel('~/Downloads/rdma-tcp-lat.xlsx', header=0, usecols=[0,1,2])

x = np.arange(0, 100)

y_rdma = np.array(data['Non-owner Write RDMA'].values.tolist())
y_tcp = np.array(data['Non-owner Write TCP'].values.tolist())
y_ipoib = np.array(data['Non-owner Write IPoIB'].values.tolist())




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


y_rdma_sort3 = np.sort(y_rdma)
y_tcp_sort3 = np.sort(y_tcp)
y_iboip_sort3 = np.sort(y_ipoib)

rdma_90 = np.percentile(y_rdma_sort3,90)
tcp_90 = np.percentile(y_tcp_sort3,90)
iboip_90 = np.percentile(y_iboip_sort3,90)

y_rdma_cdf3 = 1. * np.arange(len(y_rdma_sort3)) / (len(y_rdma_sort3) - 1)
y_tcp_cdf3 = 1. * np.arange(len(y_tcp_sort3)) / (len(y_tcp_sort3) - 1)
y_iboip_cdf3 = 1. * np.arange(len(y_iboip_sort3)) / (len(y_iboip_sort3) - 1)



plt.plot(y_rdma_sort3, y_rdma_cdf3,linewidth=1.4,label="RDMA",color=colors[3],linestyle="dotted")
plt.plot(y_tcp_sort3, y_tcp_cdf3,linewidth=1.8, label="TCP-Ethernet",color="black")
plt.plot(y_iboip_sort3, y_iboip_cdf3,linewidth=2.2, label="TCP-IBoIP",color=colors[0])

# plt.scatter(rdma_90, 0.9,color = 'black', s=15,marker='s')
# plt.scatter(tcp_90, 0.9,color = 'black', s=15,marker='s')
# plt.scatter(iboip_90, 0.9,color = 'black', s=15,marker='s')
#
# plt.text(30000, 0.87, "P90",size=11,weight='bold')

plt.xlabel("Non-owner Write Latency")
plt.xscale("log")
plt.ylim([0,1])
plt.ylabel("CDF")
# plt.xlim([2400,184500])
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
# plt.title("Non-owner Write Latency")
plt.yticks([0,0.2,0.4,0.6,0.8,1])
#
# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
#
# g1 = lambda x,pos : "${}$".format(f._formatSciNotation("%.1f" % (x)))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g1))

plt.legend(facecolor='white',framealpha=0.0,
        loc=4,frameon=True,ncol=1, edgecolor='white')
# plt.subplots_adjust(left=0.35,bottom=-0.05)


fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/latency-cdf.pdf', dpi=300, bbox_inches='tight')
plt.show()

plt.close()