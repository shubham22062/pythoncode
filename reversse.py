# Function to reverse a number using string manipulation
def reverse_number(n):
    # Convert number to string and reverse it
    reversed_num = str(n)[::-1]
    
    # Convert back to integer to remove any leading zeros
    reversed_num = int(reversed_num)
    
    return reversed_num

# Example usage
number = 12345
reversed_number = reverse_number(number)
print(f"Original number: {number}")
print(f"Reversed number: {reversed_number}")
