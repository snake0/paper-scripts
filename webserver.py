import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # statistics
    x_labels = ['8', '16', '24', '32']
    x_coordinates = np.arange(4)
    # b -- Barrelfish l -- Linux n -- concurrency level
    b10 = [111.45, 110.23, 137.39, 86.82]
    b20 = [228.61, 161.73, 185.74, 146.47]
    b40 = [280.39, 202.15, 209.57, 157.82]
    l10 = [52.85, 36.75, 28.87, 22.69]
    l20 = [45.48, 22.73, 24.40, 22.11]
    l40 = [53.62, 16.54, 19.14, 16.38]

    # constants
    font_size = 24
    marker_size = 12
    line_width = 4
    barrelfish_line_color = '#d73f37'
    linux_line_color = '#000000'
    font = {'font.size': font_size, 'font.family': 'Helvetica Neue', 'font.weight': 'medium'}
    matplotlib.rcParams.update(font)

    # paint
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 7.85)
    plt.subplots_adjust(top=0.95, right=0.95, bottom=0.15)
    # n=10,Barrelfish
    ax.plot(x_coordinates, b10, label="{10,Barrelfish}", linestyle='-', marker='+', linewidth=line_width,
            color=barrelfish_line_color, markersize=marker_size)
    # n=20,Barrelfish
    ax.plot(x_coordinates, b20, label="{20,Barrelfish}", linestyle='--', marker='x', linewidth=line_width,
            color=barrelfish_line_color, markersize=marker_size)
    # n=40,Barrelfish
    ax.plot(x_coordinates, b40, label="{40,Barrelfish}", linestyle='dashdot', marker=9, linewidth=line_width,
            color=barrelfish_line_color, markersize=marker_size)
    # n=10,Barrelfish
    ax.plot(x_coordinates, l10, label="{10,Linux}", linestyle='-', marker='+', linewidth=line_width,
            color=linux_line_color, markersize=marker_size)
    # n=20,Barrelfish
    ax.plot(x_coordinates, l20, label="{20,Linux}", linestyle='--', marker='x', linewidth=line_width,
            color=linux_line_color, markersize=marker_size)
    # n=40,Barrelfish
    ax.plot(x_coordinates, l40, label="{40,Linux}", linestyle='dashdot', marker=9, linewidth=line_width,
            color=linux_line_color, markersize=marker_size)

    ax.set_xlabel("#vCPUs")
    ax.set_ylabel("QPS")
    ax.set_title("Webserver")
    ax.set_xticks(x_coordinates)
    ax.set_xticklabels(x_labels, fontsize=font_size)
    ax.legend(title_fontsize=font_size, fontsize=16, loc='best')

    plt.savefig('../imgs/new/evaluation/webserver.pdf', dpi=300)
    plt.show()
