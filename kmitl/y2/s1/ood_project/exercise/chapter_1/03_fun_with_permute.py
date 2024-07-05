def permute(collection):
    if len(collection) == 0:
        return []
    if len(collection) == 1:
        return [collection]
    
    permutations = []
    for i in range(len(collection)):
        current = collection[i]
        remaining = collection[:i] + collection[i+1:]
        for p in permute(remaining):
            permutations.append([current] + p)
    return permutations

def main():
    print("*** Fun with permute ***")
    input_str = input("input : ")
    input_list = [int(x) for x in input_str.split(",")]
    
    print("Original Cofllection: ", input_list)
    
    permutations = permute(input_list)
    permutations_sorted = sorted(permutations, reverse=True)
    
    print("Collection of distinct numbers:")
    print(f" {permutations_sorted}")

if __name__ == "__main__":
    main()
