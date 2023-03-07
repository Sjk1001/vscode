#1.1.2 SeriesとDataFrameのデータの確認
print('-------------1.1.2 SeriesとDataFrameのデータの確認-------------')
import pandas as pd

# Seriesを作成
fruits = {"banana": 3, "orange": 2}
print(pd.Series(fruits))

# 辞書型を用いてDataFrame用のデータの作成
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
#ソート順を指定する場合は以下のように第二引数にcolumns=[リスト] を指定します。
import pandas as pd
df = pd.DataFrame(data, columns=["year", "time", "fruits"])
print(df)



#1.2.1 Seriesを生成する
# pd.Series(データ配列, index=インデックス配列)の形式で指定し、
# またpd.Series(データ配列, インデックス配列) のように、 index=を省略した記述も可能です。

# インデックスを指定しない場合は0から昇順に整数がインデックスとして自動で付きます。
print('---------------------1.2.1 Seriesを生成する---------------------')
import pandas as pd

fruit = {"banana": 3, "orange": 2}
print(pd.Series(fruit))
print('------------------------------------------')
# Pandasをpdとしてimport
import pandas as pd

index1 = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]

# dataとindexを含むSeriesを生成しseriesに代入してください
series = pd.Series(data, index1)

print(series)


#1.2.2 参照
print('---------------------------1.2.2 参照---------------------------')
import pandas as pd
fruits = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
series = pd.Series(fruits)
print(series)
print('----範囲----')
print(series[0:2])
print('----特定----')
print(series[["grape", "peach"]])
print(series[["orange"]])
print('----データのみ----')
print(series["orange"])
print('----インデックス番号----')
print(series[3])


#1.2.3 データ、インデックスを取り出す
print('----------------1.2.3 データ、インデックスを取り出す---------------')
import pandas as pd

index = ["soccer", "tennis", "basketball"]
data = [11, 4, 10]
series = pd.Series(data, index=index)
print(series.values)
print(series.index)


#1.2.4 要素を追加する
print('-----------------------1.2.4 要素を追加する----------------------')
import pandas as pd

fruit = {"banana": 3, "orange": 2}
series = pd.Series(fruit)
print(series)

grape = {"grape": 3}
series = series.append(pd.Series(grape))
print(series)

series = series.append(pd.Series([5], index=["peach"]))
print(series)


#1.2.5 要素を削除する
print('-----------------------1.2.5 要素を削除する----------------------')
import pandas as pd
fruits ={"banana": 3, "orange": 2}
series = pd.Series(fruits)
series = series.drop("banana")

print(series)


#1.2.6 フィルタリング
print('-----------------------1.2.6 フィルタリング----------------------')
import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)

conditions = [True, True, False, True, False]
print(series[conditions])
print(series[series >= 5])

# seriesの要素のうち、dataの値が5以上10未満の要素を含むSeriesを作り、seriesに再代入してください
series = series[series >= 5 ][series < 10]
print(series)


#1.2.7 ソート
print('--------------------------1.2.7 ソート-------------------------')
print('----昇順にソート----')
import pandas as pd

index = ["apple", "orange","banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)

items1 = series.sort_index()
print(items1)
print('----降順にソート----')
items2 = series.sort_values(ascending=False)
print(items2)


#1.3.1 DataFrameの生成
print('---------------------1.3.1 DataFrameの生成---------------------')
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
print('---------------------------------')
import pandas as pd
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)

print(series1)
print()
print(series2)
df = pd.DataFrame([series1, series2])
print(df)


#1.3.2 インデックスとカラムを設定する
print('----------------1.3.2 インデックスとカラムを設定する--------------')
import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
df = pd.DataFrame([series1, series2])

# dfのインデックスが1から始まるように設定してください
df.index = [1, 2]

print(df)


#1.3.3 行を追加する
print('------------------------1.3.3 行を追加する-----------------------')
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
series = pd.Series(["mango",200, 7, "12/1"],
                    index=["fruits", "year", "time", "data"])

df = df.append(series, ignore_index=True) #ignore_index=Trueを指定しないとエラーになります
print(df)

# name属性を持たないSeries
print('-------name属性を持たないSeries---------')
series = pd.Series(["mango", 2008, 7, "12/1"], index=["fruits", "year", "time", "date"])
print(series)
print('-------name属性を持つSeries---------')
series = pd.Series(["mango", 2008, 7, "12/1"], index=["fruits", "year", "time", "date"])
series.name = "test"
print(series)


#1.3.4 列を追加する
print('------------------------1.3.4 列を追加する-----------------------')
data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
df["price"] = [150, 120, 100, 300, 150]
print(df)


