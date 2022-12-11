import numpy as np

list_1 = [1, 2, 3, 4, 5]
arr_1 = np.array(list_1)

print('list型')
print(list_1)

print('ndarray型')
print(arr_1)

arr_2 = arr_1 + 5
print(arr_2)

# 配列同士の計算
import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([3, 2, 5, 4, 1])

arr_3 = arr_1 + arr_2

print(arr_3)

# NumPy配列の作成
import numpy as np

list_1 = [1, 2, 3, 4, 5]
arr_1 = np.array(list_1)
print(arr_1)

list_2 = [[1, 2], [3, 4], [5, 6]]
arr_2 = np.array(list_2)
print(arr_2)

#NumPy配列のshape 要素数
list_1 = [[1, 2], [3, 4], [5, 6]]
arr_1 = np.array(list_1)
print(arr_1.shape)
print(arr_1)

list_2 = [1, 2, 3, 4, 5, 6]
arr_2 = np.array(list_2)
list_3 = [[1, 2, 3, 4, 5, 6]]
arr_3 = np.array(list_3)

print(arr_2.shape)
print(arr_2)
print(arr_3.shape)
print(arr_3)

#numpy.loadtxt()
import numpy as np

arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv",
                    delimiter=",",  #区切り文字をカンマに指定
                    skiprows=1,     #最初の1行をスキップ
                    usecols=[0, 1, 2]) #使用する列の番号
print(arr_1)