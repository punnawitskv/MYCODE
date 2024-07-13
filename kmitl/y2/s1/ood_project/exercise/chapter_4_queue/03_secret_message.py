# จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

# รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

#     - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

#     - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

# โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

# โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

# ***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

# โดยรูปแบบการ run ดังนี้ :

class Queue:
    def __init__(self, items):
        self.queue = list(items)
        self.queue_backup = list(items)

    def my_queue(self):
        input_list = []
        for char in self.queue_backup:
            if char != ' ':
                input_list.append(char)
        return input_list

    def enqueue(self, item):
        self.queue.append(item)
        return

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

def encodemsg(q1, q2):

    encoded_message = []

    while not q1.is_empty():
        char = q1.dequeue()
        if char != ' ':
            shift = int(q2.dequeue())
            new_char = shift_char(char, shift)
            encoded_message.append(new_char)
            q2.enqueue(shift)

    print("Encode message is : ", encoded_message)
    return


def decodemsg(q1, q2):

    decoded_message = q1.my_queue()

    print("Decode message is : ", decoded_message)
    return

def shift_char(char, shift):
    if char.isalpha():
        offset = 65 if char.isupper() else 97
        return chr((ord(char) - offset + shift) % 26 + offset)
    return char

input_str = input("Enter String and Code : ")
strings_and_number = input_str.split(',')
string, number = strings_and_number[0], strings_and_number[1]

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)