#1.3.6 名前による参照
print('-----------------------1.3.6 名前による参照----------------------')
data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
#インデックスのリスト[1, 2]とカラムのリスト["time","year"]を指定
df = df.loc[[1,2], ["time", "year"]]
print(df)


#1.3.7 番号による参照
print('-----------------------1.3.7 番号による参照----------------------')
data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
df =df.iloc[[1, 2], [0, 2]]
print(df)


#1.3.8 行または列の削除
print('----------------------1.3.8 行または列の削除----------------------')
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "time": [1, 4, 5, 6, 3],
        "year": [2001, 2002, 2001, 2008, 2006]}
df = pd.DataFrame(data)

# drop()を用いてdfの0,1行目を削除
df_1 = df.drop(range(0, 2))

# drop()を用いてdfの列"year"を削除
df_2 = df.drop("year", axis=1) #列を削除する場合は第2引数にaxis=1を指定

print(df_1)
print()
print(df_2)


#1.3.9 ソート
print('---------------------------1.3.9 ソート--------------------------')
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "time": [1, 4, 5, 6, 3],
        "year": [2001, 2002, 2001, 2008, 2006]}
df = pd.DataFrame(data)
print(df)
print('-----データを昇順にソートする(引数にカラムを指定)-----')
df = df.sort_values(by="year", ascending = True)
print(df)
df = df.sort_values(by=["time", "year"],
                        ascending= True)
print(df)


#1.3.10 フィルタリング
print('-----------------------1.3.10 フィルタリング----------------------')
import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}
df = pd.DataFrame(data)
print(df)
print(df.index % 2 == 0)
print()
print(df.loc[df.index % 2 == 0])


#2.2.1 インデックス、カラムが一致しているDataFrame同士の連結
print('----2.2.1 インデックス、カラムが一致しているDataFrame同士の連結----')
import numpy as np
import pandas as pd

# 指定のインデックスとカラムを持つDataFrameを乱数によって作成する関数
def make_random_df(index, columns, seed):
    # 乱数の値を固定
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df

#インデックス、カラムが一致しているDataFrameの作成
columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

# df_data1とdf_data2を縦方向に連結しdf1に代入してください
df1 = pd.concat([df_data1, df_data2], axis=0)

# df_data1とdf_data2を横方向に連結しdf2に代入してください
df2 = pd.concat([df_data1, df_data2], axis=1)

print(df1)
print()


#2.2.2 インデックス、カラムが一致していないDataFrame同士の連結
print('----2.2.2 インデックス、カラムが一致していないDataFrame同士の連結----')
import numpy as np
import pandas as pd
# 指定のインデックスとカラムを持つDataFrameを乱数によって作成する関数
def make_random_df(index, columns, seed):
   np.random.seed(seed)
   df = pd.DataFrame()
   for column in columns:
       df[column] = np.random.choice(range(1, 101), len(index))
   df.index = index
   return df
columns1 = ["apple", "orange", "banana"]
columns2 = ["orange", "kiwifruit", "banana"]
# インデックスが1,2,3,4、カラムがcolumns1のDataFrameを作成
df_data1 = make_random_df(range(1, 5), columns1, 0)
df_data2 = make_random_df(range(1, 5), columns2, 1)
# df_data1とdf_data2を縦方向に連結しdf1に代入
df1 = pd.concat([df_data1, df_data2], axis=0)
print(df1)


#2.2.3 連結する際のラベルの指定
print('------------------2.2.3 連結する際のラベルの指定-------------------')
import numpy as np
import pandas as pd

# 指定のインデックスとカラムを持つDataFrameを乱数によって作成する関数
def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df

columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

# df_data1とdf_data2を横方向に連結し、keysに"X", "Y"を指定してMultiIndexにしてdfに代入してください
df = pd.concat([df_data1, df_data2], axis=1, keys= ["X", "Y"])

# dfの"Y"ラベルの"banana"をY_bananaに代入してください。
Y_banana = df["Y","banana"]

print(df)
print()
print(Y_banana)


#2.3.2 内部外部結合の基本--inner--outer
print('----------------------2.3.2 内部外部結合の基本---------------------')
import pandas as pd

data1 = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "amount": [1, 4, 5, 6, 3]}
df1 = pd.DataFrame(data1)

data2 = {"fruits": ["apple", "orange", "banana", "strawberry", "mango"],
        "year": [2001, 2002, 2001, 2008, 2007],
        "price": [150, 120, 100, 250, 3000]}
df2 = pd.DataFrame(data2)

# df1, df2のデータを確認してください
print(df1)
print()
print(df2)
print()

