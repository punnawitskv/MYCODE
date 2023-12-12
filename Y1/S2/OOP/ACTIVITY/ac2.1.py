# Receive input from the user
input_str = input("Enter multiple numbers (separated by spaces): ")

# Split the input into a list of integers
numbers = [int(num) for num in input_str.split()]

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Check if the smallest number is 0
if sorted_numbers[0] == 0:
    # Find the index of the first non-zero number
    non_zero_index = next((i for i, num in enumerate(sorted_numbers) if num != 0), None)
    
    # Swap 0 with the first non-zero number, if found
    if non_zero_index is not None:
        sorted_numbers[0], sorted_numbers[non_zero_index] = sorted_numbers[non_zero_index], sorted_numbers[0]

# Convert the sorted numbers to a string
result_str = ''.join(map(str, sorted_numbers))

# Display the result
print("Sorted numbers with 0 swapped if it's the smallest: ", result_str)
