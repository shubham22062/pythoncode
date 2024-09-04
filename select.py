def selection_sort(numbers):
    n = len(numbers)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
    return numbers

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_numbers = selection_sort(numbers)
print(f"Sorted list: {sorted_numbers}")
