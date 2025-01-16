# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Display operation options
def select_operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Take user input for choice and numbers
def input_choice_from_user():
    choice = input("Enter choice (1/2/3/4): ")  # Corrected assignment
    num1 = float(input("Enter first number: "))  # Collect first number
    num2 = float(input("Enter second number: "))  # Collect second number
    return choice, num1, num2  # Returning the choice and numbers

# Main program
select_operation()  # Displaying our options
choice, num1, num2 = input_choice_from_user()  # Collect user input

# Perform operation based on user's choice
if choice == "1":
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == "2":
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == "3":
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == "4":
    result = divide(num1, num2)
    if isinstance(result, str):  # Check if result is an error message (string)
        print(result)  # Display the error message
    else:
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input.")

    



