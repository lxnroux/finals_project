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