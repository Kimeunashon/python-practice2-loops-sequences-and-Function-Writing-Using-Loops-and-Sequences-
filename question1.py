
for num in range(1, 51):  # Loop through numbers 1 to 50
    if num % 3 == 0 and num % 5 == 0:  # Check if divisible by both 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:  # Check if divisible by 3
        print("Fizz")
    elif num % 5 == 0:  # Check if divisible by 5
        print("Buzz")
    else:
        print(num)  # Print the number if not divisible by 3 or 5