# df1とdf2を"fruits"をKeyに内部結合して作成したDataFrameをdf3に代入してください
df3 = pd.merge(df1, df2, on= "fruits", how="inner")

# 内部結合を行った時の挙動を確認しましょう
print(df3)


#2.3.4 同名でない列をKeyにして結合する
print('---------------2.3.4 同名でない列をKeyにして結合する----------------')
import pandas as pd

# 注文情報
order_df = pd.DataFrame([[1000, 2546, 103],
                         [1001, 4352, 101],
                         [1002, 342, 101],
                         [1003, 1192, 102]],
                         columns=["id", "item_id", "customer_id"])
# 顧客情報
customer_df = pd.DataFrame([[101, "Tanaka"],
                           [102, "Suzuki"],
                           [103, "Kato"]],
                           columns=["id", "name"])

# order_dfとcustomer_dfを顧客IDをkeyに結合してorder_dfに代入してください
order_df = pd.merge(order_df, customer_df, 
                        left_on= "customer_id", right_on="id", how="inner" )

print(order_df)


#2.3.5 インデックスをKeyにして結合する
print('---------------2.3.5 インデックスをKeyにして結合する----------------')
import pandas as pd

# 注文情報
order_df = pd.DataFrame([[1000, 2546, 103],
                         [1001, 4352, 101],
                         [1002, 342, 101],
                         [1003, 1192, 102]],
                         columns=["id", "item_id", "customer_id"])
# 顧客情報
customer_df = pd.DataFrame([["Tanaka"],
                           ["Suzuki"],
                           ["Kato"]],
                           columns=["name"])
customer_df.index = [101, 102, 103]

# order_dfとcustomer_dfを顧客IDをkeyに結合してorder_dfに代入してください
order_df = pd.merge(order_df, customer_df, left_on="customer_id", right_index= True, how= "inner")

print(order_df)


#2.4.1 一部の行を得る
print('------------------------2.4.1 一部の行を得る------------------------')
import numpy as np
import pandas as pd

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)

# dfの冒頭3行を取得し、df_headに代入してください
df_head = df.head(3)

# dfの末尾3行を取得し、df_tailに代入してください
df_tail = df.tail(3)

print(df_head)
print()
print(df_tail)


#2.4.2 計算処理を適用する
print('----------------------2.4.2 計算処理を適用する----------------------')
import pandas as pd
import numpy as np

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)
print(df)
# dfの各要素に+2、ブロードキャストによりPandasと整数の計算ができます
add_df = df+2
print(add_df)

import numpy as np
import pandas as pd

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)

# dfの各要素を2倍し、double_dfに代入してください
double_df = df * 2

# dfの各要素を2乗し、square_dfに代入してください
square_df = df ** 2

# dfの各要素の平方根を計算し、sqrt_dfに代入してください
sqrt_df = np.sqrt(df)

print(double_df)
print()
print(square_df)
print()
print(sqrt_df)


#2.4.3 要約統計量を得る
print('----------------------2.4.3 要約統計量を得る-----------------------')
import numpy as np
import pandas as pd

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、それぞれのcolumnに対応する値（要素）を10個追加する列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)

# dfの要約統計量のうち、"mean", "max", "min"を取り出してdf_desに代入してください
df_des = df.describe().loc[["mean", "max", "min"]]

print(df_des)


#2.4.4 DataFrameの行間または列間の差を求める
print('-------------2.4.4 DataFrameの行間または列間の差を求める------------')
import numpy as np
import pandas as pd

np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

# DataFrameを生成し、列を追加
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)

# dfの各行について、2行後の行との差を計算したDataFrameをdf_diffに代入してください
df_diff = df.diff(periods=-2, axis=0)

# dfとdf_diffのデータを比較して処理内容を確認してください
print(df)
print()
print(df_diff)


#2.4.5 グループ化
print('-------------------------2.4.5 グループ化--------------------------')
import pandas as pd

# 一部の都道府県に関するDataFrameを作成
prefecture_df = pd.DataFrame([["Tokyo", 2190, 13636, "Kanto"], ["Kanagawa", 2415, 9145, "Kanto"],
                              ["Osaka", 1904, 8837, "Kinki"], ["Kyoto", 4610, 2605, "Kinki"],
                              ["Aichi", 5172, 7505, "Chubu"]], 
                             columns=["Prefecture", "Area", "Population", "Region"])

# prefecture_dfを地域(Region)についてグループ化し、grouped_regionに代入してください
grouped_region = prefecture_df.groupby("Region")

# grouped_regionに出てきた地域ごとの、面積(Area)と人口(Population)の平均をmean_dfに代入してください
mean_df = grouped_region.mean()

print(prefecture_df)
print()
print(mean_df)