def bubble_sort(inp):
    swap = True
    num_step = 0
    last_step = False

    while swap:
        swap = False
        i = 0
        move = "None"
        
        if num_step > 0:
            if num_step == len(inp) - 1:
                print(f"last step : {inp} move[{move_prev}]")
                last_step = True
            else:
                print(f"{num_step} step : {inp_prev} move[{move_prev}]")

        while i <= len(inp) - 2:
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
                swap = True
                move = inp[i+1]
            i += 1
        inp_prev = list(inp)
        move_prev = move
        num_step += 1
        
    if move_prev == "None" and not last_step:
        print(f"last step : {inp} move[{move_prev}]")

inp = list(map(int, input('Enter Input : ').split(' ')))

bubble_sort(inp)

