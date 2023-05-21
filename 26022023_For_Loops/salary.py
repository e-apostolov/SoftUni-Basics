number_of_tabs = int(input())
salary = int(input())

for i in range(number_of_tabs):
    name_of_website = input()
    if name_of_website == "Facebook":
        salary -= 150
    elif name_of_website == "Instagram":
        salary -= 100
    elif name_of_website == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)


