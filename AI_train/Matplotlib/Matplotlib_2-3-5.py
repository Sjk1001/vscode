#2.3.5 サブプロット内のグラフの要素に名前を設定する
print('-----2.3.5 サブプロット内のグラフの要素に名前を設定する-----')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(2, 3, 5)

# サブプロットaxのグラフのタイトルを "y=cos(x)" に設定
ax.set_title("y=cos(x)")

# サブプロットaxのx軸のラベルを "x-axis"、y軸のラベルを "y-axis" に設定
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

ax.plot(x, y)
for i in range(6):
    if i == 4:
        continue
    fig.add_subplot(2, 3, i+1)

plt.show()