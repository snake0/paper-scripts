import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium', size=13)
plt.rcParams['hatch.color'] = '#636466'
plt.rcParams['hatch.linewidth'] = 1

fig, ax = plt.subplots()
fig.set_size_inches(8, 3.5)

name = ["BT.A", "CG.B", "DC.W", "EP.C", "FT.B", "IS.C",
        "LU.A", "MG.C", "SP.A", "UA.W"]

colors = ["#7ec1be", "#53a2bf", "#366eaa", "#0e215b"]

t = 0.5

bt = np.array(
    [0, 0, 0, 1043, 2265, 2265, 2265, 2265, 2270, 2270, 2270, 2270, 2431, 2971, 2971, 2971, 2971, 2971, 2978, 2978,
     2978, 2978, 2978, 2978, 2978, 2978, 2978, 2978, 3005, 4036, 4036, 4036, 4036, 4036, 4036, 4036, 4036, 4036, 4036,
     4036, 4036, 4036, 4036, 4036, 4815, 5125, 5125, 5125, 5286, 5554, 5554, 5554, 5554, 5554, 5554, 5554, 5654, 5995,
     6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094,
     6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6094, 6100, 6100, 6100, 6100])

cg = np.array(
    [238401, 238401, 238401, 240571, 244723, 244746, 244759, 244759, 244759, 244759, 246327, 246349, 246879, 246881,
     246881, 246881, 246881, 246881, 246881, 246889, 246889, 246889, 246898, 246898, 246898, 246898, 246898, 246898,
     246898, 246898, 246898, 246898, 246898, 246898, 246898, 246898, 249496, 250033, 250062, 250062, 250062, 256286,
     256286, 257852, 257855, 257855, 257855, 257855, 257855, 257855, 257855, 257855, 257855, 257855, 257855, 257855,
     257855, 257855, 257855, 257855, 257855])

dc = np.array(
    [6100, 6100, 6100, 11817, 12741, 12923, 12926, 12928, 12928, 12929, 12929, 12930, 12930, 12931, 12931, 12934, 12934,
     12935, 12935, 12935, 12935, 12935, 12935, 12936, 12936, 12936, 12936, 12939, 12940, 12940, 12941, 12941, 12941,
     12941, 12941, 12942, 12942, 12942, 12943, 12946, 12947, 12948, 12948, 12948, 12948, 12949, 12949, 12949, 12953,
     12953, 12953, 12953, 12953, 12953, 12953, 12954, 12954, 12956, 12957, 12961, 12964, 12965, 12965, 12965, 12967,
     12967, 12968, 12969, 12971, 12973, 12973, 12973, 12973, 12973, 12973, 12973, 12975, 12975])

ep = np.array(
    [257855, 257855, 257855, 262023, 262023, 262023, 262023, 262023, 262023, 262023, 262023, 262023, 262023, 262023,
     262023, 262023, 262023, 262023, 262025, 262025, 262025, 262025, 262025, 262025, 262025, 262025, 262025, 262025,
     262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026, 262026,
     262026, 262026, 262026, 262026, 262026, 262026])

ft = np.array(
    [12975, 12975, 12975, 12988, 13058, 13725, 33703, 37287, 41587, 42611, 42832, 47970, 51046, 51053, 51123, 69654,
     72853, 72896, 72896, 77524, 77555, 77579, 77579, 83723, 88372, 89422, 89435, 94560, 94560, 94560, 96609, 96635,
     96653, 97345, 108097, 108099, 108110, 112291, 120995, 121005, 124590, 129198, 129202, 130738, 133319, 134920,
     141283, 142870, 149014, 149061, 150707, 160439, 167607, 167630, 167718, 170790, 170790, 170790, 171814, 172980,
     173107, 174132, 174358, 181542, 181544, 183592, 185128, 186664, 186664, 186664, 187176, 187177, 189800, 199544,
     199544, 199544, 204803, 211971, 211971, 211972, 212485, 221189, 221255, 221319, 222911, 224448])

iss = np.array(
    [337653, 337653, 337653, 338677, 341749, 358133, 370933, 370954, 370967, 370969, 370969, 371201, 371713, 371713,
     372225, 372225, 372225, 372225, 372225, 372225, 372225, 372225, 372737, 373249, 373256, 373256, 373256, 373256,
     373256, 373256, 373768, 373768, 373768, 373768, 374792, 374792, 374792, 374798, 374798, 374798, 374798, 374798,
     374798, 374798, 374798])

lu = np.array(
    [379232, 379232, 379232, 380628, 381476, 381640, 381640, 381640, 382154, 382154, 382154, 382154, 382154, 382154,
     382154, 382154, 382284, 382284, 382284, 382284, 382284, 382284, 382284, 382336, 382434, 382434, 382434, 382434,
     382434, 382434, 382434, 382434, 382434, 382434, 382434, 382434, 382434, 382434, 382453, 382465, 382471, 382471,
     382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471,
     382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 382471, 383431, 383543,
     383543, 383543, 383561, 383675, 383675, 383675, 384206, 384436, 384437, 384437, 384437, 384437, 384437, 384437,
     384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437, 384437])

