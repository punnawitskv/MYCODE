# ให้นําโปรแกรมตามข้อ 1 มาขยายความสามารถให้รองรับนักศึกษาหลายคน โดยให้ refactor ฟังก์ชัน
# add_score ให้รับพารามิเตอร์เป็น add_score(subject_score, student, subject, score) โดย student
# เป็นข้อมูลของนักศึกษาเป็น string (ในที่นี้เป็น id) และ return เป็น dictionary

# Input : subject_score = { }, student = '65010001', subject = 'python', score = 50
# return : { '65010001' : { 'python' : 50 } }

# input : subject_score = { '65010001' : { 'python' : 50 } },
# student = '65010001', subject = ‘calculus’, score = 60
# return : {'65010001': {'python’: 50, 'calculus', 60} }

# โดยหากชื่อมีข้อมูล key ใดที่มีใน dictionary อยู่แล้ว ให้ถือเป็นการ update ข้อมูลนั้น
# ให้ refactor ฟังก์ชัน calc_average_score โดยให้ส่งคืนเป็น dictionary ของนักศึกษาและคะแนนเฉลี่ย
# ของนักศึกษาคนนั้น เช่น {'65010001': '55.00' }

subject_score = {
    'math' : 0,
    'phython' : 1,
    'calculus' : 2
}

def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}

    subject_score[student][subject] = score
    return subject_score
    
def calc_average_score(subject_score):
    if not subject_score:
        return "No scores available"
    
    avr_scores = {}
    for student, scores in subject_score.items():
        total_score = sum(scores.values())
        num_subjects = len(scores)
        avr_score = total_score / num_subjects
        avr_scores[student] = f"{avr_score:.2f}"
    return avr_scores

# subject_score = {}
# subject_score = add_score(subject_score, '65010001', 'python', 50)
# print(subject_score)  # Output: {'65010001': {'python': 50}}

# subject_score = add_score(subject_score, '65010001', 'calculus', 60)
# print(subject_score)  # Output: {'65010001': {'python': 50, 'calculus': 60}}

# avr_scores = calc_average_score(subject_score)
# print("Average Scores:", avr_scores)