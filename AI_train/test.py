import pulp

#問題の生成
prob = pulp.LpProblem("ex1", pulp.LpMinimize)

#変数の生成
x1=pulp.LpVariable("x1",lowBound=0, cat=pulp.LpContinuous)
x2=pulp.LpVariable("X2",lowBound=0, cat=pulp.LpContinuous)

#目的関数の生成
prob += -3*x1-2*x2

print(prob)

#制約式の追加
prob += -x1 + 3*x2 <= 12
prob += x1+x2 <= 8
prob += 2*x1 -x2 <= 10

print(prob)

#求解
status = prob.solve();
print("终了状态：",pulp.LpStatus[status])
print("最適値：",pulp.value(prob.objective))
print("最適解: (x1,x2)=(",x1.varValue,x2.varValue,")")

