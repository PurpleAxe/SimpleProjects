import random,time
arr = []
arr = [5,1,3,4,6,7,9,8,2]

def randlist():
	print("Preparing raw array ...")
	for k in range(0, 100):
		x = random.randint(0,10000000000000)
		arr.append(x)
	print("Array prepared")
	time.sleep(3)
	print(arr)
	print("\n Now sorting ",len(arr)," Items...")
	time.sleep(5)
randlist()

def insertion(arr):
	s = 0
	for i in range(0, len(arr)):
		for j in range(0, i+1):
			if arr[i] > arr[j]:
				temp = arr[j]
				arr[j] = arr[i]
				arr[i] = temp
				print(arr[i],"....Swapped....",arr[j])
				s+=1
		print(arr)
	print("Times swapped",s)
	

def quicksort(data):
	if len(data) < 1:
		return data
	pivot = data[0]
	left = []
	right = []
	for x in range(1, len(data)):
		if data[x] <= pivot:
			left.append(data[x])
		else:
			right.append(data[x])
		print(right," ..R...L.. ",left)
		print("data                                ",data)
	left = quicksort(left)
	right = quicksort(right)
	foo = [pivot]
	arr = []
	arr.append(left)
	arr.append(foo)
	arr.append(right)
	print(arr)

	

quicksort(arr)

