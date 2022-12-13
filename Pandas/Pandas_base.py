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