class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit
        self.__teacher = None
    def get_subject_name(self):
        return self.__subject_name
    def get_teacher(self):
        return self.__teacher
    def get_subject_id(self):
        return self.__subject_id
    def assign_teacher(self, teacher):
        self.__teacher = teacher
    def get_credit(self):
        return self.__credit
class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name
    def get_student_id(self):
        return self.__student_id
    def get_student_name(self):
        return self.__student_name
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name
    def get_teacher_name(self):
        return self.__teacher_name
class Enrollment:
    def __init__(self, student, subject):
        self.__student = student
        self.__subject = subject
        self.__grade = None
    def get_subject(self):
        return self.__subject
    def get_student(self):
        return self.__student
    def set_grade(self, grade):
        valid_grades = {'A', 'B', 'C', 'D', 'F'}
        if grade in valid_grades:
            if self.__grade is None:
                self.__grade = grade
                return "Done"
            else:
                return "Error"
        else:
            return "Error"

    def get_grade(self):
        return self.__grade
student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

def find_enrollment(student, subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return None
    for enrollment in enrollment_list:
        if isinstance(enrollment, Enrollment) and student == enrollment.get_student() and subject == enrollment.get_subject():
            return enrollment
    return None

# TODO 1
def search_subject_by_id(subject_id):
    return next((subject for subject in subject_list if isinstance(subject, Subject) and subject_id == subject.get_subject_id()) , None)

# TODO 2
def search_student_by_id(student_id):
    return next((student for student in student_list if isinstance(student, Student) and student_id == student.get_student_id()), None)

# TODO 3
def enroll_to_subject(student: Student, subject: Subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    enrollment = find_enrollment(student, subject)
    if not enrollment:
        enrollment_list.append(Enrollment(student, subject))
        return "Done"
    return "Already Enrolled"

# TODO 4
def drop_from_subject(student: Student, subject: Subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    enrollment = find_enrollment(student, subject)
    if enrollment and enrollment.get_subject() == subject:
        enrollment_list.remove(enrollment)
        return "Done"
    return "Not found"

# TODO 5
def search_enrollment_subject_student(subject, student):
    enrollment = find_enrollment(student, subject)
    return enrollment if enrollment and enrollment.get_subject() == subject else None

# TODO 6
def search_student_enroll_in_subject(subject):
    return [enrollment for enrollment in enrollment_list if isinstance(enrollment, Enrollment) and enrollment.get_subject() == subject]

# TODO 7
def search_subject_that_student_enrolled(student):     
    return [enrollment for enrollment in enrollment_list if isinstance(enrollment, Enrollment) and enrollment.get_student() == student]


# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    enrollment = find_enrollment(student, subject)
    return enrollment.set_grade(grade) if enrollment else "Error"
# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search : Subject):
    return subject_search.get_teacher() if subject_search in subject_list else "Not found" 

# TODO 10
def get_no_of_student_enrolled(subject):
    if not isinstance(subject, Subject):
        return "Error"
    count = sum(1 for enrollment in enrollment_list if isinstance(enrollment, Enrollment) and enrollment.get_subject() == subject)
    return count if count > 0 else "Not Found"


# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    if not isinstance(student, Student):
        return "Error"
    return {enrollment.get_subject().get_subject_id(): [enrollment.get_subject().get_subject_name(), enrollment.get_grade()] for enrollment in enrollment_list if isinstance(enrollment, Enrollment) and enrollment.get_student() == student and enrollment.get_grade() is not None}

# Assuming each subject has a method get_subject_name() in the Subject class
# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)
def get_subject_from_subject_name(subject_name : str):
    return next(subject for subject in subject_list if isinstance(subject, Subject) and subject.get_subject_name() == subject_name)
# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    if not isinstance(student, Student):
        return "Error"

    # Retrieve the student's record
    student_record = get_student_record(student)

    # Create a dictionary with subject_id as keys and [subject_name, grade] as values
    subject_info_dict = {subject_id: [subject_name, grade] for subject_id, [subject_name, grade] in student_record.items()}

    # Calculate the sum of (grade_to_count(grade) * credit) and total credit using zip
    total_gps, total_credit = zip(*((grade_to_count(grade) * get_subject_from_subject_name(subject_name).get_credit(),
                                    get_subject_from_subject_name(subject_name).get_credit())
                                   for [subject_name, grade] in subject_info_dict.values()))

    # Check if total_credit is non-zero to avoid division by zero
    return sum(total_gps) / sum(total_credit) if total_credit and any(total_credit) else 0


# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.get_student().get_student_id()] = enrollment.get_student().get_student_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.get_subject().get_subject_id()] = enrollment.get_subject().get_subject_name()
    return subject_dict

#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()
## Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

# ### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

## Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

# ### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student().get_student_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject().get_subject_id() for i in lst])
print("")

# ### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_teacher_name())
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.get_subject().get_subject_id(),enroll.get_student().get_student_id())
# print(enroll.get_subject().subject_id,enroll.student.student_id)
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))
