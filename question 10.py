def tuples_to_dictionary():
    tuples_list = []  # Initialize an empty list to store tuples
    while True:  # Loop indefinitely until the user decides to stop
        user_input = input("Enter a string and an integer separated by a comma (or type 'exit' to finish): ")
        if user_input.lower() == 'exit':  # Check if the user wants to exit
            break  # Exit the loop
        try:
            string, number = user_input.split(",")  # Split the input into string and number
            number = int(number.strip())  # Convert the number to an integer
            tuples_list.append((string.strip(), number))  # Add the tuple to the list
        except ValueError:
            print("Invalid input. Please enter in the format 'string, integer'.")  # Handle invalid input

    result_dict = {}  # Initialize an empty dictionary
    for string, number in tuples_list:  # Loop through each tuple in the list
        result_dict[string] = number  # Add the string as the key and the number as the value

    return result_dict  # Return the resulting dictionary

# Example usage
result = tuples_to_dictionary()
print("Resulting dictionary:", result)
