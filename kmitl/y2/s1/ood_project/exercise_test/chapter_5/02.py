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
        while cur.next is not None:
            cur = cur.next
            s += str(cur.value) + " "
        return s.strip()

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous is not None:
            cur = cur.previous
            s += str(cur.value) + " "
        return s.strip()

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, pos, item):
        new_node = Node(item)
        if self.isEmpty():
            if pos <= 0:
                self.head = new_node
                self.tail = new_node
            else:
                return
        else:
            if pos <= 0:
                self.addHead(item)
            else:
                cur = self.head
                index = 0
                while cur.next is not None and index < pos - 1:
                    cur = cur.next
                    index += 1
                if cur.next is None:
                    if index == pos - 1:
                        cur.next = new_node
                        new_node.previous = cur
                        self.tail = new_node
                else:
                    new_node.next = cur.next
                    new_node.previous = cur
                    cur.next.previous = new_node
                    cur.next = new_node

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        if pos < 0:
            pos = self.size() + pos
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
        else:
            cur = self.head
            idx = 0
            while cur is not None and idx < pos:
                cur = cur.next
                idx += 1
            if cur is not None:
                if cur.next is None:
                    self.tail = cur.previous
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    cur.previous.next = cur.next
                    cur.next.previous = cur.previous
        return "Success"

# Test
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
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
