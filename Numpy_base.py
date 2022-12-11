import numpy as np

list_1 = [1, 2, 3, 4, 5]
arr_1 = np.array(list_1)

print('list型')
print(list_1)

print('ndarray型')
print(arr_1)

arr_2 = arr_1 + 5
print(arr_2)
print('-----------------------------------------------------------------------------')
# 配列同士の計算
import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([3, 2, 5, 4, 1])

arr_3 = arr_1 + arr_2

print(arr_3)
print('-----------------------------------------------------------------------------')
# NumPy配列の作成
import numpy as np

list_1 = [1, 2, 3, 4, 5]
arr_1 = np.array(list_1)
print(arr_1)
print('-----------------------------------------------------------------------------')
list_2 = [[1, 2], [3, 4], [5, 6]]
arr_2 = np.array(list_2)
print(arr_2)
print('-----------------------------------------------------------------------------')
#NumPy配列のshape 要素数
list_1 = [[1, 2], [3, 4], [5, 6]]
arr_1 = np.array(list_1)
print(arr_1.shape)
print(arr_1)
print('-----------------------------------------------------------------------------')
list_2 = [1, 2, 3, 4, 5, 6]
arr_2 = np.array(list_2)
list_3 = [[1, 2, 3, 4, 5, 6]]
arr_3 = np.array(list_3)

print(arr_2.shape)
print(arr_2)
print(arr_3.shape)
print(arr_3)
print('-----------------------------------------------------------------------------')
#1.2.5 numpy.loadtxt()  
import numpy as np

arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv",
                    encoding='utf-8',#该死的日语mic保存时候文件性质是cp932 需要手动改成 utf-8
                    delimiter=",",  #区切り文字をカンマに指定
                    skiprows=1,     #最初の1行をスキップ
                    usecols=[0, 1, 2]) #使用する列の番号
print(arr_1)
print('-----------------------------------------------------------------------------')
#test of 1.2.5
import numpy as np


with open("./4002_new_numpy/weather_tokyo.csv", encoding="shift_jis") as f_in:

    arr_1 = np.loadtxt(f_in,
                       delimiter=",",
                       skiprows=3,
                       usecols=[1, 2, 3, 4])

print(arr_1)
print('-----------------------------------------------------------------------------')
# 1.3.1 Numpy配列と数値の四則演算
import numpy as np

arr_1 = np.array([[1,2],[3,4]])
arr_2 = arr_1+5

print(arr_1)
print(arr_2)

arr_3 = arr_1*5

print(arr_3)

arr_4 = arr_1 * np.array([[5,2],[2,5]])
print(arr_4)
print('-----------------------------------------------------------------------------')
#1.3.2 特定の行列に対して四則演算をする
import numpy as np

arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv",encoding='utf-8',
                    delimiter=",",
                    skiprows=1,
                    usecols=[0,1,2])

arr_2 = np.array([1, 0.394, 1 ])
arr_3 = arr_1 * arr_2

print('arr_1')
print(arr_1)
print('arr_3')
print(arr_3)
print('-----------------------------------------------------------------------------')
# test of 1.3.2
import numpy as np


with open("./4002_new_numpy/weather_tokyo.csv", encoding="shift_jis") as f_in:

    arr_1 = np.loadtxt(f_in,
                       delimiter=",",
                       skiprows=3,
                       usecols=[1, 2, 3, 4])

arr_2 = arr_1 * np.array([1.8, 1, 1, 1]) + np.array([32, 0, 0, 0])

print(arr_1)
print(arr_2)
print('-----------------------------------------------------------------------------')
########2.1.1#########リストと同様の抽出
import numpy as np

arr_1 = np.array([2,1,9,3,4,5])

num = arr_1[2] # 3番目の要素を抽出
arr_2 = arr_1[1:4] # 2番目の要素から4番目の要素までを抽出
arr_3 = arr_1[::2] # ひとつおきに要素を抽出****** 【：：】です。要注意

print(num)
print(arr_2)
print(arr_3)
print('-----------------------------------------------------------------------------')

########2.1.2#########リストではできない抽出
import numpy as np

