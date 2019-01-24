print(" |--------------------------------------| ")
print(" | my first code i think it's a code :D |")
print(" |--------------------------------------| ")
try:
	num1 = int(input("choose a number: "))
	op = input("choose an operator: ")
	num2 = int(input("choose another number: "))
	if op == "+":
		print(num1 + num2)
	elif op == "-":
		print(num1 - num2)
	elif op == "*":
		print(num1 * num2)
	elif op == "/":
		print(num1 / num2)
except:
	print("that's not right")
