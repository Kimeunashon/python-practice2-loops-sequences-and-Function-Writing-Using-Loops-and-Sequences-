def get_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ")

        if user_input.lower() == "exit":  # Check if the input is "exit" (case insensitive)
            print("Exiting the program.")
            break  # Exit the loop if "exit" is entered

        print("You entered:", user_input)  # Print the entered word


# Call the function to run the loop
get_input()
