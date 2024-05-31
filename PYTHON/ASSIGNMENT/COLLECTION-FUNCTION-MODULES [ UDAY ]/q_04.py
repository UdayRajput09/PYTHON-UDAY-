# Write a Python function to get the largest number, smallest num and sum 
# of all from a list.


def fun():
    l = [4,3,8,6,1]

    l.sort()
    print(l)

    print("Smallest : ",l[0])
    print("Biggest : ",l[-1])

    print("sum of list is : ",sum(l))


fun()