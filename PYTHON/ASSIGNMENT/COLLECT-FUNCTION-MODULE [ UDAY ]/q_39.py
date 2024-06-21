# # Write a Python function to calculate the factorial of a number (a
# nonnegative integer)


def fac():
    # Ask the user for input
    n = int(input("Enter a Number for Factorial: "))
    
    # Check if the number is zero
    if n == 0:
        return print("Enter number is zero")  # If the number is zero, print a message and exit the function
    
    else:
        # Initialize the factorial variable to 1
        fact = 1
        
        # Calculate the factorial using a loop
        for i in range(1, n + 1):
            fact = fact * i 
        
        # Print the factorial
        print("Factorial of", n, "is", fact)

# Call the function
fac()
