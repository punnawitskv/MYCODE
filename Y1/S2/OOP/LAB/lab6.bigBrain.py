# Class Code
class User:
    def __init__(self, national_id, username, account_number, balance, pin_number):
        self.__national_id = national_id
        self.__username = username
        self.__account_number = account_number
        self.__balance = balance
        self.__pin_number = pin_number

    def __str__(self):
        return f"National ID: {self.__national_id}\nUsername: {self.__username}\nAccount Number: {self.__account_number}\nBalance: {self.__balance}\nPIN Number: {self.__pin_number}\n"
    
    # def get_user_info(self):
    #     return {
    #         'national_id': self.__national_id,
    #         'username': self.__username,
    #         'account_number': self.__account_number,
    #         'balance': self.__balance,
    #         'pin_number': self.__pin_number
    #     }
        
    def get_national_id(self):
        return self.__national_id
    
    def get_username(self):
        return self.__username
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def get_pin_number(self):
        return self.__pin_number
    
    def search_account_number_from_pin_number(self, pin_to_search):
        # ตรวจสอบว่า pin_to_search เป็น PIN ของผู้ใช้หรือไม่
        if pin_to_search == self.__pin_number:
            return self.__account_number
        else:
            return None


class ATM:
    def __init__(self, atm_id, atm_balance):
        self.__atm_id = atm_id
        self.__atm_balance = atm_balance
        
    def __str__(self):
        return f"ATM ID: {self.__atm_id}\nATM Balance: {self.__atm_balance}\n"

    def get_atm_id(self):
        return self.__atm_id
    
    def get_atm_balance(self):
        return self.__atm_balance
        
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321',1000,'12346']}

users = {}
for user_id, data in user.items():
    user = User(user_id, data[0], data[1], data[2], data[3])
    users[user_id] = user

# ดึงข้อมูลของผู้ใช้งานทั้งหมด
# users_info = {}
# for user_id, user in users.items():
#     users_info[user_id] = user.get_user_info()

# แสดงข้อมูลของผู้ใช้งานทั้งหมด
# for user_id, user_info in users_info.items():
#     print(f"National ID: {user_info['national_id']}")
#     print(f"Username: {user_info['username']}")
#     print(f"Account Number: {user_info['account_number']}")
#     print(f"Balance: {user_info['balance']}")
#     print(f"PIN Number: {user_info['pin_number']}")
#     print()
for user_id, user_obj in users.items():
    print(f"National ID: {user_obj.get_national_id()}")
    print(f"Username: {user_obj.get_username()}")
    print(f"Account Number: {user_obj.get_account_number()}")
    print(f"Balance: {user_obj.get_balance()}")
    print(f"PIN Number: {user_obj.get_pin_number()}")
    print()
    
atm ={'1001':1000000,'1002':200000}

atms = {}
for atm_id, atm_balance in atm.items():
    atm_obj = ATM(atm_id, atm_balance)
    atms[atm_id] = atm_obj
    
for atm_id, atm_obj in atms.items():
    print(f"ATM ID: {atm_obj.get_atm_id()}")
    print(f"ATM Balance: {atm_obj.get_atm_balance()}")
    print()


# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
# Lab6_skeleton_code.py
# Displaying Lab6_skeleton_code.py.