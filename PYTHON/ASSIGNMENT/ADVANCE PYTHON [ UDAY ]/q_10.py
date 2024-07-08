# #Write a Python program to write a list to a file.


# Creating function for write a list into file 
def fun(data):
    file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , "w")
    for i in data:
        file.write(str(i) + "\n")

# creating list 
list = [ 9 , 8 , 7 , 6 , 5 ]
# calling function
fun(list)
print("Added successfully!!")

# Reading the file 
file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , "r")
content = file.read()

print(content)