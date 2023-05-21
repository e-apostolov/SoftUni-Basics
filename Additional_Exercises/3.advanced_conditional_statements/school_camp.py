season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

sport_type = ""
total_price = ""

if season == "Winter" and (group_type == "boys" or group_type == "girls"):
    total_price = count_students * count_nights * 9.60
    if group_type == "boys":
        sport_type = "Judo"
    if group_type == "girls":
        sport_type = "Gymnastics"
elif season == "Spring" and (group_type == "boys" or group_type == "girls"):
    total_price = count_students * count_nights * 7.20
    if group_type == "boys":
        sport_type = "Tennis"
    if group_type == "girls":
        sport_type = "Athletics"
elif season == "Summer" and (group_type == "boys" or group_type == "girls"):
    total_price = count_students * count_nights * 15
    if group_type == "boys":
        sport_type = "Football"
    if group_type == "girls":
        sport_type = "Volleyball"
else:
    if season == "Winter":
        sport_type = "Ski"
        total_price = count_students * count_nights * 10
    elif season == "Spring":
        sport_type = "Cycling"
        total_price = count_students * count_nights * 9.50
    else:
        sport_type = "Swimming"
        total_price = count_students * count_nights * 20

if 10 <= count_students < 20:
    total_price *= 0.95
elif 20 <= count_students < 50:
    total_price *= 0.85
elif count_students >= 50:
    total_price *= 0.50

print(f"{sport_type} {total_price:.2f} lv.")