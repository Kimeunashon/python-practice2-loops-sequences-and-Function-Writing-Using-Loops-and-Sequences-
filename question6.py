def find_largest_number(numbers):
    largest = numbers[0]  # Start with the first element as the largest
    for num in numbers:  # Loop through each number in the tuple
        if num > largest:  # Check if the current number is greater than the largest so far
            largest = num  # Update the largest number
    return largest  # Return the largest number found

# Example usage
nums = (10, 20, 30, 40, 50)
print("The largest number is:", find_largest_number(nums))
