# Create a Python Program that perform following tasks for any problem of your choice:
# Task 1: Introduction
# Task 2: Terminal
# Task 3: Python Interpreter
# Task 4: Variables
# Task 5: Text Editor
# Task 6: Functions
# Task 7: Lists and Tuples
# Task 8: Conditional Statements
# Task 9: The For Loop
# Task 10: User Input and the While Loop

# Task 1: Introduction
print("Welcome to the calculator program!")

# Task 2: Terminal
print("Please enter the first number:")
num1 = input()

# Task 3: Python Interpreter
print("Please enter the second number:")
num2 = input()

# Task 4: Variables
result = 0

# Task 6: Functions


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# Task 5: Text Editor
print("Please select an operation (+, -, *, /):")
operation = input()

# Task 8: Conditional Statements
if operation == "+":
    result = add(float(num1), float(num2))
elif operation == "-":
    result = subtract(float(num1), float(num2))
elif operation == "*":
    result = multiply(float(num1), float(num2))
elif operation == "/":
    result = divide(float(num1), float(num2))
else:
    print("Invalid operation selected.")

# Task 7: Lists and Tuples
history = [(num1, num2, operation, result)]

# Task 9: The For Loop
print("Do you want to perform another calculation? (y/n):")
choice = input()

while choice == "y":
    print("Please enter the first number:")
    num1 = input()

    print("Please enter the second number:")
    num2 = input()

    print("Please select an operation (+, -, *, /):")
    operation = input()

    if operation == "+":
        result = add(float(num1), float(num2))
    elif operation == "-":
        result = subtract(float(num1), float(num2))
    elif operation == "*":
        result = multiply(float(num1), float(num2))
    elif operation == "/":
        result = divide(float(num1), float(num2))
    else:
        print("Invalid operation selected.")

    history.append((num1, num2, operation, result))

    print("Do you want to perform another calculation? (y/n):")
    choice = input()

# Task 10: User Input and the While Loop
print("Thank you for using the calculator program!")
print("Here is your calculation history:")
for item in history:
    print(item)
