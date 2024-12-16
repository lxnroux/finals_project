for l in range(1,7):
	for o in range(6, l, -1):
		print(" ", end = " ")
	for o in range(l, 1, -1):
		print(o, end=" ")
	for v in range(1, l+1):
		print(v, end =" ")
	print()

for l in range(5,0,-1):
	for o in range(6, l, -1):
		print(" ", end = " ")
	for o in range(l,1,-1):
		print(o, end=" ")
	for v in range(1,l+1):
		print(v, end =" ")
	print()