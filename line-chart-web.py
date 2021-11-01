import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib
from color import *

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

plt.rc('font', family='Nimbus Sans L', weight='medium',size=11)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)

x = [8, 16, 24, 32]

b10 = [111.45, 110.23, 137.39, 86.82]
b20 = [228.61, 161.73, 185.74, 146.47]
b40 = [280.39, 202.15, 209.57, 157.82]

l10 = [52.85, 36.75, 28.87, 22.69]
l20 = [45.48, 22.73, 24.40, 22.11]
l40 = [53.62, 16.54, 19.14, 16.38]
titles = ["Web server {10,*}", "Web Server {20,*}", "Web Server {40,*}"]




fig = plt.figure(figsize=(8.92, 2.6))

colors = ["#7ec1be","#53a2bf","#366eaa","#0e215b"]


plt.subplot(131)
plt.plot(x, b10, label="Barrelfish",linewidth=1.9,color=colors_line[3],linestyle="dotted")
plt.plot(x, l10, label="Linux",linewidth=2.2, color=colors_line[0])
plt.xlim(8, 32)
plt.ylim(0, 300)
plt.xlabel('# vCPUs')
plt.ylabel('RPS (Ops/s)')
plt.xticks(range(8,40,8),["4x2","4x4","4x6","4x8"])
plt.yticks([0,100,200,300])
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[0])






plt.subplot(132)
plt.plot(x, b20, label="Barrelfish",linewidth=1.9,color=colors_line[3],linestyle="dotted")
plt.plot(x, l20, label="Linux",linewidth=2.2, color=colors_line[0])
plt.xlim(8, 32)
plt.ylim(0, 300)
plt.xlabel('# vCPUs')
plt.xticks(range(8,40,8),["4x2","4x4","4x6","4x8"])
plt.yticks([0,100,200,300])
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[1])






plt.subplot(133)
plt.plot(x, b40, label="Barrelfish",linewidth=1.9,color=colors_line[3],linestyle="dotted")
plt.plot(x, l40, label="Linux",linewidth=2.2, color=colors_line[0])
plt.xlim(8, 32)
plt.xlabel('# vCPUs')
plt.xticks(range(8,40,8),["4x2","4x4","4x6","4x8"])
plt.yticks([0,100,200,300])
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.legend(facecolor='white',framealpha=1.0,
        loc='best',frameon=True,ncol=1, edgecolor='white')
plt.title(titles[2])










fig.tight_layout()
fig.savefig('/Users/snake0/taco-journal/newimgs/webserver.pdf', dpi=300)
plt.show()

plt.close()