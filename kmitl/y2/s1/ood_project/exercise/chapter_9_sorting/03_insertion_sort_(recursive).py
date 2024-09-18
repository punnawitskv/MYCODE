def insertion_sort_recursive(arr, index=0):
    if index == len(arr):
        print("sorted")
        print(arr)
        return

    key = arr[index]
    
    insert_index = insert_recursive(arr, key, index)
    
    if index > 0:
        if arr[index+1:]:
            print(f"insert {key} at index {insert_index} : {arr[:index+1]} {arr[index+1:]}")
        else:
            print(f"insert {key} at index {insert_index} : {arr[:index+1]}")
    
    insertion_sort_recursive(arr, index + 1)

def insert_recursive(arr, key, index):
    if index == 0 or arr[index-1] <= key:
        arr[index] = key
        return index
    
    arr[index] = arr[index-1]
    return insert_recursive(arr, key, index-1)

input_list = list(map(int, input("Enter Input : ").split()))
insertion_sort_recursive(input_list)
