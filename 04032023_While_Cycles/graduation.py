name_student = input()
grade_sum = 0
grade_2 = 0
student_class = 1

while True:
    grade = float(input())
    if grade < 4.00:
        grade_2 += 1
        if grade_2 > 1:
            print(f"{name_student} has been excluded at {student_class} grade")
            break
        continue
    student_class += 1
    grade_sum += grade
    if student_class > 12:
        print(f"{name_student} graduated. Average grade: {grade_sum / 12:.2f}")
        break

