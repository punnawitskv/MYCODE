def draw_yin_yang(size):
    
    size_range = (size + 2) * 2
    quarter_range = int(size_range / 2)
    # print(f"Size range : {size_range}")
    # print(f"Quarter range : {quarter_range}\n")


    # for y in range(size_range):
    #     for x in range(size_range):
    #         print(f"{x},{y}", end="  ")

    #     print("\n")
    # print("")

    count1 = quarter_range - 1
    count2 = size_range + quarter_range

    for y in range(size_range):
        for x in range(size_range):
                
            if x < quarter_range and y < quarter_range:
                if x < count1:
                    print(".", end="")
                else:
                    print("#", end="")
            elif x >= quarter_range and y < quarter_range:
                if y == 0 or y == quarter_range - 1 or x == size + 2 or x == size_range - 1:
                    print("+", end="")
                else:
                    print("#", end="")
            elif x < quarter_range and (y == quarter_range or y == size_range - 1) or x == 0 or x == size + 1:
                print("#", end="")
            elif x < quarter_range or (x >= quarter_range and y >= quarter_range and x < count2):
                print("+", end="")
            else:
                print(".", end="")

        count1 -= 1
        count2 -= 1
        print("")

size = int(input("Enter Input : "))

draw_yin_yang(size)