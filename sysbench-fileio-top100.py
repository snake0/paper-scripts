from typing import List

import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

font_size = 30

font = {'size': font_size, 'family': 'Helvetica Neue', 'weight': 'medium'}
plt.rc('font', family='Helvetica Neue', weight='medium')
fig = plt.figure()
fig.set_size_inches(16, 9.5)
x = np.arange(0, 100)
y_read = [123491, 59329, 45551, 37612, 29861, 24477, 23978, 23653, 17370, 16467,
        15995, 15786, 15498, 15296, 14459, 13638, 12013, 11876, 11805, 10707,
        10167, 10130, 9814, 9671, 9394, 9049, 9006, 8878, 8627, 8484, 8098,
        7985, 7975, 7912, 7845, 7775, 7774, 7772, 7710, 7635, 7500, 7489,
        7462, 7450, 7368, 7174, 6988, 6935, 6933, 6383, 6368, 6337, 6241, 6090,
        6056, 5842, 5789, 5502, 5497, 5441, 5430, 5317, 5198, 5067, 4936, 4906,
        4904, 4895, 4872, 4846, 4738, 4730, 4692, 4653, 4391, 4336, 4089, 4035,
        4003, 3975, 3881, 3766, 3745, 3744, 3710, 3624, 3610, 3474, 3393, 3323,
        3109, 3051, 3048, 2991, 2884, 2675, 2674, 2645, 2614, 2402]
y_write = [184221, 145878, 106927, 36787, 29018, 27282, 21723, 21234, 19114, 18761,
        18567, 18021, 17729, 16552, 16293, 13823, 13568, 11857, 11373, 11136,
        10919, 10880, 10826, 10815, 10788, 10375, 10242, 10240, 10233, 9936,
        9929, 9902, 9281, 9076, 9035, 9020, 8972, 8825, 8622, 8504, 8323, 8144,
        8130, 8119, 8076, 7951, 7906, 7900, 7889, 7809, 7801, 7798, 7788, 7786,
        7740, 7729, 7623, 7619, 7533, 7472, 7412, 7251, 6906, 6665, 6567, 6412,
        6385, 6324, 5941, 5811, 5807, 5782, 5669, 5338, 5262, 5205, 5098,
        5082, 5023, 4956, 4927, 4900, 4875, 4843, 4581, 4330, 4169, 4135, 4120,
        4066, 3881, 3878, 3672, 3650, 3514, 3245, 3192, 3154, 3017, 2780]
s = 70
# from scipy import spatial
#
#
# def findNeighbor(point: List[int], set: List[List[int]], k: int) -> List[List[int]]:
#     tree = spatial.KDTree(set)
#     # x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
#     distance, idx = tree.query(x=point, k=k, p=2)
#     return [set[i] for i in idx] if k > 1 else [set[idx]]



colors = ['g', "#FF1493"]
title = "Page faults distribution of File I/O"
plt.title(title, fontdict=font)
plt.plot(x, y_read, s, c=colors[0], alpha=0.5, marker="o",
                    label="Number of Read Faults")
plt.plot(x, y_write, s, c=colors[1], alpha=0.5, marker="v",
                    label="Number of Write Faults")
plt.xlabel("Top 100 Pages", fontdict=font)
plt.ylabel("Number of Page Faults", fontdict=font)
plt.tick_params(axis='both', which='major', labelsize=font_size)
plt.grid(False)
plt.legend(loc=0, prop={'size': font_size}, frameon=False)
plt.savefig('../imgs/new/evaluation/sysbench-fileio-top100.pdf', dpi=300)
plt.show()

# print(findNeighbor([1, 3, 2], [[1, -2, -2], [1, -3, -3], [1, 2, 4], [1, 4, 3], [2, 1, 4]], 5))
