print("*** Fun with permute ***")

num_arr = []
output = []

def permute(num = 0):

    if num == len(input_ls):
        output.append(num_arr.copy())
        return
    
    for i in range(len(num_arr) + 1):
        num_arr.insert(i, input_ls[num])
        permute(num + 1)
        num_arr.pop(i)

user_input = input("input : ")
input_ls = list(map(int, user_input.split(",")))

print(f"Original Cofllection:  {input_ls}")
print(f"Collection of distinct numbers:")

permute()
print(f" {output}")