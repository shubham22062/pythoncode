# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to display the calculator menu
def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Validate the input choice
    if choice in ['1', '2', '3', '4']:
        # Take user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == '1':
            print(f"The result of {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"The result of {num1} / {num2} = {result}")
    else:
        print("Invalid input! Please choose a valid operation.")

# Example usage
calculator()
