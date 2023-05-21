fuel_type = input()
fuel_amount = int(input())
club_card = input()

benz_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if fuel_type == "Gasoline":
    total_price = benz_price * fuel_amount
    if club_card == "Yes":
        total_price = (benz_price - 0.18) * fuel_amount
elif fuel_type == "Diesel":
    total_price = diesel_price * fuel_amount
    if club_card == "Yes":
        total_price = (diesel_price - 0.12) * fuel_amount
elif fuel_type == "Gas":
    total_price = gas_price * fuel_amount
    if club_card == "Yes":
        total_price = (gas_price - 0.08) * fuel_amount

if 20 <= fuel_amount <= 25:
    total_price *= 0.92
elif fuel_amount > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")
