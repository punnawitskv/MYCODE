def count_char_in_string(x, c):
    return [sum(1 for char in string if char == c) for string in x]

x_input = input("Enter a list of strings separated by space: ").split()
c_input = input("Enter a character: ")

result = count_char_in_string(x_input, c_input)
print(result)
