season = input()
km_per_month = float(input())

total_income = 0

if km_per_month <= 5000:
    if season == "Summer":
        total_income = km_per_month * 0.90 * 4
    elif season == "Winter":
        total_income = km_per_month * 1.05 * 4
    else:
        total_income = km_per_month * 0.75 * 4

elif 5000 < km_per_month <= 10000:
    if season == "Summer":
        total_income = km_per_month * 1.10 * 4
    elif season == "Winter":
        total_income = km_per_month * 1.25 * 4
    else:
        total_income = km_per_month * 0.95 * 4
else:
    total_income = km_per_month * 1.45 * 4

total_income *= 0.90

print(f"{total_income:.2f}")