mg = np.array(
    [384437, 384437, 384437, 385470, 396735, 417215, 424383, 424383, 439236, 446404, 461252, 469444, 469444, 469444,
     470980, 478669, 478695, 478695, 479720, 479723, 480752, 480752, 482288, 482288, 485360, 486400, 488960, 489984,
     489984, 489984, 489985, 489985, 489985, 489985, 489985, 491009, 491009, 491009, 491013, 491013, 491525, 491525,
     491525, 491525, 491525, 491525, 491525, 491525, 491525, 491525, 492553, 492553, 492553, 492553, 493067, 493067,
     493067, 493067, 493067, 493067, 496139, 496143, 496143, 496143, 496143, 496143, 496659, 497173, 497239, 497239,
     497239, 497249, 500348, 500348, 500348, 500348, 500348, 532604, 535174, 535174, 536710, 552070, 552070, 552070,
     552070, 552070, 568454, 578183, 599175, 599687, 599687, 599687, 599687, 599687, 599687, 599692, 599692, 599692,
     599692, 599692, 599692, 599692, 599692, 599692, 599695, 600719, 603283, 616084, 616084, 631476, 631476, 631476,
     631476, 634548, 639668, 644280, 644798, 663742, 666302, 666302, 666302, 666302, 666814, 666814, 679102, 683198,
     683198, 683198, 683710, 683710, 685758, 685758, 685759, 685759, 685763, 687811, 689859, 692931, 697027, 721091,
     721184, 721189, 721200, 726329, 726329, 732985, 749369, 752441, 752441, 752441, 753977, 766265, 773945, 774995,
     776568, 780664, 780664, 780664, 780664, 780664, 780664, 780664, 791928, 796025])

sp = np.array(
    [796025, 796025, 796025, 796767, 798132, 799069, 799069, 799069, 799581, 799595, 799595, 799595, 799945, 799945,
     799945, 799945, 799945, 799945, 799945, 799945, 800627, 801009, 801009, 801009, 801134, 801516, 801516, 801516,
     801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517,
     801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801517, 801603, 801603,
     801603, 801603, 802519, 802683, 802683, 802683, 802848, 803154, 803154, 803154, 803155, 803155, 803155, 803155,
     803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155,
     803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155,
     803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155, 803155])

ua = np.array(
    [803155, 803155, 803155, 803439, 803572, 803572, 803572, 803573, 803573, 803573, 803575, 803623, 803678, 803678,
     803678, 803678, 803678, 803678, 803678, 803877, 803888, 803888, 803897, 803932, 803959, 803959, 803959, 804138,
     804183, 804183, 804200, 804200, 804200, 804200, 804226, 804270, 804300, 804300, 804313, 804325, 804332, 804332,
     804522, 804529, 804571, 804571, 804633, 804633, 804683, 804684, 804700, 804701, 804701, 804701, 804701, 804701,
     804701, 804701, 804708, 804757, 804757, 804796, 804803, 804803, 804803, 805103, 805139, 805182, 805182, 805182,
     805182, 805182, 805182, 805182, 805182, 805182, 805182, 805182, 805182, 805182, 805272, 805280, 805334, 805334,
     805496, 805519, 805519, 805519, 805519, 805529, 805531, 805537, 805570, 805581, 805581, 805581, 805887, 805912,
     805949, 805963, 806025, 806025, 806025, 806113, 806174, 806241, 806241, 806253, 806328, 806350, 806350, 806469,
     806484, 806518, 806518, 806586, 806642, 806678, 806678, 806708, 806729, 806755, 806755, 806755, 806757, 806768,
     806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768,
     806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768,
     806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768, 806768])

# data = [bt, cg, dc, ep, ft, iss, lu, mg, sp, ua]
data = [bt, lu, sp, ua]


def diff(a):
    aaa = []
    for i in range(len(a) - 1):
        aaa.append(a[i + 1] - a[i])
    return aaa


maxl = -1
for i in data:
    if len(i) > maxl:
        maxl = len(i)

x = np.arange(maxl - 1)

for i in range(len(data)):
    for j in range(len(data[i]) - 1):
        data[i][j] = data[i][j + 1] - data[i][j]
    data[i][-1] = 0

for i in range(len(data)):
    if len(data[i]) < maxl:
        while len(data[i]) < maxl:
            data[i] = np.append(data[i], 0)

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         data[i][j] += 1

x = np.arange(maxl)

for i in range(len(data)):
    plt.plot(x[::4], data[i][::4], linewidth=0.5, marker="x", label=name[i],markersize=0.3)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=False, shadow=False, ncol=5, frameon=False, prop={'size': 13})

plt.tight_layout()
# plt.yscale('log')
plt.title("Execution Time Distribution")
plt.savefig('/Users/snake0/taco-journal/newimgs/migratee.pdf', dpi=300, bbox_inches='tight')

plt.show()

plt.close()