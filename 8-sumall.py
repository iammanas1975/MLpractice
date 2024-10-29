def addi(*args):			#variable arguments (integers) gathered as a tuple
	res = 0
	for n in args:			#access each element (integer) in the tuple
		res += n
	return res

tex = ''
li = tuple()
while not tex == '0':
	tex = input('Enter a number (0 for no more)')
	li = li + (int(tex),)		#assign new number to the tuple
result = addi(*li)			#scatter the tuple into its constituent integers
print(result)
#print(li)