list_1 = [[1,2],[3,4],[5,6]]
arr_1 = np.array(list_1)
 
print(arr_1)
print(list_1[2][1])
print(arr_1[1, 0])
#print(list_1[2, 1])`はため`
print(arr_1[1][0])
print('-----------------------------------------------------------------------------')

########2.1.3#########複数要素の抽出
import numpy as np

list_1 = [[1,2],[3,4],[5,6]]
arr_1 = np.array(list_1)

# リストにより複数要素を抽出
print(arr_1[2, 1])
print(arr_1[[2, 1]])

arr_2 = np.array([2,1])
print(arr_1[arr_2])

arr_3 = np.array([[0,2],[1,0]])
print(arr_1[arr_3])
print('-----------------------------------------------------------------------------')

########2.2.1#########2次元配列の軸の入れ替え（転置）
import numpy as np

list_1 = [[1,2],[3,4],[5,6]]
arr_1 = np.array(list_1)

print('転置前のarr_1')
print(arr_1)

print('転置後のarr_1')
print(arr_1.T)
print('-----------------------------------------------------------------------------')

########2.2.2#########3次元以上の配列の軸の入れ替え transpose
import numpy as np

list_1 = [[[1, 2], [3,  4], [5 , 6]], 
          [[7, 8], [9, 10], [11, 12]]]
arr_1 = np.array(list_1)

print('軸の入れ替え前 arr_1.shape: ', arr_1.shape)
print(arr_1)

arr_2 = arr_1.transpose(1, 0, 2)
print('arr_1を0軸と1軸の入れ替え後arr_2.shape：',arr_2.shape)
print(arr_2)

arr_3 = arr_2.transpose(2, 1, 0)
print('arr_2を軸0と軸2で入れ替え後arr_3.shape：',arr_3.shape)
print(arr_3)

print(arr_1[0,2,1])
print(arr_2[2,0,1])

arr_4 = arr_1.transpose()
print(arr_4)
print('-----------------------------------------------------------------------------')

########2.2.3#########配列の形状変更-reshape-
import numpy as np
arr_1 = np.array(range(50))
print('arr-1 shape：', arr_1.shape)
print(arr_1)
print('--------------------------------------------------')
arr_2 = arr_1.reshape(2 ,5 ,5)

print('arr_2 shape:', arr_2.shape)
print(arr_2)
print('--------------------------------------------------')
#arr_3 = arr_1.reshape(10,10) 
#       -> ValueError: cannot reshape array of size 50 into shape (10,10)

arr_1 = np.array(range(np.random.randint(1, 30))) # -> ランダムな要素数を持つ配列arr_1
arr_2 = arr_1.reshape(-1, 1)  # 行数は不明だが、1列の配列に変形　
print(arr_1)
print(arr_2)
print('-----------------------------------------------------------------------------')

########2.2.4#########配列の形状変更-resize-
import numpy as np

arr_1 = np.array(range(50))

arr_1.resize(10, 10) #不足分が0で埋められています。
print(arr_1)
print('--------------------------------------------------')
arr_1 = np.array(range(50))
arr_2 = arr_1.resize(10, 10) #resize()メソッドは返り値を持ちません。

print(arr_2)
print('-----------------------------------------------------------------------------')

########3.1.1#########--データ型
import numpy as np

list_1 = [1.1, 2.1, 3.1, 4.1, 5.1]
print(list_1)
arr_1 = np.array(list_1, dtype=np.uint8) # ここでデータ型を「uint8」に指定
print(arr_1.dtype)
print(arr_1)
print('-----------------------------------------------------------------------------')

########3.1.2#########--in-place処理
import numpy as np

arr_1 = np.array(range(50))
arr_2 = arr_1.resize(10, 10) # in-place処理
print(arr_1)
print(arr_2)

#sort 昇順
arr_1 = np.array([4, 0, 6, 3, 1, 7 ,2, 8])
print(arr_1)

arr_1.sort() # in-place処理
print('sort 昇順')
print(arr_1)
print('--------------------------------------------------')
#sort 降順
arr_1 = np.array([4, 0, 6, 3, 1, 7 ,2, 8])
print(arr_1)

