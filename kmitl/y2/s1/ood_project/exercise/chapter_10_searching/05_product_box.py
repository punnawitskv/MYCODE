def can_partition(weights, max_weight, k):
    current_weight = 0
    box_count = 1
    
    for weight in weights:
        if current_weight + weight > max_weight:
            box_count += 1
            current_weight = weight
            if box_count > k:
                return False
        else:
            current_weight += weight
            
    return True

def find_minimum_max_weight(weights, k):
    low = max(weights)
    high = sum(weights)
    
    while low < high:
        mid = (low + high) // 2
        if can_partition(weights, mid, k):
            high = mid
        else:
            low = mid + 1
    
    return low

inp = input("Enter Input : ")
weights_str, k_str = inp.split('/')
weights = list(map(int, weights_str.split()))
k = int(k_str)

result = find_minimum_max_weight(weights, k)
print(f"Minimum weigth for {k} box(es) = {result}")
