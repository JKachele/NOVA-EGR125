# Justin Kachele
# NOVA Fall 2024
# EGR 125 Quiz 4

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def third_o(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

x = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([-29.5, -2.1, 12.4, 5.7, -14.2, -37.1, -47.3, -56.8, -54.9, -32.5, 19.2])

# Plot the Points
fig = plt.figure()
plt.plot(x, y, 'bo')
plt.title("Quiz 4: Curve Fitting")
plt.xlabel("x")
plt.ylabel("y")

# Call the curve fit function
coeff, cov = opt.curve_fit(third_o, x, y)

# Print out coefficients
print('Coefficients:')
print('a =', coeff[0])
print('b =', coeff[1])
print('c =', coeff[2])
print('d =', coeff[3])

# Plot the fitted curve
y_fit = third_o(x, coeff[0], coeff[1], coeff[2], coeff[3])
plt.plot(x, y_fit, 'r-')
fig.savefig("Quiz4_CurveFit.png")
