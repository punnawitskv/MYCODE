def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def fix_negative_int_bubble_sort(arr):
    non_negative = [x for x in arr if x >= 0]
    
    bubble_sort(non_negative)
    
    result = []
    non_negative_index = 0
    for num in arr:
        if num < 0:
            result.append(num)
        else:
            result.append(non_negative[non_negative_index])
            non_negative_index += 1
    
    return result

input_list = list(map(int, input('Enter Input : ').split(' ')))

fixed_negative_list = fix_negative_int_bubble_sort(input_list)
print(" ".join(map(str, fixed_negative_list)))
