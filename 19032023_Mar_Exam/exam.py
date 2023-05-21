count_of_students = int(input())
top_students = 0
students_4_5 = 0
students_3_4 = 0
failed_students = 0
sum_grades = 0

for i in range(1, count_of_students + 1):
    grade = float(input())
    sum_grades += grade
    if grade >= 5.00:
        top_students += 1
    elif 4 <= grade < 5:
        students_4_5 += 1
    elif 3 <= grade < 4:
        students_3_4 += 1
    elif grade < 3:
        failed_students += 1

print(f"Top students: {(top_students / count_of_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(students_4_5 / count_of_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(students_3_4 / count_of_students) * 100:.2f}%")
print(f"Fail: {(failed_students / count_of_students) * 100:.2f}%")
print(f"Average: {sum_grades / count_of_students:.2f}")
