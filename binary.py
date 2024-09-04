def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1  # Return -1 if the element is not found

# Example usage:
numbers = sorted([int(x) for x in input("Enter sorted numbers separated by spaces: ").split()])
target = int(input("Enter the number to search for: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list.")
