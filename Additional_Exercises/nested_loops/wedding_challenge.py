count_males = int(input())
count_females = int(input())
max_tables = int(input())


for x in range(1, count_males + 1):
    for y in range(1, count_females + 1):
        if max_tables > 0:
            print(f"({x} <-> {y})", end=" ")
            max_tables -= 1