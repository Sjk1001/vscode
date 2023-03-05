#import random
import numpy as np
# 使う関数に合わせて、import文のコメントアウトを解除してください

# 関数random_selectを作ってください
def random_select():
    slot_num = np.random.randint(5)
    return slot_num


# 関数の呼び出し
slot_num = random_select()
print(slot_num)

x = np.random.binomial(1000, 0.5, 5)
print(x)

print("_________________________________________________________")
import random
import numpy as np

random.seed(0)
np.random.seed(0)

# 環境の定義
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 関数rewardを作ってください
def reward(record, results, slot_num, times):
    # environments関数を用いて結果を取得してください
    for time in range(times):
        
        result = environments(slot_num)
        
        # recordのtime番目の値をresultにしてください
        record[time] = result
        
        # resultsの各値を更新してください
        results[slot_num][1] += 1
        results[slot_num][2] += result
        results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
        
    return results, record

# 各変数の定義
times = 1000
results = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
record = np.zeros(times)
slot_num = 2
time = 1000

# 関数の呼び出し
results, record = reward(record, results, slot_num, time)
print(results)

print("________________________greedy__________________________")
import numpy as np

np.random.seed(0)


# greedyアルゴリズムを実装して下さい
def greedy(results, n):
    # 試行回数がnより少ない場合、slot_numはそのままにする
    # 以下のfor文内を埋めてください
    slot_num = None
    for i, d in enumerate(results):
        if d[1] < n:
            slot_num = i
            break
        
    # 試行回数がnより大きい場合、slot_numを報酬の期待値の高いものにする
    # 以下のif文内を埋めてください
    if slot_num == None:
        slot_num = np.array([row[3] for row in results]).argmax()
        
    return slot_num

# 環境を定義する関数です
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 報酬を定義する関数です
def reward(record, results, slot_num, time):
    result = environments(slot_num)
    record[time] = result
    results[slot_num][1] += 1
    results[slot_num][2] += result
    results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
    return results, record

# 初期変数を設定して下さい
times = 10000
results = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
record = np.zeros(times)
n = 100

for time in range(0, times):
    slot_num = greedy(results,n)
    results, record = reward(record, results, slot_num, time)
    
print(results)

print("_____________________ε-greedy__________________________")
import random
import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)

# ε-greedy手法を実装して下さい
def epsilon_greedy(results,epsilon):
    # まだ選択したことがないマシンがある場合、そのマシンを選択して下さい(手順1)
    for i, d in enumerate(results):
        if d[1] == 0:
            slot_num = i
            return slot_num
    
    # 確率εで全てのマシンの中からランダムに選択してください(手順2)
    if np.random.binomial(1, epsilon):
        slot_num = np.random.randint(0,4)
        
    # 確率1-εでn=0のgreedy手法をとってください(手順3)
    else:
        slot_num = np.array([row[3] for row in results]).argmax()
    return slot_num

# 環境を定義する関数です
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 報酬を定義する関数です
def reward(record, results, slot_num, time):
    result = environments(slot_num)
    record[time] = result
    results[slot_num][1] += 1
    results[slot_num][2] += result
    results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
    return results, record
# 初期変数を設定しています
times = 10000
record = np.zeros(times)
epsilons = [0.01, 0.1, 0.2]

for epsilon in epsilons:
    results = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
    for time in range(0, times):
        slot_num = epsilon_greedy(results, epsilon)
        results, record = reward(record, results, slot_num, time)

    #epsilon を変更させて収束の度合いをプロットしています
    plt.plot(np.cumsum(record) / np.arange(1, record.size + 1), label ="epsilon = %s" %str(epsilon))
    

#グラフの出力をしています        
plt.legend()
plt.xlabel("試行回数")
plt.ylabel("平均報酬")
plt.title("ε-greedyのεによる収束の違い")
plt.show()

print("_____________________楽観的初期値法__________________________")

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

# 楽観的初期値法を実装して下さい
def optimistic(results, K, rsup):
    # スロットごとの報酬の期待値を計算して、配列に格納してください
    optimistic_mean = np.array([(row[2] + K*rsup) / (row[1] + K) for row in results])
    # 最も報酬の期待値が大きいスロットを選択してください
    slot_num = np.array(optimistic_mean).argmax()
    return slot_num

