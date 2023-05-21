first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

for x in range (first_pair_start, first_pair_start + first_pair_diff + 1):
    count = 0
    for a in range(1, x + 1):
        if x % a == 0:
            count += 1
    if count == 2:
        for y in range (second_pair_start, second_pair_start + second_pair_diff + 1):
            count = 0
            for b in range (1, y + 1):
                if y % b == 0:
                    count += 1
            if count == 2:
                print(f"{x}{y}")