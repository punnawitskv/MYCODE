# จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def is_empty(self):
        return len(self.items) == 0


def dec2bin(decnum):

    s = Stack()

    if decnum == 0:
        return "0"

    while decnum > 0:
        s.push(decnum % 2)
        decnum = decnum // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))