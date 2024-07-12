print("*** multiplication or sum ***")

user_input = input("Enter num1 num2 : ")

num1, num2 = user_input.split()

num1 = int(num1)
num2 = int(num2)

sum = num1 * num2

if sum > 1000:
    print(f"The result is {num1 + num2}")
elif sum <= 1000:
    print(f"The result is {num1 * num2}")