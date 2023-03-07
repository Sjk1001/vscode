#2.3.7 サブプロット内のグラフの軸に目盛りを設定する
print('-----2.3.7 サブプロット内のグラフの軸に目盛りを設定する-----')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)
positions = [0, np.pi/2, np.pi]
labels = ["0°", "90°", "180°"]

fig =plt.figure(figsize=(6, 4))
ax = fig.add_subplot(2, 3, 5)
ax.grid(True)

ax.set_xticks(positions)
ax.set_xticklabels(labels)

ax.plot(x, y)

for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i+1)

plt.show()