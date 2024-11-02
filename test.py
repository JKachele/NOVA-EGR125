import numpy as np
import math

P0 = 4.0e6 # Starting population of 4 million
a = np.arange(0, 100, 10, dtype = float)
b = np.vstack([a, a, a, a, a])

def add(a, b):
    return a + b

def calcPop(a, r, k):
    exp = math.exp(r * a)
    num = k * P0 * exp
    den = k + P0 * (exp - 1)
    return num / den

for i in range(np.shape(b)[0]):
    res = calcPop(b[i], 2, 2)
    b[i] = res
    # print(b[i])

print(b)
