#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle


# Creating circle class for finding area and perimeter of circle 
class Circle:

    # constructor 
    def __init__(self,radius):
        self.radius = radius
    
    # function area
    def area(self):
        return 3.14 * self.radius **2
    
    # function perimeter 
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

# asking user to input radius for circle 
radius = float(input("Enter Radius : "))

# printing the area and perimeter of circle by calling and printing it 
print(f"Area of circle is : {Circle(radius).area()} \n Perimeter of Circle is : {Circle(radius).perimeter()}")