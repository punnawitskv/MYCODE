user_input = [10]
user_input = input("input: ")
#print("output_test: " + user_input)

count_uppercase = 0
count_lowercase = 0

for char in user_input:
    if char.isupper():
        count_uppercase += 1
    if char.islower():
        count_lowercase += 1

print("outout_uppercase:", count_uppercase)
print("outout_lowercase:", count_lowercase)