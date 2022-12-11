#测试文件性质
#<_io.TextIOWrapper name='./4002_new_numpy/csv_example.csv' mode='r' encoding='utf-8'>
import numpy as np

f = open("./4002_new_numpy/csv_example.csv", encoding='utf-8')

print(f.read())
print(f)

import numpy as np

w= open("./4002_new_numpy/weather_tokyo.csv")

print(w.read())
print(w)
