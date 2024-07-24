# จากการหา portal ในคราวก่อน น้องๆมอง "เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่" เป็นแค่ประโยคขู่เปล่าๆ ดังนั้นในข้อนี้จึงไม่มีข้อบังคับ แค่แลกมากับความยากนิดหน่อย ใช้ความขี้โกงของ python ให้เต็มที่ พี่ซันฟงไม่ได้ติดในฝัน ไม่มีนิยายให้อ่าน แต่รอบนี้พี่ต้องการโปรแกรมที่มีรายละเอียดดังนี้

# Input

# การเชื่อมต่อของ node แทนด้วย '>' ซึ่งแต่ละการเชื่อมต่อจะขั้นด้วย ','

# รับประกันว่าจะไม่มีการ reassign node.next

# หมายถึงจะไม่มี input แบบนี้: 1>2,1>3

# Output

# แสดงตัว node ที่ linked list เชื่อมเข้าหากัน (เรียงค่าจากน้อยไปมาก)

# แสดงค่าและขนาด (ความยาว) ของ node นั้น โดยขนาดนับเริ่มตั้งแต่ตัวมันเองจนถึงตัวสุดท้ายหรือเจอตัวซ้ำ

# หากไม่มีให้แสดงว่า "No intersection"

# หากมี intersection ให้นำ node ที่เป็น intersection ออกไป แล้วนำ linked list ที่ไม่ใช่ circular มาเรียงใส่สลับกัน

# อธิบาย test case 1

# Input: 1>2,2>3,6>7,7>3,4>5,3>4

# linked list ที่ได้จะมีลักษณะแบบนี้

#   6 → 7 ↴

# 1 → 2 → 3 → 4 → 5

# intersection คือ 3

# linked list ที่มี 3 เป็น head คือ 3 → 4 → 5

# ทำให้ขนาดมีค่าเท่ากับ 3

# จึงพิมพ์ Node(3, size=3) ออกมา

# ต่อไปนำ node 3 ออกจะได้

#   6 → 7 ↴

# 1 → 2 →   → 4 → 5

# นำ linked list มาเรียงใหม่ (เรียงด้วยค่าของ head จากน้อยไปมาก)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


user_input = input("Enter edges: ").split(',')

tail_value_collect = []
tail_node_collect = []
head_value_collect = []
head_node_collect = []

for linked_value in user_input:
    head_value, tail_value = linked_value.split('>')

    if head_value in (tail_value_collect):
        for tail_node in (tail_node_collect):
            if tail_node.value == head_value:
                new_node = Node(tail_value)
                tail_node.next = new_node
                new_node.previous = tail_node

                tail_node_collect.append(new_node)
                tail_node_collect.remove(tail_node)
                # tail_value_collect.remove(tail_value)
                tail_value_collect.append(tail_value)

    elif tail_value in (head_value_collect):
        for head_node in (head_node_collect):
            if head_node.value == tail_value:
                new_node = Node(head_value)
                head_node.previos = new_node
                new_node.next = head_node

                head_node_collect.append(new_node)
                head_node_collect.remove(head_node)
                # head_value_collect.remove(head_value)
                head_value_collect.append(head_value)

    else:
        new_head_node = Node(head_value)
        head_node_collect.append(new_head_node)
        head_value_collect.append(head_value)

        new_tail_node = Node(tail_value)
        tail_node_collect.append(new_tail_node)
        tail_value_collect.append(tail_value)

        new_head_node.next = new_tail_node  
        new_tail_node.previous = new_head_node

for head_node in (head_node_collect):
    if head_node.previous is None:
        while head_node:
            print(head_node.value, end=' -> ')
            head_node = head_node.next