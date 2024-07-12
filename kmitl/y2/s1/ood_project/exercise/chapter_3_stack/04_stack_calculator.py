# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# *************************************************


class StackCalc():
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        if value is not None:
            self.items.append(value)
        else:
            print(f"Push Error {value}")
            return 

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return 0
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def run(self, arg):
        arg = arg.split(" ")
        for item in arg:
            if item.isdigit():
                machine.push(int(item))
            elif item in '+-*/':
                num1 = machine.pop()
                num2 = machine.pop()
                if item == '+':
                    machine.push(int(num1 + num2))
                elif item == '-':
                    machine.push(int(num1 - num2))
                elif item == '*':
                    machine.push(int(num1 * num2))
                elif item == '/':
                    machine.push(int(num1 / num2))
                else:
                    print(f"Run +-*/ Error {item}")
                    return
            elif item == 'DUP':
                num = machine.pop()
                machine.push(num)
                machine.push(num)
            elif item == 'POP':
                machine.pop()
            else:
                machine.push(f"Invalid instruction: {item}")
                return

    def getValue(self):
        num = machine.pop()
        return num

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())