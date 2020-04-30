import turtle
import random 

t = turtle.Turtle()
scr = turtle.Screen()
turtle.setup(900, 900)
turtle.speed(10000)
colors  = ["red","green","blue","orange","purple","pink","yellow"]
maxrand = random.randint(3, 20)
randcirc = random.randint(10, 50)
for i in range(1, 10000):
	print('i')
	randcirc = random.randint(10, 50)
	color = random.choice(colors)
	counter = 1
	
	a = turtle.Turtle()
	a.ht()
	valx = random.randint(-50, 50)
	print("x", valx)
	valy = random.randint(-50, 50)
	print("y", valy)
	a.setpos(valx, valy)
	a.circle(randcirc)
	
	b = turtle.Turtle()
	b.ht()
	b.color(color)
	valx = random.randint(-100, 100)
	print("x", valx)
	valy = random.randint(-100, 100)
	print("y", valy)
	b.setpos(valx, valy)
	b.circle(randcirc)
	
	c = turtle.Turtle()
	c.ht()
	c.color(color)
	valx = random.randint(-150, 150)
	print("x", valx)
	valy = random.randint(-150, 150)
	print("y", valy)
	c.setpos(valx, valy)
	c.circle(randcirc)
	
	d = turtle.Turtle()
	d.ht()
	d.color(color)
	valx = random.randint(-200, 200)
	print("x", valx)
	valy = random.randint(-200, 200)
	print("y", valy)
	d.setpos(valx, valy)
	d.circle(randcirc)
	
	e = turtle.Turtle()
	e.ht()
	e.pu()
	e.color(color)
	valx = random.randint(-250, 250)
	print("x", valx)
	valy = random.randint(-250, 250)
	print("y", valy)
	e.setpos(valx, valy)
	e.pd()
	e.circle(randcirc)
	
	if (counter == 1):
		f = turtle.Turtle()
		f.pu()
		f.ht()
		f.color(color)
		valx = random.randint(-750, 750)
		print("x", valx)
		valy = random.randint(-750, 750)
		print("y", valy)
		f.setpos(valx, valy)
		f.pd()
		f.circle(randcirc)
	counter-=1	

	
scr.mainloop()