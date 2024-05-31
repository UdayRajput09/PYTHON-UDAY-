# Write a Python program to calculate the area of a parallelogram


def parallelogram(b, h):
    return b * h

# Ask the user for input
b = float(input("Enter the length of the base : "))
h = float(input("Enter the height : "))

# Calculate the area of the parallelogram and print the result
area = parallelogram(b, h)
print("Area of the parallelogram:", area)
