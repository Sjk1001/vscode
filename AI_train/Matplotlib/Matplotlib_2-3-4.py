#2.3.4 サブプロット内のグラフの表示範囲を設定する
print('--------2.3.4 サブプロット内のグラフの表示範囲を設定する--------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(2, 3, 5)

#サブプロットaxのグラフのX軸の表示範囲を0~3に設定
ax.set_xlim([0, 3])

ax.plot(x, y)

for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i+1)

plt.show()