weekday = input()

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Friday":
    result = 12
elif weekday == "Wednesday" or weekday == "Thursday":
    result = 14
else:
    result = 16

print(result)

