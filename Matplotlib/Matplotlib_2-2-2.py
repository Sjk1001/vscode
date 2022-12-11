#2.2.2 系列ラベルを設定する
print('---------------2.2.2 系列ラベルを設定する---------------')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title("graphs of trigonometric functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#"y=sin(x)"と系列ラベルを設定
plt.plot(x, y1, color="r", label="y=sin(x)")

#"y=cos(x)"と系列ラベルを設定
plt.plot(x, y2, color="b", label="y=cos(x)")

#系列ラベルを表示
plt.legend()
plt.show()