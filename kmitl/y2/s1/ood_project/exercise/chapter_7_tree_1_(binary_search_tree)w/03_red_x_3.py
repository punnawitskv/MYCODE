# ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา 
# และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

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
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printTree_x(self, node, k, level = 0):
        if node:
            if node.data > k:
                node.data = node.data * 3
            self.printTree_x(node.right, k, level + 1)
            print('     ' * level, node)
            self.printTree_x(node.left, k, level + 1)


inp = input("Enter Input : ").split("/")

list_inp = [int(i) for i in inp[0].split()]
k_inp = int(inp[1])

T = BST()
for i in list_inp:
    root = T.insert(i)

T.printTree(root)

print("--------------------------------------------------")

T.printTree_x(root, k_inp)