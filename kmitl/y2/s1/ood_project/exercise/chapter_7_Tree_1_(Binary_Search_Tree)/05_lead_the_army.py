class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        if root is None:
            self.root = None
        else:
            self.root = Node(root)

    def __traverse(self, node, data):
        if node is None:
            return
        self.__traverse(node.left, data)
        data.append(node.value)
        self.__traverse(node.right, data)

    def __iter__(self):
        data = []
        self.__traverse(self.root, data)
        for d in data:
            yield d

    def insert(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            self.root = Node(value)
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            self.insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            self.insert(value, node.right)

    def __get_father(self, node, value):
        if node is None:
            return None
        if node.left and node.left.value == value:
            return node
        if node.right and node.right.value == value:
            return node
        left = self.__get_father(node.left, value)
        right = self.__get_father(node.right, value)
        if left is not None:
            return left
        return right

    def get_father(self, value):
        return self.__get_father(self.root, value)

    def __get_father_node(self, node, node_to_find):
        if node is None:
            return None
        if node.left and node.left == node_to_find:
            return node
        if node.right and node.right == node_to_find:
            return node
        left = self.__get_father_node(node.left, node_to_find)
        right = self.__get_father_node(node.right, node_to_find)
        if left is not None:
            return left
        return right

    def get_father_node(self, node):
        return self.__get_father_node(self.root, node)

    def __find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left = self.__find(node.left, value)
        right = self.__find(node.right, value)
        if left is not None:
            return left
        return right

    def find(self, value):
        return self.__find(self.root, value)

    def delete_node(self, node):
        if node is None:
            return False
        if node.left is not None and node.right is not None:
            next_node_find_val = node.value
            next_node = None
            while next_node is None:
                next_node_find_val += 1
                next_node = self.find(next_node_find_val)
            new_value = next_node.value
            self.delete(new_value)
            node.value = new_value
            return True
        father = self.get_father_node(node)
        if father is None:
            if node.left is not None:
                self.root = node.left
                return True
            if node.right is not None:
                self.root = node.right
                return True
            self.root = None
            return True
        if node.left is None and node.right is None:
            if father.left == node:
                father.left = None
            if father.right == node:
                father.right = None
            return True
        if node.left is not None:
            if father.left == node:
                father.left = node.left
            if father.right == node:
                father.right = node.left
            return True
        if node.right is not None:
            if father.left == node:
                father.left = node.right
            if father.right == node:
                father.right = node.right
            return True

    def delete(self, value):
        node = self.find(value)
        return self.delete_node(node)

    def __height(self, node):
        if node is None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def height(self):
        return self.__height(self.root)

    def __print_horizontal(self, node, level=0):
        if node is None:
            return
        self.__print_horizontal(node.right, level + 1)
        print(f' {" " * level * 5}{node.value}')
        self.__print_horizontal(node.left, level + 1)

    def __print_vertical_add_column(self, node, level, output):
        if node is None:
            return
        self.__print_vertical_add_column(node.left, level + 1, output)
        out = []
        out.extend([""] * level)
        out.append(str(node.value))
        output.append(out)
        self.__print_vertical_add_column(node.right, level + 1, output)

    def __print_vertical(self, node):
        if node is None:
            return
        output = []
        self.__print_vertical_add_column(node, 0, output)
        print(output)
        for row in range(self.height()):
            for col_data in output:
                if row < len(col_data) and col_data[row]:
                    print(f"{col_data[row]:>2}", end="")
                else:
                    print(" " * 5, end="")
            print("\n")

    def print(self, orientation="horizontal"):
        if orientation.lower() == "vertical":
            self.__print_vertical(self.root)
        else:
            self.__print_horizontal(self.root)


current_deletion_index = 0


def traverse_and_delete(tree, node, op, data, current_path="", current_sum=0):
    global current_deletion_index
    if node is None:
        return
    if node.left is not None:
        traverse_and_delete(
            tree,
            node.left,
            op,
            data,
            current_path + f"{node.value}->",
            current_sum + node.value,
        )
    if node.right is not None:
        traverse_and_delete(
            tree,
            node.right,
            op,
            data,
            current_path + f"{node.value}->",
            current_sum + node.value,
        )
    if node.left is None and node.right is None:
        branch_sum = current_sum + node.value
        if op == "L" and branch_sum < data:
            current_deletion_index += 1
            print(
                f"{current_deletion_index}) {current_path}{
                    node.value} = {branch_sum}"
            )
            tree.delete_node(node)
        elif op == "EQ" and branch_sum == data:
            current_deletion_index += 1
            print(
                f"{current_deletion_index}) {current_path}{
                    node.value} = {branch_sum}"
            )
            tree.delete_node(node)
        elif op == "M" and branch_sum > data:
            current_deletion_index += 1
            print(
                f"{current_deletion_index}) {current_path}{
                    node.value} = {branch_sum}"
            )
            tree.delete_node(node)


def main():
    global current_deletion_index
    tree = BinarySearchTree()
    city, instructions = input(
        "Enter <Create City A (BST)>/<Create conditions and deploy the army>: "
    ).split("/")
    city = city.split()
    instructions = instructions.split(",")
    for c in city:
        tree.insert(int(c))
    print("(City A) Before the war:")
    tree.print()
    for i in instructions:
        print("-" * 50)
        current_deletion_index = 0
        op, data = i.split()
        data = int(data)
        if op == "L":
            print(f"Removing paths where the sum is less than {data}:")
            traverse_and_delete(tree, tree.root, op, data)
        elif op == "EQ":
            print(f"Removing paths where the sum is equal to {data}:")
            traverse_and_delete(tree, tree.root, op, data)
        elif op == "M":
            print(f"Removing paths where the sum is greater than {data}:")
            traverse_and_delete(tree, tree.root, op, data)
        if current_deletion_index == 0:
            print("No paths were removed.")
        print("-" * 50)
        print("(City A) After the war:")
        if tree.height() == 0:
            print("City A has fallen!")
            return
        tree.print()


main()
