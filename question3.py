def sum_of_list(nums):
    total = 0  # Initialize total to 0
    for num in nums:  # Loop through each number in the list
        total += num  # Add each number to total
    return total  # Return the total sum

# example
nums = [1, 2, 3, 4, 5]
print("The sum is:", sum_of_list(nums))
