class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
            self.parent = None  

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
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        if int(data) < int(root.data):
            root.left = self._add(root.left, data)
            if root.left:
                root.left.parent = root
        else:
            root.right = self._add(root.right, data)
            if root.right:
                root.right.parent = root    

        root = self._balance(root)
        return root

    def _balance(self, root):
        if root.balanceValue() > 1:
            if root.right and root.right.balanceValue() < 0:
                root.right = self.rotateRightChild(root.right)
            root = self.rotateLeftChild(root)
        elif root.balanceValue() < -1:
            if root.left and root.left.balanceValue() > 0:
                root.left = self.rotateLeftChild(root.left)
            root = self.rotateRightChild(root)
        else:
            root.setHeight()
        return root

    def rotateLeftChild(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def postOrder(self):
        print('AVLTree post-order : ', end='')
        result = []
        self._postOrder(self.root, result)
        print(' '.join(result))

    def _postOrder(self, root, result):
        if root is not None:
            self._postOrder(root.left, result)
            self._postOrder(root.right, result)
            result.append(root.data)

    def bfs(self):
            if not self.root:
                return []

            res = []
            queue = [(self.root, 0)]

            while queue:
                node, level = queue.pop(0)
                if level == len(res):
                    res.append([])
                if node:
                    res[level].append(node.data)
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                else:
                    res[level].append(None)

            return res

    def printTree(self):
        if not self.root:
            print("Tree is empty.")
            return

        treeArray = self.bfs()
        h = len(treeArray)
        
        width = 2**h - 1
        current_level = 0

        def printSpaces(n):
            return " " * n

        for level in treeArray:
            if not level:
                continue
            # Calculate the amount of space between nodes
            level_width = width // (2 ** current_level)
            line = ""
            for i, x in enumerate(level):
                if x is None:
                    line += printSpaces(level_width) + " "
                else:
                    line += printSpaces(level_width - len(str(x)) // 2) + str(x) + printSpaces(level_width - len(str(x)) // 2)
                line += printSpaces(level_width)  # Space between nodes
            print(line.rstrip())
            current_level += 1

    def find_node(self, root, data):
        if root is None:
            return None
        if root.data == data:
            return root
        elif data < root.data:
            return self.find_node(root.left, data)
        else:
            return self.find_node(root.right, data)

    def spread_fire(self, start_data):
        start_node = self.find_node(self.root, start_data)
        if start_node is None:
            print("Start node not found.")
            return

        burnt = set()
        fire_queue = [start_node]
        minute = 0

        while fire_queue:
            current_level = []
            next_fire_queue = []

            for node in fire_queue:
                if node.data not in burnt:
                    burnt.add(node.data)
                    current_level.append(node.data)

                    if node.left and node.left.data not in burnt:
                        next_fire_queue.append(node.left)

                    if node.right and node.right.data not in burnt:
                        next_fire_queue.append(node.right)

                    if node.parent and node.parent.data not in burnt:
                        next_fire_queue.append(node.parent)

            print(f"{' '.join(map(str, current_level))}")
            fire_queue = next_fire_queue
            minute += 1


avl1 = AVLTree()

inp = input('Enter node and burn node : ').split('/')
node = inp[0].split(' ')
first_burn = inp[1]

for i in node:
        avl1.add(i)

avl1.printTree()

avl1.spread_fire(first_burn)