# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display calculator menu
print("Calculator Menu:")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s")

# Ask user to choose operation
operation = input("Choose an operation (Enter the corresponding number): ")

# Perform operation based on user's choice
if operation == '1':
    result = num1 + num2
    print("Result:", result)
elif operation == '2':
    result = num1 - num2
    print("Result:", result)
elif operation == '3':
    result = num1 * num2
    print("Result:", result)
elif operation == '4':
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result:", result)
elif operation == '5':
    result1 = num1 * num1
    result2 = num2 * num2
    print("Square of", num1, "is:", result1)
    print("Square of", num2, "is:", result2)
else:
    print("Invalid operation selected. Please choose a valid operation.")
