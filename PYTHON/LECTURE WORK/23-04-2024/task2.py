s = "Uday Rajput"

print(len(s)) # check the length 
print(type(s)) # check the Type 
print(s.capitalize())  # Capitalize
print(s.casefold())  # First letter small
print(s.lower())  # Lower
print(s.upper())  # Upper
print(s.center(15,"*"))  # Center 
print(s.count("a"))  # Count
print(s.endswith("t"))  # return true or false
print(s.find("a",3))  # finds
print(s.index("a",3))  # check index
print(s.isalnum())  # return true or false [ all the is functions]
print(s.replace("U","R"))  # replace the char
print(s.swapcase())  # swap the cases

s1 = "-".join(s)
print(s1) # take "-" [your choice] between each character 
