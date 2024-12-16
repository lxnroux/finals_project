for q in range(1, 6): 
	for w in range(6, q, -1): 
		print(" ", end = " ")

	for e in range(1, q+1): 
		print("*", end = " ")
	
	for e in range(1, q): 
		print("*", end = " ")

	print()

for q in range(1, 6): 
	for w in range(1, 5): 
		print(" ", end = " ")

	for w in range(1, 4): 
		print("*", end = " ")

	print()