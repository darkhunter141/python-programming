def nam(n=1):
	count = 1
	try:
		n = int(input("Enter your number"))
		for i in range(1,11):
		print(n, 'x', count, '=', n*count)
		count += 1
	except:
		for i in range(1,11):
		print(n, 'x', count, '=', n*count)
		count += 1
nam()