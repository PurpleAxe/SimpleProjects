"""
All code is copyrighted by Andreas Hugh Visagie
"""

import turtle
t = turtle.Turtle()
a = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("black")
turtle.setup(900, 900)
		
def Tdraw(r=1, b=10, c=1, g=250, inc=1):
	z = 1
	n = 1
	a = turtle.Turtle()
	a.speed(0)
	a.pensize(c)
	for i in range(b):
		a.color("green")
		a.fd(n)
		a.right(r+z/0.1)
		n+=inc
		z+=1
		print("Iteration count... ",z,":- -:",n," ...Increment amount...","Position...", a.pos())
		
		
Tdraw(1, 50, 1, 1000, 2)
		
scr.mainloop()