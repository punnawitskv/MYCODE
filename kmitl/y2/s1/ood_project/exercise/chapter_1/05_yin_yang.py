def draw_yin_yang(size):
    # สร้างหยิน-หยางที่ว่างเปล่า
    yin_yang = [['.' for _ in range(size * 2 + 3)] for _ in range(size * 2 + 3)]

    # วาดรูปหยิน (ด้านซ้ายของรูป)
    for i in range(size):
        yin_yang[i][size] = '#'
        yin_yang[i][size * 2 + 2 - i] = '+'

    # วาดรูปหยาง (ด้านขวาของรูป)
    for i in range(size):
        yin_yang[size + 2 + i][size] = '#'
        yin_yang[size + 2 + i][size + i + 1] = '+'

    # แปลง list เป็น string และประกาศผลลัพธ์
    for row in yin_yang:
        print(''.join(row))

# รับ input จากผู้ใช้และเรียกใช้งานฟังก์ชัน
while True:
    try:
        size = int(input("Enter Input: "))
        if size <= 0:
            print("Size must be a positive integer.")
        else:
            draw_yin_yang(size)
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
