print("*** Fun with Drawing ***")

def draw_pyramid(size):
    if size < 2:
        print("Input size must be 2 or more.")
        return
    
    size_range = size * 4 - 3
    count_for_loop = int(size_range / 2)
    
    for y in range(count_for_loop * -1, count_for_loop + 1, 1):
        for x in range(count_for_loop * -1, count_for_loop + 1, 1):
            
            map_num = 0

            if abs(x) > abs(y):
                map_num = abs(x)
            else:
                map_num = abs(y)
        
            if map_num % 2 == 0:
                print("#", end="  ")
            else:
                print(".", end="  ")
                
            # print(map_num, end=" ")
        
        print("")

size = int(input("Enter input : "))

draw_pyramid(size)