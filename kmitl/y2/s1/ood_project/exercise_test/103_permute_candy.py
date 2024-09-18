def permute(num_list):
    permutations = []
    new_list = num_list[::-1]
    a = 1
    for i in range(1,len(num_list)+1):
        a *= i
    b = a/len(num_list)
    c = int(b)
    for i in range(c):
        for j in range(1,len(new_list)+1):
            permutations.append(new_list.copy())
            if  new_list[-1] != 3:
                if j >= len(new_list):
                    break
                temp = new_list[j-1]
                new_list[j-1] = new_list[j] 
                new_list[j] = temp

        new_list.insert(0,new_list.pop())

        if i + 2 >= len(new_list):
            new_list.insert(1,new_list.pop())
        else:
            temp = new_list[i+1]
            new_list[i+1] = new_list[i+2] 
            new_list[i+2] = temp

    return  permutations

print("*** Fun with permute ***")
list_in = list(int(i) for  i in input("input : ").split(","))

print("Original Cofllection: ", list_in)
print("Collection of distinct numbers:")

permutations = permute(list_in)
print("",permutations)