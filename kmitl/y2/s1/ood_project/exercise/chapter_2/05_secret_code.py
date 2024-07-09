def bon(w): 
	count = 0
	for i in range(len(w)): 
		for j in range(i + 1, len(w)): 
			if (w[i] == w[j]): 
				count += 1
	n = len(w) 
	res = 1
	res = (res * (n - count)) 
	return res 

secretCode = input("Enter secret code : ")
print(bon(secretCode))