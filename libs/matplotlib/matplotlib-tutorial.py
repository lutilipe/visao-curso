import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color="red", marker="o")
plt.plot([1, 2, 3, 4], [5, 10, 13, 15], color="blue", marker="o")

plt.subplot(1, 2, 2)
plt.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
plt.title("Graph")
plt.xlabel("x label")
plt.ylabel("y label")
plt.grid(True)
plt.show()