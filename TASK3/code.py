total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = attended / total * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    required = 0
    while (attended + required) / (total + required) < 0.75:
        required += 1

    print("Required classes:", required)

