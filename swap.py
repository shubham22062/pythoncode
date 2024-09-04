# Function to swap two numbers using a temporary variable
def swap_numbers(a, b):
    print(f"Original values:\n a = {a}, b = {b}")
    
    # Swapping process
    temp = a
    a = b
    b = temp
    
    print(f"After swapping:\n a = {a}, b = {b}")

# Example usage
num1 = 5
num2 = 10

swap_numbers(num1, num2)
