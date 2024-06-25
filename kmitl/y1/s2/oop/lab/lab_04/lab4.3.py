class Student:
    def __init__(self, stu_id, stu_name):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.mentors_list = []

    def add_mentor(self, mentor):
        self.mentors_list.append(mentor)


def find_student_from_id(stu_id_input):
    for student in students:
        if student.stu_id == stu_id_input:
            return student
    return None


def check_mentor(student_input):
    mentors = []
    for mentor in student_input.mentors_list:
        mentors.append(mentor)
        mentors.extend(check_mentor(mentor))
    return mentors


def mentors_list_of_this_student(mentors):
    if not mentors:
        print('Not found')
        return
    for mentor in mentors:
        print(mentor.stu_id, mentor.stu_name, sep='\t')


def find_mentors_from_student_id(stu_id_input):
    student = find_student_from_id(stu_id_input)
    if student:
        student_mentors_list = check_mentor(student)
        mentors_list_of_this_student(student_mentors_list)
    else:
        print(f"Student {stu_id_input} is not found")
        
        
def is_mentor(stu_idX, stu_idY):
    senior_id = max(stu_idX, stu_idY)
    junior_id = min(stu_idX, stu_idY)

    junior_student = find_student_from_id(junior_id)

    if junior_student:
        mentors = check_mentor(junior_student)

        for mentor in mentors:
            if mentor.stu_id == senior_id:
                return True
    return False


students = [
    Student('011', 'Annie'),  # Y1
    Student('012', 'Bard'),
    Student('021', 'Caitlyn'),  # Y2
    Student('022', 'Diana'),
    Student('031', 'Elder Dragon'),  # Y3
    Student('032', 'Fizz'),
    Student('041', 'Garen'),  # Y4
    Student('042', 'Heimerdinger'),
]


students[0].add_mentor(students[2])  #
students[1].add_mentor(students[3])
students[2].add_mentor(students[4])  #
students[3].add_mentor(students[5])
students[4].add_mentor(students[6])  #
students[5].add_mentor(students[7])


print("\nStudents List : 011, 012, 021, 022, 031, 032, 041, 042")
student_id_input = input("Enter student id : ")
if find_student_from_id(student_id_input):
    student = find_student_from_id(student_id_input)
    if student is not None:
        print(f"Mentors bond of {student.stu_name}({student_id_input}) is")
    find_mentors_from_student_id(student_id_input)
else:
    print(f"Student {student_id_input} is not found")

print("\nStudents List : 011, 012, 021, 022, 031, 032, 041, 042")
student_id_X = input("Enter student id.X : ")
student_id_Y = input("Enter student id.Y : ")
mentor_check = is_mentor(student_id_X, student_id_Y)

student_name_X = "StuX"
student_name_Y = "StuY"

student_temp = find_student_from_id(student_id_X)
if student_temp is not None:
    student_name_X = student_temp.stu_name
student_temp = find_student_from_id(student_id_Y)
if student_temp is not None:
    student_name_Y = student_temp.stu_name
    
print(f"Mentor resault of {student_name_X}({student_id_X}) and {student_name_Y}({student_id_Y}) : ", end = '')
if mentor_check:
    print("True")
else:
    print("False")