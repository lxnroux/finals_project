isContinue = True
no = 0

while isContinue:
    ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()
    
    if ask == "NO":
        print("Program terminated")
        break 
    
    elif ask == "YES":
        no += 1  
        for x in range(1, 5):  
            print(" " * (5 - x), end="")
            print("* " * x)
    else:
        print("Invalid input. Please enter Yes or No.")