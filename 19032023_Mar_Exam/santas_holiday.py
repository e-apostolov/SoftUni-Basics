count_days_stay = int(input())
count_nights = count_days_stay - 1
room_type = input()
rating = input()
cost_of_stay = 0

if count_days_stay < 10:
    if room_type == "room for one person":
        cost_of_stay = count_nights * 18
    elif room_type == "apartment":
        cost_of_stay = (count_nights * 25) * 0.70
    elif room_type == "president apartment":
        cost_of_stay = (count_nights * 35) * 0.90
elif 10 <= count_days_stay <= 15:
    if room_type == "room for one person":
        cost_of_stay = count_nights * 18
    elif room_type == "apartment":
        cost_of_stay = (count_nights * 25) * 0.65
    elif room_type == "president apartment":
        cost_of_stay = (count_nights * 35) * 0.85
elif count_days_stay > 15:
    if room_type == "room for one person":
        cost_of_stay = count_nights * 18
    elif room_type == "apartment":
        cost_of_stay = (count_nights * 25) * 0.50
    elif room_type == "president apartment":
        cost_of_stay = (count_nights * 35) * 0.80

if rating == "positive":
    cost_of_stay += cost_of_stay * 0.25
else:
    cost_of_stay -= cost_of_stay * 0.10

print(f"{cost_of_stay:.2f}")