# #Write a Python program to read a file line by line store it into a variable.


# Creating function to read file line by line and store into variable
def fun():
    var = ""
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , "r")
    for i in file:
        var +=i
    return var

# Calling and printing the function and variable 
var = fun()
print(var)