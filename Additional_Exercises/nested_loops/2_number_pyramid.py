n = int(input())

current_number = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_number > n:
            exit()
        print(current_number, end=" ")
        current_number += 1
    print()




