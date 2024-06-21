#Write a Python program to returns sum of all divisors of a number

def sum(n):
    # Initialize sum
    sum = 0
    # Find all divisors
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum

# Ask the user for input
num = int(input("Enter a number: "))

# Calculate and print the sum of divisors
print(f"Sum of divisors of {num} is {sum(num)}")
