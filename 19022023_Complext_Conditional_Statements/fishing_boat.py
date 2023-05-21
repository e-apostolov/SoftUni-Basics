

budget = int(input())
season = input()
count_fishers = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Summer" or season == "Autumn":
    total_price = 4200
elif season == "Winter":
    total_price = 2600

if count_fishers <= 6:
    total_price -= total_price * 0.1
elif 7 < count_fishers <= 11:
    total_price -= total_price * 0.15
elif count_fishers >= 12:
    total_price -= total_price * 0.25

if count_fishers % 2 == 0 and season != "Autumn":
    total_price -= total_price * 0.05

diff = abs(total_price - budget)

if total_price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")