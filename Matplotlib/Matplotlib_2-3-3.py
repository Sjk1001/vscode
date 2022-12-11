#2.3.3 サブプロットのまわりの余白を調整する
print('----------2.3.3 サブプロットのまわりの余白を調整する----------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(2, 3, 5)

#figure内のaxesを、横2、縦1の間隔を開ける。
fig.subplots_adjust(wspace=2, hspace=1)
ax.plot(x,y)

for i in range(6):
    if i == 4 :
        continue
    fig.add_subplot(2, 3, i+1)

plt.show()