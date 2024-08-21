def generate_binary_recursive(n, current, result):
    if len(current) == n:
        result.append(current)
    else:
        generate_binary_recursive(n, current + "0", result)
        generate_binary_recursive(n, current + "1", result)
    return result


inp = int(input("Enter Number : "))
print(f'2^{inp} - 1 is {(2**inp) - 1}')

if inp < 0:
    print("Only Positive & Zero Number ! ! !")
elif inp == 0:
    print("0")
else:
    results = generate_binary_recursive(inp, "", [])
    for number in results:
        print(number)