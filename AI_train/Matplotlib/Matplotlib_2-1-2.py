#2.1.2 グラフの表示範囲を設定する
print('---------------2.1.2 グラフの表示範囲を設定する---------------')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi)
y = np.cos(x)

# x=[0,3]
plt.xlim([0, 3])
plt.plot(x, y)
plt.show()