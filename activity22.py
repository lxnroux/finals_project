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

        try:
            compile = True

            while compile:

                  print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                        "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]"
                        "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]"
                        "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]"
                        "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]"
                        "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [23]"
                        "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [24]"
                        "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [25]"
                        "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", "\tExit - [0]")

                  num = int(input("\n\n\tSelect a Program: "))

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

                  elif num == 23:
                        act23()
                        continue

                  elif num == 24:
                        act24()
                        continue

                  elif num == 25:
                        act25()
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
                              print("Wrong Input. Invalid Answer")


                  elif num < 0:
                        print("Wrong Input. Must Be A Positive Number.")
                        continue

                  else:
                        print("Wrong Input. Invalid Answer")
                        continue

        except ValueError:
            print("Wrong Input. Must Be A Number.")
      
act22()