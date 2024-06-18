# #Write a Python program to read first n lines of a file.

# Creating function for readline
def fun(n):
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt"  , 'r')
    
    # for loop for getting  n number of line 
    for i in range(n):
        l = file.readline()
        if l == " ":
            break
        print(l.strip())

# calling the function
n = 2
fun(n)