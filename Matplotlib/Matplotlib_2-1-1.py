#2.1.1 グラフにデータをプロットする
print('---------------2.1.1 グラフにデータをプロットする---------------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi)
y = np.cos(x)

plt.plot(x,y)
plt.show()