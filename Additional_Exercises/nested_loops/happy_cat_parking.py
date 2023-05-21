count_days = int(input())
count_hours = int(input())
price = 1
total_price = 0

for days in range(1, count_days + 1):
    daily_price = 0
    for hours in range(1, count_hours + 1):
        price = 1
        if days % 2 == 0 and hours % 2 != 0:
            price = price * 2.5
            daily_price += price
        elif days % 2 != 0 and hours % 2 == 0:
            price = price * 1.25
            daily_price += price
        else:
            daily_price += price
    print(f"Day: {days} - {daily_price:.2f} leva")
    total_price += daily_price
print(f"Total: {total_price:.2f} leva")

