# ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
# 4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 9. size           คืนค่าเป็นขนาดของ Linked List
# 10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
# 11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

# ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น
# 1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
# 2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
# 3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]
# 4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

# โดยรูปแบบ Input มีดังนี้
# 1. append    ->  AP
# 2. addHead  ->  AH
# 3. search      ->  SE
# 4. index        ->   ID
# 5. size          ->   SI
# 6. pop          ->   PO
# 7. insert       ->   IS

# โดยให้เพิ่มเติมจากส่วน #CodeHere ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
# ********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        # Code Here
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, item):
        # Code Here
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, pos, item):
        # Code Here

        list_size = self.size()

        new_node = Node(item)

        if self.isEmpty() or (pos <= 0 and pos*-1 > list_size) or pos == 0:
            self.addHead(item)
            return

        if pos > list_size:
            self.append(item)
            return
        
        if pos < 0:
            pos = list_size + pos

        current_node = self.head
        count = 0
        while current_node:
            if count == pos:
                current_node.previous.next = new_node
                new_node.previous = current_node.previous
                current_node.previous = new_node
                new_node.next = current_node
                return
            count += 1
            current_node = current_node.next

    def search(self, item):
        # Code Here
        current_node = self.head
        found = 'Not Found'
        while current_node and found == 'Not Found':
            if current_node.value == item:
                found = 'Found'
            current_node = current_node.next

        return found

    def index(self, item):
        # Code Here
        pos = -1
        found = False
        current_node = self.head
        while current_node and not found:
            pos += 1
            if current_node.value == item:
                found = True
            current_node = current_node.next

        if found:
            return pos
        else:
            return -1

    def size(self):
        # Code Here
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def pop(self, pos):
        # Code Here
        if pos < 0 or pos > self.size() or self.isEmpty():
            return 'Out of Range'
        else:
            count = 0
            current_node = self.head
            while current_node:
                if count == pos:
                    if current_node.next and current_node.previous: # cur is not head or tail
                        current_node.next.previous = current_node.previous
                        current_node.previous.next = current_node.next

                    elif current_node.next: # cur is head not tail
                        current_node.next.previous = None
                        self.head = None

                    elif current_node.previous: # cur is tail not head
                        current_node.previous.next = None
                        self.tail = None

                    else: # cur is head and tail
                        self.head = None
                        self.tail = None

                    return 'Success'
                pos += 1
                current_node = current_node.next


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
