# Class Code
class Bank:
    def __init__(self, user, atm):
        self.__users = user
        self.__atms = atm
    @property
    def user(self):
        return self.__users
class ATM:
    def __init__(self, number_atm, moneny_in_atm):
        self.__number_atm = number_atm
        self.__moneny_in_atm = moneny_in_atm
    @property
    def money(self):
        return self.__moneny_in_atm
    @money.setter
    def money(self, money):
        self.__moneny_in_atm = money 
    @property
    def number_atm(self):
        return self.__number_atm    

    def insert_card(self, bank, pin_number):
        for user_instance in bank.user:
            if user_instance.account.atm_card.pin_number == pin_number:
                return user_instance.account
        return "None"
class User:
    def __init__(self, citizen_id, name, account_number, amount_of_money, atm_card):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account_number = account_number
        self.__account = Account(account_number, self, atm_card, amount_of_money)
        self.__account_fixed = Fixed_Account(account_number, self, amount_of_money)
    @property
    def account(self):
        return self.__account
    @property
    def account_number(self):
        return self.__account_number
    @property
    def account_fixed(self):
        return self.__account_fixed


class Account:
    def __init__(self, account_number, user, atm_card, amount_of_money):
        self.__account_number = account_number
        self.__user = user
        self.__amount_of_money = amount_of_money
        self.__atm_card = ATM_Card(atm_card)
        self.__transaction = Transactions(self, amount_of_money)
        self.__total_transactions = []
        self.__debit_card = Debit_Card(atm_card)
        
    @property
    def amount_of_money(self):
        return self.__amount_of_money
    @amount_of_money.setter
    def amount_of_money(self, money):
        self.__amount_of_money = money
    @property
    def transaction(self):
        return self.__transaction
    @property
    def total_transactions(self):
        return self.__total_transactions
    @property
    def atm_card(self):
        return self.__atm_card
    @property
    def debit_card(self):
        return self.__debit_card
    @property
    def user(self):
        return self.__user
    
class Fixed_Account(Account):
    interest  = 0.02
    def __init__(self, account_number, user, money):
        super().__init__(account_number, user, None, money)
    @property
    def Annual_fee(self):
        Annual_fee = self.amount_of_money * Fixed_Account.interest
        return Annual_fee


class ATM_Card:
    def __init__(self, atm_card):
        self.__atm_card = atm_card
        self.__out_money = 0
        self.__annual_free = 150
    @property
    def out_money(self):
        return self.__out_money
    @out_money.setter
    def out_money(self, money):
        self.__out_money = money
    @property
    def pin_number(self):
        return self.__atm_card
    @property
    def annual_free(self):
        return self.__annual_free
    
class Debit_Card(ATM_Card) :
    def __init__(self, debit_card):
        super().__init__(debit_card)

class Transactions :
    def __init__(self, account, money):
        self.__account = account
        self.__money = money

    def Purchase(self, atm, account, paid, money):
        if money > 0 and account.amount_of_money >= money :
            account.amount_of_money -= money 
            account.total_transactions.append(
                f"P-ATM:{atm.number_atm}-{money}-{account.amount_of_money}")
            account.debit_card.out_money += money
            return "success"
        else:
            return "error"

    def Deposit(self, atm, account, money):
        if money > 0 :
            account.amount_of_money += money
            account.total_transactions.append(f"D-ATM:{atm.number_atm}-{money}-{account.amount_of_money}")
            atm.money += money
            return "success"
        else:
            return "error"

    def Withdraw(self, atm, account, money):
        if money > 0 and account.amount_of_money >= money and atm.money >= money and account.atm_card.out_money <= 40000:
            account.amount_of_money -= money
            account.total_transactions.append(
                f"W-ATM:{atm.number_atm}-{money}-{account.amount_of_money}")
            atm.money -= money
            account.atm_card.out_money += money
            return "success"
        else:
            return "error"

    def Transfer(self, atm, account_own, account_transfer_to, money):
        if money > 0 and account_own.amount_of_money >= money and account_own.atm_card.out_money<= 40000:
            account_own.amount_of_money -= money
            account_own.atm_card.out_money += money
            account_transfer_to.amount_of_money += money
            account_transfer_to.total_transactions.append(
                f"T-ATM:{atm.number_atm}-+{money}-{account_transfer_to.amount_of_money}"
            )
            account_own.total_transactions.append(
                f"T-ATM:{atm.number_atm}-+{money}-{account_own.amount_of_money}"
            )
            return "success"
        else:
            return "error"


##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user = {
    "1-1101-12345-49-0": ["Harry Potter", "1234567890", 20000, "12345"],
    "1-1101-12345-50-0": ["Hermione Jean Granger", "0987654321", 1000, "1234"],
}

atm = {"1001": 1000000, "1002": 200000}  # หมายเลขตู้,เงินที่มีในตู้

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
print("Ans : 12345, 1234567890, Success")
accout = atms[0].insert_card(bank, "12345")  
print(f"Expected : {accout.atm_card.pin_number}, {accout.user.account_number}, Success\n")
# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2")
print("Ans :\nHermione account before test : 1000")
print("Hermione account after test : 2000")
print("Expected :")
print(f"Hermione account before test : {users[1].account.amount_of_money}")
users[1].account.transaction.Deposit(atms[1], users[1].account, 1000)
print(f"Hermione account before test : {users[1].account.amount_of_money}\n")


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
print("Ans : error")

print(f"Expected :{users[1].account.transaction.Deposit(atms[1], users[1].account, -1)}\n")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4")
print("Ans :\nHermione account before test : 2000")
print("Hermione account after test : 1500")
print("Expected :")
print(f"Hermione account before test : {users[1].account.amount_of_money}")
users[1].account.transaction.Withdraw(atms[1], users[1].account, 500)
print(f"Hermione account after test : {users[1].account.amount_of_money}\n")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5")
print("Ans : error")
print(f"Expected : {users[1].account.transaction.Withdraw(atms[1], users[1].account, 2000)}\n")
# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6")
print("Ans :\nHarry account before test : 20000")
print("Harry account after test : 10000")
print("Hermione account before test : 1500")
print("Hermione account after test : 11500")

print(f"Expected :\nHarry account before test : {users[0].account.amount_of_money}")
print(f"Hermione account before test : {users[1].account.amount_of_money}")
users[0].account.transaction.Transfer(atms[1], users[0].account, users[1].account, 10000)
print(f"Harry account after test : {users[0].account.amount_of_money}")
print(f"Hermione account after test : {users[1].account.amount_of_money}\n")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
print("Ans :")
print("Hermione transaction : D-ATM:1002-1000-2000")
print("Hermione transaction : W-ATM:1002-500-1500")
print("Hermione transaction : T-ATM:1002-+10000-11500")
print("Expected : ")
for transaction in users[1].account.total_transactions:
    print(f"Hermione transaction : {transaction}")
# users[1].account.transaction.Purchase(atms[1], users[1].account, 'GGG' ,700)
print(users[1].account_fixed.Annual_fee)