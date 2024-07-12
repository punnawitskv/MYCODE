# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

# 2. วงเล็บปิดเกิน

# 3. วงเล็บเปิดเกิน

# แล้วให้แสดงผลตามตัวอย่าง

user_input = str(input("Enter expresion : "))

def parenthesis_matching():

    stack = []
    open_paren_amount = 0
    close_paren_amount = 0
    
    for chr_i in user_input:
        if chr_i in "([{":
            open_paren_amount += 1
            stack.append(chr_i)

        elif chr_i in ")]}":
            close_paren_amount += 1

            if not stack:
                return f"{user_input} close paren excess"
            
            top = stack.pop()
            if chr_i == ')' and top != '(':
                return f"{user_input} Unmatch open-close"
            
            if chr_i == ']' and top != '[':
                return f"{user_input} Unmatch open-close"
            
            if chr_i == '}' and top != '{':
                return f"{user_input} Unmatch open-close" 

    if open_paren_amount > close_paren_amount:
        open_paren_excess = "(" * (open_paren_amount - close_paren_amount)
        return f"{user_input} open paren excess   {open_paren_amount - close_paren_amount} : {open_paren_excess}"
    
    if open_paren_amount < close_paren_amount:
        return f"{user_input} close paren excess   {close_paren_amount - open_paren_amount}"

    return f"{user_input} MATCH"

print(parenthesis_matching())
