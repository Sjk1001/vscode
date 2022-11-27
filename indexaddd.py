print('Hello world')

# 変数
num = 10
print(num)

# 変数の上書き
num = 10
num = 30

# 変数の代入
num = 10
copy_num  = num
print(copy_num)

# 変数の計算
num1 = 10
num2 = 5
result = num1 + num2

#同じ変数に対して計算を行う
# [num = num + 1]
num /=5

# 整数を代入する場合
num = 10
print(type(num))
# 小数を代入する場合
num = 33.14
print(type(num))

#single quatation ''
#double quatation ""
text = 'apple'
print(text)
print(type(text))

# 文字列の連携
text = 'Hello' + ',' +'Aidemyy'
print(text)

# 変数に文字入れ
text2 = 'Python'
text = 'Hello' + ', ' + text2
print(text)

# 文字繰り返す
text = 'Hello' * 4
print(text)
text = 'Hello'
text += ',World'
print(text)
text1 = '1111'
text2 = '2222'
print(text1+text2)

# bool Type
data1 = True
print(data1)
print(type(data1))
data2 = False
print(data2)
print(type(data2))

#The type of number(str int float)
num = 5
num = str(num)
text = 'りんごは' + num + 'こあります。'
print(text)

num = 6
text = 'りんごは' + str(num) + 'こあります。'
print(text)

num = '1111'
int_num  = int(num)
float_num = float(num)
print(int_num)
print(float_num)
print(type(int_num))
print(type(float_num))

apple = '100'
num = 4 
apple = int(apple)
text = 'あなたの合計金額は' + str(apple * num) + '円です'
print(text)

#持っているリンゴの数
apple = 12
# [apple >= 12]は条件を表し、apple変数は２以上なので、True
print(apple >= 2 )

# if and else
apple = 10
if apple >= 2 #食べるのでリンゴのかずをへらす。
    apple -= 1 
    print('リンゴを食べました！のこりのかずは' + str(apple) + 'こです。')
else :
    apple += 1 #買うのでリンゴの数を増やす
    print('リンゴを買いました！残りの数は' + str(apple)　