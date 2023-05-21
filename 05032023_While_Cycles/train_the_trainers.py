jury = int(input())
count_grades = 0
sum_grades = 0
count_presentation = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break
    sum_current_grade = 0
    for i in range(jury):
        grade = float(input())
        count_grades += 1
        sum_grades += grade
        sum_current_grade += grade
    average_grade = sum_current_grade / jury
    print(f"{presentation_name} - {average_grade:.2f}.")

final_average_grade = sum_grades / count_grades
print(f"Student's final assessment is {final_average_grade:.2f}.")
