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