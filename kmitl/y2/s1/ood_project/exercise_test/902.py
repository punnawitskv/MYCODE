def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def fix_negative_int_bubble_sort(arr):
    # Create a copy of the list with non-negative integers only
    non_negative = [x for x in arr if x >= 0]
    
    # Sort the non-negative integers using bubble sort
    bubble_sort(non_negative)
    
    # Replace the non-negative integers back into their original positions
    result = []
    non_negative_index = 0
    for num in arr:
        if num < 0:
            result.append(num)
        else:
            result.append(non_negative[non_negative_index])
            non_negative_index += 1
    
    return result

# Input: a list of integers
input_list = list(map(int, input('Enter Input : ').split(' ')))

# Standard bubble sort
sorted_list = input_list.copy()
bubble_sort(sorted_list)
print("standard bubble sort :", sorted_list)

# Fix negative int bubble sort
fixed_negative_list = fix_negative_int_bubble_sort(input_list)
print("fix negative int bubble sort :", fixed_negative_list)
