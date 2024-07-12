
# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

# D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

queue = []
user_input = input("Enter Input : ").split(',')

for input in user_input:
    if input[0] == 'E':
        queue.append(int(input[2:]))
        print(len(queue))
    
    elif input[0] == 'D':
        if queue:
            output = queue.pop(0)
            print(f"{output} 0")
        else:
            print("-1")

if queue == []:
    print("Empty")
else:
    for num in queue:
        print(num, end=" ")