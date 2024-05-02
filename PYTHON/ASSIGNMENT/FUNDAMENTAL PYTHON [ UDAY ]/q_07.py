# Write a Python program to find whether a given number is even or odd, 
# print out an appropriate message to the user.

num = int(input("Enter number :"))

if num == 0 :
    print(num," is Zero!!")
elif num%2 == 0 :
    print(num," is even!!")
else:
    print(num," is odd!!")
