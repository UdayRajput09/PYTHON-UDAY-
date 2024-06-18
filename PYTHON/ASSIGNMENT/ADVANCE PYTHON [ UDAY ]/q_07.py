# #Write a python program to find the longest words.


# Creating function for finding longest
def fun():
    longest = " "
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , "r")
    for i in file :
        for j in i.split():
            if len(j) > len(longest):
                longest = j
    return longest


# Calling the function 
longest = fun()

# Printing the function 
print(f"longest word in the file  is : {longest} ")