class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get_node_by_index(self, index: int):
        current_node = self.head
        if self.size == 0:
            return None
        
        for i in range(index):
            current_node = current_node.next
        return current_node

    def set_next(self, index1, index2):
        index1 = int(index1)
        index2 = int(index2)
        if self.size == 0:
            print('Error! {list is empty}')
        elif index1 > self.size - 1:
            print('Error! {index not in length}: ' + str(index1))
        elif index2 > self.size - 1:
            self.append(index2)
            print('index not in length, append : ' + str(index2))
        else:
            node1 =  self.get_node_by_index(index1)
            node2 = self.get_node_by_index(index2)
            self.head = node1
            node1.next = node2
            print(f'Set node.next complete!, index:value = {str(index1)}:{str(node1.value)} -> {str(index2)}:{str(node2.value)}')

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return "->".join(result)

ll = LinkedList()
commands = input("Enter input : ")

for command in commands.split(','):
    if command.startswith("A"):
        value = int(command.split()[1])
        ll.append(value)
        cur = ll.head
        while cur:
            print(cur.value, end='')
            cur = cur.next
            if cur:
                print(end='->')
        print('')
    elif command.startswith("S"):
        indices = command.split()[1].split(':')
        index1 = int(indices[0])
        index2 = int(indices[1])
        ll.set_next(index1, index2)
        
print("Found Loop" if ll.detect_loop() else "No Loop")
if ll.detect_loop() == False:
    if ll.size == 0:
        print("Empty")
    else:
        print(ll)
