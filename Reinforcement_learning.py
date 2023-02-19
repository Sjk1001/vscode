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