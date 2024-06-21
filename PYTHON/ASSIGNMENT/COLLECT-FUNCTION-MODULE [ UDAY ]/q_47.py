# # Write a Python program to calculate surface volume and area of a
# cylinder


import math

# Ask the user for input
r = float(input("Enter the radius of the cylinder : "))
h = float(input("Enter the height of the cylinder : "))

# Calculate the surface area
surface = 2 * math.pi * r * (r + h)
# Calculate the volume
volume = math.pi * r**2 * h

# Print the results
print("Surface area of the cylinder :", surface)
print("Volume of the cylinder :", volume)
