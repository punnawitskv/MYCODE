def only_english(input_string):
    english_letters = [char for char in input_string if char.isalpha() and char.isascii()]

    result_string = ''.join(english_letters)

    return result_string

input_str = input("Enter a string: ")
result = only_english(input_str)
print("Result:", result)