arr_1.sort() # in-place処理
arr_2 = arr_1[::-1]
print('sort 降順')
print(arr_2)
print('-----------------------------------------------------------------------------')

########3.2.1#########--ビューについて
import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = arr_1

arr_2[3] = 100 #arr_2の値を変更する

print(arr_1)
print(arr_2)
print('--------------------------------------------------')
arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = arr_1[:2]

arr_2[0] = 100

print(arr_1)
print(arr_2)
print('-----------------------------------------------------------------------------')

########3.2.2#########コピーについて
import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = arr_1.copy()

arr_2[3] = 100
print(arr_1)
print(arr_2)
print('-----------------------------------------------------------------------------')

########4.1.1#########引数axisについて 特定轴的合計
import numpy as np

arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv",encoding='utf-8',
                        delimiter=",",
                        skiprows=1,
                        usecols=[1, 2])
print('axis指定しないの場合、すべての要素の合計をとる')
print(arr_1.sum())
print('axis=0の場合、0番目の軸に沿って合計をとる')
print(arr_1.sum(axis=0))
print('axis=1の場合、1番目の軸に沿って合計をとる')
print(arr_1.sum(axis=1))
print('-----------------------------------------------------------------------------')

########4.1.2#########合計
# ./4002_new_numpy/csv_example.csvを読み込む
arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv", encoding="utf-8",
                   delimiter=",",    # カンマ区切りであることを明示
                   skiprows=1,       # 最初の1行を無視
                   usecols=[1, 2])    # 1列目と2列目を使用
print(arr_1)
print('axis指定なしの場合')
print(arr_1.sum())

print('axis=0の場合')
print(arr_1.sum(axis=0))

print('axis=1の場合')
print(arr_1.sum(axis=1))
print('-----------------------------------------------------------------------------')

########4.1.3#########平均
import numpy as np

list_1 = [1,3,5,7,9,2,4,6,8,10,11,13,15,17,19]
arr_1 = np.array(list_1)

#arr_1の平均値を求める
print(arr_1.mean())
print('--------------------------------------------------')
arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv", encoding="utf-8",
                   delimiter=",",    # カンマ区切りであることを明示
                   skiprows=1,       # 最初の1行を無視
                   usecols=[1, 2])    # 1列目と2列目を使用
print('axis指定なしの場合')
print(arr_1.mean())
print('axis=0の場合')
print(arr_1.mean(axis=0))
print('axis=1の場合')
print(arr_1.mean(axis=1))
print('-----------------------------------------------------------------------------')

########4.1.4#########分散
arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv", encoding="utf-8",
                   delimiter=",",    # カンマ区切りであることを明示
                   skiprows=1,       # 最初の1行を無視
                   usecols=[1, 2])    # 1列目と2列目を使用
print('axis指定なしの場合')
print(arr_1.var())
print('axis=0の場合')
print(arr_1.var(axis=0))
print('axis=1の場合')
print(arr_1.var(axis=1))
print('-----------------------------------------------------------------------------')

########4.1.5######### MAX&MIN
arr_1 = np.loadtxt("./4002_new_numpy/csv_example.csv", encoding="utf-8",
                   delimiter=",",    # カンマ区切りであることを明示
                   skiprows=1,       # 最初の1行を無視
                   usecols=[1, 2])    # 1列目と2列目を使用
print('axis=0の場合の最大値')
print(arr_1.max(axis=0))
print('axis=0の場合の最小値')
print(arr_1.min(axis=0))
print('-----------------------------------------------------------------------------')

########4.1.5######### MAX&MIN index
arr_1 = np.loadtxt("./4002_new_numpy/weather_tokyo.csv", 
                   delimiter=",",    # カンマ区切りであることを明示
                   skiprows=3,       # 最初の1行を無視
                   usecols=[1, 2, 3, 4])    

max_temp_index = arr_1.argmax(axis=0)[0]

#気温が最高だった日の行数を出力
print(max_temp_index)

#気温が最高だった日の行全体を出力
print(arr_1[max_temp_index])