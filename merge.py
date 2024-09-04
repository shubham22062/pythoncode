def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2  # Finding the middle of the list
        left_half = numbers[:mid]  # Dividing the elements into 2 halves
        right_half = numbers[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1
    
    return numbers

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_numbers = merge_sort(numbers)
print(f"Sorted list: {sorted_numbers}")
