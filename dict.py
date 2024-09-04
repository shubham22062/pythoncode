def merge_dicts(dict1, dict2):
    # Create a new dictionary that contains all items from dict1
    merged_dict = dict1.copy()
    
    # Update the new dictionary with items from dict2
    merged_dict.update(dict2)
    
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)
