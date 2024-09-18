class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object): 
    #code here
    class AVLNode:

        def __init__(self, data, left=None, right=None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        def __str__(self):

            return str(self.data)

        def setHeight(self):

            a = self.getHeight(self.left)

            b = self.getHeight(self.right)

            self.height = 1 + max(a, b)

            return self.height

        def getHeight(self, node):

            return -1 if node == None else node.height

        def balanceValue(self):

            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):

        self.root = None if root is None else root

    def add(self, data):

        # code here
        self.root = self._add(self.root, data)

    def _add(self, root, data):

        # code here
        if root is None:
            return AVL_Tree.AVLNode(data)

        if int(data) < int(root.data):
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

        root = self._balance(root)
        return root

    def _balance(self, root):
        if root.balanceValue() > 1:
            print('Not Balance, Rebalance!')
            if root.right and root.right.balanceValue() < 0:
                root.right = self.rotateRightChild(root.right)
            root = self.rotateLeftChild(root)
        elif root.balanceValue() < -1:
            print('Not Balance, Rebalance!')
            if root.left and root.left.balanceValue() > 0:
                root.left = self.rotateLeftChild(root.left)
            root = self.rotateRightChild(root)
        else:
            root.setHeight()
        return root

    def rotateLeftChild(self, root):

        # code here
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(self, root):

        # code here
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def postOrder(self):

        # code here
        print('AVLTree post-order : ', end='')
        result = []
        self._postOrder(self.root, result)
        print(' '.join(result))

    def _postOrder(self, root, result):

        # code here
        if root is not None:
            self._postOrder(root.left, result)
            self._postOrder(root.right, result)
            result.append(root.data)

    def printTree(self):

        AVL_Tree._printTree(self.root)

        # print()

    def _printTree(node, level=0):

        if not node is None:

            AVL_Tree._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            AVL_Tree._printTree(node.left, level + 1)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree() 
# root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    # root = myTree.insert(root, e)
    myTree.add(e)
    # printTree90(root)
    myTree.printTree()
    print("===============")