# • Write a python program to sum of the first n positive integers

num = int(input("Enter number :"))

sum = 0

if num <=0 :
    print("Please enter positive integer!!")
else:
    for i in range(1,num+1):
        sum += i
    print("sum of the",num," is :",sum)