# (参考)１つ前のchapterで実装したepsilon_greedy法です
def epsilon_greedy(results,epsilon):
    if np.random.binomial(1, epsilon):
        slot_num = random.randint(0, 4)
    else:
        slot_num = None
        for i, d in enumerate(results):
            if d[1] == 0:
                slot_num = i
                break
        if slot_num == None:
            slot_num = np.array([row[3] for row in results]).argmax()     
    return slot_num

# 環境を定義する関数です
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 報酬を定義する関数です
def reward(record, results, slot_num, time):
    result = environments(slot_num)
    record[time] = result
    results[slot_num][1] += 1
    results[slot_num][2] += result
    results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
    return results, record

# 初期変数を設定しています
times = 10000
record = np.zeros(times)
Ks = range(1,6)

# Kを変更させて収束の度合いをプロットしています
for K in Ks:
    results = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
    for time in range(times):
        slot_num = optimistic(results, K, 1)
        results, record = reward(record, results, slot_num, time)
    plt.plot(np.cumsum(record) / np.arange(1, record.size + 1), label ="K = %d" % K)
plt.legend()
plt.xlabel("試行回数")
plt.ylabel("平均報酬")
plt.title("楽観的初期値法のKの変動による結果の差異")
plt.show()


print("____________________soft-max__________________________")
import numpy as np
# 回答確認用です。変えないでください
np.random.seed(55)

tau = 0.1

# soft-max法を実装して下さい
def softmax(results, tau):
    # 各マシンの予想期待値を配列にしてください
    q = np.array([row[3] for row in results])
    
    # 今までのデータがない場合、全ての行動の報酬を1で仮定してください
    if np.sum(q) == 0:
        q = np.ones(len(results))
        
    # 各マシンの選択確率を設定してください
    probability = np.exp(q/ tau) / sum (np.exp(q / tau))
    
    # 確率分布に基づいて、slot_numを決定してください
    slot_num = np.random.choice([row[0] for row in results], p=probability)
    
    return slot_num



# 環境を定義する関数です
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 報酬を定義する関数です
def reward(record, results, slot_num, time):
    result = environments(slot_num)
    record[time] = result
    results[slot_num][1] += 1
    results[slot_num][2] += result
    results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
    return results, record

print("___________________UCB1_________________________")

import numpy as np
import math
np.random.seed(0)

R = 1

#　UCB1法を実装して下さい
def UCB(results, R):
    slot_num = None
    # まだ選んだことのないマシンがあればそれをslot_numにしてください
    for i, d in enumerate(results):
        if d[1] == 0:
            slot_num = i
            break
        
    # 全て一度は選んでいる場合
    if slot_num == None:
        
        # これまでの総試行回数を計算してください
        times = sum([row[1] for row in results])
        
        # マシンごとに今までの結果から得られた成功率uiを取り出してリストに格納してください
        ui = [row[3] for row in results]
        
        # マシンごとの偶然による成功率のばらつきの大きさxi を計算してリストに格納してください
        xi = [R*math.sqrt(2*math.log(times) / row[1]) for row in results]
        
        # ui+xiを計算してリストに格納してください
        uixi = [x + u for x, u in zip(xi, ui)]
        
        # uixiが最大値となるマシンをslot_numにしてください
        slot_num = uixi.index(max(uixi))
        
    return slot_num

# 環境を定義する関数です
def environments(band_number):
    coins_p = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
    results = np.random.binomial(1, coins_p)
    result = results[band_number]
    return result

# 報酬を定義する関数です
def reward(record, results, slot_num, time):
    result = environments(slot_num)
    record[time] = result
    results[slot_num][1] += 1
    results[slot_num][2] += result
    results[slot_num][3] = results[slot_num][2] / results[slot_num][1]
    return results, record


results = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0]]
times = 1000
record = np.zeros(times)
for time in range(0, times):
    slot_num = UCB(results,R)
    results, record = reward(record, results, slot_num, time)
print(results)