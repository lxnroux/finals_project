gold = 0
min = input("Hi, What is your name? ")

isgold = input("Is the mineral gold? [Yes / No]: ").upper().strip()

if isgold == "YES":
    gold += 1
    print(f"Hi {min}, Your total number of gold is: {gold}")

elif isgold == "NO":
    print("Please input a gold")

else:
    print("Wrong input")
