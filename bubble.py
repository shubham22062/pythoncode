def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Track if any swap was made
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            if numbers[j] > numbers[j + 1]:
                # Swap if the element found is greater than the next element
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break

    return numbers

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_numbers = bubble_sort(numbers)
print(f"Sorted list: {sorted_numbers}")

