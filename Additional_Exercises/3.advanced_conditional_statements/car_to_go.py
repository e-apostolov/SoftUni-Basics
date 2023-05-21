available_budget = float(input())
season = input()

car_class = ""
car_type = ""
car_cost = 0

if available_budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_cost = available_budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        car_cost = available_budget * 0.65
elif 100 < available_budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_cost = available_budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        car_cost = available_budget * 0.80
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_cost = available_budget * 0.90

print(car_class)
print(f"{car_type} - {car_cost:.2f}")

