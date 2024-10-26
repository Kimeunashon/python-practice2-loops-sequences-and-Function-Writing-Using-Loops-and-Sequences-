def reverse_strings(strings):
    reversed_list = []  # Initialize an empty list to store reversed strings
    for s in strings:  # Loop through each string in the list
        reversed_list.append(s[::-1])  # Reverse each string and add it to the new list
    return reversed_list  # Return the list of reversed strings

# Example usage
input_list = ["apple", "banana", "cherry"]
print(reverse_strings(input_list))
