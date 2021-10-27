import csv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

if __name__ == "__main__":

    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

    # constants
    width = 0.1
    font_size = 28
    aspect = 0.4
    file_path = './stress-ng-scale.CSV'
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    plt.rc('font', family='Nimbus Sans L', weight='medium',size=14)
    matplotlib.rcParams['axes.linewidth'] = 0.5  # set the value globally

    # colors & labels
    labels = ['ackermann', 'clongdouble', 'decimal128', 'fft', 'hamming', 'jenkin', 'matrixprod', 'nsqrt', 'rand48']
    colors = ["#fcfcd8", "#f4f8c2", "#d9ecb8", "#bcdfba", "#a7d5b9", "#6db8be", "#3b7cb1", "#1e307c"]

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 6.5)
    ax.tick_params(labelsize=font_size)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data_list = list(csv_reader)
        n = len(data_list)
        x = np.arange(len(data_list[0]))
        for i in range(n):
            data = [float(x) for x in data_list[i]]
            rects = ax.bar(x - width * 4 + i * width + width / 2, data, width,
                           color=colors[i], label="4x"+str(i + 1))
    ax.set_ylabel('Normalized Results', fontsize=font_size)
    ax.set_title('Scalability of Stress-ng CPU Methods on GiantVM', fontsize=font_size)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=font_size-4, rotation=45)
    ax.legend(title='# vCPUs', title_fontsize=font_size, fontsize=font_size, \
            loc='center left', bbox_to_anchor=(1, 0.5) ,frameon=False,facecolor="white")
    ax.set_aspect(aspect)
    fig.tight_layout()

    plt.grid(axis='y', linewidth=0.4, linestyle=(0, (2, 4)), color="#000000")

    plt.subplots_adjust(bottom=0.0, top=1.1)

    fig.savefig('/Users/snake0/taco-journal/newimgs/stress-ng-scale.pdf', dpi=300)
    plt.show()
