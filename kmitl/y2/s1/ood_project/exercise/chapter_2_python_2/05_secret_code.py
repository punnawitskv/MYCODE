def bon(w): 
    char_count = {}
    max_count = 0

    for char in w:
        if char.isalpha(): 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

            if char_count[char] > max_count:
                max_count = char_count[char]
                most_dup_char = char
	
    char_position = ord(most_dup_char) - ord('a') + 1
    return char_position * 4


secretCode = input("Enter secret code : ").lower()
print(bon(secretCode))