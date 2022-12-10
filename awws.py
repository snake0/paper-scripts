from statistics import mean

import matplotlib.pyplot as plt

from common import *

# font["font.size"] = 8
# plt.rcParams.update(font)

plt.rc('font', family='Nimbus Sans L', weight='heavy', size=8)


# Useless invalidations
xlabel = []
for i in range(1, 61, 1):
    xlabel.append(str(i))

pagerank_awws = [0, 58.01, 65.50, 67.13, 70.25, 72.70, 73.29, 75.42, 76.88, 79.59, 80.29, 81.00, 81.12, 81.18, 81.25,
                 81.23, 81.24, 81.23, 81.23, 81.24, 81.23, 81.25, 81.27, 81.26, 81.25, 81.29, 81.27, 81.31, 81.35,
                 81.35]
oltp_ro_awws = [0, 2.01, 2.66, 3.04, 3.24, 3.77, 3.89, 4.03, 4.08, 4.14, 4.19,
                4.25, 4.39, 4.42, 4.45, 4.48, 4.48, 4.49, 4.50, 4.50, 4.50, 4.50]
oltp_rw_awws = [0, 7.15, 15.21, 19.19, 21.52, 22.33, 22.81, 23.21, 23.47, 23.72,
                23.91, 24.07, 24.17, 24.48, 24.58, 24.63, 24.70, 24.74, 24.81, 24.85,
                24.91, 24.95, 24.98, 25.01, 25.07, 25.12, 25.15, 25.20, 25.22]
stress_ng_cpu_awws = [0, 0.47, 0.52, 0.55, 0.53, 0.46, 0.52, 0.54, 1.68, 1.61,
                      1.61, 1.66, 1.67, 1.69, 1.65, 1.65, 1.66, 1.65, 1.65, 1.62, 1.78, 1.74,
                      1.72, 1.73, 1.75, 1.73, 1.73, 1.72, 1.75, 1.73, 1.77, 1.74]
stress_ng_malloc_awws = [0, 41.80, 43.00, 43.45, 44.71, 45.61, 45.95, 46.68, 47.33,
                         47.97, 48.97, 49.24, 49.95, 50.73, 51.31, 51.71, 52.09, 52.58, 52.88,
                         53.31, 53.40, 54.19, 55.28, 55.35, 55.14, 55.25, 55.33, 55.42, 55.15,
                         55.35, 55.43, 55.30, 55.34, 55.47]
stress_ng_io_awws = [0, 0.24, 0.28, 0.28, 0.28, 0.28, 0.29, 0.29, 0.31, 1.37, 1.37,
                     1.38, 1.37, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.40,
                     1.41]
apache_awws = [0, 5.29, 7.45, 10.83, 12.73, 13.48, 13.62, 13.63, 13.71, 13.75,
               13.75, 13.67, 13.76, 13.77, 13.81, 13.80, 13.76, 13.82, 13.79, 13.82,
               13.77, 13.84, 13.83, 13.83, 13.86, 13.86, 13.79, 13.85, 13.91, 13.82]
resnet50_infer_awws = [0, 2.65, 3.08, 3.18, 3.46, 3.62, 3.22, 3.83, 7.76, 7.61,
                       7.65, 7.81, 7.69, 8.05, 7.81, 15.05, 14.69, 14.85, 15.09, 14.85, 15.02,
                       14.27, 15.07]
redis_get_awws = [0, 10.83, 23.33, 30.85, 35.39, 38.27, 40.72, 43.04, 45.10, 46.53,
                  47.61, 48.43, 49.08, 49.68, 50.11, 50.45, 50.71, 54.86, 55.08, 55.16,
                  55.33, 55.49, 55.76]
redis_get_set_awws = [0, 9.21, 18.58, 25.72, 30.41, 34.13, 37.08, 39.54, 41.60,
                      43.30, 44.79, 46.19, 47.44, 48.32, 49.01, 49.47, 49.88, 50.33, 50.73,
                      51.08, 51.45, 51.74, 51.97, 52.10, 52.34, 52.53, 52.70, 52.93, 53.04,
                      53.14, 53.31, 53.42, 53.46, 53.61, 53.66, 53.74, 53.80, 53.86, 53.93,
                      53.98, 54.02, 54.06, 54.10, 54.21, 54.24]
mp3_awws = [0, 4.19, 4.50, 4.52, 4.73, 4.74, 4.72, 4.74, 4.74, 4.74, 4.78, 4.73,
            4.81, 4.73, 4.83, 4.91, 4.90, 4.96, 4.91, 4.91, 4.93, 4.91, 4.93, 4.95,
            4.97, 4.94, 4.97, 5.00, 5.00, 5.00]
