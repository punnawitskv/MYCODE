def generate_binary_numbers(n):
    if n < 0:
        return ["Only Positive & Zero Number ! ! !"]
    elif n == 0:
        return ["0"]
    else:
        return generate_binary_recursive(n, "", [])

def generate_binary_recursive(n, current, result):
    if len(current) == n:
        result.append(current)
    else:
        generate_binary_recursive(n, current + "0", result)
        generate_binary_recursive(n, current + "1", result)
    return result


inp = int(input("Enter Number : "))
if inp < 0:
    print("Only Positive & Zero Number ! ! !")
else:
    results = generate_binary_numbers(inp)
    for number in results:
        print(number)