# # Write a Python program to count the number of lines in a text file.

# Creating function for counting number of lines
def fun():

    # Count = 0
    count = 0

    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , "r")
    for i in file:
        count += 1
    return count

# Calling and printing function
lines = fun()

print(f"Numbers of line is : {lines}")