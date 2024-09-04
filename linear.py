def linear_search(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
target = int(input("Enter the number to search for: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list.")
