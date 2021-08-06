from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.array([123491, 59329, 45551, 37612, 29861, 24477, 23978, 23653, 17370, 16467,
        15995, 15786, 15498, 15296, 14459, 13638, 12013, 11876, 11805, 10707,
        10167, 10130, 9814, 9671, 9394, 9049, 9006, 8878, 8627, 8484, 8098,
        7985, 7975, 7912, 7845, 7775, 7774, 7772, 7710, 7635, 7500, 7489,
        7462, 7450, 7368, 7174, 6988, 6935, 6933, 6383, 6368, 6337, 6241, 6090,
        6056, 5842, 5789, 5502, 5497, 5441, 5430, 5317, 5198, 5067, 4936, 4906,
        4904, 4895, 4872, 4846, 4738, 4730, 4692, 4653, 4391, 4336, 4089, 4035,
        4003, 3975, 3881, 3766, 3745, 3744, 3710, 3624, 3610, 3474, 3393, 3323,
        3109, 3051, 3048, 2991, 2884, 2675, 2674, 2645, 2614, 2402])
data_sorted = np.sort(x)
p = 1. * np.arange(len(x)) / (len(x) - 1)

plt.plot(data_sorted, p)
plt.yscale("logit")

plt.title('How to calculate and plot a cumulative distribution function ?')

plt.savefig("cumulative_density_distribution_04.png", bbox_inches='tight')
plt.close()
