# #Write a Python program to append text to a file and display the text


file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" , 'a')
file.write("\nHello I'm append \nHello I'm append \nHello I'm append \nHello I'm append")


file = open("C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt" ,'r')
r = file.read()
print(r)