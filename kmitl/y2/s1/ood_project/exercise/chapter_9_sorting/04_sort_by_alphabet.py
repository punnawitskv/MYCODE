def custom_sort(arr):
    def get_alpha(s):
        for char in s:
            if 'a' <= char <= 'z':
                return char
        return ''

    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and get_alpha(arr[j]) > get_alpha(key):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    insertion_sort(arr)
    return arr

input_string = input("Enter Input : ")
string_list = input_string.split()
sorted_list = custom_sort(string_list)
print(" ".join(sorted_list))
