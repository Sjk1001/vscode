#2.3.6 サブプロット内のグラフにグリッドを表示する
print('-----2.3.6 サブプロット内のグラフにグリッドを表示する-----')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(2, 3, 5)
# サブプロットaxのグラフにグリッドを表示
ax.grid(True)

ax.plot(x, y)
for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i+1)

plt.show()