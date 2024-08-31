def name_check(name_input):
    
    patterned_name = ''
    abbreviated = ''
    
    for word in name_input:
        abbreviated += word[0].upper()
        
        count = 0
        while count < len(word):
            if count == 0:
                patterned_name += word[count].upper()
            else:
                patterned_name += word[count].lower()
            count += 1
        patterned_name += " "
        
    count = 0
    while count < len(abbreviated):
        if abbreviated[count].lower() != patterned_name[count].lower():
            return False
        count += 1
        
    return True

name_input = input("Enter Name:\t").split()
if (name_check(name_input=name_input)):
    print("It's A Perfect Name!!!")
else:
    print("It's A Bad Name :(")