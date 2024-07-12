def find_triplets_with_sum(arr):
    n = len(arr)
    triplets = []

    if n < 3:
        triplets = "Array Input Length Must More Than 2"
        return triplets

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 5:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
    
    return triplets

input_list = input("Enter Your List : ")
arr = list(map(int, input_list.split()))

triplets = find_triplets_with_sum(arr)
print(triplets)
