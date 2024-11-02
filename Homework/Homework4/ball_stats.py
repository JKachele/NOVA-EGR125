# Justin Kachele
# EGR 125 Homework 4
# External module

def find_max(diameters):
    max = 0

    for d in diameters:
        if d > max:
            max = d

    return max

def find_min(diameters):
    min = 1000000

    for d in diameters:
        if d < min:
            min = d

    return min

def count_within_nominal(diameters, nominal, tolerance):
    count = 0
    onePercent = nominal * (tolerance / 100)

    for d in diameters:
        diff = abs(d - nominal)
        if diff <= onePercent:
            count += 1

    return count
