def rjust(s):
	l = len(s)
	for i in range(70 - l):	#these many spaces at front
		st = ' ' * i
	mst = st + s		#new string with leading spaces
	print(mst)

rjust('fullmonty')
rjust('this is a fantastic line')
rjust('i love it so much!')
