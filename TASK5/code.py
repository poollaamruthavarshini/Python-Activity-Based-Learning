n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / n

print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))

