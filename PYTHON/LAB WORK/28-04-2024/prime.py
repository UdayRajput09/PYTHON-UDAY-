## prime numbers 

# num = int(input("Enter Number : "))
# print(f"Prime Numbers Up to {num} are : ")

# for i in range(2,num+1):
#     prime =True

#     for j in range(2,int(i ** 0.5)+1):
#         if i % j == 0:
#             prime = False
#             break

#     if prime:
#         print(i)
        
    
    

## prime numbers with function


def Prime(num):
    print(f"Prime numbers up to {num} are : ")

    for i in range(2,num+1):
        prime = True

        for j in range(2,int(i ** 0.5)+1):
            if i % j == 0:
                prime = False
                break

        if prime:
            print(i)


num = int(input("Enter Number for prime Numbers : "))
Prime(num)