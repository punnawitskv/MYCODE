def find_first_greater_value(left_list, right_list):
    sorted_left = sorted(left_list)
    for value in right_list:
        found = False
        for left_value in sorted_left:
            if left_value > value:
                print(left_value)
                found = True
                break
        if not found:
            print("No First Greater Value")

left, right = input("Enter Input : ").split('/')
left_list = list(map(int, left.split()))
right_list = list(map(int, right.split()))

find_first_greater_value(left_list, right_list)
