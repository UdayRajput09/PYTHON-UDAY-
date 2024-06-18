#Write a Python program to read an entire text file.


# Opening the file on the read mode 
file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt"  , 'r')

# Reading the entire content of file
r = file.read()

# printing the entire text file
print(r)