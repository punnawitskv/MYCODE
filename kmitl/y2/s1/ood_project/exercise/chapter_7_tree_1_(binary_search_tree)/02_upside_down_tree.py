# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# จากนั้นให้ สลับทุกๆ node จาก Left node เป็น Right node และจาก Right node เป็น Left node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        #CODE HERE
        if node:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            self.reverseTree(node.left)
            self.reverseTree(node.right)

        

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
#CODE HERE
print("Before:")
T.printTree(root)

T.reverseTree(root)

print("After:")
T.printTree(root)