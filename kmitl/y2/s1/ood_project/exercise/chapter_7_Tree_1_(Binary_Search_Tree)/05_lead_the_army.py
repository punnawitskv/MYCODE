# เมือง A มีการวางผังเมืองคล้ายกับ Binary Search Tree โดยมีเมืองหลวง/ศูนย์กลางคือ root และหัวเมืองอื่นๆคือ node ต่างๆที่ขึ้นตรงกันเป็นทอดๆไปยัง

# ศูนย์กลาง ในข้อนี้นักศึกษาจะได้รับบทเป็นขุนพลแห่งเมือง B เพื่อนำทัพไปบุกเมือง A โดยจะต้องโจมตีตั้งแต่หัวเมืองที่อยู่นอกสุด(เริ่มจากซ้าย-ไป-ขวา) 
# ไปถึงยังศูนย์กลาง และหากเมืองหลวง A ถูกทำลายได้จะถือว่าขุนพลแห่งเมือง B นำทัพชนะในครั้งนี้ได้


# เมือง A:

# รับตัวเลขจาก input เพื่อสร้างกำลังในหัวเมืองต่างๆ ซึ่งจะถือว่าตัวเลขที่รับเข้ามาจะเเทน nodeๆ นึง (ตัวเลขตัวแรกจะถือเป็นกำลังของเมืองหลวง), 
# (กำลังพลจะเป็นตัวเลขจำนวนเต็มเท่านั้น)

# ตัวเลขแต่ละตัวใน BST จะเเทนกำลังทั้งหมดที่เมืองนั้นๆมีต่อมาในตามลำดับ

# เมื่อแต่ละหัวเมืองจะถูกโจมตี พระราชาแห่งเมือง A ได้สั่งให้กำลังทั้งหมดของแต่ละเมืองที่มีเส้นทางไปถึงยังหัวเมืองนั้นๆ ไปรวมกำลังเพื่อช่วยป้องกันหัวเมืองนั้นๆไว้

# หน้าที่ของขุนพลเมือง B:

# รับ input เพื่อที่จะกำนดกำลังพลฝ่ายของตน ซึ่งเนื่องจากพลเมืองที่ร่วมรบนั้นมีจำนวนที่จำกัด ทำให้ขุนพลต้องแบ่งพลเมืองในการต่อสู่ศึกครั้งนี้ 
# อีกทั้งยังไม่สามารถตีเมืองทั้งหมดได้ในรอบเดียว จึงต้องแบ่งเป็นรอบๆในการตีอีกด้วย โดยในการตีแต่ละรอบจะถูกกำหนดตามเงื่อนไขที่ขุนพลสั่ง 
# โดยเงื่อนไขที่ขุนพลสั่งได้จะมีดังนี้ (k = จำนวนพลเมืองที่ต้องมี), (กำลังพลจะเป็นตัวเลขจำนวนเต็มเท่านั้น)

# 1. รวมกำลังพลเมือง ให้มากกว่า k และไปร่วมรบ : M

# 2. รวมกำลังพลเมือง ให้น้อยกว่า k และไปร่วมรบ : L

# 3. รวมกำลังพลเมือง ให้เท่ากับ k และไปร่วมรบ : EQ

# โดยที่ขุนพลไม่สนใจว่ากำลังในแต่หัวเมือง A นั้นมีเท่าไหร่ คิดแค่ว่าส่งไปเป็นเงื่อนไขแบบนี้คงจะชนะ


# การทำลายแต่ละหัวเมือง A:

# หากหัวเมืองที่จะถูกโจมตีรวมกำลังแล้ว ยังแพ้ให้กับเงื่อนไขกองทัพของทัพ B จะถือว่าเมืองนั้นถูกทำลาย และจะต้องแสดงเส้นทางของกำลังพล 
# และผลลัพธ์รวมของหัวเมืองที่ถูกทำลายนั้นทาง output ด้วย และเมื่อตีเมืองใดเมืองนึงสำเร็จจะกองทัพกองนั้นจะรุกตีเมืองอื่นต่อทันที 
# จนกว่าจะเจอเมืองที่กองทัพนั้นสู้ไม่ไหวตามเงื่อนไขที่กำหนดมา

# หากทัพ B ตีไม่ชนะ(ไม่ตรงกับเงื่อนไขของขุนพล B) จะถือว่าตีเมืองนั้นไม่สำเร็จ และจะไม่แสดงอะไรออกมาที่ output

# หากทัพโค่นเมืองหลวง A ได้จะแสดงประโยคว่า “City A has fallen!” และจะจบการรบทันที แม้ว่าขุนพลจะส่งกองทัพมาเพิ่มก็ตาม


# ตัวอย่าง

# Input :

# Enter <Create City A (BST)>/<Create conditions and deploy the army>:

# 100 70 200 34 80 300/L 250,EQ 250,M 250

# อธิบาย input:

# 100 70 200 34 80 300 : นำเลขเหล่านี้ไปสร้างเป็นเมือง A ตามหลักของ Binary Search Tree (100 = root)

# L 250,EQ 250,M 250 : การกำหนดเงื่อนไข(L, EQ, M) พร้อมกับกำลังพลของทัพ B(250, 250, 250 ตามลำดับ)



