# เขียนฟังก์ชัน add_score(subject_score, subject, score) โดยมีพารามิเตอร์ 3 ตัว ได้แก่ subject_score
# เป็น dictionary ที่มีคู่ key : value เป็น subject : score พารามิเตอร์ตัวที่ 2 และ 3 เป็น subject และ
# score โดย subject เป็น string และ score เป็น integer โดยให้นํา subject และ score ไปเพิ่มใน
# dictionary เช่น

# Input : subject_score = { }, subject = ‘python’, score = 50
# return : { ‘python’ : 50 }
# input : subject_score = { ‘python’ : 50 }, subject = ‘calculus’, score = 60
# return : { ‘python’ : 50, ‘calculus : 60 }

# จากนั้นให้เขียนฟังก์ชัน calc_average_score หาค่าเฉลี่ยของคะแนนในทุกรายวิชาใน dictionary ที่ได้จาก
# ฟังก์ชัน add_score โดยให้ส่งค่าคืนมาเป็น string ที่มีทศนิยม 2 ตําแหน่ง

subject_score = {
    'math' : 0,
    'phython' : 1,
    'calculus' : 2
}

def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score
    
def calc_average_score(subject_score):
    if not subject_score:
        return "No scores available"
    
    total_score = sum(subject_score.values())
    num_subject = len(subject_score)
    avr_score = total_score / num_subject
    return f"{avr_score:.2f}"

# subject_score = {}
# subject_score = add_score(subject_score, 'python', 50)
# print(subject_score)  # Output: {'python': 50}

# subject_score = add_score(subject_score, 'calculus', 60)
# print(subject_score)  # Output: {'python': 50, 'calculus': 60}

# average = calc_average_score(subject_score)
# print("Average Score:", average)