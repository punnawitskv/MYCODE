def count_minus(input_str):
    negative_numbers = [int(num) for num in input_str.split() if int(num) < 0]
    return len(negative_numbers)

user_input = input("Enter numbers separated by space: ")

result = count_minus(user_input)
print("The number of negative numbers is:", result)
