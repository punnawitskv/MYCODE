# Class Code
class User:
    def __init__(self, citizen_id, name, account_number, amount_of_money, atm_card):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account_number = account_number
        self.__amount_of_money = amount_of_money
        self.__atm_card = atm_card
        self.__account = Account(account_number, self)
        self.__transactions = []
    
    def get_transactions(self):
        return self.__transactions
        
    @property
    def amount_of_money(self):
        return self.__amount_of_money
    
    @amount_of_money.setter
    def amount_of_money(self, money):
        self.__amount_of_money = money
        
    @property
    def atm_card(self):
        return self.__atm_card
    
    @property
    def account(self):
        return self.__account
    
    @property
    def account_number(self):
        return self.__account_number
    

class Account:
    def __init__(self, account_number, user):
        self.__account_number = account_number
        self.__user  = user
        
    @property
    def user(self):
        return self.__user
    
        
class ATM_Card:
    def init(self, account_number, pin_number):
        self.account_number = account_number
        self.pin_number = pin_number
        

class ATM:
    def __init__(self, number_atm, moneny_in_atm):
        self.__number_atm = number_atm
        self.__moneny_in_atm = moneny_in_atm

    def insert_card(self, bank ,atm_card):
        for user_instance in bank.user :
            if user_instance.atm_card  == atm_card :
                return user_instance.account
        return 'None'

    def Deposit(self, atm, account, money):
        if money > 0 :
            account.user.amount_of_money += money
            account.user.get_transactions().append(f'D-ATM:{self.__number_atm}-{money}-{account.user.amount_of_money}')
            return 'Success'
        else : return 'Error'

    def Withdraw(self, atm, account, money):
        if money > 0 and account.user.amount_of_money >= money :
            account.user.amount_of_money -= money
            account.user.get_transactions().append(f'W-ATM:{self.__number_atm}-{money}-{account.user.amount_of_money}')
            return 'Success'
        else : return 'Error'   

    def Transfer(self, atm, account_own, account_transfer_to, money):
            if money > 0 and account_own.user.amount_of_money >= money :
                account_own.user.amount_of_money -= money
                account_transfer_to.user.amount_of_money += money
                account_own.user.get_transactions().append(f'T-ATM:{self.__number_atm}-+{money}-{account_own.user.amount_of_money}')
                account_transfer_to.user.get_transactions().append(f'T-ATM:{self.__number_atm}-+{money}-{account_transfer_to.user.amount_of_money}')
                return 'Success'
            else : return 'Error'   
               

# class Debit_Card(ATM):
    
               
                              
class Bank:
    def __init__(self, user, atm):
        self.__users = user
        self.__atms = atm
    @property
    def user(self):
        return  self.__users
    
    
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user = {'1-1101-12345-49-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-50-0':['Hermione Jean Granger','0987654321',1000,'1234']}

atm = {'1001':1000000,'1002':200000} #หมายเลขตู้,เงินที่มีในตู้

users = []
atms = []

for citizen_id, data in user.items():
    user_instance = User(citizen_id, *data)
    users.append(user_instance)

for number_atm, data in atm.items():
    atm_instance = ATM(number_atm, data)
    atms.append(atm_instance)
bank = Bank(users, atms)

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

# TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1")
print("Expected : 12345, 1234567890, Success")
print("Actual\t : ", end='')
accout = atms[0].insert_card(bank ,'12345')
if accout != 'None':
    print(f"{accout.user.atm_card}, {accout.user.account_number}, Success")
else:
    print("Error")
print("")
    
    
# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2")
print("Expected :\nHermione account before test : 1000")
print("Hermione account after test : 2000")
print("Actual :")
print(f'Hermione account before test : {users[1].amount_of_money}')
atms[1].Deposit(atms[1], users[1].account, 1000)
print(f'Hermione account after test : {users[1].amount_of_money}')
print("")


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
print("Expected : Error")
print("Actual\t : ", end='')
print(atms[1].Deposit(atms[1], users[1].account, -1))
print("")


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4")
print("Expected :\nHermione account before test : 2000\nHermione account after test : 1500")
print("Actual\t :")
print("Hermione account before test : ", end='')
print(f"{users[1].amount_of_money}")
atms[1].Withdraw(atms[1], users[1].account, 500)
print("Hermione account after test : ", end='')
print(f"{users[1].amount_of_money}")
print("")


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5")
print("Expected : Error")
print("Actual\t : ", end='')
print(atms[1].Deposit(atms[1], users[1].account, -2000))
print("")


# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6")
print("Expected :\nHarry account before test : 20000\nHermione account before test : 1500\nHarry account after test : 10000\nHermione account after test : 11500")
print("Actual\t :")

print("Harry account before test : ", end='')
print(f"{users[0].amount_of_money}")

print("Hermione account before test : ", end='')
print(f"{users[1].amount_of_money}")

atms[1].Transfer(atms[1], users[0].account, users[1].account, 10000)

print("Harry account after test : ", end='')
print(f"{users[0].amount_of_money}")

print("Hermione account after test : ", end='')
print(f"{users[1].amount_of_money}")
print("")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
print("Expected :\nHermione transaction : D-ATM:1002-1000-2000\nHermione transaction : W-ATM:1002-500-1500\nHermione transaction : T-ATM:1002-+10000-11500")
print("Actual\t :")
for transaction in users[1].get_transactions():
    print(f"Hermione transaction : {transaction}")
print("")