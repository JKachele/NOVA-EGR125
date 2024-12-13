import numpy as np
import matplotlib.pyplot as plt

# Define function
def fun(x):
    return (400*x**5 - 900*x**4 + 675*x**3 - 200*x**2 \
    + 25*x + 0.2)

# Analytical derivative
def dfun(x):
    return (2000*x**4 - 3600*x**3 + 2025*x**2 \
    - 400*x + 25)

# Generate x data values
x_data = np.arange(0, 0.9, 0.1)

# Corresponding y data values
y_data = fun(x_data)

# Derivative using differences
der_diff = np.diff(y_data)/np.diff(x_data)
x_diff = []
for i in range(len(x_data)-1):
    val = (x_data[i+1] + x_data[i])/2
    x_diff.append(val)

# Derivative using gradients
der_grad = np.gradient(y_data, x_data)

# Plot curve of analytically derived first derivative
# and approximations at discrete points
x_plot = np.linspace(0, 0.8, 50)
y_plot = dfun(x_plot)
fig = plt.figure()
plt.plot(x_plot, y_plot)
plt.title("First Derivatives")
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.plot(x_diff, der_diff, 'bo', label="Diff")
plt.plot(x_data, der_grad, 'ro', label="Gradient")
plt.legend()
fig.savefig("derivatives.png")
