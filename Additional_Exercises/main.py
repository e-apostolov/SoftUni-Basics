a = int(input())
b = int(input())
c = int(input())

for x in range (1, a + 1):
    for y in range(1, b + 1):
        count = 0
        for n in range(1, 10):
            if y % n == 0:
                count += 1
        if count == 2:
            for z in range (1, c + 1):
                print(f"{x}{y}{z}")