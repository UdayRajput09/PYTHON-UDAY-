## fibonacci series 

# num1 = 0
# num2 = 1

# num = int(input("Enter Number : "))

# print("-----Fibonacci series-----")
# print(num1)
# print(num2)

# for i in range(1,num +1):
#     num1 , num2 = num2 , num1 + num2
#     print(num2)



## Fibonacci series with function

def fibonacci(num):
    
    num1 = 0
    num2 = 1

    print("-----Fibonacci Series-----")
    print(num1)
    print(num2)

    for i in range(1,num+1):
        num1 , num2 = num2 , num1 + num2
        print(num2)

    
num = int(input("Enter Number : "))
fibonacci(num)


