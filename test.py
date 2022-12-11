import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(9,6))
for i in range(6):
    if i != 5:
        fig.add_subplot(2, 3, i+1)

plt.show()