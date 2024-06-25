def delete_minus(x):
    return [list(filter(lambda num: num >= 0, sublist)) for sublist in x]

input_list = [[1, -3, 2], [-8, 5], [-1, -4, -3]]
result = delete_minus(input_list)
print(result)
