# Justin Kachele
# NOVA Fall 2024
# EGR 125 Final Exam
# Problem 4

import numpy as np
import matplotlib.pyplot as plt

# Input variables
R0 = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
E = 0.9

# Herd Immunity Threshold
def hit(r0):
    return 1 - (1 / r0)

# Critical Vaccination Coverage 
def cvc(r0):
    return (1 / E) * hit(r0)

h = hit(R0)
v = cvc(R0)

fig1 = plt.figure()
plt.plot(R0, h, 'bo')
plt.title("Herd Immunity")
plt.xlabel("R0")
plt.ylabel("Herd Immunity Threshold(h)")
fig1.savefig("herd_immunity_threshold.png")

fig2 = plt.figure()
plt.plot(R0, v, 'bo')
plt.title("Critical Vaccination")
plt.xlabel("R0")
plt.ylabel("Critical Vaccination Threshold(v)")
fig2.savefig("vaccination_coverage.png")
