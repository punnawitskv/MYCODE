def only_english(input_string):
    # Use list comprehension to filter out non-English alphabets
    english_letters = [char for char in input_string if char.isalpha() and char.isascii()]

    # Join the list of English letters to form a string
    result_string = ''.join(english_letters)

    return result_string

# Example usage:
input_str = input("Enter a string: ")
result = only_english(input_str)
print("Result:", result)
