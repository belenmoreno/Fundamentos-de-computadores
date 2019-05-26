import numpy as numpy
a1 = np.array([[1, 1, 1], [2, 2, 2]])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1)
print(a2)
print(a1 + a2)
print(a1.dot(a2))
a3 = a1.T
print(a3)
print(a3.dot(a2))