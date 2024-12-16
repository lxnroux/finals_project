def act22():
      
      def act1():
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *", "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b\b\b* * * * * * *", "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *", "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b")

      def act2():
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))

            print(num1, "floor divided to", num2 ,"=", num1 // num2)

      def act3():
            fullname = "Fender B. Cruz"
            birthplace = "Lucena City"
            address = "Purok Maligaya Gulang Gulang Lucena City"
            birthmonth = "August"
            birthdate = 16
            birthyear = 2006
            gender = "Male"
            nationality = "Filipino"
            strand = "STE and STEM"
            oldschool = "Gulang Gulang National High School"
            grade = 94.688
            school = "Dalubhasaan ng Lungsod ng Lucena" 
            year = "First Year"
            course = "Bachelor of Science in Information Technology"
            email = "felixcruz8166@gmail.com"
            contactnumber = 639512446514
            single = True
            religion = "Catholic"
            hobbies = "art, like sketching, designing and fashion"



            print (fullname , "was born in" , birthplace , "and currently resides in" , address , "\nBorn" , birthmonth , birthdate , birthyear,". A" , gender , nationality , "student that took" , strand , "and graduated at" , oldschool , "with an average of" , grade , "with high honors \nNow a" , year , "student at" , school , "taking" , course,". For inquiries, his email is" , email , "and contact number is" , contactnumber , "\nIt is" , single , "that his marital status is single and he is" , religion , "\nMost of his interest revolves around" , hobbies  ) 
      
      def act4():
            number1 = eval(input("Enter A Number: "))
            number2 = eval(input("Enter Another Number: "))

            add = number1 + number2
            sub = number1 - number2
            mul = number1 * number2
            div = number1 / number2
            flr_div = number1 // number2
            exp = number1 ** number2
            mod = number1 % number2

            print("The sum of",number1,"and",number2,"in addition is",add, "\nThe sum of",number1,"and",number2,"in subtraction is",sub,"\nThe sum of",number1, "and",number2,"in multiplication is",mul,"\nThe sum of",number1,"and",number2,"in division is",div, "\nThe sum of",number1,"and",number2,"in floor division is",flr_div,"\nThe sum of",number1,"and",number2, "in exponentiation is",exp,"\nThe sum of",number1,"and",number2,"in modulus is",mod)

      def act5():
            temp = float(input("Enter temperature in farenheit: "))

            cel = (temp - 32) * 5/9

            print(f"The conversion of {temp} degrees farenheit is {round(cel, 2)} degrees celcius.")

      def act6():
            x = 5
            print(x)

            x += 10
            print(x)

            x += 15
            print(x)

            x += 10
            print(x)

      def act7():
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

      def act8():
            pre = int(input("Prelim Score: "))
            mid = int(input("Midterm Score: "))
            semi = int(input("Semi-Final Score: "))
            final = int(input("Final Score: "))
            quiz = int(input("Quiz Score: "))
            proj = int(input("Project Score: " ))

            fg = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)


            print(f"Your grade is {fg}")

            if pre > 100:
                  print("Error, wrong input")
            elif fg >= 65:
                  print("Congratulations! You have passed the course")
            else:
                  print("Unfortunately, you have failed")

      def act9():
            age = int(input("Enter your age: "))

            if age > 130:
                  print("Enter your real age")
            elif age >= 60 and age <= 130:
                  print("You are a senior")
            elif age >= 46 and age <= 59:
                  print("You are at post adulthood")
            elif age >= 32 and age <= 45:
                  print("You are at mid adulthood")
            elif age >= 19 and age <= 31:
                  print("You are at an early adulthood")
            elif age >= 14 and age <= 18:
                  print("You are a teenager")
            elif age >= 8 and age <= 13:
                  print("You are at pre-teen")
            elif age >= 1 and age <= 7:
                  print("You are a todler")
            else:
                  print("Enter your real age")

      def act10():
            name= input("Enter your name here:  ")
            isStud = input ("Are you currently enrolled in DLL? [yes/no]:  ").upper().strip()

            if isStud == "YES":
                  yearLev = input("What year are you currently enrolled? \nF- Freshmen \nS-Sophomore \nJ-Junior  \nR-Senior \nPlease enter your answer here: ").upper().strip()               
                  if yearLev == "F":
                        print(f"Hello Freshie {name}, and welcome to DLL") 
                  elif yearLev == "S":
                        print(f"Hello Sophomore {name}, and welcome to DLL") 
                  elif yearLev == "J":
                        print(f"Hello Junior {name}, and welcome to DLL") 
                  elif yearLev == "R":
                        print(f"Hello Senior {name}, welcome to DLL")
                  elif isStud == "NO":
                        print("Thank you for using the system").upper().strip()
                  else:
                        print("Wrong input")

      def act11():
            for i in range(1, 11):
                  print("Hello everyone!")
                  print("Happy Foundation Day!")
                                    
                  single = True

                  print(f"{single}, that everyone will enjoy.")

      def act12():
            for x in range(10, 1, -1):
                  print(x)

      def act13():
            sum = 0

            for x in range(4, 0, -1):
                  x *= x
                  sum += x

            print(x)
            print(sum)

      def act14():
            for x in range(0,11):
                  print(x, end=" ")
                  for y in range(0,11):
                        print("*", end= (" "))
                  print()

      def act15():
            for x in range(0, 11):
                  print(x, end=" ")
                  for y in range(0, x):
                        print("*", end= (" "))
                  print()

      def act16():
            for x in range(1, 11):
                  for y in range(1, x + 1):
                        print(" ", end=" ")
                  for z in range(11, x, -1):
                        print("*", end= " ")

                  print()

      def act17():
            for x in range(6, 0, -1):
                  for y in range(1, x + 1):
                        print(" ", end= " ")

                  for z in range(6, x, -1):
                        print("*", end= " ")

                  for a in range(5, x, -1):
                        print("*", end= " ")

                  print()

            for x in range(1, 6):
                  for y in range(1, x + 2):
                        print(" ", end= " ")

                  for z in range(5, x, -1):
                        print("*", end= " ")

                  for a in range(4, x, -1):
                        print("*", end= " ")

                  print()

      def act18():
            num = int(input("Enter a number of right triangle: ")) 

            for x in range(1, 6):
                  for y in range(1, num + 1):
                        print(" ", end= " ")
                        for z in range(1, x + 1):
                              print("*", end= " ")
                        for a in range(5, x, -1):
                              print(" ", end= " ") 

                  print()

      def act19():
            contin = True
            count = 0

            while contin == True:
                  name = input("Enter a name: ").upper().strip()

                  if name == "STOP":
                        print("The loop has now stopped")
                        print(f"You have entered {count} number of names")
                        break

                  else:
                        count += 1
                        continue

      def act20():
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

      def act21():

            def Hello(name):
                  print(f"Hello {name}")

            while True:
                  ask = input("Please provide a name: ").strip()
                  if ask.upper() == "STOP":
                        print("Goodbye!")
                        break
                  Hello(ask)

      def act23():

            def add(num1, num2):
                  print(f"The sum of the numbers is: {num1 + num2}")

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            add(num1, num2)

      def act24():
            
            from activity1 import print
            import activity1

            activity1.print()

      def act25():

           def list():

            fruits = ["orange", "lime", "lemon", "grapefruit", "tangerine", "strawberry", "delete one", "delete two"]

            fruits.remove("delete one")
            fruits.pop()
            fruits.append("blueberry")
            fruits.insert(0, "banana")

            print(fruits)

      list()
      
      def cc1():
            print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t    * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t  * * * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t    * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      * * *  \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")

      def cc2():
            name= input("What is your name?")
            print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t    * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *"+ " Hi," + name + " * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t    * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      * * *  \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")

      def cc3():
            fullname = "Fender B. Cruz"
            birthplace = "Lucena City"
            address = "Purok Maligaya Gulang Gulang Lucena City"
            birthmonth = "August"
            birthdate = 16
            birthyear = 2006
            gender = "Male"
            nationality = "Filipino"
            strand = "STE and STEM"
            oldschool = "Gulang Gulang National High School"
            grade = 94.688
            school = "Dalubhasaan ng Lungsod ng Lucena" 
            year = "First Year"
            course = "Bachelor of Science in Information Technology"
            email = "felixcruz8166@gmail.com"
            contactnumber = 639512446514
            single = True
            religion = "Catholic"
            hobbies = "art, like sketching, designing and fashion"



            print (fullname , "was born in" , birthplace , "and currently resides in" , address , "\nBorn" , birthmonth , birthdate , birthyear,". A" , gender , nationality , "student that took" , strand , "and graduated at" , oldschool , "with an average of" , grade , "with high honors \nNow a" , year , "student at" , school , "taking" , course,". For inquiries, his email is" , email , "and contact number is" , contactnumber , "\nIt is" , single , "that his marital status is single and he is" , religion , "\nMost of his interest revolves around" , hobbies  ) 

      def cc4():
            number1 = eval(input("enter a number --> "))

            number2 = eval(input("enter a number --> "))


            answer1= number1 + number2

            answer2 = number1 - number2

            answer3 = number1 * number2

            answer4 = number1 / number2

            answer5 = number1 ** number2

            answer6 = number1 % number2

            answer7 = number1 // number2

            print("The sum of" , number1 , "and" , number2 , " is" , answer1)

            print("The difference of" , number1 , "and" , number2 , "is" , answer2) 

            print("The product of" , number1 , "and" , number2 , " is" , answer3)
            
            print("The quotient of" , number1 , "and" , number2 , " is" , answer4) 

            print(number1 , "exponent by" , number2 , "is" , answer5)

            print("The remainder of" , number1 , "and" , number2 , "is" , answer6)

            print("The floor division of" , number1 , " and " , number2 , " is" , answer7)

      def cc5():
            print("Fahrenheit to Celsius Converter Program")

            fahrenheit = eval(input("Enter temperature in Fahrenheit --> : "))

            celsius = ((fahrenheit - 32) * 5) / 9

            print(f"{fahrenheit} degrees Fahrenheit converted to Celsius is {round(celsius, 2)} degrees")

      def cc6():
            x = 2

            print(x)

            x += 4

            print(x)

            x += 6 

            print(x)

            x += 8 

            print(x)

            x += 10

            print(x)

      def cc7():
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

      def cc8():
            sum = 0

            for x in range (1,11):
                  num= eval(input(f"Enter a number: "))
                  sum += num

            print(f"The sum of all the numbers entered is {sum}")

      def cc9():
            for x in range(10, 0, -1):
                   print("  " * (10 - x) + " *" * x)

      def cc10():
            for x in range(1,6):
                  for y in range(6, x, -1): 
                        print(" ", end = " ")

                  for z in range(1, x+1): 
                        print("*", end =" ")

                  for a in range(1, x+1): 
                        print("*", end =" ")
                  print()

            for x in range(1,6):
                  for y in range(1, x + 1): 
                        print(" ", end = " ")

                  for z in range(6, x, -1): 
                        print("*", end =" ")

                  for a in range(6, x, -1):
                        print("*", end =" ")
                  print()

      def cc11():
            for q in range(1, 6):
                  for w in range(6, q, -1): 
                        print(" ", end = " ")

                  for e in range(1, q+1): 
                        print("*", end = " ")

                  for e in range(1, q): 
                        print("*", end = " ")
                  print()

            for q in range(1, 5): 
                  for w in range(1, q + 2): 
                        print(" ", end = " ")

                  for e in range(5, q, -1): 
                        print("*", end = " ")

                  for e in range(4, q, -1): 
                        print("*", end = " ")
                  print()

      def cc12():
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

      def cc13():
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

      def cc14():
            c = True
            count = 0
            total_sum = 0

            while c:
                  user_input = input("Please enter a number (or type 'stop' to end) -> ")

                  if user_input.lower() == "stop":
                        print("Loop has been terminated.")
                        print(f"The sum of all the given numbers is {total_sum}")
                        break
                  else:
                        try:
                              number = float(user_input)  
                              total_sum += number  
                              count += 1  
                        except ValueError:
                              print("Invalid input. Please enter a valid number or 'stop'.")
                       
      def cc15():
            import os

            c = True
            no = 0

            while c:
                  ask = input("Do you wish to create a new triangle (yes or no) --> ")

                  if ask.lower() == "no":
                        print("Program/loop terminated")
                        break         

                  elif ask.lower() == "yes":
                        os.system("cls")
                        no += 1
                        for x in range(1, 6):
                              for r in range(1, no + 1):
                                    for y in range(1, x + 1):
                                          print("^", end=" ")
                                    for z in range(6, x, -1):
                                          print(" ", end=" ")
                              print()
                  else:
                        os.system("cls")
                        print("Invalid answer, please only answer 'yes' or 'no'")

      def cc16():
            class BankAccount:
                  def __init__(self, name, initial_deposit):
                        self.name = name
                        self.balance = initial_deposit

                  def deposit(self, amount):
                        if amount > 0:
                              self.balance += amount
                              print(f"Successfully deposited {amount}.")
                              self.show_balance()
                              self.breakdown_denomination(amount)
                        else:
                              print("Deposit amount must be positive.")

                  def withdraw(self, amount):
                        if amount > 0:
                              if self.balance >= amount:
                                    self.balance -= amount
                                    print(f"Successfully withdrew {amount}.")
                                    self.show_balance()
                                    self.breakdown_denomination(amount)
                              else:
                                    print("Insufficient balance.")
                        else:
                              print("Withdrawal amount must be positive.")

                  def show_balance(self):
                        print(f"Current balance: {self.balance}")

                  def breakdown_denomination(self, amount):
                        print(f"Breakdown of {amount}:")
                        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
                        for denom in denominations:
                              count = amount // denom
                              if count > 0:
                                    print(f"{denom} = {count}")
                              amount %= denom


                  def main():
                        print("Welcome to the Bank System!")
                        accounts = {}

                        while True:
                              print("\nMenu:")
                              print("1. Create Account")
                              print("2. Deposit")
                              print("3. Withdraw")
                              print("4. Show Balance")
                              print("5. Exit")

                              choice = input("Enter the number of your choice: ")

                              if choice == "1":
                                    name = input("Enter your name: ")
                                    initial_deposit = float(input("Enter initial deposit: "))
                                    if name in accounts:
                                          print("Account already exists.")
                                    else:
                                          accounts[name] = BankAccount(name, initial_deposit)
                                          print(f"Account created for {name} with initial deposit of {initial_deposit}.")

                              elif choice == "2":
                                    name = input("Enter account name: ")
                                    if name in accounts:
                                          amount = float(input("Enter amount to deposit: "))
                                          accounts[name].deposit(amount)
                                    else:
                                          print("Account not found.")

                              elif choice == "3":
                                    name = input("Enter account name: ")
                                    if name in accounts:
                                          amount = float(input("Enter amount to withdraw: "))
                                          accounts[name].withdraw(amount)
                                    else:
                                          print("Account not found.")

                              elif choice == "4":
                                    name = input("Enter account name: ")
                                    if name in accounts:
                                          accounts[name].show_balance()
                                    else:
                                          print("Account not found.")

                              elif choice == "5":
                                    print("Thank you for using the Bank System!")
                                    break

                              else:
                                    print("Invalid choice. Please try again.")


                  if __name__ == "__main__":
                        main()

      try:
            compile = True

            while compile:

                  print("\n\tSelect from the programs below: \n\t"
                        "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]", "\tCode Challenge 2 - [26]", "\tCode Challenge 10 - [34]"
                        "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]", "\tCode Challenge 3 - [27]", "\tCode Challenge 11 - [35]"
                        "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]", "\tCode Challenge 4 - [28]", "\tCode Challenge 12 - [36]"
                        "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]", "\tCode Challenge 5 - [29]", "\tCode Challenge 13 - [37]"
                        "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [22]", "\tCode Challenge 6 - [30]", "\tCode Challenge 14 - [38]"
                        "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [23]", "\tCode Challenge 7 - [31]", "\tCode Challenge 15 - [39]"
                        "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [24]", "\tCode Challenge 8 - [32]", "\tCode Challenge 16 - [40]"
                        "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", "\tCode Cha. 1 - [25]", "\tCode Challenge 9 - [33]", "\tExit - [0]")
            

                  num = int(input("\n\n\tSelect a program: "))

                  if num == 1:
                        act1()
                        continue

                  elif num == 2:
                        act2()
                        continue

                  elif num == 3:
                        act3()
                        continue

                  elif num == 4:
                        act4()
                        continue

                  elif num == 5:
                        act5()
                        continue

                  elif num == 6:
                        act6()
                        continue
                  
                  elif num == 7:
                        act7()
                        continue

                  elif num == 8:
                        act8()
                        continue

                  elif num == 9:
                        act9()
                        continue

                  elif num == 10:
                        act10()
                        continue

                  elif num == 11:
                        act11()
                        continue

                  elif num == 12:
                        act12()
                        continue

                  elif num == 13:
                        act13()
                        continue

                  elif num == 14:
                        act14()
                        continue
                        
                  elif num == 15:
                        act15()
                        continue

                  elif num == 16:
                        act16()
                        continue

                  elif num == 17:
                        act17()
                        continue
                  
                  elif num == 18:
                        act18()
                        continue

                  elif num == 19:
                        act19()
                        continue

                  elif num == 20:
                        act20()
                        continue

                  elif num == 21:
                        act21()
                        continue

                  elif num == 22:
                        act23()
                        continue

                  elif num == 23:
                        act24()
                        continue

                  elif num == 24:
                        act25()
                        continue

                  elif num == 25:
                        cc1()
                        continue

                  elif num == 26:
                        cc2()
                        continue
                  
                  elif num == 27:
                        cc3()
                        continue

                  elif num == 28:
                        cc4()
                        continue

                  elif num == 29:
                        cc5()
                        continue

                  elif num == 30:
                        cc6()
                        continue

                  elif num == 31:
                        cc7()
                        continue

                  elif num == 32:
                        cc8()
                        continue

                  elif num == 33:
                        cc9()
                        continue

                  elif num == 34:
                        cc10()
                        continue

                  elif num == 35:
                        cc11()
                        continue

                  elif num == 36:
                        cc12()
                        continue

                  elif num == 37:
                        cc13()
                        continue

                  elif num == 38:
                        cc14()
                        continue

                  elif num == 39:
                        cc15()
                        continue

                  elif num == 40:
                        cc16()
                        continue

                  elif num == 0:
                        cont = input("Do you want to continue? [Yes] / [No]: ").upper().strip()

                        if cont == "YES":
                              print("The program will not be terminated")
                              print("Thank you for using the program")
                              break

                        elif cont == "NO":
                              print("The program will now continue")
                              continue

                        else:
                              print("Wrong input. Invalid answer")


                  elif num < 0:
                        print("Wrong input. Please try again")
                        continue

                  else:
                        print("Wrong input. Invalid answer")
                        continue

      except ValueError:
            print("Wrong input. Must be a number")
      
act22()