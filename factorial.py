number_00 = input()

def factorial_of_number(x):
	factorial = 1
	if x < 0:
		print("no factorial")
	elif x == 0:
		print("factorial is 1")
	else:
		for i in range(1,x+1):
			factorial=factorial*i
		print(factorial)


factorial_of_number(number_00)