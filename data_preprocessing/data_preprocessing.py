# 例: x^2を出力する関数 pow1(x)
def pow1(x):
    return x ** 2

pow2 = lambda x: x ** 2


# lambda式でた辺スの関数を作成する
# 例: ２つの引数を足し合わせる関数 add1
add1 = lambda x, y: x + y
print((lambda x,y: x+ y)(3,5))

# 1.1.3 ifを用いたlambda
# 引数xが3未満ならば2を掛け、3以上ならば3で割って5を足す関数
def lower_three1(x):
    if x < 3:
        return x * 2
    else:
        return x / 3 + 5

tower_three2 = lambda x :x * 2 if x < 3 else x/3 +5

#1.2.1 listの分割（split）
# 分割したい文字列
test_sentence = "this is a test sentence."
#List the sentence by 'split'
print(  test_sentence.split(" ")  )

test_sentence = "this/is/a/test/sentence."
print(  test_sentence.split("/" , 3 ))   #分割回数

#1.2.2 listの分割（re.split）
import re
test_sentence = "this,is a.test,sentence"
print(  re.split("[, .]", test_sentence)  )

#1.2.3 高階関数（map）
a = [1, -2, 3, -4, 5]
new = []
for x in a :
    new.append(abs(x))
print(new)

print(list(map(abs, a)))

#习题
import re
# 配列time_list
time_list = [
    "2006/11/26_2:40",
    "2009/1/16_23:35",
    "2014/5/4_14:26",
    "2017/8/9_7:5",
    "2017/4/1_22:15"
]
# 文字列から"時"を取り出す関数を作成して下さい
get_hour = lambda x: int(re.split("[/_:]", x)[3]) # int()でstring型をint型に変換する

# 上で作った関数を用いて各要素の"時"を取り出し、配列にして下さい
hour_list = list(map(get_hour, time_list))

# 配列を出力して下さい
print(hour_list)



#1.2.4 filter
a = [1, -2, 3, -4, 5]
new = []
for x in a :
    if x > 0 :
        new.append(x)
print(new)

print(list(filter(lambda x: x>0 , a)))


#1.2.5 sorted
print("#####################1.2.5 sorted")
nest_list = [
    [0, 9],
    [1, 8],
    [2, 7],
    [3, 6],
    [4, 5],
]
#第二要素をKEYとしてSORT
print(sorted(nest_list,key=lambda x: x[1]))


#1.3.1 リストの生成 List comprehension
a = [1, -2, 3, -4, 5]
print(  [abs(x) for x in a]  )



#分和时的换算
a = 155
hour = lambda x: [(x//60),(x%60)]
print(hour(a))
print(type(hour(a)))

#1.3.2 if文を用いたループ  if后置
a = [1, -2, 3, -4, 5]
print(  [x for x in a if x > 0]  )

#1.3.3 複数配列の同時ループ
a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]
for x,y in zip(a, b):
    print(x, y)

print([x**2 + y**2 for x,y in zip(a, b)])


#########习题
# 時間データhour, 分データminute
hour = [0, 2, 3, 1, 0, 1, 1]
minute = [30, 35, 0, 14, 11, 0, 22]

# 時, 分を引数に、分に換算する関数を作成して下さい
hour_to_minute = lambda x, y: x*60 + y

# リスト内包表記を用いて所定の配列を作成してください
minute_list = [hour_to_minute(x,y) for x,y in zip(hour,minute)]

# 出力して下さい
print(minute_list)

print("###########1.3.4 多重ループ##########")
a = [1, -2, 3]
b = [9, 8]
for x in a:
    for y in b:
        print(x, y)
print([[x,y] for x in a for y in b])

print("---习题---")
# 二進数の桁
fours_place = [0, 2]
twos_place  = [0, 1]
ones_place  = [0, 1]

# リスト内包表記の多重ループを用いて、二進数を変換して、0から7までの整数を計算し、配列にして下さい
digit = [x*4 + y*2 + z for x in fours_place for y in twos_place for z in ones_place]

# 出力して下さい
print(digit)

print("###########1.4.1 defaultdict##########")
#辞書ｄにリストlstの各要素の出現回数を記録
d = {}
lst = ["foo", "bar", "pop", "foo", "popo"]
for key in lst :
    #ｄにKEY(要素)がすでに登録されているかいないかで処理を分ける
    if key in d:
        #ｄにKEY要素が登録されている場合要素の個数を加算する
        d[key] += 1
    else:
        #ｄにKEY要素が登録されていない場合要素の個数の初期化が必要
        d[key] = 1
print(d)

from collections import defaultdict
d = defaultdict(int)
lst = ["foo", "bar", "pop", "pop", "foo", "popo"]
for key in lst:
    d[key] += 1
    #  else: d[key] = 1 を書く必要ない
print(d)

print("---习题---")
from collections import defaultdict

# 文字列 description
description = \
"Artificial intelligence (AI, also machine intelligence, MI) is " + \
"intelligence exhibited by machines, rather than " + \
"humans or other animals (natural intelligence, NI)."
print(description)
# defaultdict を定義して下さい
char_freq = defaultdict(int)
print(char_freq)
# 文字の出現回数を記録して下さい
for i in description: 
    char_freq[i] += 1
    
# value の降順にソートし、上位10要素を出力して下さい
print(sorted(char_freq.items(), key= lambda x: x[1], reverse=True)[:10])



print("###########1.4.2 value内の要素の追加##########")
# 辞書にvalueの要素を追加
d ={}
price = [
    ("apple", 50),
    ("banana", 120),
    ("grape", 500),
    ("apple", 70),
    ("lemon", 150),
    ("grape", 1000)
]
for key, value in price:
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
print(d)


from collections import defaultdict

price = [
    ("apple", 50),
    ("banana", 120),
    ("grape", 500),
    ("apple", 70),
    ("lemon", 150),
    ("grape", 1000)
]
# defaultdict を定義
d = defaultdict(list)

# value の要素に値段を追加(条件分岐が不要)
for key, value in price:
        d[key].append(value)

print(d.items())
print(d.values())



print("###########1.4.3 Counter##########")
from collections import Counter

lst = ["foo", "bar", "pop", "pop", "foo", "popo"]
d = Counter(lst)
print(d)

d = Counter("A Counter is a dict subclass for counting hashable objects.")
#最も多い５要素を並べる
print(d.most_common(5))