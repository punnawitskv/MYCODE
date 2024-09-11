class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.data = val
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return str(self.data)

    def __init__(self, root=None) -> None:
        self.root = root

    def search_subtree(self, root, data) -> BSTNode:
        data = int(data)
        if root.data == data:
            return root
        if data < root.data:
            return self.search_subtree(root.left, data)
        else:
            return self.search_subtree(root.right, data)

    def insert(self, root, data):
        data = int(data)
        if not root:
            return BST.BSTNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def delete_subtree(self, root, data):
        data = int(data)
        if root.data == data:
            return None
        if data < root.data:
            root.left = self.delete_subtree(root.left, data)
        else:
            root.right = self.delete_subtree(root.right, data)
        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.data = val
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def setHeight(self):
            a = AVLTree.AVLNode.getHeight(self.left)
            b = AVLTree.AVLNode.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(node):
            return  -1 if node == None else node.height

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, root, data):
        data = int(data)
        if not root:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.setHeight()
        return AVLTree._rebalance(root)

    def left_rotate(self, node: AVLNode):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def right_rotate(self, node: AVLNode):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def get_height(self, root: AVLNode):
        return root.height

    def get_balance(self, root: AVLNode):
        return AVLTree.AVLNode.getHeight(root.left) - AVLTree.AVLNode.getHeight(root.right)

    def _rebalance(node: AVLNode):
        balance = AVLTree.get_balance(AVLTree, node)
        if balance == -2:
            if AVLTree.get_balance(AVLTree, node.right) == 1:
                node.right = AVLTree.left_rotate(AVLTree, node.right)
            node = AVLTree.right_rotate(AVLTree, node)
        elif balance == 2:
            if AVLTree.get_balance(AVLTree, node.left) == -1:
                node.left = AVLTree.right_rotate(AVLTree, node.left)
            node = AVLTree.left_rotate(AVLTree, node)
        return node

    def bst_to_avl(self, bst_root):
        sorted_values = self.inorder_traversal(bst_root)
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right))

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)

inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))

print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)