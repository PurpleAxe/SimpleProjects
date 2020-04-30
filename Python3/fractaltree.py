import turtle, colorsys
t = turtle.Turtle()
r = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("black")
t.left(90)
t.speed(10)
t.color("white")
t.ht()
t.pu()
t.goto(0,-100)
t.pd()


def treefrac(l):
	if(l<4):
		return 
	else:
		colors = colorsys.hsv_to_rgb(l/100, 1.0, 1.0)
		t.color(colors)
		t.forward(l)
		t.left(30)
		treefrac(3*l/4)
		t.right(60)
		treefrac(3*l/4)
		t.left(30)
		t.back(l)
		t.color(colors)

treefrac(100)

scr.mainloop()
