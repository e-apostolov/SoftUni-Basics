no_of_days = int(input())
room_type = input()
rating = input()

no_of_nights = no_of_days - 1

total_cost = 0

if room_type == "room for one person":
    total_cost = no_of_nights * 18
elif room_type == "apartment":
    total_cost = no_of_nights * 25
    if no_of_nights < 10:
        total_cost -= total_cost * 0.3
    elif 10 <= no_of_nights <= 15:
        total_cost -= total_cost * 0.35
    else:
        total_cost -= total_cost * 0.50
elif room_type == "president apartment":
    total_cost = no_of_nights * 35
    if no_of_nights < 10:
        total_cost -= total_cost * 0.1
    elif 10 <= no_of_nights <= 15:
        total_cost -= total_cost * 0.15
    else:
        total_cost -= total_cost * 0.2

if rating == "positive":
    total_cost += total_cost * 0.25
elif rating == "negative":
    total_cost -= total_cost * 0.10

print(f"{total_cost:.2f}")


