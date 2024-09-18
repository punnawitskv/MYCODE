# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# โดยมีการป้อน input ดังนี้

# i <int> = insert data

# d <int> = delete data

# หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว



class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, data):  
        #code here
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data and cur.left != None:
                    cur = cur.left
                elif data >= cur.data and cur.right != None:
                    cur = cur.right
                elif data < cur.data:
                    cur.left = Node(data)
                    break
                else:
                    cur.right = Node(data)
                    break
        return self.root

    def delete(self,r, data):
        #code here
        def find_min(r):
            current = r
            while current.left is not None:
                current = current.left
            return current
    
        if r is None:
            print("Error! Not Found DATA")
            return r

        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else: #found it!!!
            if r.left is None and r.right is None:
                r = None
            elif r.left is None:
                r = r.right
            elif r.right is None:
                r = r.left
            else:
                temp = find_min(r.right)
                r.data = temp.data
                r.right = self.delete(r.right, temp.data)
        return r
        
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

#code here
for item in data:
    operation, value = item.split()
    value = int(value)
    if operation == 'i':
        print(f'insert {value}')
        tree.insert(value)
    elif operation == 'd':
        print(f'delete {value}')
        tree.root = tree.delete(tree.root, value)
    printTree90(tree.root)
