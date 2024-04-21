import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b

print(c)


# Definindo a matriz A e o vetor B
A = np.array([[4, 2, 1], [2, 3, 5], [1, 5, 7]])
B = np.array([9, 8, 10])

x = np.linalg.solve(A, B)

print(x)

# Arrays

o = np.arange(12)
print(np.split(o, 3))
print(np.vstack(np.split(o, 3)))

# Array ops

array = np.arange(11)
escalar = 2
print(array + 2)

matriz = np.array([[1, 2, 3], [4,5,6]])
print("\n", matriz * np.arange(3))

# Bool
print(array[array < 3])
print(np.logical_and(array > 3, array < 5))