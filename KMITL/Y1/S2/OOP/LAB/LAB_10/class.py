class Controller:
    def __init__(self) -> None:
        self.__users = User
        self.__coupons = Coupon
        self.__payment = Payment
        self.__category = Category
        self.__progress = Progress
        
class User:
    def __init__(self, user_id, user_name, cart, orders, my_courses) -> None:
        self.__user_id = user_id
        self.__user_name = user_name
        self.__cart = cart
        self.__orders = orders
        self.__my_courses = my_courses
        
    def buy_course(self, cart):
        pass
    
class Progress:
    def __init__(self) -> None:
        pass
    
class Category:
    def __init__(self) -> None:
        pass

class Teacher:
    def __init__(self) -> None:
        pass

class Course:
    def __init__(self) -> None:
        pass
    
class Order:
    def __init__(self) -> None:
        pass        
    
class Coupon:
    def __init__(self) -> None:
        pass
    
class CouponCourse:
    def __init__(self) -> None:
        pass
    
class CouponTeacher:
    def __init__(self) -> None:
        pass
    
class Payment:
    def __init__(self) -> None:
        pass    