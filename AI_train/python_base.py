#List
list_1 = [0,1,2]
list_2 = ['象' 'キリン' 'パタン']

print(list_1)
print(list_2)

#different type of cell in the list
data = ['リンゴ', 3, 'ゴリラ']

print(data)

n = 3
data = ['リンゴ', n, 'ゴリラ']
print(data)

#List in list
data = [[1, 2], [3, 4], [5, 6]]
print(data)

data = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(data)

 #Catch data from list
ListSample = [1, 2, 3, 4]
print(ListSample[1])

list_num = ["one", "two", "three"]
print("２は英語で" + list_num[1] + "です")

# 後ろから数う
ListSample = [1, 2, 3, 4]
print(ListSample[-2])

#LIST区間
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(alphabet[1:5])
print(alphabet[:5])
print(alphabet[0:20])
print(alphabet[1:-5])

# LIST内要素置換
alphabet = ["a", "b", "c", "d", "e"]
alphabet[0] = "A"
print(alphabet)

alphabet[1:4] = ["B", "C", "D"]
print(alphabet)

#LIST内要素追加
alphabet = ["a", "b", "c", "d", "e"]
alphabet.append("f")
print(alphabet)

#LIST+LIST
alphabet = ["a", "b", "c", "d", "e"]
add_list = ["e", "f", "g"]
alphabet_new = alphabet + add_list
print(alphabet_new)

alphabet = ["a", "b", "c", "d", "e"]
alphabet.extend(["f", "g", "h"])
print(alphabet)

#del by LIST
alphabet = ["a", "b", "c", "d", "e"]
del alphabet[3:]
print(alphabet)

alphabet = ["a", "b", "c", "d", "e"]
del alphabet[1:3]
print(alphabet) #['a', 'd', 'e']

#copy_list
alphabet = ["a", "b", "c"]
alphabet_copy = alphabet
alphabet_copy[0] = "A"

print(alphabet_copy)
print(alphabet) #The only different bettewn alphabet_copy and alphabet is name.要素共有
################
alphabet = ["a", "b", "c"]
alphabet_copy = list(alphabet)
alphabet_copy[0] = "A"

print(alphabet_copy)
print(alphabet)

#Dictionary
dic ={"Japan": "Tokyo", "Korea": "Seoul"}
print(dic)

dic ={"Japan": "Tokyo", "Korea": "Seoul"}
print(dic["Japan"])
print("東京はローマ字で" + dic["Japan"] + "です。")

#change the data of dic
dic ={"Japan": "Tokyo", "Korea": "Seoul"}
dic["Japan"] = "Osaka"
print(dic)

#ADD TO dic
dic ={"Japan": "Tokyo", "Korea": "Seoul"}
dic["China"] = "Beijing"
print(dic)

#del the data of dic
dic ={"Japan": "Tokyo", "Korea": "Seoul", "China": "Beijing"}
del dic["China"]
print(dic)

#for
numbers = [1, 2, 0, 8]
for num in  numbers :
    print(num)

fruits = {"strawberry": "red", "peach": "pink", "banana":"yellow"}
for key in fruits :
    print(key)

fruits = {"strawberry": "red", "peach": "pink", "banana":"yellow"}
for key in fruits :
    print(key +  " " + fruits[key])

#for the break
storages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in storages :
    print(n)
    if n >= 5 :
        print("nが5以上になりましたので処理をしゅうりょうしました。")
        break

#range
for i in range(3) :
    print(i)

#(start, stop(end+1), (step))
for i in range(3, 13, 4) :
    print(i)

#for list in list
list_ = [[1, 2, 3], [4, 5, 6]]
for data in list_ :
    print(data)

list_ = [[1, 2, 3], [4, 5, 6]]
for a, b, c in list_ :
    print(a, b, c)

# 中のリストの数が全て同じではない
# ×list_ = [[1, 2, 3], [4, 5]]
# ×for a, b, c in list_:
# ×    print(a, b, c)

# ×>>> 出力結果
# ×not enough values to unpack (expected 3, got 2)

#関数
str_val = str(123)
print(type(str_val))

#独自関数
def sing():
    print ("歌います！")

sing()

#変数
def song_sing(song) :
    text = song + "を歌います！"
    print(text)

song_sing( "歌")

volume = "大声で"
song_sing(volume)

volume = "小声で"
song_sing(volume)

def song_sing(song) :
    text = str(song) + "をうたいます。"
    print(text)

song_sing(12)

def introduce(first, family) :
    print("名前は" + family + "で、名前は" + first + "です。")
introduce("taro",  "yamada")

#引数の初期値
def introduce(family="Yamada", first="Taro") :
    print("名字は" + family + "で、名前は" + first + "です。")

introduce("Suzuki")

#戻り値（return）
def pow_sum(x) :
    result = x**2 + x**3
    return result
data = pow_sum(10)
print(data)

#enumerate
list_ = ["a", "b"]
for index, value in enumerate(list_) :
    print(index, value)

a = 2**0
print(a)


#class
class Human :
    def __init__(self,name,age) :
        self.name = name
        self.age = age 
    def age_check(self) :
        if self.age >=18 :
            return "成年です"
        else :
            return "未成年です"
        
#関数のインポート
import scipy.linalg.basic

print(scipy.linalg.basic.solve(2,6))
