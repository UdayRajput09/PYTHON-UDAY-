def srev():
    s = input("Enter String : ")

    print("Reverse string is : ",s[::-1])
def slen():
    s = input("Enter String : ")
    print(f"length of string is : {len(s)}")

def middle():
    s = input("Enter String : ")
    s1 = int(len(s)/2)

    print(s[s1-1]+s[s1]+s[s1+1])

def concat():
    s1 = input("Enter String 1 : ")
    s2 = input("Enter String 2 : ")

    print(f"Merge String is : {s1+s2}")