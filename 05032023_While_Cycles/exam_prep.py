bad_grades = int(input())

problem_name = input()
sum_grades = 0
poor_grades_count = 0
count_of_problems = 0
last_problem = ""

while problem_name != "Enough":
    last_problem = problem_name
    current_grade = int(input())
    if current_grade <= 4.00:
        poor_grades_count += 1
    sum_grades += current_grade
    count_of_problems += 1
    if poor_grades_count >= bad_grades:
        print(f"You need a break, {poor_grades_count} poor grades.")
        break
    problem_name = input()
average_score = sum_grades / count_of_problems

if poor_grades_count < bad_grades:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_of_problems}")
    print(f"Last problem: {last_problem}")







