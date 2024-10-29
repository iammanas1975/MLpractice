def facto(n):
	if n == 1:
		return n
	else:
		frac = n*facto(n-1)	#recursive calls evaluated in loop till n becomes 1 and then backtracks
		return frac

number = 7
print("Factorial of ", number, "is", facto(number))
