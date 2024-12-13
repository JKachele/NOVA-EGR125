# Justin Kachele
# NOVA Fall 2024
# EGR 125 Project 2

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


# Part 1: Filling a horizontal cylindrical tank
def f1(x, height):
    return (math.acos(1 - x) -((1 - x) * math.sqrt((2 * x) - (x ** 2)))) * (8 / math.pi) - height


# Find roots for Volumes of 1 - 7 cupic meters
for i in range(1, 8):
    height = opt.newton(f1, 1, None, (i,))
    print("Height for V =", i, "m3 is", height)


# Part 2: Electric circuit analysis
def f2(x):
    # Subtract 3.5 at end to move the points where it equals 3.5 \
    # to zero so we can use root finding.
    return (9 * (math.pow(math.e, -1 * x)) * math.sin(2 * math.pi * x)) - 3.5

# PLot function from 0 to 30 to find section where it crosses 0
xs = np.linspace(0, 30, 300)
fs = np.vectorize(f2)
plt.plot(xs, fs(xs))
plt.show()

# Plot shows area of intrest is between 0 and 1
rangeStart = 0
rangeEnd = 1

# Divide range into n brackets of same width
n = 50
width = (rangeEnd - rangeStart) / n

# List to store roots
roots = []

# Bisection method to search for roots in each bracket
left = rangeStart
right = left
for i in range(1, n+1):
    left = right
    right = left + width
    if (f2(left) * f2(right) <= 0):
        r = opt.bisect(f2, left, right)
        roots.append(r)

print("Roots:")
for i in range(len(roots)):
    print('%8.4f' %(roots[i]))
