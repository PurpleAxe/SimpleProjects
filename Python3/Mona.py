import turtle,colorsys

t = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("black")

inp = input('Enter a word, \n ')
inpLen = len(inp)

x = 0

for i in range(0, inpLen):
	letter = inp[x]
	x += 1
	ordinp  = ord(letter)
	print("angle... ", ordinp, " ...amount forward... ",ordinp+ordinp, " ...character... ", chr(ordinp))
	ordi = ordinp//2
	for i in range(0, ordinp//2):
		t.begin_poly()
		cl = colorsys.hsv_to_rgb(i/ordinp, 1.0, 1.0)
		t.color(cl)
		t.right(ordinp)
		t.fd(ordinp+ordinp)
		print("Running... ",ordi," ...times")
		ordi -= 1
	t.end_poly()
print("END...")
scr.mainloop()