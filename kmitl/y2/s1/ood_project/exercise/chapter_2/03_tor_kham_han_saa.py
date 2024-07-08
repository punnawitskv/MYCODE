# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
# 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# จะไม่สามารถพูดว่า “Apple” ได้อีก


# 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


# 3. Ignore Case Sensitive


# โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# - P < word > จะเป็นการต่อคำ
# - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# - X เป็นการระบุว่าจบการทำงาน

# โดยใช้ class รูปแบบดังนี้

class TorKham:

	def __init__(self):

		self.words = []

	def restart(self):

		### Enter Your Code Here ###

		return "game restarted"

	def play(self, word):

		### Enter Your Code Here ###

		return "game over"



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')
for word in S:
	print(word)
### Enter Your Code Here ###	