n = int(input("Enter number :"))

for i in range(1,n+1):
    if i == 6 :
        break
    print(i)

print("countinue")
for i in range(1,n+1):
    if i == 6 :
        continue
    print(i)