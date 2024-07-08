# #Write a Python program to read last n lines of a file.


# Creating function for reading last lines from a file
def fun(n):
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , 'r')
    l = file.readlines()
    last = l[-n:]
    for i in last :
        print(l.strip())


# Calling function 
n = 2
fun(n)