class Node:
    def __init__(self,data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, data):
        data = int(data)
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.size += 1
        
        return node
    
    def find_loop(self):
        slow = self.head
        fast = self.head
        found = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        
        if found:
            print('Found Loop')
        else:
            print('No Loop')
            print(self)


    
    def __str__(self) -> str:
        log = ''
        current_node = self.head
        while current_node != None and current_node.next != None:
            log += f'{str(current_node.data)}->'
            current_node = current_node.next
        if current_node != None:
            log += str(current_node.data)
        log = log if log else 'Empty'
        return log 
    
    def set_next(self, node1, node2):
        self.head = node1
        node1.next = node2

    def S(self, index1, index2):
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
            self.set_next(node1=node1,node2=node2)
            print(f'Set node.next complete!, index:value = {str(index1)}:{str(node1.data)} -> {str(index2)}:{str(node2.data)}')
            

    def get_node_by_index(self, index: int):
        current_node = self.head
        if self.size == 0:
            return None
        
        for i in range(index):
            current_node = current_node.next
        return current_node

    def run(self, user_input : str):
        commands = user_input.split(',')
        for command in commands:
            parts = command.strip().split()
            action = parts[0]
            if action == 'A':
                data = parts[1]
                self.append(data)
                print(self)
            elif action == 'S':
                index1, index2 = parts[1].split(':')
                self.S(index1,index2)
        self.find_loop()
    

user_input = input('Enter input : ')
ls = LinkedList()
ls.run(user_input=user_input)