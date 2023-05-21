K = int(input())
L = int(input())
M = int(input())
N = int(input())

count_substitutes = 0

for a in range(K, 8 + 1):
    if a % 2 == 0:
        for b in range(9, L - 1,-1):
            if b % 2 != 0:
                for c in range(M, 8 + 1):
                    if c % 2 == 0:
                        for d in range(9, N - 1,-1):
                            if d % 2 != 0:
                                number_1 = str(f"{a}{b}")
                                number_2 = str(f"{c}{d}")
                                number_1 = int(number_1)
                                number_2 = int(number_2)
                                if number_1 == number_2:
                                    print("Cannot change the same player.")
                                else:
                                    print(f"{a}{b} - {c}{d}")
                                    count_substitutes += 1
                                    if count_substitutes == 6:
                                        exit()