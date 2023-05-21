luggage_price = float(input())
luggage_weight = float(input())
days_to_travel = int(input())
count_luggage = int(input())

single_luggage_price = 0

if luggage_weight < 10:
    single_luggage_price = luggage_price * 0.20
elif 10 <= luggage_weight <= 20:
    single_luggage_price = luggage_price * 0.5
elif luggage_weight > 20:
    single_luggage_price = luggage_price


if days_to_travel > 30:
    single_luggage_price += single_luggage_price * 0.10
elif 7 <= days_to_travel <= 30:
    single_luggage_price += single_luggage_price * 0.15
elif days_to_travel < 7:
    single_luggage_price += single_luggage_price * 0.4

total = single_luggage_price * count_luggage

print(f"The total price of bags is: {total:.2f} lv.")
