upper_range_hundreds = int(input())
upper_range_tens = int(input())
upper_range_ones = int(input())

for x in range(1, upper_range_hundreds + 1):
    if x % 2 == 0:
        for y in range(2, upper_range_tens + 1):
            count = 0
            for n in range(1, 10):
                if y % n == 0:
                    count += 1
            if count == 2:
                for z in range(1, upper_range_ones + 1):
                    if z % 2 == 0:
                        print(x, y, z)


