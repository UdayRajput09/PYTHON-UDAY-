## Factorial  

# num = int(input("Enter Number : "))
# fact=1

# if num < 0 :
#     print("Number Can't be negative!!")
# else:
#     for i in range(1,num+1):
#         fact *= i
    
    
# print(f"Factorial of {num} is : {fact}")



## Factorial with function


def Factorial(num):

    fact = 1

    if num < 0 :
        print("Number can't be negative!!")
    else:
        for i in range(1,num+1) :
            fact *= i
        return fact


num = int(input("Enter Number : "))

fact = Factorial(num)


print(f"Factorial of {num} is : {fact}")
