fuel_type = input()
fuel_available = float(input())

if fuel_available >= 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_available < 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")

