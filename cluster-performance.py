import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rc('font', family='Helvetica Neue', weight='medium', size=11)

x = np.arange(10)
vanilla = [251.88, 133.6, 0.117, 23.13, 252.58, 4.74, 166.34, 162.97, 100.86, 0.0687]

name = ["BT.A.*", "CG.B.*", "DC.W.*", "EP.C.*", "FT.B.*", "IS.C.*",
        "LU.A.*", "MG.C.*", "SP.A.*", "UA.W.*"]

clique = [36.81117993, 12.46257485, 32.47863248, 0.302637268, -0.581993824,
          19.4092827, 14.56053866, 53.81358532, 102.0523498, 31.87772926]

nb = [-9.242496427, -4.513473054, 28.20512821, -5.361003026, -55.42006493,
      -7.383966245, -9.582782253, -62.10959072, -9.884989094, -11.20815138]
