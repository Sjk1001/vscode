import numpy as np


# シードを設定せずに、X, Y にそれぞれ5つの乱数を格納し表示する
print("シードを設定しない場合")

X = np.random.randn(5)
print("X:", X)

Y = np.random.randn(5)
print("Y:", Y)
print()


# シードを設定して、x, y にそれぞれ5つの乱数を格納し表示する
print("シードを設定した場合")

np.random.seed(0)    # シードを設定
x = np.random.randn(5)
print("x:", x)

np.random.seed(1)    # シードを設定
y = np.random.randn(5)
print("y:", y)

print('-----------------------------------------------------------------------------')
####1.2.2 正規分布に従う乱数を生成する####
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

#正規分布に従う乱数を100000個生成
x = np.random.randn(100000)

#可視化
plt.hist(x, bins='auto')
plt.show()




