class Student:
    def __init__(self, stu_id, stu_name):
        self.__stu_id = stu_id
        self.__stu_name = stu_name

    def get_id(self):
        return self.__stu_id
    
    def get_name(self):
        return self.__stu_name
    
    def set_id(self, id):
        if type(id) == int:
            self.__stu_id = int(id)
            return True
        else:
            return False
        
    def set_name(self, name):
        if type(name) == str:
            self.__stu_name = str(name)
            return True
        else:
            return False


class Subject:
    def __init__(self, sub_id, sub_name, section, credit):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.section = section
        self.credit = credit
        self.students_list = []

    def enroll_teacher(self, teacher):
        teacher.subjects_taught_list.append(self)

    def enroll_student(self, student):
        if student not in self.students_list:
            self.students_list.append(student)
            student.enroll_subject(self)


class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.subjects_taught_list = []

students = [
    Student('001', 'John'),
    Student('002', 'Peter'),
    Student('003', 'Katy*'),
    Student('004', 'Linda'),
    Student('005', 'Alice'),
    Student('006', 'Po')
]

teachers = [
    Teacher('101', 'Wilson'),
    Teacher('102', 'Cherry'),
    Teacher('103', 'Shifu'),
    Teacher('104', 'Oogway')
]

subjects = [
    Subject('011', 'OOP 1', 'Section 1', 3),
    Subject('012', 'OOP 2', 'Section 2', 3),
    Subject('021', 'Kungfu 1', 'Section 1', 10),
    Subject('022', 'Kungfu 2', 'Section 2', 10)
]

# Enroll teacher
subjects[0].enroll_teacher(teachers[0])
subjects[1].enroll_teacher(teachers[1])
subjects[2].enroll_teacher(teachers[2])
subjects[3].enroll_teacher(teachers[3])

# Enroll student
subjects[0].enroll_student(students[0]) #sec1
subjects[0].enroll_student(students[1])
subjects[0].enroll_student(students[2])
subjects[1].enroll_student(students[2]) #sec2
subjects[1].enroll_student(students[3])
subjects[1].enroll_student(students[4])
subjects[2].enroll_student(students[5]) #sec1
subjects[3].enroll_student(students[5])


def find_students_by_teacher(teacher_id):
    new_students_list = []
    for teacher in teachers:
        if teacher.teacher_id == teacher_id:
            for subject_taught in teacher.subjects_taught_list:
                for student in subject_taught.students_list:
                    new_students_list.append(student.stu_name)
                # new_students_list.extend(student.stu_name for student in subject_taught.students_list)
    return new_students_list


def find_subjects_by_student(student_id):
    new_subjects_list = []
    for student in students:
        if student.stu_id == student_id:
            for subject in student.subjects_list:
                new_subjects_list.append(subject.sub_name)
            # new_subjects_list.extend(subject.sub_name for subject in student.subjects_list)
    return new_subjects_list


teacher_id = input("Input teacher ID (101, 102, 103, 104): ")
teacher_students = find_students_by_teacher(teacher_id)
print(f"Teacher teaches the following students: {teacher_students}")


student_id = input("Input student ID (001, 002, 003, 004, 005, 006): ")
student_subjects = find_subjects_by_student(student_id)
print(f"Student is enrolled in the following subjects: {student_subjects}")