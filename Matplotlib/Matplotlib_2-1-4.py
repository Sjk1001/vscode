#2.1.4 グラフにグリッド（目盛線）を表示する
print('--------------2.1.4 グラフにグリッドを表示する--------------')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

plt.title("cos Graph")
plt.xlabel("x-axis")
plt.xlim([0, 3])

#グラフにグリッドを表示
plt.grid(True)

plt.plot(x, y)
plt.show()