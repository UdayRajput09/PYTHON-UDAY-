# Write a Python program to check if a number is positive, negative or 
# zero.

number = int(input("Enter Number :"))

if number == 0:
    print("Number is 0 !!")
elif number > 0 :
    print(number,"is positive!!")
else:
    print(number,"is negative!!")