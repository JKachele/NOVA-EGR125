# Justin Kachele
# NOVA Fall 2024
# EGR 125 Final Exam
# Problem 3

import numpy as np
import scipy.interpolate as intp
import scipy.integrate as int

# Arrays containing x and y points
x_data = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
y_data = np.array([-29.5, -2.1, 12.4, 5.7, -14.2, -37.1, -47.3, -56.8, -54.9, -32.5, 19.2])

# Interpolate using a single polynomial
poly_interp = intp.BarycentricInterpolator(x_data, y_data)

# Integrate using adaptive quadrature
integral, error = int.quad(poly_interp, x_data[0], x_data[-1])

print("Integral: %.2f" %(integral))
