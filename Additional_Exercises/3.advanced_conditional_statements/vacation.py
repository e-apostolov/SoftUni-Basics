available_budget = float(input())
season = input()

accommodation_type = ""
accommodation_price = 0
location = ""

if available_budget <= 1000:
    accommodation_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        accommodation_price = available_budget * 0.65
    else:
        location = "Morocco"
        accommodation_price = available_budget * 0.45
elif 1000 < available_budget <= 3000:
    accommodation_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        accommodation_price = available_budget * 0.80
    else:
        location = "Morocco"
        accommodation_price = available_budget * 0.60
else:
    accommodation_type = "Hotel"
    accommodation_price = available_budget * 0.90
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {accommodation_type} - {accommodation_price:.2f}")


