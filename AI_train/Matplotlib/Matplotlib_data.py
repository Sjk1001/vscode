#1.2.3 二項分布に従う乱数を生成する
print('----------------1.2.3 二項分布に従う乱数を生成する---------------')
import numpy
#0.5の確率で成功する試行を100回行なったときの成功数を10,000回分求め
binomial_data = numpy.random.binomial(100, 0.5, 10000)
print(binomial_data)

# 成功率の平均を出力します
print(binomial_data.mean()/100)



#1.2.4 リストからランダムに選択する
print('----------------1.2.4 リストからランダムに選択する---------------')
import numpy as np

list = ['Python', 'PHP', 'Ruby', 'Node,js']

#seedを設定
np.random.seed(0)
# リストlistの中からランダムに2個選ぶ
selected_language = np.random.choice(list, 2)

print(selected_language)



#1.3.1 datetime型  省略した場合は 0 になります。
print('------------------------1.3.1 datetime型-----------------------')
import datetime

dt = datetime.datetime(2022, 12, 11, hour=10, second=30, microsecond=200)
print(dt)



#1.3.2 timedelta型
print('------------------------1.3.2 timedelta型------------------------')
import datetime

td = datetime.timedelta(days=1, seconds=2, microseconds=3, 
                        milliseconds=4, minutes=5, hours=6, weeks=7)
print(td)

# -1日(days=-1)-10時間(hours=-10)
# =-1日-10時間
# =-1日+(-1日+1日)-10時間
# =-1日+(-1日+２４時間)-10時間
# =-1日-1日+24時間-10時間
# =-2日+14時間
td = datetime.timedelta(days=-1, hours=-10)
print(td)



#1.3.3 datetime型とtimedelta型の演算
print('----------------1.3.3 datetime型とtimedelta型の演算---------------')
import datetime

d1 = datetime.datetime.now()
d2 = datetime.datetime(2022,12,10,23,57,0)
td = d2 - d1
print(td)
print(type(td))



#1.3.4 時を表す[文字列]からdatetimeオブジェクトを作成する
print('-------1.3.4 時を表す[文字列]からdatetimeオブジェクトを作成する--------')
import datetime

s = "2017-12-20 10:00:00"
str_dt = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(str_dt)
print(type(str_dt))



#1.4.2 等間隔の数列を生成する1
print('------------------1.4.2 等間隔の数列を生成する1-------------------')
import numpy as np

x =np.arange(0, 5, 2)
print(x)



#1.4.3 等間隔の数列を生成する2
print('-----------------1.4.3 等間隔の数列を生成する2------------------')
import numpy as np

x = np.linspace(0, 15, 4)
print(x)
print('-------------------')
x = np.linspace(0, 15)  #また分割したい個数の値が指定されない場合は50点生成
print(x)




#2.2.1 1つのグラフに複数のデータをプロットする
print('-----------2.2.1 1つのグラフに複数のデータをプロットする-----------')

# matplotlib.pyplot.plot(x, y, color="色指定")
# "b" : 青
# "g" : 緑
# "r" : 赤
# "c" : シアン
# "m" : マゼンタ
# "y" : 黄色
# "k" : 黒
# "w" : 白

#3.1.1 マーカーの種類と色を設定する
print('-----------3.1.1 マーカーの種類と色を設定する-----------')
# matplotlib.pyplot.plot(x, y, marker="マーカーの種類", markerfacecolor="マーカーの色")
# 以下は指定できるマーカーの種類とその色の一部です。


# マーカー
# "o": 円
# "s": 四角
# "p": 五角形
# "*": 星
# "+": プラス
# "D": ダイアモンド
# 色
# "b" : 青
# "g" : 緑
# "r" : 赤
# "c" : シアン
# "m" : マゼンタ
# "y" : 黄色
# "k" : 黒
# "w" : 白