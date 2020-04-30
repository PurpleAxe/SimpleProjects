import math
import turtle

ws = turtle.Screen()
ws.bgcolor("white")
t = turtle.Turtle()
for i in [(0,250), (0,0), (0,-250), (0,0), (400,0), (0,0)]:
    t.goto(i, None)
    t.write(i, font=("Arial", 12))

t.color("red")

for angle in range(360):
    y = math.sin(math.radians(angle))        
    t.goto(angle, y * 200)

t.penup()
t.setpos(0,200)
t.goto(0,200)
t.pendown()
t.color("blue")

for angle in range(360):
    y = math.cos(math.radians(angle))       
    t.goto(angle, y * 200)

t.penup()
t.setpos(0,0)
t.goto(0,0)
t.pendown()
t.color("green")

for angle in range(360):
    y = 1//math.sin(math.radians(angle))
    t.goto(angle, y * 200)

ws.exitonclick()