#Write python program that user to enter only odd numbers, else will raise an exception.

# Creating function to check the user enter odd numbers only !
def fun():

    # While loop for infinite loop
    while True:

        # try except for error handling 
        try:
            num = int(input("Enter an odd number : "))
            if num % 2 != 0:
                return num
            else:

                #raise the valueError for exception
                raise ValueError("Please enter an odd Number only !!")
        except ValueError as e:
            print(f"Error : {e}")


# printing and calling the function
print(f"\nYour entered odd number is : {fun()}")