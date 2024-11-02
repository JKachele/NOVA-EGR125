# Justin Kachele
# EGR 125 Homework 4
# Main program

import numpy as np
import statistics
import ball_stats # This is your custom module

# Generate random data set
np.random.seed(5000)
diameters = np.random.randint(780, 821, 1000000)

# Conduct statistical analysis
mean = statistics.mean(diameters)
median = statistics.median(diameters)
mode = statistics.mode(diameters)
# Using tolist() function to avoid numpy type error with the stat module
std_dev = statistics.stdev(diameters.tolist())

# Perform custom analysis with ball_stats module
max_diameter = ball_stats.find_max(diameters)
min_diameter = ball_stats.find_min(diameters)
within_nominal = ball_stats.count_within_nominal(diameters, 800, 1)

# Output the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")
print(f"Maximum Diameter: {max_diameter}")
print(f"Minimum Diameter: {min_diameter}")
print(f"Count Within +/- 1% of Nominal: {within_nominal}")
