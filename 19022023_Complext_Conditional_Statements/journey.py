budget = float(input())
season = input()

spent_amount = 0
accommodation = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_amount = budget * 30/100
        accommodation = "Camp"
    elif season == "winter":
        spent_amount = budget * 70/100
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_amount = budget * 40/100
        accommodation = "Camp"
    elif season == "winter":
        spent_amount = budget * 80/100
        accommodation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent_amount = budget * 90/100
    accommodation = "Hotel"


print(f"Somewhere in {destination}")
print(f"{accommodation} - {spent_amount:.2f}")


