def has_pair_with_sum(numbers, target_sum):
    seen = set()  # Initialize an empty set to keep track of numbers we've seen
    for number in numbers:  # Loop through each number in the list
        complement = target_sum - number  # Calculate the complement needed to reach the target sum
        if complement in seen:  # Check if the complement is already in the set
            return True  # If found, return True
        seen.add(number)  # Add the current number to the set
    return False  # If no pair is found, return False

# Example usage
example_list = [10, 15, 3, 7]
target = 17
print(has_pair_with_sum(example_list, target))  # Output: True
