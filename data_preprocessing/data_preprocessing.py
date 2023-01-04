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