checkIn1, checkIn2, checkOut1, checkOut2 = [int(e) for e in input("input: ").split()]

checkIntime = checkIn1*60 + checkIn2
checkOutTime = checkOut1*60 + checkOut2
parkingTime = checkOutTime-checkIntime

#check input
if (checkIn1 < 7 or checkIn1 >= 23) or (checkIn2 >= 60 or checkIn2 < 0) or (checkOut1 > 23 or checkOut1 <= 6) or (checkOut2 >= 60 or checkOut2 < 0) or (parkingTime < 0) or (checkOut1 == 23 and checkOut2 > 0):
    print("CALL THE GUARD!!!")
    
else:
    print("output:", end=" ")
    if parkingTime <= 15:
        print(0)
        
    elif parkingTime > 15 and parkingTime <= 180:
        if parkingTime % 60 == 0:
            print((parkingTime/60)*10)
        else:
            print(((parkingTime//60)+1) *10)
            
    elif parkingTime > 180 and parkingTime <= 360:
        if parkingTime % 60 == 0:
            print(((parkingTime-180)/6)*20+30)
        else:
            print((((parkingTime-180)//60)+1)*20+30)
            
    else:
        print(200)