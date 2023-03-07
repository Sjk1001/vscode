#2.3.1 図の大きさを設定する
print('---------------2.3.1 図の大きさを設定する---------------')

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, np.pi)
y =np.cos(x)

#figureオプション作成 省略するとfigsize=(8, 6)
plt.figure(figsize=(3, 2))

plt.plot(x, y)
plt.show()