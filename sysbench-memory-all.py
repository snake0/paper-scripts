import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

plt.rc('font', family='Nimbus Sans L', weight='medium', size=11)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

x = [4, 8, 12, 16, 20, 24]
y1 = [42061.26, 92469.49, 131072.9, 183858.78, 223154.86, 229467.97]
y2 = [75527.9, 143261.82, 211938.7, 277095.76, 336383.4, 365684.81]
y3 = [8683.06, 6484.08, 6208.55, 6126.54, 6436.79, 6278.47]
y4 = [3022.08, 4809.57, 6008.72, 6461.55, 7645.22, 7311.65]
y5 = [256.36, 496.97, 598.65, 897.33, 1146.98, 1050.94]
y6 = [27193.03, 47503.08, 58012.17, 63876.5, 68984.96, 76913.48]
y7 = [74320.72, 152924.43, 224953.49, 300204.18, 422482.79, 414039.46]
y8 = [138041.83, 258236.07, 384571.71, 499286.39, 615887.18, 656600.11]

y9 = [4113.1, 5921.72, 7533.25, 7427.28, 7343.97, 7135.68]

y1 = np.array(y1)/1024.0
y2 = np.array(y2)/1024.0
y3 = np.array(y3)/1024.0
y4 = np.array(y4)/1024.0
y5 = np.array(y5)/1024.0
y6 = np.array(y6)/1024.0
y7 = np.array(y7)/1024.0
y8 = np.array(y8)/1024.0
y9 = np.array(y9)/1024.0



fig = plt.figure(figsize=(12.5, 2.7))

colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]

titles= ["Memory {4KiB,local,write,*}","Memory {4KiB,global,read,*}","Memory {4KiB,global,write,*}","Memory {4MiB,global,write,*}"]

plt.subplot(141)
plt.plot(x, y1,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[0],linestyle="dotted")
plt.plot(x, y2,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[0])
plt.xlim(4, 24)
plt.xlabel('# vCPUs')
plt.ylabel('Memory Transfer Speed (GiB/s)')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[0])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))





plt.subplot(142)
plt.plot(x, y7,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[1],linestyle="dotted")
plt.plot(x, y8,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[1])
plt.xlim(4, 24)
plt.xlabel('# vCPUs')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[1])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))




plt.subplot(143)
plt.plot(x, y3,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[2],linestyle="dotted")
plt.plot(x, y4,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[2])
plt.plot(x, y9,linewidth=2, marker="o",markersize=6,label="GiantVM-IPoIB",color=colors[2],linestyle=(0,(5,3)),markerfacecolor='none')
plt.xlim(4, 24)
plt.xlabel('# vCPUs')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[2])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))




plt.subplot(144)
plt.plot(x, y5,linewidth=2, marker="x",markersize=8,label="GiantVM",color=colors[3],linestyle="dotted")
plt.plot(x, y6,linewidth=2, marker="x",markersize=8,label="baseline",color=colors[3])
plt.xlim(4, 24)
plt.yscale('log')
plt.xlabel('# vCPUs')
plt.xticks(range(4,28,4),["4x"+str(i) for i in range(1,7)])
plt.grid(axis='y',linewidth=0.8,linestyle=(0,(5,3)))
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[3])

# g = lambda x,pos : "${}$".format(f._formatSciNotation('%d' % x))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))








fig.tight_layout()
# plt.subplots_adjust(wspace=0,hspace=0)

fig.savefig('/Users/snake0/taco-journal/newimgs/sysbench-memory-all.pdf', dpi=100)
plt.show()

plt.close()