# Justin Kachele
# NOVA Fall 2024
# EGR 125 Quiz 3

import numpy as np

def main():
    print("Select an operation:")
    print("1. Calculate the determinant of a square matrix")
    print("2. Solve a system of n equations for n unknowns")
    print("3. Calculate the dot product of two vectors in 3D space")
    print("4. Calculate the cross product of two vectors in 3D space")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        calculate_determinant()
    elif choice == '2':
        solve_system_of_equations()
    elif choice == '3':
        calculate_dot_product()
    elif choice == '4':
        calculate_cross_product()
    else:
        print("Invalid choice.")

def calculate_determinant():
    # Prompt for matrix size and elements
    sizex = int(input("Enter Matrix Width: "))
    sizey = int(input("Enter Matrix Height: "))

    # Get 2d Array
    inputList = []
    for x in range(sizex):
        list1 = []
        for y in range(sizey):
            n = int(input("Enter value for position(%d, %d): " % (x, y)))
            list1.append(n)
        inputList.append(list1)
    m = np.array(inputList)

    # Use numpy.linalg.det() to calculate the determinant
    det = np.linalg.det(m)
    print("\nDeterminant for\n", m, "\nis", det)

def solve_system_of_equations():
    # Prompt for number of equations, coefficients, and constants
    numEqs = int(input("Enter number of equations: "))
    print("Equations are formatted as aA + bB + cC + ... = Constant")
    print("Lowercase letters are the coefficients")

    coefList = []
    constList = []
    # Loop for each equation
    for n in range(numEqs):
        coefList1 = []
        # Loop through each variable to get coefficients
        for v in range(numEqs):
            var = chr(ord('A') + v) # Get var letter (A, B, C, ...)
            c = int(input("Enter coefficient for variable\"{0}\" \
in equation {1}: ".format(var, n + 1)))
            coefList1.append(c)
            var = chr(ord(var) + 1) # Increment char (A -> B ...)
        coefList.append(coefList1)
        c = int(input("Enter Constant For The Equation: "))
        constList.append(c)
    a = np.array(coefList)
    b = np.array(constList)

    # Use numpy.linalg.solve() to find the solution
    x = np.linalg.solve(a, b)
    print(x)

def calculate_dot_product():
    # Prompt for vector components
    i1 = int(input("Input i value for Vector 1: "))
    j1 = int(input("Input j value for Vector 1: "))
    k1 = int(input("Input k value for Vector 1: "))
    i2 = int(input("Input i value for Vector 2: "))
    j2 = int(input("Input j value for Vector 2: "))
    k2 = int(input("Input k value for Vector 2: "))
    
    v1 = np.array([i1, j1, k1])
    v2 = np.array([i2, j2, k2])
    print("Vector1:", v1, "Vector2:", v2)

    # Use numpy.dot() for calculation
    dot = np.dot(v1, v2)
    print("V1 dot V2 =", dot)

def calculate_cross_product():
    # Prompt for vector components
    i1 = int(input("Input i value for Vector 1: "))
    j1 = int(input("Input j value for Vector 1: "))
    k1 = int(input("Input k value for Vector 1: "))
    i2 = int(input("Input i value for Vector 2: "))
    j2 = int(input("Input j value for Vector 2: "))
    k2 = int(input("Input k value for Vector 2: "))
    
    v1 = np.array([i1, j1, k1])
    v2 = np.array([i2, j2, k2])
    print("Vector1:", v1, "Vector2:", v2)

    # Use numpy.cross() for calculation
    cross = np.cross(v1, v2)
    print("V1 x V2 =", cross)

if __name__ == "__main__":
    main()
