#2.1.5 グラフの軸に目盛りを設定する
print('-------------2.1.5 グラフの軸に目盛りを設定する-------------')

import matplotlib.pyplot as plt

plt.plot([2,3,9,1,5])
#matplotlib.pyplot.xticks(目盛りを挿入する位置, 表示する目盛りの文字列)
plt.xticks([2.7,2.1,3.5],["i","ii","iii"])
plt.show()