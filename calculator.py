'''
	make a calculator with 2 inputs
	show addition, subtraction, multiplication, dividios, power, modulus, floor division
'''

def addition(a,b):		#function for addition
	c=a+b
	print(f"The addition of {a} & {b} is {c}")


def subtraction(a,b):	#function for subtraction
	c=a-b
	print(f"The subtraction of {a} & {b} is {c}")


def multiplication(a,b):	#function for multiplication
	c=a*b
	print(f"The multiplication of {a} & {b} is {c}")


def division(a,b):		#function for division
	c=a/b
	print(f"The division of {a} & {b} is {c}")


def mod(a,b):		#function for modulus
	c=a%b
	print(f"The modulus of {a} & {b} is {c}")


def exponential(a,b):		#function for exponential
	c=a**b
	print(f"The exponential of {a} & {b} is {c}")


def floor_num(a,b):			#function for floor division
	c=a//b
	print(f"The floor division of {a} & {b} is {c}")


while True:		# Continues the loop until false 

		# To select the relevent operation and save the number in n variable
	print("\nSelect the desired opperation.\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponential\n7.Floor division")
	n=int(input("Enter your selection: "))

	if 7>=n>0:
		print("\nEnter two numbers to calculate in the format x/y")
		x=float(input("\nEnter the first number (x): "))
		y=float(input("Enter the first number (y): "))
		print("\n")


		if n==1:
			addition(x,y)

		elif n==2:
			subtraction(x,y)

		elif n==3:
			multiplication(x,y)

		elif n==4:
			division(x,y)

		elif n==5:
			mod(x,y)

		elif n==6:
			exponential(x,y)

		elif n==7:
			floor_num(x,y)
    

	else:
		print("Selected the wrong number, try again")



	next_calculation = input("\nLet's do next calculation? (yes/no): ")
	        
	if next_calculation == "no":
		break

		
