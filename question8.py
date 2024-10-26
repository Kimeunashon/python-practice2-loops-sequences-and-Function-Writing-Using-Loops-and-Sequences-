def keys_with_value_greater_than_n(input_dict, n):
    result_keys = []  # Initialize an empty list to store keys
    for key, value in input_dict.items():  # Loop through each key-value pair in the dictionary
        if value > n:  # Check if the value is greater than n
            result_keys.append(key)  # Add the key to the result list if the condition is met
    return result_keys  # Return the list of keys

# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_value_greater_than_n(example_dict, n))
