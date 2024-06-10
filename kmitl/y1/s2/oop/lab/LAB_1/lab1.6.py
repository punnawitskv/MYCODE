i = 10
j = 1

print(" ", end='')
for n in range(1, 101, 1):
    if i <= j:
        print("#", end='')
        
    else:
        print(" ", end='')
        
    i = i - 1
    
    if n % 10 == 0 and n != 100:
        i = 10
        j = j + 1
        print("")
        print(" ", end='')