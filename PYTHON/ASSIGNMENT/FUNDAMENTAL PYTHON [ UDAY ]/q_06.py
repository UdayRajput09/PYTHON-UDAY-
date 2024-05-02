# Write python program that swap two number with temp variable and 
# without temp variable.

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

print("Before swapping  num1 is :",num1,"num2 is : " ,num2)

temp = num1
num1 = num2
num2 = temp

print("After swapping with temp num1 is :",num1 , "num2 is : ",num2)


n1 = 5 
n2 = 4

n1 , n2 = n2 , n1

print("after swapping the numbers without temp is :",n1 ,"," , n2)