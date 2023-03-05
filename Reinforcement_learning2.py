import numpy as np

state_transition = np.array(
    # ここに答えを入力してください
    # 要素は[s,s',a,p(s'|a,s),r(s,a,s')]
    [[0, 0, 0, 0.3, 5],
     [0, 1, 0, 0.7, -10],
     [0, 0, 1, 1, 5],
     [1, 0, 1, 1, 5],
     [1, 2, 0, 0.8, 100],
     [1, 1, 0, 0.2, -10]]
)

print(*sorted(state_transition, key = lambda x: (x[0],x[1],x[2])), sep='\n')