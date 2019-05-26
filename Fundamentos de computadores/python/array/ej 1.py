import numpy as np

a1 = np.array([1, 2, 3])
print(a1)

a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
print(a3)

print(np.zeros((3,2)))
print(np.ones((3,4)))
print(np.full((3,3), "hola"))

print(np.identity(6))

print(np.arange(0, 10, 2))
print(np.linspace(0, 10, 5))
print(np.random.random((3,5)))

print(a2.ndim)
print(a2.shape)
print(a2.size)
print(a2.dtype)

print(a2)
print(a2[1, 0])
print(a2[1][0])

print(a1[0:2])
print(a2[0:2, 1:])

print(a2[(a2 % 2 == 0) & (a2 > 3)])

