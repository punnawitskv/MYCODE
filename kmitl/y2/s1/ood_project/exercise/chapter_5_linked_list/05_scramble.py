# เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

# ***** รูปแบบ input *****

# แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

# 1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน

# 2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

# ***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****

# ***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    # Code Here
    if not LL:
        return None
    head = Node(LL[0])
    current = head
    for value in LL[1:]:
        current.next = Node(value)
        current = current.next
    return head

def printLL(head):
    # Code Here
    if head is None:
        return "Empty"
    result = []
    current = head
    while current:
        result.append(str(current.value))
        current = current.next
    return " ".join(result)

def SIZE(head):
    # Code Here
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def scramble(head, b, r, size):
    # Code Here
    head1 = bottom_up(head, b, size)
    print(f"BottomUp {b:.3f} % : {printLL(head1)}")
    head2 = riffle(head1, r, size)
    print(f"Riffle {r:.3f} % : {printLL(head2)}")
    return head1, head2

def splitLL(head, size):
    if size == 0 or head is None:
        return None, None
    current = head
    prev = None
    for _ in range(size):
        prev = current
        current = current.next
    if prev:
        prev.next = None
    return head, current

def bottom_up(head, percent, size):
    if head is None or size == 0:
        return head
    split_point = int(size * percent / 100)
    if split_point == 0 or split_point == size:
        return head
    first_part, last_part = splitLL(head, split_point)
    if not last_part:
        return first_part
    new_head = last_part
    current = last_part
    while current.next:
        current = current.next
    current.next = first_part
    return new_head

def riffle(head, percent, size):
    if head is None or size == 0:
        return head
    riffle_point = int(size * percent / 100)
    if riffle_point == 0 or riffle_point == size:
        return head
    first_part, last_part = splitLL(head, riffle_point)
    dummy = Node(0)
    current = dummy
    while first_part and last_part:
        current.next = first_part
        first_part = first_part.next
        current = current.next
        current.next = last_part
        last_part = last_part.next
        current = current.next
    current.next = first_part if first_part else last_part
    return dummy.next

inp1, inp2 = input("Enter Input : ").split("/")
print('-' * 50)
for i in inp2.split('|'):
    h = createLL(inp1.split())
    h1 = createLL(inp1.split())
    h2 = createLL(inp1.split())
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == 'B' and k[1][0] == 'R':
        h_bottom, h_riffle = scramble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
        print(f"Deriffle {float(k[1][2:]):.3f} % : {printLL(bottom_up(h2, float(k[0][2:]), SIZE(h2)))}")
        print(f"Debottomup {float(k[0][2:]):.3f} % : {printLL(h1)}")
    elif k[0][0] == 'R' and k[1][0] == 'B':
        h_bottom, h_riffle = scramble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
        print(f"Deriffle {float(k[0][2:]):.3f} % : {printLL(bottom_up(h2, float(k[1][2:]), SIZE(h2)))}")
        print(f"Debottomup {float(k[1][2:]):.3f} % : {printLL(h1)}")
    print('-'*50)