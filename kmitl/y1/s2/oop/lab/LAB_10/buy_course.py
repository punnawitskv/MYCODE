class Controller:
    def __init__(self, user_input, coupon_input, payment_input, category_input, progress_input) -> None:
        self.__users = user_input
        self.__coupons = coupon_input
        self.__payment = payment_input
        self.__category = category_input
        self.__progress = progress_input
        
    def get_course_from_course_id_ctrl(self, course_id_input):
        pass
    
    def get_teacher_from_course(self, course_input):
        pass
    
    def validate_coupon(self, course_input, coupon_id_input, teacher_input):
        pass
    
    def create_order(self):
        pass
    
        
class User:
    def __init__(self, user_id_input, user_name_input, cart_input, orders_input, my_courses_input) -> None:
        self.__user_id = user_id_input
        self.__user_name = user_name_input
        self.__cart = cart_input
        self.__orders = orders_input
        self.__my_courses = my_courses_input
        
    def buy_course(self, user_id_input, course_id_input, coupon_id_input):
        pass
    
    
class Progress:
    def __init__(self) -> None:
        pass
    
    
class Category:
    def __init__(self, category_input, courses_input) -> None:
        self.__category = category_input
        self.__courses = courses_input
    
    def get_course_from_course_id_ctgr(self, course_id_input):
        pass


class Teacher:
    def __init__(self, my_teaching_course_input) -> None:
        self.__my_teaching_course = my_teaching_course_input
        
    def add_course(self, course_for_add_input):
        pass


class Course:
    def __init__(self, category_input, course_id_input) -> None:
        self.__category = category_input
        self.__course_id = course_id_input
    
    
class Order:
    def __init__(self, payment_input) -> None:
        self.__payment = payment_input
    
    def create_payment(self, status_input, amount_input, country_input, type_input):
        pass
    
    
class Coupon:
    def __init__(self, coupon_input, amount_input) -> None:
        self.coupon = coupon_input
        self.amount = amount_input
    
    def check_coupon_course(self, coupon_id_input, course_input):
        pass
    
    def check_coupon_teacher(self, coupon_id_input, teacher_input):
        pass
    
    
class CouponCourse:
    def __init__(self, course_input, coupon_id_input) -> None:
        self.__course = course_input
        self.__coupon_id = coupon_id_input
   
    
class CouponTeacher:
    def __init__(self, teacher_input, coupon_id_input) -> None:
        self.__teacher = teacher_input
        self.__coupon_id = coupon_id_input
   
    
class Payment:
    def __init__(self, status_input, amount_input, country_input, type_input) -> None:
        self.__status = status_input
        self.__amount = amount_input
        self.__country = country_input
        self.__type = type_input