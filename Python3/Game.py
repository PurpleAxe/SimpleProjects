import turtle
import random 
import colorsys
turtle.setup(900, 900)
Scr = turtle.Screen()
Scr.bgcolor("black")
Scr.delay(5)
t = turtle.Turtle()
t.color("white")
t.speed(10)
t.pu()


x = turtle.Turtle()
x.color("red")
x.shape("turtle")
#x.pu()


def xDetection():
    x.setheading(x.towards(t))
    x.forward(8)
    Scr.ontimer(xDetection, 80)
	
def xxpos():
	valx = random.randint(-250, 250)
	print("x", valx)
	valy = random.randint(-250, 250)
	print("y", valy)
	x.setpos(valx, valy)
xxpos()


def up():
	t.seth(90)
	t.fd(5)
	print("up")
def right():
	t.seth(0)
	t.fd(5)
	print("right")
def left():
	t.seth(180)
	t.fd(5)
	print("left")
def down():
	t.seth(270)
	t.fd(5)
	print("down")	
Scr.onkeypress(up, "w")
Scr.onkeypress(right, "d")
Scr.onkeypress(left, "a")
Scr.onkeypress(down, "s")
Scr.listen()
xDetection()

Scr.mainloop()	
	