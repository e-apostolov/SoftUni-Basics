flower_type = input()
flower_qty = int(input())
budget = int(input())

total_sum = 0

if flower_type == "Roses":
    total_sum = flower_qty * 5
    if flower_qty > 80:
        total_sum -= total_sum * 0.1
elif flower_type == "Dahlias":
    total_sum = flower_qty * 3.8
    if flower_qty > 90:
        total_sum -= total_sum * 0.15
elif flower_type == "Tulips":
    total_sum = flower_qty * 2.8
    if flower_qty > 80:
        total_sum -= total_sum * 0.15
elif flower_type == "Narcissus":
    total_sum = flower_qty * 3
    if flower_qty < 120:
        total_sum += total_sum * 0.15
elif flower_type == "Gladiolus":
    total_sum = flower_qty * 2.5
    if flower_qty < 80:
        total_sum += total_sum * 0.2

diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"Hey, you have a great garden with {flower_qty} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
