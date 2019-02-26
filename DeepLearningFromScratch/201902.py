# class Man:
#     def __init__(self, name):
#         self.name = name
#         print("Initialized")
#
#     def sayHell(self):
#         print("Hello " + self.name)
#
#
# m = Man("test")
# m.sayHell()

# 201902
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x)
print(type(x))
print(x + y)
print(x - y)
print(x * y)
print(x / y)

a = np.array([[1, 2],[3, 4]])
print(a)
print(a.shape)
print(a.dtype)

b = np.array([[3, 0], [0, 6]])
print(a + b)
print(a * b)