rnn_infer_awws = [0, 17.57, 30.51, 31.96, 29.86, 32.06, 31.52, 40.54, 41.14,
                  42.68, 41.99, 40.79, 38.86, 41.56, 40.66, 40.34, 40.73, 39.25, 41.35,
                  41.11, 40.78, 40.36, 39.95, 39.17, 41.34, 41.22, 40.94, 40.47, 39.09,
                  41.14, 41.27, 40.19, 39.37, 41.15, 41.16, 40.40, 40.29, 40.29, 40.87,
                  40.89]
rnn_traning_awws = [0, 20.68, 28.26, 28.74, 28.65, 28.81, 29.10, 31.57, 31.68,
                    31.66, 31.58, 31.73, 31.79, 31.80, 31.62, 31.72, 31.81, 31.73, 31.84,
                    31.89, 31.88, 31.91, 31.83, 31.81, 31.79, 31.84, 31.53, 31.88, 31.75,
                    31.80, 31.73, 31.74]


def generate_figure(awws, filename):
    while (len(awws) < len(xlabel)):
        awws.append(awws[len(awws) - 1])
    aaws = []
    # for i in awws:
    #     aaws.append(i + 10)

    fig, ax = plt.subplots()
    fig.set_size_inches(2, 1)
    marker_size = 0.1
    ax.plot(xlabel, awws, markersize=marker_size, linewidth=2, \
            label="", color=color_jxg_grey, marker="*")
    # ax.plot(xlabel, aaws, markersize=marker_size, linewidth=2, \
    #         label="", color=color_light_grey, marker="*")
    ax.set_xscale("log")

    ax.grid(True, linestyle=':')
    ax.tick_params(labelsize='medium', width=1, color="black")
    ax.set_ylim([0, 110])

    plt.subplots_adjust(bottom=0.20, left=0.15)
    # plt.show()
    fig.savefig(filename, dpi=300)
    plt.close()


generate_figure(pagerank_awws, "/Users/snake0/yanni-img/page_rank_awws.pdf")
generate_figure(oltp_ro_awws, "/Users/snake0/yanni-img/oltp_ro_awws.pdf")
generate_figure(oltp_rw_awws, "/Users/snake0/yanni-img/oltp_rw_awws.pdf")
generate_figure(stress_ng_cpu_awws, "/Users/snake0/yanni-img/stress_ng_cpu_awws.pdf")
generate_figure(stress_ng_malloc_awws, "/Users/snake0/yanni-img/stress_ng_malloc_awws.pdf")
generate_figure(stress_ng_io_awws, "/Users/snake0/yanni-img/stress_ng_cpu_io.pdf")
generate_figure(apache_awws, "/Users/snake0/yanni-img/apache_awws.pdf")
generate_figure(resnet50_infer_awws, "/Users/snake0/yanni-img/resnet50_infer_awws.pdf")
generate_figure(redis_get_awws, "/Users/snake0/yanni-img/redis_get_awws.pdf")
generate_figure(redis_get_set_awws, "/Users/snake0/yanni-img/redis_get_set_awws.pdf")
generate_figure(mp3_awws, "/Users/snake0/yanni-img/mp3_awws.pdf")
generate_figure(rnn_infer_awws, "/Users/snake0/yanni-img/rnn_infer_awws.pdf")
generate_figure(rnn_traning_awws, "/Users/snake0/yanni-img/rnn_traning_awws.pdf")

final = []
final.append(pagerank_awws[len(pagerank_awws) - 1])
final.append(oltp_ro_awws[len(oltp_ro_awws) - 1])
final.append(oltp_rw_awws[len(oltp_rw_awws) - 1])
final.append(oltp_rw_awws[len(stress_ng_cpu_awws) - 1])
final.append(stress_ng_malloc_awws[len(stress_ng_malloc_awws) - 1])
final.append(stress_ng_io_awws[len(stress_ng_io_awws) - 1])
final.append(apache_awws[len(apache_awws) - 1])
final.append(resnet50_infer_awws[len(resnet50_infer_awws) - 1])
final.append(redis_get_set_awws[len(redis_get_set_awws) - 1])
final.append(mp3_awws[len(mp3_awws) - 1])
final.append(rnn_infer_awws[len(rnn_infer_awws) - 1])
final.append(rnn_traning_awws[len(rnn_traning_awws) - 1])

print(mean(final))
