count_roll_paper = int(input())
count_roll_cloth = int(input())
count_liters_glue = float(input())
discount = int(input())

total_cost = count_roll_paper * 5.80 + count_roll_cloth * 7.20 + count_liters_glue * 1.20
total_cost -= total_cost * (discount / 100)

print(f"{total_cost:.3f}")
