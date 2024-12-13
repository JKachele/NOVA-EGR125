# Justin Kachele
# NOVA Fall 2024
# EGR 125 Quiz 4

import numpy as np

x = np.array([0, 25.4, 104.7, 206.3, 355.9, 580.1, 922.6, 1379.8])
t = np.arange(0, 40, 5);

vel = np.gradient(x, t)
accel = np.gradient(vel, t)

print("Position:", x)
print("Velocity:", vel)
print("Acceleration:", accel)
