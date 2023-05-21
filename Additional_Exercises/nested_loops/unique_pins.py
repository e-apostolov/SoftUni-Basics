number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

for a in range(1, number_1 + 1):
    if a % 2 == 0:
        for b in range(2, number_2 + 1):
            count = 0
            for n in range(1, 10):
                if b % n == 0:
                    count += 1
            if count == 2:
                for c in range(1, number_3 + 1):
                    if c % 2 == 0:
                        print(a, b, c)

