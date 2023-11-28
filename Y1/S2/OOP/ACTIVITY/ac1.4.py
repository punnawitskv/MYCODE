userInput = int(input("input: "))

#check input
#print("outputTest:", userInput)

if userInput < 10 and userInput >= 0:
    a = userInput
    aa = userInput*10 + a
    aaa = userInput*100 + aa
    aaaa = userInput*1000 + aaa
    print("output:", (a + aa + aaa + aaaa), "( =", a, "+", aa, "+", aaa, "+", aaaa, ")")

else:
    print("Brrrrrrrrr")