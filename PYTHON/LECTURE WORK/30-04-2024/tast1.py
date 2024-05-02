## Prime 

def prime():
    num = int(input("Enter Number : "))
    c=0

    for i in range(1,num+1):
        if(num%i==0):
            c+=1

    if c == 2:
        return num,"is Prime"
    else:
        return num,"is not prime"
        

print(prime())