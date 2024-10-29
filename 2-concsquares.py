import turtle			#turtle module

def mksqr(tl, pix):		#t1 is a turtle draw object
	tl.fd(pix)
	tl.lt(90)
	tl.fd(pix)
	tl.lt(90)
	tl.fd(pix)
	tl.lt(90)
	tl.fd(pix)
	tl.lt(90)

bob = turtle.Turtle()		#Turtle method in turtle module to initialize a draw object
print(bob)			#call the object to initially draw turtle
for i in range(10,210,20):
	mksqr(bob,i)		#call function to keep moving the object
turtle.mainloop()		#loop (retain) the display till window is manually closed
