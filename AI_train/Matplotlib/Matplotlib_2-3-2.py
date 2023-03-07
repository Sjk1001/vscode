#2.3.2 サブプロットを作成する
print('--------------2.3.2 サブプロットを作成する--------------')

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,6))
#axesオブジェクトを2行3列に分割して右下にグラフを追加
ax = fig.add_subplot(2, 3, 6)

# y=xのグラフをaxesオブジェクトに描画
x = np.linspace(0, 100)
y = x
ax.plot(x, y)
plt.show()

# add_subplot(行数, 列数, 何番目か)
#   行数：図を何行に分割するのか。
#   列数：図を何列に分割するのか。
#   何番目：図の左上から右方向に1, 2, 3 ...と数えて何番目に追加するのか。
print("-----------------------------")

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(2, 3, 6)
x = np.linspace(0, 100)
y = x
ax.plot(x, y)

for i in range(6):
    if i !=5:
        fig.add_subplot(2, 3, i+1)


plt.show()