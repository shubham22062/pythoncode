# Recursive function to swap two numbers
def swap_numbers(a, b, depth=1):
    if depth == 1:
        print(f"Original values:\n a = {a}, b = {b}")

    # Base case: When depth reaches 3, the swap is complete
    if depth == 3:
        print(f"After swapping:\n a = {a}, b = {b}")
        return a, b

    # Recursive call, reducing depth and swapping values
    return swap_numbers(b, a, depth + 1)

# Example usage
num1 = 5
num2 = 10

# Call the recursive swap function
swap_numbers(num1, num2)
