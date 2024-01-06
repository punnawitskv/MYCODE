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
    print("Student not found")
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


students = [
    Student('011', 'Annie'),  # Y1
    Student('012', 'Bard'),
    Student('021', 'Caitlyn'),  # Y2
    Student('022', 'Diana'),
    Student('031', 'Elder Dragon'),  # Y3
    Student('032', 'Fizz'),
    Student('041', 'Garen'),  # Y4
    Student('042', 'Heimerdinger')
]

students[0].add_mentor(students[2])  #
students[1].add_mentor(students[3])
students[2].add_mentor(students[4])  #
students[3].add_mentor(students[5])
students[4].add_mentor(students[6])  #
students[5].add_mentor(students[7])

student_id_input = input("Enter student id : ")
print(f"Mentors bond of {find_student_from_id(student_id_input).stu_name} is")
find_mentors_from_student_id(student_id_input)
