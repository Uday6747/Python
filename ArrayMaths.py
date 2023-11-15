import numpy as np
n, m = map(int, input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))

