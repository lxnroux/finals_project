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