num = int(input("Enter a number of right triangle: ")) 

for x in range(1, 6):
    for y in range(1, num + 1):
        print(" ", end= " ")
        for z in range(1, x + 1):
            print("*", end= " ")
        for a in range(5, x, -1):
            print(" ", end= " ") 

    print()