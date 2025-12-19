marks = []
total = 0

for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)
    total += m

percentage = total / 5

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

file = open("student_result.txt", "a")
file.write("-----------------------------\n")
file.write(f"Total Marks: {total}\n")
file.write(f"Percentage: {percentage}%\n")
file.write(f"Grade: {grade}\n")
file.close()





















print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
