def ackmann(m,n):
	if m == 0:
		return n+1
	if m > 0 and n == 0:
		return ackmann(m-1, 1)
	if m > 0 and n > 0:
		return ackmann(m-1, ackmann(m,n-1))

result = ackmann(3,4)
print("Result is ",result)
