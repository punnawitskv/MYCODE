def count_minus(input_str):
    # ใช้ List comprehension เพื่อดึงจำนวนที่เป็นลบ
    negative_numbers = [int(num) for num in input_str.split() if int(num) < 0]
    
    # คืนค่าจำนวนที่เป็นลบทั้งหมด
    return len(negative_numbers)

# รับข้อมูลจากผู้ใช้
user_input = input("Enter numbers separated by space: ")

# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
result = count_minus(user_input)
print("The number of negative numbers is:", result)
