class TreeNode(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getHeight(self, node = None):
        return -1 if node == None else node.height

    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

    def __str__(self):
        return str(self.data)

class AVL_Tree(object):
    def __init__(self, root = None):
        self.root: TreeNode = None if root is None else root

    def insert(self, root, data):
        data = int(data)
        self.root = AVL_Tree._insert(root, data)
        return self.root

    def _insert(root, data):
        if not root:
            return TreeNode(data)
        if data < root.data:
            root.left = AVL_Tree._insert(root.left, data)
        else:
            root.right = AVL_Tree._insert(root.right, data)
        root.setHeight()
        return AVL_Tree._rebalance(root)

    def rotateLeftChild(node: TreeNode):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(node: TreeNode):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def _rebalance(node: TreeNode):
        balance = node.balanceValue()
        if balance == -2:
            if node.right.balanceValue() == 1:
                node.right = AVL_Tree.rotateLeftChild(node.right)
            node = AVL_Tree.rotateRightChild(node)
        elif balance == 2:
            if node.left.balanceValue() == -1:
                node.left = AVL_Tree.rotateRightChild(node.left)
            node = AVL_Tree.rotateLeftChild(node)
        return node
    def height_of_tree(node: TreeNode):
        if node is None:
            return 0
        return 1 + max(AVL_Tree.height_of_tree(node.left), AVL_Tree.height_of_tree(node.right))
    def print_space(self, n, removed):
        for _ in range(n):
            print("  ", end="")
        if removed is None:
            print("  ", end="")
        else:
            print(removed.data, end=" ")
    def printTree(self):
        tree_level = []
        temp = []
        tree_level.append(self.root)
        counter = 0
        height = AVL_Tree.height_of_tree(self.root) - 1
        number_of_elements = 2 ** (height + 1) - 1
        while counter <= height:
            removed = tree_level.pop(0)
            if len(temp) == 0:
                self.print_space(int(number_of_elements / (2 ** (counter + 1))), removed)
            else:
                self.print_space(int(number_of_elements / (2 ** counter)), removed)
            if removed is None:
                temp.append(None)
                temp.append(None)
            else:
                temp.append(removed.left)
                temp.append(removed.right)
            if len(tree_level) == 0:
                print("\n",end='')
                tree_level = temp
                temp = []
                counter += 1

def burnTreeUtil(node, target, q):
    if node is None:
        return 0
    if node.data == target:
        print(node.data)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        return 1
    a = burnTreeUtil(node.left, target, q)
    if a == 1:
        q_size = len(q)
        while q_size:
            temp = q[0]
            print(temp.data, end=' ')
            q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            q_size -= 1
        if node.right is not None:
            q.append(node.right)
        print(node.data)
        return 1
    b = burnTreeUtil(node.right, target, q)
    if b == 1:
        q_size = len(q)
        while q_size:
            temp = q[0]
            print(temp.data, end=' ')
            q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            q_size -= 1
        if node.left is not None:
            q.append(node.left)
        print(node.data)
        return 1
def burnTree(root, target):
    q = []
    burnTreeUtil(root, target, q)
    while q:
        q_size = len(q)
        while q_size:
            temp = q[0]
            print(temp.data, end='')
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            if len(q) != 1:
                print(' ',end = '')
            q.pop(0)
            q_size -= 1
        print()

myTree = AVL_Tree()
root = None

data, target = input("Enter node and burn node : ").split('/')
for e in data.split():
    root = myTree.insert(root, e)
myTree.printTree()
if target not in data:
    print(f"There is no {target} in the tree.")
burnTree(root, int(target))