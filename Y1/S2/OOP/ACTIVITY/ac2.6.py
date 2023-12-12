def add2list(lst1, lst2):
    # ใช้ list comprehension ในการสร้าง list ที่เป็นผลบวกของ lst1 และ lst2
    result = [x + y for x, y in zip(lst1, lst2)]
    return result

# ตัวอย่างการใช้งาน
x = [1, 2, 3]
y = [4, 5, 6]

result_list = add2list(x, y)
print(result_list)