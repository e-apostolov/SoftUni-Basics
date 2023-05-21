n = int(input())

for a in range(1, 10):
    sum_a = 0
    for b in range(1, 10):
        sum_a = a + b
        if n % sum_a == 0:
            for c in range(1, 10):
                sum_b = 0
                for d in range(1, 10):
                    sum_b = c + d
                    if sum_a == sum_b:
                        print(f"{a}{b}{c}{d}", end=" ")
