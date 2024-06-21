#Write a Python function to check whether a number is perfect or not    


def perfect_check(num):
    # Initialize sum of factors
    total = 0
    
    # Find all factors of the number
    for i in range(1, num):
        if num % i == 0:
            total += i
    
    # Check if the sum of factors equals the number itself
    return total == num

# Ask the user for input
number = int(input("Enter a number: "))

# Check if the number is perfect and print the result
if perfect_check(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

