#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle


# Creating class for finding area of rectangle 
class Rectangle():

    # constructor
    def __init__(self , length , width):
        self.length = length
        self.width = width

    # function area
    def area(self):
        return self.length * self.width
    
# asking user to input length and width of rectangle 
length = float(input("Enter Length : "))
width = float(input("Enter Width : "))


# printing the area of rectangle by calling the function and printing 
print(f"Area of Rectangle is : {Rectangle(length,width).area()}")