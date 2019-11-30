arrnum = []

b = True
i = 1

def summer(x):
	k = 0
	xSplit = list(map(int, str(x))) 
	for l in range(0, len(xSplit)):
		k += xSplit[l]
	return k


while b is True:
	x = i * 9
	print("\x1b[94m"+"The value is : ", x)
	sum = summer(x)
	print("\x1b[95m"+str(sum))
	if len(str(sum)) > 1:
		print("\x1b[97m"+str(summer(sum)))
	i += 1

