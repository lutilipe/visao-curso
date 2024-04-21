import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.rand(20)
y = np.random.rand(20)

x2 = np.random.rand(20)
y2 = np.random.rand(20)

plt.scatter(x, y, color="red")
plt.scatter(x2, y2, color="blue")

plt.show()