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
R07 = 0.07 / 100
R08 = 0.08 / 100
R09 = 0.09 / 100
R10 = 0.10 / 100
R11 = 0.11 / 100
R12 = 0.12 / 100
# Population Capacity
K1 = 8.0e9
K2 = 10.9e9
K3 = 12e9
