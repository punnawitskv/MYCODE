def add2list(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Brrrrrrrrr"

    result = [x + y for x, y in zip(lst1, lst2)]
    return result

x = [1, 2, 3]
y = [4, 5, 6]

result_list = add2list(x, y)
print(result_list)
