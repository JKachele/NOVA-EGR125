# Justin Kachele
# NOVA Fall 2024
# EGR 125 Final Exam
# Problem 2

import numpy as np
import scipy.interpolate as intp

# Arrays containing x and y points
x_data = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
y_data = np.array([-29.5, -2.1, 12.4, 5.7, -14.2, -37.1, -47.3, -56.8, -54.9, -32.5, 19.2])

# Interpolate points using cubic splines
cubic_spline = intp.interp1d(x_data, y_data, 'cubic')

# Get y value at x = 2.5
y = cubic_spline(2.5)
print("f(2.5) = %.1f" %(y))
