print("*** Converting hh.mm.ss to seconds ***")

user_input = [3]
user_input = input("Enter hh mm ss : ")

hh, mm, ss = user_input.split()
hh = int(hh)
mm = int(mm)
ss = int(ss)

if mm >= 60 or mm < 0:
    print(f"mm({mm}) is invalid!")
elif ss >= 60 or ss < 0:
    print(f"ss({ss}) is invalid!")
elif hh >= 24 or hh < 0:
    print(f"hh({hh}) is invalid!")
else: 
    seconds = hh*60*60 + mm*60 + ss
    formatted_seconds = "{:,}".format(seconds)
        
    if hh < 10:
        hh = "0" + str(hh)
    else:
        hh = str(hh)
        
    if mm < 10:
        mm = "0" + str(mm)
    else:
        mm = str(mm)
        
    if ss < 10:
        ss = "0" + str(ss)
    else:
        ss = str(ss)
        
    print(f"{hh}:{mm}:{ss} = {formatted_seconds} seconds")