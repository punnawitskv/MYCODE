# วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้

# อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง

# อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้

# D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList

# R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi

# A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList


# ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย /

# ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case

# ก่อนจะทำตาม operation ต่างๆที่ป้อนมา

# หลังจากทำตาม operation

# LinkedList ที่ไม่มีข้อมูลซ้ำกัน


# สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้


# ****Note****

# -หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที

# -ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!


# *******ห้ามใช้ List! ให้ใช้ class Node ในการทำ Linked List เท่านั้น*********

class Node:

    def __init__(self, value=None, next=None):

        self.value = value

        self.next: Node = next


class LinkList:

    def __init__(self):

        self.head: Node = None

    def appendHead(self, value):

        node = Node(value, self.head)

        self.head = node

    def appendLast(self, value):

        if self.head is None:

            self.appendHead(value)

            return

        # CODE HERE

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def removeLast(self):

        # CODE HERE
        if self.head is None:
            print("Error!!!")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def rename(self, newName):

        # CODE HERE
        if self.head is None:
            print("Error!!!")
            return

        current = self.head
        while current.next:
            current = current.next
        current.value = newName

    def printList(self):

        # CODE HERE
        if self.head is None:
            print("Linklist is empty!")
            return

        current = self.head
        while current is not None:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def printListWithNoDuplicate(self):

        # CODE HERE
        if self.head is None:
            print("Linklist is empty!")
            return

        seen = set()
        current = self.head
        while current:
            if current.value not in seen:
                seen.add(current.value)
                print(current.value, end='')
                if (current.next) and (current.next.value not in seen):
                    print(end=" -> ")
            elif current.next.value not in seen:
                print(end=" -> ")

            current = current.next



def convertToLinkList(ls):

    # CODE HERE
    linked_list = LinkList()
    for item in ls:
        linked_list.appendLast(item)
    return linked_list


print("*** My Favourite Keynote ***")

user_input = input("Enter Input / List of operation : ").split(" / ")

listSong = user_input[0].split(' ')

operations = user_input[1].split(", ")

# print(operations)

myLinkList = convertToLinkList(listSong)

myLinkList.printList()

# CODE HERE
for operation in operations:
    if operation[0] == 'D':
        myLinkList.removeLast()
    elif operation[0] == 'R':
        myLinkList.rename(operation[2:])
    elif operation[0] == 'A':
        myLinkList.appendLast(operation[2:])
    else:
        "BRRRRR"
        break

myLinkList.printList()

myLinkList.printListWithNoDuplicate()
