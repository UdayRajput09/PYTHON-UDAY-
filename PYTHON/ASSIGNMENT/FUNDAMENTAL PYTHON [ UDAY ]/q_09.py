# • Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

num1 = int(input("Enter number one :"))
num2 = int(input("Enter number two :"))
num3 = int(input("Enter number three :"))

if num1 == num2 or num1 == num3 or num2 == num3 :
    print(" If two number is equal then sum of three number is : 0")
else:
    print("sum of three number is : ",num1+num2+num3)
