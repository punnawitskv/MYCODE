# PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

# เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

# Input :
# EN <value>  เป็นโอตะธรรมดา  id = value
# ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
# D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty

queue = []
queue_with_rank = []
user_input = input("Enter Input : ").split(',')

for input in user_input:
    if input[:2] == 'EN':
        queue.append(input[3:])
        queue_with_rank.append(input)
    elif input[:2] == 'ES':
        inserted = False
        for num_index, queued in enumerate(queue_with_rank):
            if queued[:2] == 'EN':
                queue.insert(num_index, input[3:])
                queue_with_rank.insert(num_index, input)
                inserted = True
                break
        if not inserted:
            queue.append(input[3:])
            queue_with_rank.append(input)
    elif input[0] == 'D':
        if queue:
            output = queue.pop(0)
            queue_with_rank.pop(0)
            print(output)
        else:
            print("Empty")
