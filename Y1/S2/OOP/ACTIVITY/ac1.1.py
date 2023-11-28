for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i, end = " ")
        
        for j in range(i+1, 3200):
            if (j % 7 == 0) and (j % 5 != 0):
                print(",", end = " ")
                break