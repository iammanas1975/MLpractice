def putword(d,z):
	if z not in d:
		d[z] = 1
	else:
		d[z] += 1
	return d[z]

f = open('words.txt')
di = dict()
count = 0
x = 'any'
while x != '':				#this is not required of using 'for x in f:'
	x = f.readline()		#not required if above for loop used
	idx = x.strip()[:1]
	#print(idx)			#debug line
	if idx != '':			#check not required if above for loop used
		di[idx] = putword(di,idx)
		count += 1
print(di,'\nCount = ', count)
