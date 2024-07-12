user_input = str(input("Enter Input : "))

check = True
stack = []

for chr_i in user_input:
    if chr_i in "([{":
        stack.append(chr_i)
    elif chr_i in ")]}":
        if not stack:
            check = False
            break
        top = stack.pop()
        if chr_i == ')' and top != '(':
            check = False
            break
        elif chr_i == ']' and top != '[':
            check = False
            break
        elif chr_i == '}' and top != '{':
            check = False
            break

if check and not stack:
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")
