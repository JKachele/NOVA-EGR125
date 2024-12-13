# Justin Kachele
# NOVA Fall 2024
# EGR 125 Final Exam
# Problem 1

import scipy.optimize as opt

def f(x):
    return (x ** 3) - (8 * (x ** 2)) + x + 10 

# Create 50 divisions from -2 to 8
divisions = 50
div_width = (8.0 - (-2.0)) / divisions

# list to store roots once found
roots = []
# Left and right side on the division being solved
left = -2.0
right = -2.0
for i in range(1, divisions + 1):
    left = right
    right = left + div_width
    # if value on one side is negative, and the other is positive, Root in div 
    if (f(left)*f(right)<=0):   
        # use bisect function to find root in division
        r = opt.bisect(f, left, right)
        roots.append(r)

# Print roots
print('Roots:')
for i in range(len(roots)):
    print('%8.4f' %(roots[i]))
