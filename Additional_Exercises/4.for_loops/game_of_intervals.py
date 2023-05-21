rounds_count = int(input())

count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_49 = 0
count_invalid = 0
count_points = 0

for i in range(rounds_count):
    points = int(input())
    if 0 <= points <= 9:
        count_points += points * 0.2
        count_0_9 += 1
    elif 10 <= points <= 19:
        count_points += points * 0.3
        count_10_19 += 1
    elif 20 <= points <= 29:
        count_points += points * 0.4
        count_20_29 += 1
    elif 30 <= points <= 39:
        count_points += 50
        count_30_39 += 1
    elif 40 <= points <= 50:
        count_points += 100
        count_40_49 += 1
    else:
        count_points /= 2
        count_invalid += 1

total_count = count_0_9 + count_10_19 + count_20_29 + count_30_39 + count_40_49 + count_invalid

print(f"{count_points:.2f}")
print(f"From 0 to 9: {count_0_9 / total_count * 100:.2f}%")
print(f"From 10 to 19: {count_10_19 / total_count * 100:.2f}%")
print(f"From 20 to 29: {count_20_29 / total_count * 100:.2f}%")
print(f"From 30 to 39: {count_30_39 / total_count * 100:.2f}%")
print(f"From 40 to 50: {count_40_49 / total_count * 100:.2f}%")
print(f"Invalid numbers: {count_invalid / total_count * 100:.2f}%")
