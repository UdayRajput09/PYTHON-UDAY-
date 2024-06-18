# #Write a Python program to read a file line by line and store it into a list


# Creating function for reading file line by line and storing into a list 
def fun():
    l = []
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo1.txt", "r")
    for i in file:
        l.append(i.strip())
    return l

# Calling the function
l = fun()

# for loop for printing number that are stored into list
for i in l:
    print(i)

# Printing the list
print(l)