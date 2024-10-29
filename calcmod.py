def add(x,y):		#this program is used as a module in 10a-usemodule.py
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	try:
		return x/y
	except:
		print("this is not a valid division")
		return 0

if __name__ == '__main__':	#true if this program runs as independent program;
	a1 = add(45,67)		#else if imported as module in another program, does not execute this test code
	a2 = subtract(889,344)
	a3 = multiply(24,65)
	a4 = divide(67,19)
	a5 = divide(5,0)
	print("Results are: ",a1,a2,a3,a4,a5)
print('mode of execution: ',__name__)
