mostPalindrome = 0
for num1 in range(999, 99, -1) :
    for num2 in range(num1, 99, -1) :
        if (str(num1*num2) == str(num1*num2)[::-1]) :
            if mostPalindrome < num1*num2:
                mostPalindrome = num1*num2
print(mostPalindrome)
            