# Write a Python program to convert degree to radian

import math

def radians(degrees):
    return degrees * (math.pi / 180)

# Ask the user for input
degre = float(input("Enter degrees: "))

# Convert degrees to radians and print the result
radians = radians(degre)
print(f"{degre} degrees is equal to {radians} radians")
