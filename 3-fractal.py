import turtle
bob = turtle.Turtle()
print(bob)

def draw(t,ln,n):
	if n == 0:
		return
	angle = 50
	t.fd(ln*n)
	t.lt(angle)
	draw(t,ln,n-1)
	t.rt(2*angle)
	draw(t,ln,n-1)
	t.lt(angle)
	t.bk(ln*n)
		
draw(bob,10,5)
turtle.mainloop()
