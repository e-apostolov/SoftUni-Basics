n = int(input())

number_of_combinations = 0

# x1 + x2 + x3 = n

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            if x1 + x2 + x3 == n:
                number_of_combinations += 1

print(number_of_combinations)