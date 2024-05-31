#  Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.

def fun():
    l = [1 , 2 , 4 , 6 , 8, 1 , 2 , 4 ]
    l1 =[]

    for i in l:
        if i not in l1:
            l1.append(i)

    return l1

print(fun())
        