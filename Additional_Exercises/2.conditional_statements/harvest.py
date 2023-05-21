from math import floor, ceil

x_size_grapes = int(input())
y_grapes_per_m2 = float(input())
z_liters_wine_needed = int(input())
workers_count = int(input())


total_grapes = x_size_grapes * y_grapes_per_m2
wine_produced = (total_grapes * 0.40) / 2.5


diff_wine = abs(z_liters_wine_needed - wine_produced)

if wine_produced < z_liters_wine_needed:
    print(f"It will be a tough winter! More {floor(diff_wine)} liters wine needed.")
elif wine_produced >= z_liters_wine_needed:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(diff_wine)} liters left -> {ceil(diff_wine / workers_count)} liters per person.")