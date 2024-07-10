def bon(w): 
    char_count = {}
    max_count = 0
    most_dup_char = set()

    for char in w:
        if char.isalpha(): 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

            if char_count[char] > max_count:
                max_count = char_count[char]
                most_dup_char = {char}
            elif char_count[char] == max_count:
                most_dup_char.add(char)

		
    return most_dup_char


secretCode = input("Enter secret code : ")
print(bon(secretCode))