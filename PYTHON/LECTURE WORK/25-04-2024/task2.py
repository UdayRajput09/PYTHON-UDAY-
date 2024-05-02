s = input("Enter string : ")

l1 = int(len(s)/2)
print(l1)


if len(s)%2==0:
    print(s[l1])
else:
    print(s[l1-1]+s[l1]+s[l1+1])
