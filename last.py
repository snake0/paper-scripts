import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import gridspec

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

plt.rc('font', family='Nimbus Sans L', weight='medium', size=14.5)

# fig, axs = plt.subplots(1, 4, figsize=(12, 2.9))
plt.figure(figsize=(11, 3.3))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])

plt.subplot(gs[0])

x = np.arange(8)


mins = np.array([142368,302,2620,2522,1963,1157,218,129])
maxes = np.array([100537575,8869,100631826,30920,37926,51996,333354937,1347])

means = np.array([471237.8,1280.57,218935.89,5449.39,3777.88,3781.1,164924.74,349.03])
std=np.array([335968.26,725.79,212149.82,1083.51,695.37,3468.03,131524.62,119.82])
# std=np.array([1000,1000,1000,1000,1000,1000,1000,1000])
# create stacked errorbars:

# create stacked errorbars:
plt.errorbar(np.arange(8), means, std, fmt='ok', lw=2,capsize=2, capthick=2, markersize=1)
plt.errorbar(np.arange(8), means, [means - mins, maxes - means],capsize=2, capthick=2,markersize=7,
             fmt='.k', ecolor='gray', lw=1)

plt.yscale("log")
plt.ylabel("Latency (ns)")
plt.xlabel("Functions")

# plt.ylim([0.1,10000000000])
plt.xlim(-1, 10)

x=np.arange(8)
x_title = np.array(["A1*","A2","A3*","A4","A5","B1","B2*","B3*"])


plt.xticks(x, labels=x_title)

plt.title("Page Fault and Eviction Critical-path Function Latencies")

plt.subplot(gs[1])

plt.title("Latencies")


data = pd.read_excel('~/MasterThesis/tcp-latency.xlsx', header=0, usecols=[0, 1, 2])

y_rdma = np.array(data['write'].values.tolist())
y_tcp = np.array(data['read'].values.tolist())
y_ipoib = np.array(data['xbzrle'].values.tolist())

y_rdma = y_rdma / 1000
y_tcp = y_tcp / 1000
y_ipoib = y_ipoib / 1000

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

y_rdma_sort3 = np.sort(y_rdma)
y_tcp_sort3 = np.sort(y_tcp)
y_iboip_sort3 = np.sort(y_ipoib)

rdma_90 = np.percentile(y_rdma_sort3, 90)
tcp_90 = np.percentile(y_tcp_sort3, 90)
iboip_90 = np.percentile(y_iboip_sort3, 90)

rdma_50 = np.percentile(y_rdma_sort3, 50)
tcp_50 = np.percentile(y_tcp_sort3, 50)
iboip_50 = np.percentile(y_iboip_sort3, 50)

# print(rdma_50,tcp_50,iboip_50)
# print(rdma_90,tcp_90,iboip_90)

y_rdma_cdf3 = 1. * np.arange(len(y_rdma_sort3)) / (len(y_rdma_sort3) - 1)
y_tcp_cdf3 = 1. * np.arange(len(y_tcp_sort3)) / (len(y_tcp_sort3) - 1)
y_iboip_cdf3 = 1. * np.arange(len(y_iboip_sort3)) / (len(y_iboip_sort3) - 1)

plt.plot(y_rdma_sort3, y_rdma_cdf3, label="B2", linewidth=1.4, color=colors[3], linestyle="dotted")
plt.plot(y_tcp_sort3, y_tcp_cdf3, label="A1", linewidth=1.8, color="black")
plt.plot(y_iboip_sort3, y_iboip_cdf3, label="B3", linewidth=2.2, color=colors[0])

plt.xlabel("Network Latencies (ns)")
plt.xscale("log")
plt.ylim([0, 1])
plt.ylabel("CDF")
plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

plt.legend(facecolor='white', framealpha=0.0,
              loc='lower right', frameon=True, ncol=1, edgecolor='white')

plt.tight_layout()
plt.savefig('/Users/snake0/MasterThesis/figures/_last.pdf', dpi=100)
plt.show()

plt.close()
