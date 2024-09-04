def find_maximum(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    
    max_num = numbers[0]  # Assume the first number is the maximum
    
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    
    return max_num

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
max_value = find_maximum(numbers)

if max_value is not None:
    print(f"The maximum value in the list is {max_value}")
else:
    print("The list is empty.")
