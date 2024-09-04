def is_armstrong_number(num):
    # Convert the number to string to easily iterate over digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits each raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == num

# Example usage:
number = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
