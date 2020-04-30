import turtle, time

t = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("black")
t.color("White")

subjAmt = int(input("How many subjects do you have ? : "))
ProgressLn = 0
subjAvg = 0

print("Status : RUNNING")
t.pensize(3)
t.ht()
t.pu()
t.setpos(0, -200)
t.pd()
t.circle(200)
print("Status : STOPPED")
time.sleep(1.5)
print("Status : LOADING...")
time.sleep(1.5)
print("Status : LOADED")
time.sleep(1.5)
print("Status : RUNNING")
for i in range(0,subjAmt):
	t.pu()
	t.setpos(0, 0)
	t.pd()
	Subject = input("Subject :  ")
	Percentage = int(input("Percentage :  "))
	if(Percentage<30):
		t.color("red")
	elif(Percentage<40):
		t.color("orange")
	elif(Percentage<50):
		t.color("yellow")
	elif(Percentage<80):
		t.color("yellowgreen")
	elif(Percentage<90):
		t.color("greenyellow")
	elif(Percentage<100):
		t.color("lawngreen")
	else:
		t.color("lime")
	ProgressLn = 360 / subjAmt
	t.right(ProgressLn)
	t.fd(Percentage*2)
	t.color("white")
	t.write(Subject)
	ProgressLn+=ProgressLn
	subjAvg += Percentage

subjAvg = round(subjAvg / (subjAmt * 100) * 100, 2)
print(subjAvg)
	
scr.mainloop()	