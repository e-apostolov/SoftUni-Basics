count_students = int(input())

count_grades_2_3 = 0
count_grades_3_4 = 0
count_grades_4_5 = 0
count_grades_5 = 0
sum_grade = 0
total_grades = 0

for i in range(1, count_students + 1):
    grade = float(input())
    sum_grade += grade
    if grade <= 2.99:
        count_grades_2_3 += 1
    elif 3 <= grade <= 3.99:
        count_grades_3_4 += 1
    elif 4 <= grade <= 4.99:
        count_grades_4_5 += 1
    else:
        count_grades_5 += 1

total_grades = count_grades_5 + count_grades_4_5 + count_grades_3_4 + count_grades_2_3
average = sum_grade/total_grades

print(f"Top students: {count_grades_5/total_grades * 100:.2f}%")
print(f"Between 4.00 and 4.99: {count_grades_4_5/total_grades * 100:.2f}%")
print(f"Between 3.00 and 3.99: {count_grades_3_4/total_grades * 100:.2f}%")
print(f"Fail: {count_grades_2_3/total_grades * 100:.2f}%")
print(f"Average: {average:.2f}")
