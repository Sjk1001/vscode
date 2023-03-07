#2.1.3 グラフの要素に名前を設定する
print('--------------2.1.3 グラフの要素に名前を設定する--------------')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

#set the title for graph
plt.title("cos Graph")

plt.xlabel("x-axis")
plt.xlim([0, 3])
plt.plot(x, y)
plt.show()