def factorial(num):
	num = round(num)
	answer = 1

	if num == 0:
		return answer
	elif num <= 0:
		return print("Number must be a positive integer!")
	else:
		while num >= 1:
			answer = answer * num
			num -= 1

	return answer

def py_fact(num):
	if num == 0:
		return 1
	answer = 1
	for val in range(num, 1, -1):
		answer *= val

	return answer

print(factorial(8))
print(py_fact(8))