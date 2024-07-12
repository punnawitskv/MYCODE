# ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def size(self):
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(user_input):

    for char in user_input:
        if char.isalnum(): 
            postfix.append(char)
        elif char == '(':
            S.push(char)
        elif char == ')':
            while not S.isEmpty() and S.items[-1] != '(':
                postfix.append(S.pop())
            S.pop() 
        else:
            while (not S.isEmpty() and precedence(S.items[-1]) >= precedence(char)):
                postfix.append(S.pop())
            S.push(char)

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

postfix = []

infix_to_postfix(inp)

while not S.isEmpty():
    postfix.append(S.pop())

print(''.join(postfix))

