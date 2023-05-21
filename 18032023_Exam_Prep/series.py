budget = float(input())
count_series = int(input())
total_price = 0

for i in range (1, count_series + 1):
    name_series = input()
    price_series = float(input())
    if name_series == "Thrones":
        price_series -= price_series * 0.5
    elif name_series == "Lucifer":
        price_series -= price_series * 0.4
    elif name_series == "Protector":
        price_series -= price_series * 0.3
    elif name_series == "TotalDrama":
        price_series -= price_series * 0.2
    elif name_series == "Area":
        price_series -= price_series * 0.1
    total_price += price_series

diff = abs(total_price - budget)

if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")

