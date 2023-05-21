coins_1lv = int(input())
coins_2lv = int(input())
notes_5lv = int(input())
total_sum = int(input())

for x in range(0, coins_1lv + 1):
    for y in range(0, coins_2lv + 1):
        for z in range(0, notes_5lv + 1):
            if (x * 1) + (y * 2) + (z * 5) == total_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {total_sum} lv.")


