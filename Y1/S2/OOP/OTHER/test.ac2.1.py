# รับข้อมูลจากผู้ใช้
input_str = input("ป้อนตัวเลขหลายตัว (คั่นด้วยช่องว่าง): ")

# แยกตัวเลขที่ป้อนเข้ามาและแปลงเป็นรายการ (list)
numbers = [int(num) for num in input_str.split()]

# เรียงลำดับเลขจากน้อยไปมาก
sorted_numbers = sorted(numbers)

# ถ้าตัวที่น้อยสุดเป็น 0 ให้สลับกับเลขในลำดับถัดไป
if sorted_numbers[0] == 0:
    sorted_numbers[0], sorted_numbers[1] = sorted_numbers[1], sorted_numbers[0]

# ใช้ join เพื่อเชื่อมตัวเลขเป็นสตริง
result_str = ''.join(map(str, sorted_numbers))

# แสดงผลลัพธ์
print("เลขที่เรียงลำดับจากน้อยไปมาก: ", result_str)
