# Class Code
class User:
    def __init__(self, national_id, username, account_number, balance, pin_number):
        self.__national_id = national_id
        self.__username = username
        self.__account_number = account_number
        self.__balance = balance
        self.__pin_number = pin_number
        self.__transactions = []
        
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
    
    def increase_balance(self, amount):
        self.__balance += amount

    def decrease_balance(self, amount):
        self.__balance -= amount
        
    def add_transaction(self, transaction):
        self.__transactions.append(transaction)

    def get_transactions(self):
        return self.__transactions
    
    def get_last_transaction(self):
        if self.__transactions:
            return self.__transactions[-1]
        else:
            return None
        

class Bank:
    def __init__(self, users, atms):
        self.__users = users
        self.__atms = atms

    def get_user_by_national_id(self, national_id):
        if national_id in self.__users:
            return self.__users[national_id]
        else:
            return None

    def get_atm_by_id(self, atm_id):
        if atm_id in self.__atms:
            return self.__atms[atm_id]
        else:
            return None

    def transfer_money(self, sender_account, receiver_account, amount):
        if amount <= 0 or sender_account.get_balance() < amount:
            return "Error: Invalid amount or insufficient balance."

        sender_account.decrease_balance(amount)
        receiver_account.increase_balance(amount)

        sender_account.add_transaction(f"Transfer to {receiver_account.get_username()}: -{amount}")
        receiver_account.add_transaction(f"Transfer from {sender_account.get_username()}: +{amount}")

        return "Success"

class ATM:
    def __init__(self, atm_id, atm_balance):
        self.__atm_id = atm_id
        self.__atm_balance = atm_balance

    def get_atm_id(self):
        return self.__atm_id

    def get_atm_balance(self):
        return self.__atm_balance

    def insert_card(self, bank, atm_card):
        user_instance = bank.get_user_by_national_id(atm_card)

        if user_instance:
            return user_instance
        else:
            return None

    def deposit_money(self, user_account, amount):
        if amount <= 0:
            # return "Error: Invalid deposit amount."
            return "Error"

        user_account.increase_balance(amount)
        user_account.add_transaction(f"Deposit: +{amount}")

        return "Success"

    def withdraw_money(self, user_account, amount):
        if amount <= 0 or amount > user_account.get_balance():
            # return "Error: Invalid withdrawal amount."
            return "Error"

        user_account.decrease_balance(amount)
        user_account.add_transaction(f"Withdrawal: -{amount}")

        return "Success"

    def transfer_money(self, sender_account, receiver_account, amount, bank):
        transfer_result = bank.transfer_money(sender_account, receiver_account, amount)
        return transfer_result

        
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321',1000,'12346']}

users = {}
for user_id, data in user.items():
    user = User(user_id, data[0], data[1], data[2], data[3])
    users[user_id] = user
    
atm ={'1001':1000000,'1002':200000}

atms = {}
for atm_id, atm_balance in atm.items():
    atm_obj = ATM(atm_id, atm_balance)
    atms[atm_id] = atm_obj


# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
bank = Bank(users, atms)
atm1 = ATM('1001', 1000000)
atm2 = ATM('1002', 200000)
atms = {'1001': atm1, '1002': atm2}


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
print("\nTest Case #1:")
print('Expected :\n12345, 1234567890, Success')
print('Actual :')
atm1_card_number = '1-1101-12345-12-0'
atm1_user_instance = atm1.insert_card(bank, atm1_card_number)

if atm1_user_instance:
    print(f"{atm1_user_instance.get_pin_number()}, {atm1_user_instance.get_account_number()}, Success")
else:
    print("Invalid card. Please try again.")


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("\nTest Case #2:")
print('Expected : \nHermione account before test : 1000\nHermione account after test : 2000')
print('Actual :')
hermione_account_before_test = users['1-1101-12345-13-0'].get_balance()
print(f"Hermione account before test : {hermione_account_before_test}")

# Use increase_balance method instead of directly modifying balance attribute
deposit_result = atm2.deposit_money(users['1-1101-12345-13-0'], 1000)
hermione_account_after_test = users['1-1101-12345-13-0'].get_balance()
print(f"Hermione account after test : {hermione_account_after_test}")
# print(f"Transaction: {users['1-1101-12345-13-0'].get_transactions()}")


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("\nTest Case #3:")
print('Expected :\nError')
print('Actual :')
invalid_deposit_result = atm2.deposit_money(users['1-1101-12345-13-0'], -1)
print(invalid_deposit_result)


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("\nTest Case #4:")
print('Expected :\nHermione account before test : 2000\nHermione account after test : 1500')
print('Actual :')
hermione_account_before_test = users['1-1101-12345-13-0'].get_balance()
print(f"Hermione account before test : {hermione_account_before_test}")

# Use decrease_balance method instead of directly modifying balance attribute
withdraw_result = atm2.withdraw_money(users['1-1101-12345-13-0'], 500)
hermione_account_after_test = users['1-1101-12345-13-0'].get_balance()
print(f"Hermione account after test : {hermione_account_after_test}")
# print(f"Transaction: {users['1-1101-12345-13-0'].get_transactions()}")


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("\nTest Case #5:")
print('Expected :\nError')
print('Actual :')
invalid_withdrawal_result = atm2.withdraw_money(users['1-1101-12345-13-0'], 2000)
print(invalid_withdrawal_result)


# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("\nTest Case #6:")
print('Expected :\nHarry account before test : 20000\nHarry account after test : 10000\nHermione account before test : 1500\nHermione account after test : 11500')
print('Actual :')
harry_account_before_test = users['1-1101-12345-12-0'].get_balance()
print(f"Harry account before test: {harry_account_before_test}")

# Use transfer_money method to transfer money from Harry to Hermione
transfer_result = atm2.transfer_money(users['1-1101-12345-12-0'], users['1-1101-12345-13-0'], 10000, bank)
print(f"Harry account after test: {users['1-1101-12345-12-0'].get_balance()}")
print(f"Hermione account before test : 1500")
print(f"Hermione account after test : {users['1-1101-12345-13-0'].get_balance()}")
# print(f"Transaction: {users['1-1101-12345-13-0'].get_transactions()}")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("\nTest Case #7:")
print('Expected :\nHermione transaction : D-ATM:1002-1000-2000\nHermione transaction : W-ATM:1002-500-1500\nHermione transaction : T-ATM:1002-+10000-11500')
print('Actual :')
hermione_transactions = users['1-1101-12345-13-0'].get_transactions()
if hermione_transactions:
    for transaction in hermione_transactions:
        if "Deposit" in transaction:
            amount = transaction.split(":")[1].strip()
            transaction = f"D-ATM:1002-{amount}-2000"
        elif "Withdrawal" in transaction:
            amount = transaction.split(":")[1].strip()
            transaction = f"W-ATM:1002-{amount}-1500"
        elif "Transfer from" in transaction:
            amount = transaction.split(":")[1].strip()
            transaction = f"T-ATM:1002-{amount}-11500"
        print(f"Hermione transaction : {transaction}")
else:
    print("No transactions found for Hermione.")

# Lab6_skeleton_code.py
# Displaying Lab6_skeleton_code.py.