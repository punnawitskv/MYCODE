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

        self.next = next


class LinkList:

    def __init__(self):

        self.head = None

    def appendHead(self, value):

        node = Node(value, self.head)

        self.head = node

    def appendLast(self, value):

        if self.head is None:

            self.appendHead(value)

            return

        # CODE HERE
        current_node = self.head
        while current_node.next:  # find last node
            current_node = current_node.next

        new_node = Node(value)
        current_node.next = new_node

    def removeLast(self):

        # CODE HERE
        if self.head is None:
            print('Error!!!')
            return

        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def rename(self, newName):

        # CODE HERE
        if self.head is None:
            print("Error!!!")
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.value = newName

    def printList(self):

        # CODE HERE
        if self.head is None:
            print("Linklist is empty!")
            return
        
        current_node = self.head
        print(current_node.value, end='')
        while current_node.next:
            print(' ->', current_node.next.value, end='')
            current_node = current_node.next
        print('')

    def printListWithNoDuplicate(self):

        # CODE HERE
        if self.head is None:
            print("Linklist is empty!")
            return
        
        seen_value = set()
        current_node = self.head
        print(current_node.value, end='')
        seen_value.add(current_node.value)

        while current_node:
            if current_node.value not in seen_value:
                print(' ->', current_node.value, end='')
                seen_value.add(current_node.value)
            current_node = current_node.next
            
def convertToLinkList(ls):

    # CODE HERE
    linked_list = LinkList()
    for item in ls:
        linked_list.appendLast(item)

    return linked_list


print("*** My Favourite Keynote ***")

inputl = input("Enter Input / List of operation : ").split('/')

listSong = [ele for ele in inputl[0].strip().split(' ')]

operations = [ele for ele in inputl[1].strip().split(", ")]


myLinkList = convertToLinkList(listSong)

myLinkList.printList()

# CODE HERE
for item in operations:
    order = item[0]
    note = item[2:]

    if order == 'A':
        myLinkList.appendLast(note)

    if order == 'R':
        myLinkList.rename(note)

    if order == 'D':
        myLinkList.removeLast()

myLinkList.printList()

myLinkList.printListWithNoDuplicate()
