# Write a Python program to calculate the area of a trapezoid


def trapezoid(b1, b2, h):
    return (b1 + b2) * h / 2

# Ask the user for input
b1 = float(input("Enter the length of the 1st base : "))
b2 = float(input("Enter the length of the 2nd base : "))
h = float(input("Enter the height : "))

# Calculate the area of the trapezoid and print the result
area = trapezoid(b1, b2, h)
print("Area of the trapezoid:", area)
