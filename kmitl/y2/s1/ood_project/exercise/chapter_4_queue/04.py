# สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
# ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

# กิจกรรม                                       สถานที่
# 0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
# 1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
# 2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
# 3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

# โดยการรับ Input จะประกอบด้วย

# กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

# เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
#        วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
# จะได้ว่า 0:0 2:0,1:3 3:2

# ***มีการคิดคะแนนดังนี้***

# ·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

# ·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

# ·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

# ·       ไม่เหมือนกันเลย                                   - 5

# หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

# โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง


def activity_convert(activity_num):
    if activity_num == '0':
        activity = 'Eat'
    elif activity_num == '1':
        activity = 'Game'
    elif activity_num == '2':
        activity = 'Learn'
    elif activity_num == '3':
        activity = 'Movie'
    else:
        raise "Error"
    return activity
    
def location_convert(location_num):    
    if location_num == '0':
        location = 'Res.'
    elif location_num == '1':
        location = 'ClassR.'
    elif location_num == '2':
        location = 'SuperM.'
    elif location_num == '3':
        location = 'Home'
    else:
        raise "Error Calc"
    return location

def score_calc(my_activity_num, your_activity_num, my_location_num, your_location_num, score):
    if my_activity_num == your_activity_num:
        if my_location_num == your_location_num:
            score += 4
        elif my_location_num != your_location_num:
            score += 1
    elif my_activity_num != your_activity_num:
        if my_location_num == your_location_num:
            score += 2
        elif my_location_num != your_location_num:
            score += -5
    return score

all_ours_queue_num = input("Enter Input : ").split(',')

my_queue_num_list = []
your_queue_num_list = []

score = 0

my_activity_and_location_list = []
your_activity_and_location_list = []

for ours_today_queue_num in all_ours_queue_num:
    ours_queue_num = ours_today_queue_num.split(' ')
    my_queue_num_list.append(ours_queue_num[0])
    your_queue_num_list.append(ours_queue_num[1])

    my_today_activity_and_location_num = ours_queue_num[0].split(':')
    my_activity_num = my_today_activity_and_location_num[0]
    my_location_num = my_today_activity_and_location_num[1]

    your_today_activity_and_location_num = ours_queue_num[1].split(":")
    your_activity_num = your_today_activity_and_location_num[0]
    your_location_num = your_today_activity_and_location_num[1]

    score = score_calc(my_activity_num, your_activity_num, my_location_num, your_location_num, score)

    my_activity_and_location_list.append(f"{activity_convert(my_activity_num)}:{location_convert(my_location_num)}")
    your_activity_and_location_list.append(f"{activity_convert(your_activity_num)}:{location_convert(your_location_num)}")

my_queue_str = ', '.join(my_queue_num_list)
your_queue_str = ', '.join(your_queue_num_list)

print(f"My   Queue = {my_queue_str}")
print(f"Your Queue = {your_queue_str}")

my_activity_and_location_str = ', '.join(my_activity_and_location_list)
your_activity_and_location_str = ', '.join(your_activity_and_location_list)

print(f"My   Activity:Location = {my_activity_and_location_str}")
print(f"Your Activity:Location = {your_activity_and_location_str}")

if score >= 7:
    print("Yes! You're my love! : ", end='')
elif score <= 7 and score > 0:
    print("Umm.. It's complicated relationship! : ", end='')   
else:
    print("No! We're just friends. : ", end='')

print(f"Score is {score}.")