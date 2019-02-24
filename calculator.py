def calculator():

	try:		
		while True:

			print("                      |------------|")

			print("                      | Calculator |")

			print("                      |------------|")

			num1 = float(input("Enter a number: "))

			print("""

Operators:

+

-

*

/

""")

			op = input("Enter an operator: ")

			num2 = float(input("Enter another number: "))

			if op == "+":

				print(num1+num2)

			elif op == "-":

				print(num1-num2)

			elif op == "*":

				print(num1*num2)

			elif op ==  "/":

				print(num1/num2)

			elif op == "+" or "-" or "*" or "/":

				print("not a valid operator")

	except ZeroDivisionError:

		print("you can't divide by 0")

		calculator()

	except ValueError:

		print("A NUMBER")

		calculator()

	

calculator()
