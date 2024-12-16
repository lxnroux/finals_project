bought = input("Would you like to shop in our grocery? (Yes/No) : ")

if bought.lower() == "yes":
	item = input("Welcome! \nItems:\nchicken - 120.00 \nfish - 100.00 \npork - 130.00 \nChoose what you would like to buy : ")
	price = eval(input("Input the price of your chosen item : "))
	age = eval(input("Input your age: "))
	pay = eval(input("Input your payment: "))
	discount = round((price * 0.052), 2)
	discprice = round((price - discount), 2)
	tax = round((price * 0.123), 2)
	taxprice = round((price + tax), 2)
	if age >= 60: 
		print(f"Hi Customer, you have purchased a {item} with a price of {price} plus a 12.3% tax (30.75PHP), a total of {round((price - discount), 2)} ")
		print(f"Your change is {round((pay - discprice), 2)}")
		print("Thank you for shopping at our grocery!")
	elif age <60:
		print(f"Hi Customer, you have purchased a {item} with a price of {price} plus a 12.3% tax (30.75PHP), a total of {round((price + tax), 2)} ")
		print(f"Your change is {round((pay - taxprice), 2)}")
		print("Thank you for shopping at our grocery!")
else:
	print("Thank you! Come again.")

 
