# Justin Kachele
# NOVA Fall 2024
# EGR 125 Project 1

import math
import numpy as np
import matplotlib.pyplot as plt

# Time arrays: time - years from 0, years - years from -10000
time = np.arange(0, 12100, 10, dtype = float)
year = np.arange(-10000, 2100, 10, dtype = float)

# Constants
P0 = 4.0e6 # Starting population of 4 million
# rates
rates = np.array([0.07/100, 0.08/100, 0.09/100, 0.10/100, 0.11/100, 0.12/100])
# Population Capacity
K1 = 8.0e9
K2 = 10.9e9
K3 = 12e9

# Generate arrays
# Each array has 6 rows representing the 6 rates per K
k8 = np.array([])
k10 = np.array([])
k12 = np.array([])
for i in range(5):
    k8 = np.vstack([time, time, time, time, time, time])
    k10 = np.vstack([time, time, time, time, time, time])
    k12 = np.vstack([time, time, time, time, time, time])

# Function that calculated population from time, rate, and max population
def calcPop(t, r, k):
    exp = math.exp(r * t)
    num = k * P0 * exp
    den = k + (P0 * (exp - 1))
    return num / den

# Loops through arrays usinf time value to calculate population and replacing
# that into the array
for i in range(6):
    for j in range(time.size):
        k8[i][j] = calcPop(k8[i][j], rates[i], K1)
        k10[i][j] = calcPop(k10[i][j], rates[i], K2)
        k12[i][j] = calcPop(k12[i][j], rates[i], K3)

# Plot each row of array relative to the year
fig, ax = plt.subplots()
ax.plot(year, k8[0], "b-", label="r = 0.07%")
ax.plot(year, k8[1], "g-", label="r = 0.08%")
ax.plot(year, k8[2], "r-", label="r = 0.09%")
ax.plot(year, k8[3], "c-", label="r = 0.10%")
ax.plot(year, k8[4], "m-", label="r = 0.11%")
ax.plot(year, k8[5], "k-", label="r = 0.12%")
ax.legend(loc="upper left", fontsize="x-large")
plt.title("Population Curves: K = 8 billion")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

fig, ax = plt.subplots()
ax.plot(year, k10[0], "b-", label="r = 0.07%")
ax.plot(year, k10[1], "g-", label="r = 0.08%")
ax.plot(year, k10[2], "r-", label="r = 0.09%")
ax.plot(year, k10[3], "c-", label="r = 0.10%")
ax.plot(year, k10[4], "m-", label="r = 0.11%")
ax.plot(year, k10[5], "k-", label="r = 0.12%")
ax.legend(loc="upper left", fontsize="x-large")
plt.title("Population Curves: K = 10.9 billion")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

fig, ax = plt.subplots()
ax.plot(year, k12[0], "b-", label="r = 0.07%")
ax.plot(year, k12[1], "g-", label="r = 0.08%")
ax.plot(year, k12[2], "r-", label="r = 0.09%")
ax.plot(year, k12[3], "c-", label="r = 0.10%")
ax.plot(year, k12[4], "m-", label="r = 0.11%")
ax.plot(year, k12[5], "k-", label="r = 0.12%")
ax.legend(loc="upper left", fontsize="x-large")
plt.title("Population Curves: K = 12 billion")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

# Get index of year 2020
index_12020 = np.where(time == 12020)

print("K=8  billion, r=0.07%, population in 2020:", k8[0][index_12020],
      "Error:", abs(k8[0][index_12020] - 7.8e9))
print("K=8  billion, r=0.08%, population in 2020:", k8[1][index_12020],
      "Error:", abs(k8[1][index_12020] - 7.8e9))
print("K=8  billion, r=0.09%, population in 2020:", k8[2][index_12020],
      "Error:", abs(k8[2][index_12020] - 7.8e9))
print("K=8  billion, r=0.10%, population in 2020:", k8[3][index_12020],
      "Error:", abs(k8[3][index_12020] - 7.8e9))
print("K=8  billion, r=0.11%, population in 2020:", k8[4][index_12020],
      "Error:", abs(k8[4][index_12020] - 7.8e9))
print("K=8  billion, r=0.12%, population in 2020:", k8[5][index_12020],
      "Error:", abs(k8[5][index_12020] - 7.8e9))

print("K=10 billion, r=0.07%, population in 2020:", k10[0][index_12020],
      "Error:", abs(k10[0][index_12020] - 7.8e9))
print("K=10 billion, r=0.08%, population in 2020:", k10[1][index_12020],
      "Error:", abs(k10[1][index_12020] - 7.8e9))
print("K=10 billion, r=0.09%, population in 2020:", k10[2][index_12020],
      "Error:", abs(k10[2][index_12020] - 7.8e9))
print("K=10 billion, r=0.10%, population in 2020:", k10[3][index_12020],
      "Error:", abs(k10[3][index_12020] - 7.8e9))
print("K=10 billion, r=0.11%, population in 2020:", k10[4][index_12020],
      "Error:", abs(k10[4][index_12020] - 7.8e9))
print("K=10 billion, r=0.12%, population in 2020:", k10[5][index_12020],
      "Error:", abs(k10[5][index_12020] - 7.8e9))

print("K=12 billion, r=0.07%, population in 2020:", k12[0][index_12020],
      "Error:", abs(k12[0][index_12020] - 7.8e9))
print("K=12 billion, r=0.08%, population in 2020:", k12[1][index_12020],
      "Error:", abs(k12[1][index_12020] - 7.8e9))
print("K=12 billion, r=0.09%, population in 2020:", k12[2][index_12020],
      "Error:", abs(k12[2][index_12020] - 7.8e9))
print("K=12 billion, r=0.10%, population in 2020:", k12[3][index_12020],
      "Error:", abs(k12[3][index_12020] - 7.8e9))
print("K=12 billion, r=0.11%, population in 2020:", k12[4][index_12020],
      "Error:", abs(k12[4][index_12020] - 7.8e9))
print("K=12 billion, r=0.12%, population in 2020:", k12[5][index_12020],
      "Error:", abs(k12[5][index_12020] - 7.8e9))

