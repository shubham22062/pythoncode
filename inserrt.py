def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        
        # Move elements of numbers[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        
        numbers[j + 1] = key
    
    return numbers

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_numbers = insertion_sort(numbers)
print(f"Sorted list: {sorted_numbers}")
