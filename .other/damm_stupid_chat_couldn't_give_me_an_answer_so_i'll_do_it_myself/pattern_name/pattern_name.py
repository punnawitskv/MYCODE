def make_pattern(name_input):
    patterned_name = ''
    for word in name_input:
        count = 0
        while count < len(word):
            if count == 0:
                patterned_name += word[count].upper()
            else:
                patterned_name += word[count].lower()
            count += 1
        patterned_name += " "
    return patterned_name

def name_abbreviation(name_input):
    abbreviation = ''
    for word in name_input:
        first_letter = word[0]
        uppercase_letter = first_letter.upper()
        abbreviation += uppercase_letter
    return abbreviation

def abbreviated_with_name(name_input, abbreviated_input):
    count = 0
    new_name = ''
    while count < len(name_input):
        if count < len(abbreviated_input):
            new_name += abbreviated_input[count]
        else:
            new_name += name_input[count]
        count += 1
    return new_name

def abbreviated_check(name_input, abbreviated):
    count = 0
    while count < len(abbreviated):
        if abbreviated[count].lower() != name_input[count].lower():
            return False
        count += 1
    return True

name_input = input("Enter Name:\t").split()

print(f"Name Input:\t{make_pattern(name_input)}")
print(f"Abbreviation:\t{name_abbreviation(name_input)}")

if abbreviated_check(make_pattern(name_input), name_abbreviation(name_input)):
    print(f"New Name:\t{(abbreviated_with_name(make_pattern(name_input), name_abbreviation(name_input)))}")
    print("It's A Perfect Name!!!")
else:
    print("It's A Bad Name :(")