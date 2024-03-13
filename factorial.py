# Factorial.py

# Ask the user to input an integer
number = int(input("Enter a positive integer: "))

# Initialize variables
factorial = 1
counter = 1

# Calculate factorial using a while loop
while counter <= number:
    factorial *= counter
    counter += 1

# Display the factorial
print(f"The factorial of {number} is {factorial}")
