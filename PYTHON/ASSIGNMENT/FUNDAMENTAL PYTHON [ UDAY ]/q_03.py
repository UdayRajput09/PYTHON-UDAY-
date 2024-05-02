#Write a Python program to get the Fibonacci series of given range.

a = 0
b = 1

n = int(input("Enter Number :"))

print("Fibonacci series")
print(a)
print(b)
for i in range(2,n+1):
    a , b = b , a+b
    print(b)
