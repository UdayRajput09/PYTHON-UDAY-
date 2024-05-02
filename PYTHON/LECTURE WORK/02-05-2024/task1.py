l = [ 1,"Uday" , "Rajput" , 3, 5, 2.09 ,1]
l1 = [ 3,6,2,9,7,1,5]

l.append(100)   ## add value at end
print(l) 

# print(l.copy()) 


l.index(1)     ## index value given
print(l)

count =  l.count(1)  ## count the number 
print(count)


l.extend([1,2,3,4]) ## add full list at the end
print(l)


l.insert(5,500) ##  insert the value at given index
print(l)

l.pop(2) ## remove the value at given index
print(l)

l.reverse  ## reverse the list 
print(l)

l1.sort() ## sort the list who has save variable type ex: int , string
print(l1)