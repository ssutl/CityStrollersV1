# This script calculates the resistance of a serpentine PCB trace with 20 traces.

import math

total = 0

def calculateResistance(length_meters):
    resistivity = 1.77e-8  # Copper resistivity in ohm meters
    width = 0.3e-3  # 0.3mm trace width
    thickness = 35e-6/2  # 1/2oz micrometers
    return resistivity * length_meters / (width * thickness)

def calculateStraightSection():
    # 4 tracks of 20 traces each, each 5 cm (0.05m) long
    return 4 * 20  * calculateResistance(50e-3)

def calculateMiniCurvedSection():
    mini_curve_total = 0
    radius = 12e-3  # 12 mm 
    for i in range(20):
        mini_curve_total += (radius - (0.3e-3 * i)) * math.pi  # 0.3 mm steps

    return calculateResistance(3 * mini_curve_total)

def calculateMainCurvedSection():
    main_curve_total = 0
    radius = 24e-3  # 24 mm 
    for i in range(20):
        main_curve_total += (radius - (0.3e-3 * i)) * math.pi  # 0.3 mm steps

    return calculateResistance(main_curve_total)

total = calculateStraightSection() + calculateMiniCurvedSection() + calculateMainCurvedSection()
print(total) # 23.780803171318148