# Output :

# (City A) Before the war:

#        		300

#   	200

#  100

#        		80

#   	70

#        		34

# >> ผลลัพธ์จากการสร้างเมือง A ตามหลัก Binary Search Tree

# --------------------------------------------------

# Removing paths where the sum is less than 250:

# 1) 100->70->34 = 204

# --------------------------------------------------

# (City A) After the war:

#        		300

#   	200

#  100

#        		80

#   	70

# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลน้อยกว่า 250 ทำให้เมือง 34 ที่มีกำลังผลรวมได้ 204 แตกไปในที่สุด

# --------------------------------------------------

# Removing paths where the sum is equal to 250:

# 1) 100->70->80 = 250

# --------------------------------------------------

# (City A) After the war:

#        		300

#   	200

#  100

#   	70

# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลเท่ากับ 250 ทำให้เมือง 80 ที่มีกำลังผลรวมได้ 250 แตกไปในที่สุด

# --------------------------------------------------

# Removing paths where the sum is greater than 250:

# 1) 100->200->300 = 600

# 2) 100->200 = 300

# --------------------------------------------------

# (City A) After the war:

#  100

#   	70

# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลมากกว่า 250 ทำให้เมือง 300 และ 200 ที่มีกำลังผลรวมได้ 600 และ 300 ตามลำดับแตกไปในที่สุด

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
    
    def print_tree(self, node, level = 0):
        if node:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)
        else:
            print('City A has fallen!')

    def find_leaf_nodes(self, root):
        leaves = []
        
        def dfs(node:Node): # Depth-First Search
            if node:
                if node.left is None and node.right is None:
                    leaves.append(node)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return leaves
    
    def find_parent(self, root, data):
        if root is None:
            return None
        if (root.left and root.left.data == data) or (root.right and root.right.data == data):
            return root
        elif data < root.data:
            return self.find_parent(root.left, data)
        else:
            return self.find_parent(root.right, data)
    
    def find_path_to_root(self, root, target):
        path = []
        
        def dfs(node):
            if node is None:
                return False
            path.append(node.data)
            if node.data == target.data:
                return True
            if dfs(node.left) or dfs(node.right):
                return True
            path.pop()
            return False
        
        dfs(root)
        return path
    
    def attack_loop_L(self, leaf_nodes, root, forces, num=1):
        for node in leaf_nodes:
            path = self.find_path_to_root(root, node)
            if sum(path) < forces:
                if path:
                    print(f'{num})', end=' ')
                    path_str = "->".join(map(str, path))
                    print(f"{path_str} = {sum(path)}")

                    self.delete(root, node.data)
                    leaf_nodes = self.find_leaf_nodes(root)

                    self.attack_loop_L(leaf_nodes, root, forces, num+1)
                else:
                    print("Node not found")

    def attack_loop_EQ(self, leaf_nodes, root, forces, num=1):
        for node in leaf_nodes:
            path = self.find_path_to_root(root, node)
            if sum(path) == forces:
                if path:
                    print(f'{num})', end=' ')
                    path_str = "->".join(map(str, path))
                    print(f"{path_str} = {sum(path)}")

                    self.delete(root, node.data)
                    leaf_nodes = self.find_leaf_nodes(root)

                    self.attack_loop_EQ(leaf_nodes, root, forces, num+1)
                else:
                    print("Node not found")

    def attack_loop_M(self, leaf_nodes, root, forces, num=1):
        for node in leaf_nodes:
            path = self.find_path_to_root(root, node)
            if sum(path) > forces:
                if path:
                    print(f'{num})', end=' ')
                    path_str = "->".join(map(str, path))
                    print(f"{path_str} = {sum(path)}")

                    self.delete(root, node.data)
                    leaf_nodes = self.find_leaf_nodes(root)

                    self.attack_loop_M(leaf_nodes, root, forces, num+1)
                else:
                    print("Node not found")

    def attack(self, signal, forces, root):
        leaf_nodes = self.find_leaf_nodes(root)

        if signal == 'L':
            print('--------------------------------------------------')
            print(f'Removing paths where the sum is less than {forces}:')
            self.attack_loop_L(leaf_nodes, root, forces)
            print('--------------------------------------------------')
            print('(City A) After the war:')
            self.print_tree(root)
            
        if signal == 'E':
            print('--------------------------------------------------')
            print(f'Removing paths where the sum is equal to {forces}:')
            self.attack_loop_EQ(leaf_nodes, root, forces)
            print('--------------------------------------------------')
            print('(City A) After the war:')
            self.print_tree(root)

        if signal == 'M':
            print('--------------------------------------------------')
            print(f'Removing paths where the sum is greater than {forces}:')
            self.attack_loop_M(leaf_nodes, root, forces)
            print('--------------------------------------------------')
            print('(City A) After the war:')
            self.print_tree(root)

tree = BinarySearchTree()
data = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split("/")

a_city_inp = data[0].split(" ")
b_army_inp = data[1].split(",")

# create city A
for forces in a_city_inp:
    root = tree.insert(int(forces))
print("(City A) Before the war:")
tree.print_tree(root)

# army B attacking
for order in b_army_inp:
    tree.attack(order[0], int(order[2:]), root)