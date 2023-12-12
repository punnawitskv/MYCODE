def is_leap(year):
    """
    ตรวจสอบว่าปีที่กำหนดเป็น Leap Year หรือไม่
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def day_of_year(day, month, year):
    """
    คืนค่าวันที่ลำดับที่เท่าใดของปีคริสตศักราช year
    """
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # เพิ่ม 1 วันสำหรับ Leap Year
    if is_leap(year):
        days_in_month[2] = 29

    # ตรวจสอบความถูกต้องของวันและเดือน
    if month < 1 or month > 12 or day < 1 or day > days_in_month[month]:
        return "Invalid date"

    # คำนวณ day_of_year
    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year

# ตัวอย่างการใช้งาน
day_result = day_of_year(15, 3, 2023)
print(f"The day of the year is: {day_result}")
