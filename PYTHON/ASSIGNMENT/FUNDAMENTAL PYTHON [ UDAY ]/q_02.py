# Write a Python program to get the Factorial number of given number.

number = int(input("Enter number : "))

if number < 0:
    print("Number can't be negative")
else:
    fact = 1
    for i in range(1,number+1):
        fact *= i 
        
print("Factorial of ",number , "is :",fact)