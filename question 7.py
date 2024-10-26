def remove_duplicates(input_list):
    new_list = []  # Initialize an empty list to store unique elements
    for item in input_list:  # Loop through each item in the input list
        if item not in new_list:  # Check if the item is not already in the new list
            new_list.append(item)  # Add the item to the new list if it's unique
    return new_list  # Return the list with duplicates removed

# Prompt user for input
user_input = input("Enter a list of items separated by commas: ")  # Get input as a string
input_list = user_input.split(",")  # Split the input string into a list

# Remove leading/trailing whitespace from each item
input_list = [item.strip() for item in input_list]

# Remove duplicates and display the result
result = remove_duplicates(input_list)
print("List with duplicates removed:", result)
